# Photorealistic Pet Quality Gates

Use these checks before asking the user to approve a representative frame, MP4 preview, or packaged Codex pet.

User confirmation is part of quality control for real pets, not optional polish. When a pose, expression, frame order, or prop contact was manually corrected by the user, preserve that correction as a locked requirement until the user changes it.

## Identity

- Face shape, eye spacing, nose, muzzle, ears, fur color, chest fur, leg thickness, and tail must match the real pet references.
- Avoid identity drift between states. A state can change pose and expression, but the pet should not become a different breed, age, coat texture, or body type.
- Compare the generated state against the nearest canonical view: front, left, right, or action-specific reference.

## State Semantics

- `idle`: calm, almost still, tiny breathing/blink/head motion only.
- `running-right`: faces right with a real running gait.
- `running-left`: faces left with a real running gait, mirrored only if safe.
- `waving`: use the user's chosen meaning. For a real dog, this may be tail wagging or standing happily rather than a human-like paw wave.
- `jumping`: use plausible vertical body motion and any user-approved prop physics.
- `failed`: disappointed or deflated without text, red X symbols, or floating UI.
- `waiting`: expectant, alert, looking for the owner or user input.
- `running`: busy task execution, not literal running.
- `review`: curious inspection or thinking without papers, magnifiers, UI, or symbols unless requested.

## Frame And Motion

- Keep the pet inside every cell with enough padding for fur, tail, legs, and props.
- Confirm key frames for actions with timing or contact: peak jump, ball hit, tail-wag extremes, running stride extremes, and return-to-idle.
- Use anatomical anchors for scale and alignment:
  - front views: head size, chest/body width, foot baseline
  - side views: head width, back-top midpoint, torso center, contact-foot baseline
- Do not let full silhouette bounds drive scale for running rows; stretched legs and tail spread change the silhouette without changing body size.
- Check adjacent-frame jumps. A visible shake usually means the torso or back alignment is moving too much, even if the full frame is centered.
- For bouncing or thrown props, verify contact frames and acceleration. A ball should enter from the intended direction, touch the correct body part, then leave quickly along a plausible path.

## Transparency

- Fully transparent pixels should have cleared hidden RGB.
- Boundary pixels should not retain blue, green, or white halo color from the source background.
- Inspect on at least one dark and one light background after extraction.
- If fur edges cannot be extracted cleanly, pause and ask about a transparent-output generation path before changing style.

## Package And Release

- Required tracked package files: `pet/pet.json` and `pet/spritesheet.webp`.
- `pet.json` should use `spriteVersionNumber: 2`.
- The atlas must match the expected v2 cell grid used by `$hatch-pet`.
- MP4 previews and QA JSON should be regenerated after any atlas change.
- Local production caches belong in ignored directories such as `outputs/`; do not commit them.
- After installation, byte-compare installed files against project files and ask the user to fully restart Codex.
