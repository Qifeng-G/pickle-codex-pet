# Real Pet Animation Design

Use this reference before designing or repairing the nine animation states. The goal is not only to make a valid Codex atlas; the pet should still feel like the user's real animal.

## Choosing References

- Sort source media by role before prompting or editing:
  - identity anchors: front, left side, right side, distinctive face/body/tail images
  - action anchors: videos or photos named for a state, such as running, failed, waiting, or task-in-progress
  - expression anchors: closeups that define eyes, mouth, muzzle, curiosity, disappointment, or excitement
  - proportion anchors: full-body images used to compare body height, head size, leg thickness, and tail volume
- Prefer full-body identity anchors for body scale. Use closeups only for facial angle or expression, not overall body proportion.
- If two references conflict, ask which one is more faithful unless the conflict is only pose, lighting, or camera perspective.
- Never let a state-specific action reference override the pet's core identity. Motion can change posture; it should not change breed, coat, muzzle, ears, or body mass.

## Representative Frame Confirmation

Ask for user approval on representative PNGs before making MP4s when:

- the state concept is new or was not directly provided by reference media
- the state includes a prop, unusual pose, wide-angle perspective, or nonstandard interpretation
- the user has already corrected that state once
- the generated pose changes the pet's apparent body size, leg thickness, head size, or tail shape

For each representative frame, show the frame and summarize what to check: identity, pose semantics, scale, expression, prop placement, and background cleanliness. Do not advance to MP4 until the user approves or gives a correction.

## Key Frames To Confirm

- `idle`: confirm the neutral body size and foot baseline. This often becomes the scale reference for front-facing states.
- `running-right`: confirm the direction, gait, side-profile identity, and whether it is safe to mirror for `running-left`.
- `running-left`: if mirrored, show the mirrored row or contact sheet; if independently generated, confirm it against the left-side reference.
- `waving`: confirm what "wave" means for this animal. For a dog, avoid a human hand gesture unless explicitly requested. If the user wants tail wagging, confirm a still-body representative frame and isolate tail motion in the MP4.
- `jumping`: confirm the peak/contact frame first. If a ball or toy is present, confirm the exact contact point before animating the full sequence.
- `failed`: confirm emotion without symbols or text. The pet can be disappointed, deflated, or guilty, but still must look like itself.
- `waiting`: confirm it reads as expectant or asking for input, not just idle.
- `running`: confirm it reads as busy task execution and not literal locomotion.
- `review`: confirm curiosity/thinking. If using wide angle, confirm that the nose/camera exaggeration is intentional and does not deform identity.

## Motion Planning

- Design the loop from anchors first, then fill in-between frames. For short MP4 previews, a simple ordered frame sequence is often clearer than over-smoothing.
- State the intended order when it matters, such as `1 2 3 4 5 4 3 2 1` for a ping-pong loop or `1 2 3 4 5` for a one-way action.
- For prop interactions, define:
  - entry point
  - contact frame
  - body reaction at contact
  - exit path
  - return-to-idle frame
- Keep the dog body stable unless the action itself requires movement. Isolate the moving part when the user asks, such as tail-only wagging or a ball-only correction.
- Do not animate by horizontal mirroring unless the visual semantics call for a direction flip. Mirroring a happy dog back and forth often reads as identity flicker.

## Correction Workflow

When the user marks up a frame or describes a problem:

1. Translate the correction into locked constraints. Example: "delete the old ball positions; put the ball in the circled positions; contact is above the nose."
2. Preserve approved parts explicitly. Example: "keep the dog's face and body from V2; only slim the paws."
3. Rebuild the smallest affected artifact first: representative frame, then MP4, then spritesheet.
4. Show the corrected frame or preview before packaging when the user asked for staged confirmation.
5. If the user says the issue remains, measure it or make a contact sheet instead of guessing. For size/jitter, compare adjacent-frame anatomy and report the measured jump.

## Common Manual Interventions To Preserve

- "Use this previous version, only change X": copy the previous approved artifact as the base and make a localized edit.
- "Do not change the expression": lock the mouth, eyes, and muzzle pixels or pose family; animate only the requested body part.
- "The body is too tall/fat/large": compare against the baseline frame using anatomy, not just overall alpha bounds.
- "The frame order is wrong": regenerate previews with the exact requested order before changing atlas packaging.
- "This is cache": verify timestamps, hashes, and output paths; show evidence that the displayed artifact is newly generated.
