# Canonical base — 2026-10-14

Tool: built-in `image_gen__imagegen`; transparent_background: true.

Reference: downloaded existing stable pet's sheet, `source/stored-before.webp`. The response was copied to `decoded/base.png` and `references/canonical-base.png`.

## Actual prompt

Use case: identity-preserve. Asset: canonical reference sprite for the EXISTING ChatGPT pet 银月 (Yinyue). Reference image is the downloaded existing sprite atlas, an identity reference, not a layout to reproduce. Generate ONE single centered full-body neutral pose of the SAME silver-haired fox-eared chibi girl, polishing her appearance. Preserve her compact approx three-head-tall proportions, warm amber brown eyes, long silver-white layered hair, pointed fox ears with pink interiors and fine white fur, ivory-white shrine-maiden style clothing, red obi bow and long red ribbon ends, broad white sleeves with restrained gray embroidered trim, short red-and-white skirt and white calf-height ornamental boots. Keep same recognizable face, hair silhouette, costume palette and modest outfit. Improve clean facial drawing, bright eyes, fine hair strands, sleeve folds, red bow knot, silver garment and boot details. Refined 2D anime game sprite, confident crisp thin dark-gray outlines, polished cel shading with delicate controlled highlights; clear silhouette and readable at 192x208 pet size. Whole body and all hair/ear/boot tips visible, neutral relaxed arms down pose, both boots on same ground line, front slightly three-quarter face with both eyes visible; no dramatic tilt. Transparent RGBA background, no printed checkerboard, no ground shadow, no halo. No tail, no new props, no text or labels, no borders, no extra characters, no scenery, no loose particles or effects. Render a single high quality character ONLY, not an animation sheet. Preserve identity but increase drawing finesse compared with the old low-resolution raster artwork.

## Visual acceptance

The generated base was displayed and inspected. Same silver hair, white fox ears, warm amber eyes, red obi and ribbons, white embroidered sleeves and white boots. Fine anime linework replaces the coarse raster treatment as requested. The base has no tail, held prop, label or scenic background. Animation jobs must leave more outer padding than the tall reference and use the base's refined design as the appearance authority.

The selected chroma key remains green for deterministic checks, but actual generation uses transparent RGBA and does not request an opaque green backdrop.
