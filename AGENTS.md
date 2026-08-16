# Pickle repository instructions

When the user asks to install this pet, run `scripts/install.sh` from the repository root. If writing to the Codex pets directory needs approval, request it. After installation, verify that `pet/pet.json` and `pet/spritesheet.webp` exactly match the files installed under `${CODEX_HOME:-$HOME/.codex}/pets/pickle/`, then tell the user to fully restart Codex.

Do not regenerate, resize, recompress, or rename the packaged pet files during installation. Do not commit anything under `outputs/`; it contains local production caches.
