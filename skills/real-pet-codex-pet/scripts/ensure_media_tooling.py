#!/usr/bin/env python3
"""Check and optionally install media tooling for Codex pet MP4 previews."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys


def command_version(binary: str) -> str | None:
    path = shutil.which(binary)
    if not path:
        return None
    result = subprocess.run(
        [path, "-version"],
        check=False,
        capture_output=True,
        text=True,
    )
    first_line = result.stdout.splitlines()[0] if result.stdout else ""
    return first_line or path


def brew_path() -> str | None:
    return shutil.which("brew")


def install_ffmpeg() -> tuple[bool, str]:
    brew = brew_path()
    if not brew:
        return False, "Homebrew is not installed or not on PATH; ask the user how they want to install ffmpeg."
    result = subprocess.run(
        [brew, "install", "ffmpeg"],
        check=False,
        capture_output=True,
        text=True,
    )
    output = (result.stdout + "\n" + result.stderr).strip()
    return result.returncode == 0, output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--install", action="store_true", help="install ffmpeg with Homebrew if missing")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args()

    ffmpeg_version = command_version("ffmpeg")
    ffprobe_version = command_version("ffprobe")
    installed = False
    install_output = ""

    if args.install and not ffmpeg_version:
        installed, install_output = install_ffmpeg()
        ffmpeg_version = command_version("ffmpeg")
        ffprobe_version = command_version("ffprobe")

    report = {
        "ok": bool(ffmpeg_version),
        "ffmpeg": ffmpeg_version,
        "ffprobe": ffprobe_version,
        "installed": installed,
        "install_output": install_output,
        "next_step": None,
    }
    if not report["ok"]:
        report["next_step"] = "Ask for approval to install ffmpeg, then rerun with --install."

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=True))
    else:
        if report["ok"]:
            print("ffmpeg-ok")
            print(ffmpeg_version)
            if ffprobe_version:
                print(ffprobe_version)
        else:
            print("ffmpeg-missing")
            print(report["next_step"])
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
