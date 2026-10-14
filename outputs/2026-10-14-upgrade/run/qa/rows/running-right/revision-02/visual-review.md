# running-right visual review

Generation: built-in `image_gen__imagegen`, true transparent background, canonical base + old identity atlas + eight-slot layout guide attached. Two attempts total; the second additionally used the first strip as the repair target.

Current candidate: `decoded/running-right.png` (2172 × 724).

The bundled extraction and inspection commands completed successfully. `review.json` reports `ok: true`, 8 expected / 8 actual frames, component extraction, no errors and no warnings. All extracted frames are 192 × 208; no frame has edge pixels or chroma-adjacent pixels. This is structural QA only.

Manual checks of the full strip and native frames 00, 02, 04 and 07:

- Eight complete separate poses; right-facing noses, faces and body direction remain clear.
- Silver fox ears, silver hair, amber eye, white/red embroidered clothing and calf boots preserve the broad identity. Face/head size is stable. No text, shadows, motion effects or new props.
- Leg silhouette changes through extension, support and knee lift, with small head/torso shifts. However, the repair still repeats a very similar near-leg cycle in the second half. Opposite near/far lead-leg phases for 00/04 and 02/06 are not reliably readable. I cannot certify a physically alternating eight-frame gait from this candidate.
- Frame 04/07 arm-forward poses also show a red bow/knot toward the back of the waist; the canonical reference puts its large bow at the front. Parent should inspect this potential costume-placement drift together with the gait issue.

Disposition: structural pass, visual gait acceptance withheld. Do not mark the visual job complete or derive running-left merely from `review.json`. No further regeneration was performed after the one targeted repair, as requested by the parent.

First strip and its actual structural report/frames are preserved under `revision-01/`. The first strip is also retained as `attempt-01.png`.

Prompts: `prompts/rows/running-right.actual.md` and `prompts/rows/running-right.retry-01.md`.
