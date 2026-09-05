#!/usr/bin/env bash

set -euo pipefail

PET_SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PET_REPO_DIR="$(cd -- "$PET_SCRIPT_DIR/.." && pwd)"
PET_CHOICE="${1:-}"

case "$PET_CHOICE" in
  pickle)
    PET_SOURCE_DIR="$PET_REPO_DIR/pet"
    PET_DISPLAY_NAME="Pickle"
    ;;
  xiaozuo|小佐)
    PET_SOURCE_DIR="$PET_REPO_DIR/pets/xiaozuo"
    PET_CHOICE="xiaozuo"
    PET_DISPLAY_NAME="小佐"
    ;;
  *)
    echo "Usage: $0 <pickle|xiaozuo>" >&2
    echo "Available pets: pickle, xiaozuo (小佐)" >&2
    exit 64
    ;;
esac

PET_CODEX_ROOT="${CODEX_HOME:-$HOME/.codex}"
PET_TARGET_DIR="$PET_CODEX_ROOT/pets/$PET_CHOICE"

for PET_REQUIRED_FILE in pet.json spritesheet.webp; do
  if [[ ! -f "$PET_SOURCE_DIR/$PET_REQUIRED_FILE" ]]; then
    echo "Missing required file: $PET_SOURCE_DIR/$PET_REQUIRED_FILE" >&2
    exit 1
  fi
done

mkdir -p "$PET_TARGET_DIR"
cp "$PET_SOURCE_DIR/pet.json" "$PET_TARGET_DIR/pet.json"
cp "$PET_SOURCE_DIR/spritesheet.webp" "$PET_TARGET_DIR/spritesheet.webp"

for PET_REQUIRED_FILE in pet.json spritesheet.webp; do
  if ! cmp -s "$PET_SOURCE_DIR/$PET_REQUIRED_FILE" "$PET_TARGET_DIR/$PET_REQUIRED_FILE"; then
    echo "Verification failed: $PET_REQUIRED_FILE" >&2
    exit 1
  fi
done

echo "$PET_DISPLAY_NAME installed successfully in: $PET_TARGET_DIR"
echo "Fully quit and reopen Codex, then select $PET_DISPLAY_NAME from the Pets list."
