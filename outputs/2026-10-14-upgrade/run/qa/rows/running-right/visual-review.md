# running-right visual review — fresh small-step cycle

Current source: `decoded/running-right.png` (2172 × 724), generated with built-in `image_gen__imagegen`, actual transparent alpha. The third attempt changes strategy: fresh canonical-base + old identity sheet + layout guide, with neither previous running candidate attached. Exact prompt: `prompts/rows/running-right.retry-02.md`.

The prior second candidate, structural report, extracted frames and original visual findings are preserved under `revision-02/`. First-attempt artifacts remain under `revision-01/`.

## Structural evidence

Bundled `extract_strip_frames.py --method auto` and `inspect_frames.py --require-components` completed successfully. `review.json` reports `ok: true`, 8 expected / 8 actual frames, method `components`, no errors and no warnings. All eight frames are 192 × 208, with zero edge pixels and zero chroma-adjacent pixels. Apparent character height is stable at 192–198 pixels; occupied baseline ranges from y=199 to y=203, consistent with the small-step bounce.

## Visual evidence

Inspected the complete strip and all eight native extracted frames.

- All eight full bodies remain separated and unclipped; both boots are complete. The canonical silver hair, fox ears, amber eyes, embroidered white sleeves, red waist bow and detailed boots remain consistent.
- Nose and gaze point screen-right in a stable shallow three-quarter view. The torso exposes its front enough to keep the red obi bow visible below the chest in every pose.
- The front bow stays at the abdomen throughout. The backside contains ribbon ends, with no migrated or newly invented rear bow. This resolves the previous candidate's costume-placement concern.
- Frame 00 has an extended front boot and a rear boot; frame 01 brings the legs closer under the body; frame 03 raises the rear heel higher while the forward leg supports; frame 04 opens the stride again. Frames 05–07 repeat the compact step rhythm with varying boot separation and low heel lift. These are visibly changing step silhouettes, not eight static copies.
- Arm swing is small and leaves the front bow visible. Hair and attached red ribbons follow subtly. Head scale, viewpoint and body proportions stay stable. No shadows, motion lines, dust, text, detached effects or new props are visible in native extracted frames.
- The generator used more vertical space than the prompt's 40–45% guide target, but extraction retains safe padding and no clipping. This is a source-layout observation, not a required final-cell defect.

Disposition: passes this row's initial structural and visual check under the revised light small-step movement brief. The leg phases are intentionally modest; this is a brisk small-step cycle rather than a wide sprint. Parent should still inspect final assembled playback for cross-row scale, timing and looping continuity before final atlas acceptance. No global manifest or other row was edited, and running-left was not generated.
