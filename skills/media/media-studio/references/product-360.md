# Product 360, turntable and reveal video (merged)

Condensed from seedance-product-360 (995 lines), corrected against the Higgsfield vendor docs, with the media-studio video
rules applied. The member's five long worked examples (watch, sneaker, earbuds, perfume, seat covers) and per-category
lighting essays stay in `members/seedance-product-360/SKILL.md`. The member has no upstream license: personal use only.

## What was corrected or dropped

- Feature claims with no source ("real-time ray tracing", "particle system support", "text animation", "motion
  smoothing", "Higgsfield logo acceptable on Amazon videos"): dropped. Amazon's video rules are checked on Seller Central.
- "5-60 s per video": Seedance 2.5 renders 4-30 s up to 1080p; Seedance 2.0 renders 4-15 s up to 4K. A 25 s story is
  several shots joined in the edit (or a `video_extension` run), not one prompt.
- 20-26 line labeled prompts: Higgsfield models distort past about 200 tokens. The template below is a planning sheet;
  each generation gets a compressed prompt for one shot.
- Text overlays and audio mix "inside Seedance": overlays (name, specs, price, CTA) are added in post (Remotion,
  Hyperframes, CapCut or ffmpeg) so they stay sharp and editable. Audio: Seedance 2.0 has native audio on by default; for
  a designed mix generate `seed_audio` separately or add music in the edit.

## Plan the sequence (planning sheet, not the prompt)

| Beat | Length | Decide |
|---|---|---|
| Hook | 0-2 s | one hook style matched to the category's energy |
| Hero angle | 2-3 s | the view that sells (table below) |
| Rotation | 3-8 s | full 360 / half / pendulum / orbit, speed by category |
| Details | 2-5 s | 2-3 macro shots of what proves quality (stitching, print, grain, facets) |
| Context (optional) | 2-3 s | in use / on body / in hand; answers "where does this belong?" |
| Finale | 1-2 s | back to hero angle; CTA overlay added in post |

Hook styles (match energy to category: luxury = calm and precise, tech = fast, fashion = lifestyle): particle
materialization, spotlight snap, crash with shockwave, unwrap/peel, macro-to-wide pull back, self-assembly, exploded view
snapping together, liquid pour / transparency bloom, slow-motion lift into rotation, 180-degree spin-to-reveal, zoom into
texture then pan, halo light flare. A crash hook on a luxury watch is a mismatch.

Hero angles: watches and rings front face tilted about 35 degrees, then side profile for case depth; bags three-quarter
front, then side; electronics screen-front, then rear; shoes three-quarter for the profile, then sole; jewelry light into
the stone facets; cosmetics top-down, then side. Apparel: front print first, back print second, worn on the
lifter for fit, fabric macro last.

Rotation speed for a full 360: slow 10-15 s (luxury, detail-heavy); medium 5-8 s (fashion, cosmetics, shoes); fast 2-4 s
(tech, energetic). Multi-speed (slow on the hero angle, faster mid-turn, slow finale) keeps attention.

## Lighting and background by category (key / fill / rim / color temperature / ground)

| Category | Light | Background and surface |
|---|---|---|
| Tech, phones, earbuds | key 45 deg above, cool 5600K; fill 50-55% slightly warm 4000K; subtle rim | dark-to-mid gray gradient or white; matte dark surface |
| Jewelry, watches | hard key 30-35 deg to the side; minimal fill; strong rim (halo); rotate so facets flash about every half second | black, deep navy or mirror; black velvet or leather |
| Bags, belts, accessories | key 45 deg, warm 3200-4000K; fill 60%; moderate rim; light grazing the texture | white, light gray, soft gradient, wood or linen |
| Apparel, footwear | key 45 deg, warm 3500K; fill 60%; moderate rim | white or light gradient; neutral surface |
| Cosmetics, perfume | key 60 deg above, diffused, warm 3200K; fill 80%; subtle rim; backlight for liquid color | white, pale gradient, frosted surface |
| Automotive parts | key 45 deg dramatic; fill 40%; strong rim; multiple sources for reflections | dark gradient or mirror, polished black |
| Furniture, home | key 45 deg diffused, 3200-3500K; fill 70%; subtle rim; a hand or use-case for scale | neutral or lifestyle setting |
| Food, packaging | key 45 deg warm 3200K; fill 70% (harsh shadows read stale); subtle rim | warm neutral, wood, linen, ceramic |

Materials: metal = hard directional key, let highlights travel across the surface, cool for steel and warm for gold;
glass = multi-directional light to show refraction, cool 5200-5600K; leather and wood = warm grazing light for grain;
fabric = soft 45-degree key for weave and drape, 3500-4000K; matte = soft diffuse, no speculars; glossy = hard key, moving
speculars; liquid = backlight or side light for color and meniscus.

## Camera moves (pick 1-3)

Product rotation: slow / medium / fast full 360, spin + float, half turn (180), quarter turn (90), pendulum (45 left to 45
right), overhead turntable spin. Camera moves: continuous orbit around a still product (large items), push-in to macro,
pull-back reveal, dolly slide, tilt up/down, boom-up while rotating (shows the sole or base), parallax orbit, Dutch-tilted
rotation (25-35 degrees, tech/fashion). Combos: spin-to-stop then push in on the hero angle; zoom to a detail, hold, pull
out to context.

## Using the user's product photos (image-to-video beats text-to-video)

- 1 photo: `--mode omni_reference --start-image hero.png`, describe only the motion.
- 3 photos: front (hero), side, detail/back. 5: front, right, back, left, detail or lifestyle. 7: add the two 45-degree
  views. 9: eight views every 45 degrees around + one macro/lifestyle.
- Matching light across the photos matters more than the count: mixed lighting makes the turn jump. Start and end frames
  from the same shoot (`--start-image` / `--end-image`) give the cleanest arcs.
- For a GLB the customer can spin on the site, `multi_image_to_3d` (1-4 photos) may beat a video; ask the user which the user wants.

## Compressed shot prompt (one generation, under about 200 tokens)

```text
[Product, from the reference image] on [surface/background], [hook action in one clause]. [Rotation or camera move with
speed, e.g. "rotates a slow full 360 degrees over 12 seconds, pausing briefly at the three-quarter front view"].
[Light: key position + temperature, fill, rim]. [Material behavior: "speculars travel across the brushed steel",
"print stays flat and legible on the cotton"]. [Camera: lens feel, depth of field]. Smooth, steady motion, no jitter,
product fills most of the frame.
```
Run on `seedance_2_5` (`--duration 4-30 --resolution 1080p --aspect_ratio 16:9|1:1|9:16`), or `seedance_2_0` for 4K.
Cost it first (`higgsfield generate cost seedance_2_5 <same flags>`), one draft at 720p, then the final.

## Overlays and sound (in post)

- Overlay timing for a 15 s cut: 0-2 s hook, no text; 2-2.5 s product name in; 2.5-8 s feature callouts timed to the angle
  that shows them; 8-12 s little or no text; 12-14.5 s price or key spec; last 0.5-1 s brand or CTA.
- Type: legible sans-serif; primary 48-72 px, secondary 24-36 px, nothing under 24 px; high contrast or a subtle backing
  box; animate in 0.3-0.5 s, hold at least 2 s, out 0.3-0.5 s. Always end with a CTA ("Shop now", price).
- Sound: product sounds 60-70% of the mix, ambience 30-40%; light reverb (0.5-1.5 s) on product sounds; hook = silence or
  one impact; last 2 s = a short brand sting. Captions or on-screen text carry the message for muted autoplay.

## Platform video notes (verify current specs on each platform's help page before upload)

| Placement | Aspect | Length | Notes |
|---|---|---|---|
| Amazon listing video | 16:9 | 15-30 s | no watermarks or outside branding; check Seller Central rules and AI-content labels |
| Shopify product page | 1:1 or 16:9 | 10-30 s | muted autoplay loop; keep a static image fallback; compress for mobile |
| Brand site hero | 16:9 | 8-30 s | muted autoplay, poster image, WebM/MP4, lazy-load below the fold |
| TikTok, Reels, Shorts | 9:16 | under 20 s | hook in the first 0.5-2 s, burned-in text, label AI content where required |
| Instagram feed, Pinterest | 1:1 (feed), 2:3 or 1:1 (pins) | 5-15 s | |

## Review checklist (before showing the user)

- [ ] Hook lands in 2 s and matches the category's energy
- [ ] Product fills 50-80% of the frame; product-to-background contrast at least 3:1
- [ ] Rotation smooth, no jitter or warping of the product (print, logo, seams, proportions match the real product)
- [ ] 2-5 s of macro detail that proves quality
- [ ] Light consistent across shots and right for the material
- [ ] Overlays readable (24 px minimum, 2 s minimum hold) and a CTA at the end
- [ ] Aspect, length and file size fit the target platform; static fallback image ready for e-commerce
- [ ] Watched on a phone and a desktop
