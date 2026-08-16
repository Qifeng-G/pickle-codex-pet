#!/usr/bin/env bash

set -euo pipefail

PICKLE_SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PICKLE_REPO_DIR="$(cd -- "$PICKLE_SCRIPT_DIR/.." && pwd)"
PICKLE_SOURCE_DIR="$PICKLE_REPO_DIR/pet"
PICKLE_CODEX_ROOT="${CODEX_HOME:-$HOME/.codex}"
PICKLE_TARGET_DIR="$PICKLE_CODEX_ROOT/pets/pickle"

for PICKLE_REQUIRED_FILE in pet.json spritesheet.webp; do
  if [[ ! -f "$PICKLE_SOURCE_DIR/$PICKLE_REQUIRED_FILE" ]]; then
    echo "Missing required file: $PICKLE_SOURCE_DIR/$PICKLE_REQUIRED_FILE" >&2
    exit 1
  fi
done

mkdir -p "$PICKLE_TARGET_DIR"
cp "$PICKLE_SOURCE_DIR/pet.json" "$PICKLE_TARGET_DIR/pet.json"
cp "$PICKLE_SOURCE_DIR/spritesheet.webp" "$PICKLE_TARGET_DIR/spritesheet.webp"

for PICKLE_REQUIRED_FILE in pet.json spritesheet.webp; do
  if ! cmp -s "$PICKLE_SOURCE_DIR/$PICKLE_REQUIRED_FILE" "$PICKLE_TARGET_DIR/$PICKLE_REQUIRED_FILE"; then
    echo "Verification failed: $PICKLE_REQUIRED_FILE" >&2
    exit 1
  fi
done

echo "Pickle installed successfully in: $PICKLE_TARGET_DIR"
echo "Fully quit and reopen Codex, then select Pickle from the Pets list."
