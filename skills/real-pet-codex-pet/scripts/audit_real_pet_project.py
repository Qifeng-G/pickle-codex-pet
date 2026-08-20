#!/usr/bin/env python3
"""Audit a real-pet Codex pet project for common stale or stray artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


STANDARD_STATES = [
    "idle",
    "running-right",
    "running-left",
    "waving",
    "jumping",
    "failed",
    "waiting",
    "running",
    "review",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_ignored(root: Path, path: Path) -> bool | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "check-ignore", "-q", str(path.relative_to(root))],
            check=False,
        )
    except Exception:
        return None
    return result.returncode == 0


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception:
        return {}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--pet-id", help="installed pet id; defaults to pet/pet.json id or the project folder name")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    root = args.project_root.expanduser().resolve()
    pet_json = root / "pet" / "pet.json"
    spritesheet = root / "pet" / "spritesheet.webp"
    validation = root / "qa" / "validation.json"
    previews_dir = root / "previews"
    outputs_dir = root / "outputs"

    report: dict[str, object] = {
        "project_root": str(root),
        "ok": True,
        "errors": [],
        "warnings": [],
        "files": {},
    }
    errors: list[str] = report["errors"]  # type: ignore[assignment]
    warnings: list[str] = report["warnings"]  # type: ignore[assignment]
    files: dict[str, object] = report["files"]  # type: ignore[assignment]

    manifest = load_json(pet_json) if pet_json.exists() else {}
    pet_id = args.pet_id or manifest.get("id") or root.name
    report["pet_id"] = pet_id

    for required in [pet_json, spritesheet]:
        if not required.exists():
            errors.append(f"missing required file: {required}")
        else:
            files[str(required.relative_to(root))] = {
                "bytes": required.stat().st_size,
                "sha256": sha256(required),
            }

    if pet_json.exists():
        if manifest.get("spriteVersionNumber") != 2:
            errors.append("pet/pet.json does not declare spriteVersionNumber: 2")

    if previews_dir.exists():
        missing = [
            state
            for state in STANDARD_STATES
            if not (previews_dir / f"{state}.mp4").exists()
        ]
        if missing:
            warnings.append("missing MP4 previews: " + ", ".join(missing))
        if spritesheet.exists():
            stale = [
                state
                for state in STANDARD_STATES
                if (previews_dir / f"{state}.mp4").exists()
                and (previews_dir / f"{state}.mp4").stat().st_mtime
                < spritesheet.stat().st_mtime
            ]
            if stale:
                warnings.append(
                    "MP4 previews older than pet/spritesheet.webp: "
                    + ", ".join(stale)
                )
    else:
        warnings.append("missing previews/ directory")

    if validation.exists() and spritesheet.exists():
        if validation.stat().st_mtime < spritesheet.stat().st_mtime:
            warnings.append("qa/validation.json is older than pet/spritesheet.webp")
    elif not validation.exists():
        warnings.append("missing qa/validation.json")

    if outputs_dir.exists():
        ignored = git_ignored(root, outputs_dir)
        if ignored is False:
            warnings.append("outputs/ exists but is not ignored by git")

    installed = Path.home() / ".codex" / "pets" / str(pet_id)
    installed_pet_json = installed / "pet.json"
    installed_spritesheet = installed / "spritesheet.webp"
    if installed.exists():
        if pet_json.exists() and installed_pet_json.exists() and sha256(pet_json) != sha256(installed_pet_json):
            warnings.append("installed pet.json differs from project pet/pet.json")
        if spritesheet.exists() and installed_spritesheet.exists() and sha256(spritesheet) != sha256(installed_spritesheet):
            warnings.append("installed spritesheet.webp differs from project spritesheet.webp")

    report["ok"] = not errors
    rendered = json.dumps(report, indent=2, ensure_ascii=True)
    print(rendered)
    if args.json_out:
        args.json_out.write_text(rendered + "\n")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
