# Jumping strip visual QA

- Selected source: `decoded/jumping.png` (2170 x 725, built-in image_gen, genuine transparency).
- Actual prompt: `prompts/rows/jumping-actual.md`; all job references viewed and supplied: canonical base, old identity atlas, five-slot layout guide.
- Bundled `extract_strip_frames.py --states jumping --method auto` succeeded using connected-component extraction.
- Bundled `inspect_frames.py --states jumping --require-components` returned `ok: true`, 5/5 frames, no errors or warnings. Report: `qa/rows/jumping/review.json`.
- Viewed the source and all five 192 x 208 extracted frames. Consistent identity: fox ears, silver hair, amber eyes, white/red dress, sleeve embroidery, red bow/ribbons and detailed white boots. No new props or extra limbs.
- Action reads as crouched anticipation, lift, airborne apex, descent, upright landing. Head and torso visibly move upward in source coordinates. Apex uses naturally bent knees; it is not a scaled-down standing character.
- Native alpha bounds (top, bottom): frame 0 (58, 203), frame 1 (25, 183), frame 2 (5, 159), frame 3 (29, 191), frame 4 (34, 203). Peak foot lift is 44 px relative to the grounded first/last frames, exceeding the requested 20 px. Grounded first and last frames share bottom 203. All frames have zero edge pixels.
- Native frames have attached hands/sleeves, distinct complete boots, and no visible floor, shadow, dust, marks or detached effects. Large source preview has very thin low-opacity baseline/color fringe artifacts; component extraction removes the baseline remnants from the delivered native frames. This was an extraction/background detail, not a pose failure; no regeneration was needed.
- This is row-level acceptance only. Parent remains responsible for shared scale versus idle, final contact-sheet and animation review, edge cleanup and exact-atlas validation.
