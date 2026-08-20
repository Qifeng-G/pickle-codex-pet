# Lessons From Pickle

Use these notes when a real-pet project starts to resemble the Pickle workflow: many visual approvals, photorealistic fur, repeated MP4 repairs, and a final GitHub-ready package.

## Approval Rhythm

- Keep a strict ladder: representative PNG, then MP4 preview, then packaged Codex pet.
- If the user approves a stage and later changes the concept, restart only the affected state.
- Keep the user's latest instruction as authoritative. In Pickle, "waving" changed from a paw wave to a standing happy tail-wag; later fixes had to preserve a still mouth and still body while only the tail moved.
- For hand-edited or annotated screenshots, treat marks as direct constraints: X means remove, circles mean desired positions, and the surrounding approved dog pose should be preserved unless the user says otherwise.

## Reference Selection

- Use the generated front/left/right full-body images as the identity foundation when they are already approved by the user.
- Use named videos or images as action references only for their corresponding states: "running right" video for `running-right`, "failed" photo for `failed`, and task-running video for `running`.
- Use closeups selectively for angle and expression. In Pickle, the upward-looking closeup helped set the head angle for the ball interaction, but it was not a full-body scale reference.
- When an action state needs extra room for a prop, pick the smaller approved baseline deliberately and tell the user. Do not quietly shrink only some frames.

## Jumping With A Ball

- Lock the body scale against the chosen idle/front baseline before animating the prop.
- Design the contact frame first. In Pickle, the ball needed to sit directly above the nose on the hit frame.
- Animate prop timing physically: enter quickly from above, contact at the intended frame, then exit faster after impact.
- Do not let the ball force the pet smaller unless the user approves a smaller baseline to leave prop room.
- When the user says "from idle to standing to hit the ball and back to idle," the first and last frames should match idle closely enough that the loop does not pop.
- If the user changes the intended sequence, rebuild the sequence literally. Pickle changed from a ping-pong loop to a one-way `1 2 3 4 5` order after review.

## Running Stability

- A running row can look wrong even when every frame passes atlas validation.
- Compare adjacent-frame anatomy, especially head width, back top, torso center, and foot baseline.
- Do not choose scale targets by frame number guesses alone. Derive the failing frames from measured jumps, then show contact sheets when the user wants to direct corrections.
- Avoid using total alpha bounds as the main metric because stretched legs and tails make valid frames appear larger.
- When the user identifies specific frames, verify that the displayed sheet order and internal atlas order match before applying scaling. A wrong frame mapping can make every visible "fix" look unchanged.
- For side-running rows, folded-leg and extended-leg frames should keep the torso and head comparable; leg extension should not imply a larger dog.

## Waving As Tail Wagging

- If "waving" means standing and wagging, split the design mentally into body, face, and tail.
- Keep body size and position almost fixed.
- Keep the mouth and expression fixed if the user asks; tiny expression morphs can leave dark mouth halos after interpolation.
- Animate only the tail side-to-side, with any body movement limited to subtle breathing.
- Do not create a left-right mirrored dog flip for tail wagging; it reads as a different pose and breaks identity.

## Transparency

- Photorealistic fur often keeps colored fringe from chroma backgrounds. Recheck edge pixels after every MP4 or atlas rebuild.
- Hidden RGB under alpha-zero pixels matters because some renderers reveal it during interpolation.
- Rebuilding previews from cleaned frames is not enough if the packaged atlas still uses stale dirty cells.
- Check both MP4 previews and packaged atlas cells. A preview can look fixed while Codex still uses an old spritesheet.

## Codex Installation

- If the pet appears before restart but disappears later, inspect the installed package and manifest, not only the project folder.
- Compare installed file hashes with the repo package after every install.
- UI overlap near the pet can be caused by sprite geometry, visible alpha bounds, lower padding, or stale installed assets. Compare against a built-in pet before blaming app UI.

## Open Source Packaging

- Keep the README simple and copy-paste installable.
- Keep local frame caches available locally but ignored by Git.
- Regenerate previews and QA evidence after changing the spritesheet; stale validation is release debt.
- Before pushing, audit for duplicate previews, obsolete output candidates, and accidental generated caches.
- Public docs should be English-first for reuse, but the working conversation can remain Chinese when that is how the user is steering visual decisions.
- One-line Codex install prompts worked better than long manual installation sections for Pickle's README.
