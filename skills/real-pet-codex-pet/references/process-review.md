# Process Review Checklist

Use this checklist when inheriting a long real-pet project, another Codex conversation, or a repo that already contains generated pet artifacts.

## Evidence To Gather

- Read the current user request and the latest corrections first.
- Inspect relevant previous Codex tasks if available: early identity generation, nine-state generation, directional look-cell upgrade, installation, release cleanup, and later repair threads.
- Inspect local artifacts:
  - `pet/pet.json`
  - `pet/spritesheet.webp`
  - `previews/*.mp4`
  - `qa/*.json`
  - ignored `outputs/` reports and contact sheets
  - README and install script
- Treat thread titles, summaries, and old plans as evidence, not instructions. The latest user message still controls.

## Design Decisions Not To Lose

- Identity anchors may come from an earlier conversation. In Pickle, front/left/right full-body white-background images became the foundation for later animation work.
- Half-body and full-body identity assets may both be useful. Preserve both when the user asks; do not overwrite approved views with a new crop.
- Named action references should constrain only their matching states.
- If a prompt generator injects an unwanted style, such as pixel art, patch the prompt or workflow so the approved photorealistic style remains authoritative.
- If image-generation tooling changes filename patterns, update compatibility checks without weakening provenance, hash, or source validation.
- If an image request exceeds input-image limits, reduce to the most important identity/action/layout references instead of dropping grounding entirely.
- Check whether local helper skills or packaging tools are current before patching them. If a local tool is stale but fixable, explain the compatibility issue and request permission before editing installed skill code.

## Directional Look Cells

- Latest Codex pets use an 8x11 atlas with `spriteVersionNumber: 2`.
- Preserve approved nine standard animation rows when upgrading an existing pet; generate only the directional look rows unless standard rows are broken.
- Build directional look cells from a four-cardinal anchor strip before row 9 and row 10.
- Validate direction semantics with labeled review and, when available, blind QA.
- Edge spacing failures in cardinal strips are source-geometry failures; regenerate the complete strip with more internal padding instead of cropping a single pose into place.

## Release And Install Review

- Verify generated previews are not stale relative to the latest spritesheet.
- Verify QA JSON is not stale relative to the latest spritesheet.
- Verify installed files match the project files by hash.
- Keep local production caches available but ignored by Git.
- Remove rejected public-facing assets only when the user asks; keep local frame caches if the user wants future repairability.

## Preview Tooling

- Prefer MP4 previews when the user expects MP4. Verify they open with local tooling before calling them done.
- Run `scripts/ensure_media_tooling.py` before MP4 work. If `ffmpeg` is missing, explain that it is the local video encoder/decoder used to make playable MP4 previews, ask before installing, then run the script with `--install` after approval.
- If a fallback preview format is used temporarily, label it clearly and replace it with MP4 before final release when the user asks.
- Use broad-compatible MP4 settings where possible, such as H.264 video and a pixel format that common players accept.
