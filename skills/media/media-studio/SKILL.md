---
name: media-studio
description: "Make any image, banner, video, GIF, 3D or generative-art asset. AI image and video via Higgsfield (GPT Image 2.6, Nano Banana, Soul, Seedream, Seedance 2.5, Kling, Veo, Marketing Studio), OpenAI GPT Image or Gemini. Product photoshoots (studio, lifestyle, Pinterest pin, hero, carousel, ad pack, virtual try-on, restyle), marketplace listing images and A+ modules, UGC and unboxing ad videos, product 360 turntables and reveals, character face lock, outfit plates and character sheets (Banana Pro), cinematic scene plates, Soul ID, Virality Predictor, GLB from photos. Also blog hero, OG and social images, mockups, banners and display ads, Remotion and Hyperframes video, demo recordings, p5.js generative art, Slack GIFs, upscale and WebP. Use for: generate an image, make a video, animate this photo, remove background, inpaint, product photo, Amazon listing images, turntable, Higgsfield, Seedance, B-roll, talking head, GIF, enhance a screenshot. Logos go to brand-studio."
members: [imagegen, imagen, fal-ai-media, image, banner-design, video, remotion-video-creation, algorithmic-art, slack-gif-creator, image-enhancer, higgsfield-generate, higgsfield-product-photoshoot, higgsfield-marketplace-cards, higgsfield-soul-id, banana-pro-director-30, seedance-product-360]
---

# Media Studio

One entry point for every image, banner, video, GIF, 3D and generative-art task. It merges sixteen skills: the Higgsfield
suite (one credit pool for most image, video, audio and 3D models, plus product and marketplace enhancers), OpenAI and
Gemini image scripts, fal, two marketing-production guides (image, video), banner design, Remotion rules, a photoreal
character prompt director, a product-360 video guide, p5.js art, Slack GIFs and image enhancement. Load this file first,
pick a mode, run the unified workflow, and open a member or reference file only when a route names it. `members/<name>/`
points at the original skill folder; `<skill>` in commands means this skill's absolute folder,
`~/.claude/skill-library/media/media-studio`.

## Pick the mode

| Task looks like | Mode | What to do / open |
|---|---|---|
| Photo, illustration, texture, sprite, concept art or scene from a prompt | AI-IMAGE | Workflow 1-9; model table in Core rules; recipes by use-case slug in `members/imagegen/references/sample-prompts.md` |
| Change an existing image: background swap, object removal, cut-out, relight, style transfer, composite | AI-EDIT | Same as AI-IMAGE plus the invariant rules; `members/imagegen/references/prompting.md` |
| Brand product visual from the user's real product photo: studio, lifestyle, Pinterest pin, hero, carousel, ad pack, try-on, surreal, seasonal restyle | PRODUCT-PHOTO | `higgsfield product-photoshoot create --mode <mode>`; modes and questions in `references/higgsfield.md` |
| Marketplace listing set: main image, secondary images, infographic, A+ modules | MARKETPLACE-CARDS | `higgsfield marketplace-cards create --scope ...`; marketplace rules in `references/platform-specs.md` |
| AI ad video: UGC, unboxing, tutorial, review, try-on, TV spot; branded ad image from a format template | AD-VIDEO | Higgsfield Marketing Studio / DTC ads in `references/higgsfield.md`; ad strategy from ads-and-measurement |
| Product turntable, 360 spin, reveal, beauty shot, hero product video | PRODUCT-360 | `references/product-360.md`, then Seedance via Higgsfield |
| Original recurring character (mascot, model, lifter): face lock, outfit plate, character sheet, outfit swap | CHARACTER | `references/higgsfield-prompt-craft.md` pipeline; verbatim templates in `members/banana-pro-director-30/SKILL.md` |
| Photoreal cinematic still or environment plate, often the start frame for a video | SCENE-PLATE | Prompt-craft reference, "Scene plates" section |
| Train a face identity for consistent images and video | SOUL-ID | `members/higgsfield-soul-id/SKILL.md` + photo guide; consent and paid plan first (house rules) |
| Score a finished video's hook, attention and retention | VIDEO-SCORE | Higgsfield Virality Predictor (`brain_activity`); A/B tests stay in conversion-lab |
| Real 3D mesh (GLB) of a product from photos | 3D-ASSET | Higgsfield `multi_image_to_3d`; a "3D-looking picture" is AI-IMAGE |
| Blog hero, OG preview, social post, profile or listing banner, email header | MARKETING-IMAGE | Compose in HTML/CSS, AI only for the background; sizes in `references/platform-specs.md`; OG and per-placement workflows in `members/image/SKILL.md` |
| Banner set (social cover, display ads, web hero, print) in several art directions | BANNER | `members/banner-design/SKILL.md` steps; 22 styles + print specs in `members/banner-design/references/banner-sizes-and-styles.md` |
| Show the real product UI (feature shot, store screenshots, directory gallery) | REAL-SCREENSHOT | Capture real screens (Playwright MCP or Chrome headless), frame and annotate in HTML. Never AI-generate UI [image] |
| Make an existing image sharper, larger, smaller or web-ready | ENHANCE | Local pipeline in Core rules > Enhance and optimize. Paid AI upscalers only after the user says yes |
| Templated, data-driven or batch video, motion graphics, captions | PROGRAMMATIC-VIDEO | Hyperframes vs Remotion rule below; Remotion topics in `members/remotion-video-creation/rules/<topic>.md` |
| Repeatable demo video of a web app flow | DEMO-RECORDING | `members/video/references/product-demo-recording.md` (Playwright, visible cursor, subtitles, local-app gotchas) |
| AI footage, B-roll, image-to-video, AI avatar presenter, reframe a video to 9:16 | AI-VIDEO | Higgsfield Seedance 2.5 by default (model table below); prompts in `members/video/references/ai-video-prompting.md`; `reframe` / `draw_to_video` workflows. Paid: ask the user |
| "Make it like this reference video" | EDIT-ANATOMY | Beat-sheet method in `members/video/references/edit-anatomy.md`; copy the editing grammar, never the footage |
| Generative art, flow field, particles, "art from code", seed gallery | GENERATIVE-ART | `members/algorithmic-art/SKILL.md`, start from `members/algorithmic-art/templates/viewer.html` |
| Static poster, print piece or art PNG/PDF driven by a design philosophy | POSTER | Built-in `anthropic-skills:canvas-design` |
| Animated GIF, Slack emoji, reaction GIF | GIF | Free first: `members/slack-gif-creator/SKILL.md` + its `core/` helpers; paid AI GIF: `gpt_image_2_6 --output_format gif` |
| Voice-over, music, sound effects | AUDIO | Higgsfield `seed_audio` (paid, ask the user); ElevenLabs not set up; `members/fal-ai-media/SKILL.md` audio section for options |
| Logo, brand mark, palette, icon system | elsewhere | brand-studio (AI only for logo concepts) |
| Ad strategy, ad copy, platform ad policy | elsewhere | ads-and-measurement; this skill only makes the visual |

## Unified workflow

1. **Frame the job.** Write down: deliverable, placement (platform and exact px from `references/platform-specs.md`),
   new or edit, one asset or a set, preview-only or project-bound, and the exact on-image text. Label every input image
   by role: reference, edit target, or insert/style input [imagegen decision tree + image intake]. Ask the user only for true
   blockers (missing copy, platform, or the real product photo); otherwise default (3 options for banners
   [banner-design]) and state assumptions.
2. **Load context before inventing anything.** Read `.agents/product-marketing.md` or `.claude/product-marketing.md` if
   present [image, video], the project's brand source (`docs/brand-guidelines.md`, design tokens, Tailwind theme) and
   existing assets. Use only supplied or verified brand rules; never invent a palette, slogan or logo use [banner-design].
3. **Choose the cheapest route that meets the need.** Climb this ladder and stop at the first rung that works
   [merged from imagegen "when not to use", image approach table, banner-design visual sources]:
   1. existing or supplied asset (licensed);
   2. code-native: HTML/CSS, SVG, canvas, p5.js, Pillow; best for shapes, icons, diagrams, type-led banners and anything
      that must match repo assets;
   3. real capture: screenshots or screen recordings for anything showing the product UI; real product photos;
   4. AI generation or editing (paid). Use it for photos, illustrations, textures, lifestyle scenes, B-roll, product
      scenes built FROM the real product photo, and video.
   Text, logos and CTAs never live inside generated pixels when the asset is HTML-composed: they are overlaid in
   HTML/CSS so they stay sharp, editable and accessible [banner-design, image].
4. **If AI: pick the route and model** with "Which generator and model" below: a Higgsfield enhancer command for product
   and marketplace work, a Higgsfield model id for everything else, OpenAI or Gemini direct only for the listed cases.
   Inside the CHARACTER pipeline, use the director's models [banana-pro-director-30]. Check current ids before promising
   one: they drift fast [fal-ai-media, higgsfield-generate].
5. **Write the prompt** for the route [imagegen, higgsfield-generate, banana-pro-director-30, seedance-product-360]:
   direct model calls use the shared schema (40-80 words for stills, under about 200 tokens for any Higgsfield model);
   enhancer commands (product-photoshoot, marketplace-cards) get a short intent line, never a hand-written prompt;
   character and scene work follows the prompt-craft reference; video describes motion, not the start frame. Match
   augmentation to specificity: a detailed prompt is only normalized; a generic one gets composition, lighting and
   intended-use hints, never new objects, brands, slogans or palettes [imagegen].
6. **Gate the spend.** Free checks first: OpenAI/Gemini script `--dry-run`; Higgsfield `account status` (plan, balance)
   and `generate cost <id> <flags>` / `generate cost workflow` / `--cost-only`. Then ask the user once per batch with route,
   model, count, size, quality and the estimate (credits or $), folding any open choices into labeled options and, for
   characters, the pre-prompt check bullets. Draft at count 1, low quality or the cheap model; scale only the winner
   [fal-ai-media, image cost tips, higgsfield]. Never auto-retry an uncertain billable call [imagen, higgsfield dtc-ads].
7. **Compose and export.** Overlay copy, logo and CTA in HTML/CSS using the banner rules; capture at exact px with
   Chrome headless or Playwright at 2x scale after a 3-5 s font/image wait [design social-photos, banner-design]. Video
   overlays and sound go in post (Remotion, Hyperframes, CapCut, ffmpeg) [video, product-360 corrected].
8. **Validate like a reviewer.** Check subject, style, composition, text spelled right (zoom in), edit invariants held,
   real-product fidelity (print, logo, colorway, cut), identity held across a set, safe-zone crop at real display size,
   contrast >= 4.5:1, file size within platform limit [imagegen, banner-design, image, banana-pro-director-30]. Iterate
   with one change at a time and repeat the invariants in every edit round [imagegen].
9. **Optimize and deliver.** Download Higgsfield result URLs; web assets get the optimization checklist [image]. Save
   finals into the project's asset folder by its convention, never overwrite (write `hero-v2.png`), keep only selected
   finals, put drafts in the scratchpad. Report path (and source URL), final prompt or intent line, route/model/settings,
   and the real cost (balance before vs after for credits) [imagegen, higgsfield].

Video runs the same frame -> context -> route -> gate -> validate loop: script first (problem -> solution -> CTA),
then pick programmatic, AI footage (Seedance), Marketing Studio ad, avatar or screen recording with the video approach
table, captions always, and export per platform aspect [video]. Image-to-video from an approved still (a scene plate or a
product photo) is the most controllable path [fal-ai-media, banana-pro-director-30].

## Core rules and checklists

### Which generator and model [new: higgsfield-generate catalog + image tree + the user's setup]

1. The ladder in workflow step 3 comes first: code, screenshots and real photos beat any generator.
2. **Higgsfield is the default paid route** for images, video, audio and 3D when `higgsfield account status` shows
   credits: one credit pool for most model families, a free cost estimate, product and marketplace enhancers, and the CLI
   is installed. The user is on the free plan, so the pool is small: check the balance before promising a batch.
3. **OpenAI direct** (`image_gen.py`) when Higgsfield is out of credits or logged out, when the job needs a transparent
   background, a mask inpaint, `input_fidelity` or the script's JSONL batch, or when the user asks. Always pass
   `--model gpt-image-2.5-sunburst` (OpenAI's named replacement per the image member; `-flare` is the other variant) after
   checking OpenAI's models/deprecations page, since Higgsfield already serves GPT Image 2.6 and a newer direct id may
   exist. Never rely on the script default `gpt-image-1.5` (retires 2026-12-01); `gpt-image-1` retired 2026-10-23, so any
   note naming it is stale. The key is exported, so a real call bills the user's OpenAI account at once.
4. **Gemini direct** only when the user wants Google billing or a Gemini-only feature; the Nano Banana models are on Higgsfield.
5. **fal stays off**: Higgsfield covers the same families (Nano Banana, Seedance, Kling, Veo) plus audio. Ideogram,
   Midjourney, Runway, HeyGen: recommend only.

| Job | Higgsfield route (id or command) | Fallback / note |
|---|---|---|
| Brand product visual from the real product photo | `product-photoshoot create --mode <mode> --image <photo>` | OpenAI edit with the photo |
| Marketplace listing set | `marketplace-cards create --scope main\|product-images\|aplus\|full-set` | HTML composition over real photos |
| General image, design, UI mock, short text in pixels, edits | `gpt_image_2_6` | OpenAI direct `gpt-image-2.5-sunburst` |
| Animated GIF or SVG from a prompt | `gpt_image_2_6 --output_format gif\|svg` | GIF: Pillow builder is free |
| Cartoon or illustrated mascot, heavy texture | `nano_banana_flash` (Nano Banana 2) | Gemini direct |
| New original photoreal person (UGC, editorial, fashion) | `text2image_soul_v2` | `--soul-id` for a trained identity |
| Cinematic still, concept mood | `soul_cinematic` | |
| Character pipeline (face lock, outfit, 3-panel sheet, outfit swap) | `nano_banana_pro`; GPT Image for chest-up detail; `soul_cinematic` for cheap face exploration | prompt-craft reference |
| One-shot face sheet or face edit from reference photos | `seedream_v5_pro` | |
| Environment, no people | `soul_location` | |
| Vector, icon, logo concept | `recraft_v4_1 --model_type vector` | finals in brand-studio |
| Same person or look across many images | trained Soul + `text2image_soul_v2`, or `nano_banana_pro` with reference images | Flux multi-reference (fal, off) |
| Style transfer, typography remix, a look unlike the defaults (when named) | Flux 2.0 / Flux Kontext Max | Ideogram (best text-in-image) and Midjourney: not set up |
| Cheap drafts (only when cheaper/faster is wanted) | `z_image`, `nano_banana_2_lite` | |
| Video: default (motion, image-to-video, multi-shot, 4-30 s, up to 1080p) | `seedance_2_5` | |
| Video: native 4K (4-15 s) | `seedance_2_0` | say why you switched |
| Video: cheaper or faster (only when asked) | `kling3_0_turbo`, Veo 3.1 Lite, Seedance 1.5 Pro | |
| Ad video (UGC, unboxing, tutorial, review, try-on, TV spot) | `marketing_studio_video` | |
| Branded ad image | `marketing-studio dtc-ads generate --format-id` or `marketing_studio_image` | |
| Reframe a video / edit it from a sketched frame | workflow `reframe` / `draw_to_video` | |
| Sound effect, ambience, voice-style, music bed | `seed_audio` | ElevenLabs not set up |
| GLB mesh from 1-4 product photos | `multi_image_to_3d --should_texture true` | |
| Score a finished video | `brain_activity` | |

Gotchas [higgsfield-generate]: `nano_banana_2` is an alias for Nano Banana PRO; Flare is its own id, never `--variant`;
prompt-only models (Z Image, Recraft, Soul Cast, Soul Location) reject media flags; Cinema Studio ids are missing from
`model list` (use `model get`); never pick an older model because its schema looks simpler; a model the user names stays for
follow-ups. Cost: credits vary with model, resolution, duration and count. The members only rank them: GPT Image costs more than
Banana Pro; Z Image, Nano Banana 2 Lite, Kling 3.0 Turbo, Veo 3.1 Lite and Seedance 1.5 Pro are the budget picks. Never
quote a number from memory: run the cost command. Commands, params, modes and
errors: `references/higgsfield.md`.

### Providers on the user's machine [imagegen, imagen, fal-ai-media, image, higgsfield-*]

| Provider | Status | Best at | How to run |
|---|---|---|---|
| Higgsfield | CLI via Homebrew; log in once with `higgsfield auth login`; `higgsfield account status` (free) confirms | most image and video models, product/marketplace enhancers, Marketing Studio ads, Soul ID, audio, 3D, video scoring | `higgsfield generate create <id> --prompt "..." --wait` after `generate cost`; never the vendor `curl \| sh` installer |
| OpenAI GPT Image | `OPENAI_API_KEY` set in the shell; `openai` SDK on `python3.12` | transparent background, masks, edits with up to 16 input images, n=1-10, JSONL batch | `python3.12 <skill>/members/imagegen/scripts/image_gen.py generate --model gpt-image-2.5-sunburst --size 1536x1024 --quality low --out <path> --dry-run` (also `edit`, `generate-batch`; sizes 1024x1024, 1536x1024, 1024x1536, auto); drop `--dry-run` after the user's OK |
| Google Gemini image (Nano Banana) | `GEMINI_API_KEY` kept in a credentials file, not exported | native editing, multi-image reference | `python3.12 <skill>/members/imagen/scripts/generate_image.py --model <id> --size 2K "<prompt>" <new>.png` (1K, 2K, 4K), key exported for that one command only; helper uses `generateContent` |
| fal.ai | not set up: no key, no MCP | same families as Higgsfield | Off; recommend only if Higgsfield lacks a model the user needs |
| Ideogram, Recraft direct, Runway, HeyGen, ElevenLabs | not set up | Ideogram text-in-image, Runway motion control, HeyGen avatars (has MCP), ElevenLabs voice | Recommend with the install/signup step; the user decides |

Use the bundled scripts as they are: no edits to them and no one-off SDK runners [imagegen].

### Prompt schema (direct model calls) [imagegen + image]
```text
Use case: <slug: photorealistic-natural | product-mockup | ui-mockup | infographic-diagram | logo-brand |
           illustration-story | stylized-concept | historical-scene | text-localization | identity-preserve |
           precise-object-edit | lighting-weather | background-extraction | style-transfer | compositing | sketch-to-render>
Asset type: <where it will be used, px>
Primary request: <one line>
Input images: <Image 1: role; Image 2: role>
Scene/backdrop | Subject | Style/medium | Composition/framing | Lighting/mood | Color palette | Materials/textures
Text (verbatim): "<exact text>"
Constraints: <change only X; keep Y unchanged>   Avoid: <no logos, no watermark, no extra text>
```
- Order: scene -> subject -> details -> constraints. Name the intended use; it sets polish level [imagegen].
- Always state aspect ratio or px (on Higgsfield as the `--aspect_ratio` flag, not prompt text) and a style word
  ("clean commercial photography", "flat illustration", "3D render").
- Photoreal: camera language (lens, depth of field, light direction). Leave negative space where copy will sit.
- Text in pixels: 3-5 words max, quoted verbatim, tricky words spelled letter by letter; anything longer goes in an
  overlay [imagegen, image]. Logo placement by prompt is unreliable: add logos in post [image].
- Multi-image input: refer to images by index and say what each contributes. Reuse a `seed` when iterating [fal-ai-media].
- Image-to-image: describe the change, not the input; phrase positively ("tack sharp", not "no blur") [higgsfield-generate].
- For batches: test 3-4 style prompts, pick the winner, save that exact prompt as the template, feed the winner back as a
  style reference, then vary only the subject [image batch workflow].

### Paid-call request and delivery report [imagegen report + fal cost check + imagen data rules + higgsfield cost]
Ask once, before any billable call or batch:
```text
Paid generation request: <route> <model or command/mode>, <n> output(s) at <size/res/duration>, quality <...>
Estimated cost: <N credits from `generate cost` (balance B) | $ from provider pricing | unknown until a count-1 run>
Uploads: <files that go to the provider, or none>. Prompt has no private data.
Why AI and not code/screenshot/photo: <one line>. Draft first at <cheap setting>, final only for the pick.
Options (defaults marked): <labeled choices, if any>. OK?
```
Deliver with: final file path(s), px and source URL, the final prompt or intent line, route/model/settings, real cost,
what was checked (text, invariants, product fidelity, crop), and any assumption made.

### Never AI-generate these [image, video]
Product UI (hallucinated interfaces), real locations people know, logos as finals, paragraphs of text, and the product
being sold from text alone. A product image or video is AI-made only when conditioned on the user's real product photo or
design file (PRODUCT-PHOTO, MARKETPLACE-CARDS, PRODUCT-360, AI-EDIT composite).

### Real product in AI imagery [image + higgsfield product members + seedance-product-360]
- Pass the real product photo or the design file every time (`--image`); text-only product renders never ship.
- Compare each output with the real product: print artwork position, scale, colors and spelling; logo; colorway; garment
  cut and fit; proportions. Prints and small text are where models drift most: reject drifted ones rather than fixing in
  prose.
- Marketplace images: check the target marketplace's current rules before upload (Amazon main image: pure white, product
  about 85% of the frame); a `full-set` is 13 jobs, so cost it as 13.
- Label AI-made content where TikTok, Meta or Amazon require it.

### Higgsfield job rules [higgsfield-generate, product-photoshoot, marketplace-cards, soul-id]
- Run with `--wait` (one command, blocks, prints the URL); `--json` only for chaining. Timeouts may still bill: check
  `higgsfield generate list --json` before any rerun.
- Every local path in a media flag is uploaded to Higgsfield. Product/brand-kit import from a URL: the user's own store or site only.
- Enhancer commands own their prompt: pass a short intent; never call `gpt_image_2` directly for product shots (worse
  output) and never paste the enhanced prompt back.
- Marketing Studio: an ad reference video OR hook/setting blocks, never both; `--hook_id`/`--setting_id` only on `ugc`,
  `ugc_how_to`, `ugc_unboxing`, `product_review`, `ugc_virtual_try_on`; arrays as `@file.json`; DTC ads need a format the user
  picks; custom avatars only from consented faces.
- Discovery: run the unfiltered `higgsfield model list --json` / `workflow list` before saying a model or feature is missing.

### Character and scene prompt craft [banana-pro-director-30; full guide in `references/higgsfield-prompt-craft.md`]
- Order: existing-or-new check -> text spec -> Mode 0 face lock -> Mode 1 base outfit plate -> Mode 2A 3-panel sheet
  (headless front, rear, tight chest-up face) -> Mode 3 scene plates on request; Mode 4 detail and Mode 5 outfit swap on
  explicit request. Never skip or combine steps: every later image anchors to the locked face.
- Reference plates (Modes 0, 1, 2, 5) close with the flat grade: one even 18% gray value, shadowless matched-fill light,
  zero cast shadow, true skin and fabric color, baseline black camisole or ribbed tank for face locks. Gray, because video
  models amplify high-contrast edges; flat, because baked shadows get inherited by every later generation.
- References carry identity and geometry: one short visual handle per subject, words spent on composition, pose, light
  and the close; under about 2,500 characters with strong references.
- Scene plates: five unlabeled DP-prose paragraphs, resolution-aware detail (drop what the lens couldn't resolve),
  positional words instead of coordinates, the cinema-stack close with "photographed not generated".
- Universal: no character names or ages, flattering realism (fine even skin, never blemished), closed-lip default
  expression, no negative-prompt blocks, aspect ratio only as a flag.

### Product 360 and reveal video [seedance-product-360, corrected; full guide in `references/product-360.md`]
- Beats: 2 s hook matched to the category's energy -> hero angle -> rotation (slow 10-15 s, medium 5-8 s, fast 2-4 s per
  360) -> 2-3 macro details (2-5 s total) -> optional context -> finale on the hero angle.
- Product fills 50-80% of the frame; product-to-background contrast at least 3:1; light per category and material table.
- Seedance limits: 2.5 = 4-30 s up to 1080p; 2.0 = 4-15 s up to 4K. Longer stories are several shots (start/end frames
  from the same shoot) joined in the edit. One shot per prompt, under about 200 tokens; the long template is a planning sheet.
- Names, specs, prices and CTA are overlays in post; sound is native Seedance 2.0 audio, `seed_audio`, or music in the edit.

### Layout rules for banners, social and OG images [banner-design + design social-photos]
- Safe zone: critical content in the central 70-80%; nothing within 50-100 px of edges; YouTube channel art keeps
  content inside 1546 x 423 of 2560 x 1440; Meta/Instagram central 80% (UI chrome).
- 3-zone hierarchy: top = logo or value prop, middle = message + visual, bottom = CTA.
- One CTA, high contrast, bottom-right, >= 44 px tall, action verb (Get, Start, Claim, Shop).
- Max 2 typefaces; body >= 16 px, headline >= 32 px; contrast >= 4.5:1; ads <= 7 words a line and 3 lines.
- Text share: paid social ads under 20% of the canvas; social covers about 60/40 image to text.
- Print: 300 DPI (150 for large format), CMYK, 3-5 mm bleed, headlines 70 pt+ for 3-5 m viewing.
- File names: project convention first; otherwise `assets/banners/<campaign>/<style>-<w>x<h>.png`, date prefix
  `YYMMDD-` for time-bound campaigns [banner-design].

### Export (free, local) [design social-photos, banner-design]
```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1200,630 --virtual-time-budget=5000 --screenshot=og.png "file:///abs/path/og.html"
```
Then confirm pixel size (`sips -g pixelWidth -g pixelHeight og.png`) and that fonts loaded. With 2x scale the file is
2400 x 1260: downscale to the platform size if it has a hard limit. Playwright MCP (`browser_resize` +
`browser_take_screenshot`) is the alternative when the page needs interaction first.

### Enhance and optimize [image + image-enhancer, made concrete]
- Measure first: dimensions, format, file size, what is wrong (blur, noise, artifacts, too large).
- Keep the original as a sibling (`name-original.png`); write `name-enhanced.png`. Tune for the intended use (web,
  slides, print). Folders: loop the same steps per file and report size and dimensions before vs after.
- Screenshots: re-capture at 2x device scale instead of upscaling; upscaling adds no real detail.
- Photos/graphics (Pillow is on `python3.12`): upscale at most 2x with `Image.LANCZOS`, then
  `ImageFilter.UnsharpMask(radius=2, percent=80-150, threshold=3)`; `MedianFilter(3)` only on visibly noisy photos.
- Format: WebP default (photos and graphics), AVIF for max compression, PNG for transparency and UI text, SVG for logos
  and icons, JPEG as fallback. `cwebp -q 80 in.png -o out.webp` is installed; `sips -Z <px>` resizes.
- Web checklist: quality 75-85 for photos, near-lossless for screenshots; hero under 200 KB; resize to display size;
  explicit `width`/`height` (no layout shift); `loading="lazy"` below the fold; descriptive alt text; CDN auto-format.
- OG/social preview: 1200 x 630 plus `og:image`, `og:image:width`, `og:image:height`, `twitter:card=summary_large_image`,
  `twitter:image`; for many pages generate per-page OG images with `@vercel/og` / Satori [image].

### Video [video + remotion-video-creation + higgsfield-generate]
- Prompt = subject + action + camera move + style + mood; name the camera move (dolly, pan, static, pull back).
  Image-to-video is more controllable than text-to-video [fal-ai-media]. No readable text from AI video: overlay it.
- Seedance 2.5 modes: `t2v` (prompt only, no media), `omni_reference` (any references incl. `--start-image` /
  `--end-image`), `video_edit`, `video_extension`. Reframe an existing clip with the `reframe` workflow instead of
  regenerating it [higgsfield-generate].
- Captions always (most social video plays muted). Aspect: 9:16 social, 16:9 YouTube/site, 1:1 or 4:5 feed.
- Hyperframes vs Remotion: plain HTML/CSS + GSAP, short templated clips, no React project -> Hyperframes (one HTML file
  per composition: root `data-composition-id`, `data-duration`, `data-width`, `data-height`; clips `class="clip"` with
  `data-start`, `data-duration`, `data-track-index`; paused GSAP timeline registered in `window.__timelines`).
  React project, spring physics, rich captions, 3D/Lottie, or Lambda batch rendering -> Remotion.
- Remotion hard rules: every animation comes from `useCurrentFrame()`; write timings in seconds times `fps` from
  `useVideoConfig()`; CSS transitions/animations and Tailwind `animate-*` classes do not render; reference `public/`
  files with `staticFile()`; premount every `<Sequence>`; composition props must be JSON-serializable. Open the matching
  `rules/*.md` (captions, audio, fonts, transitions, charts, 3d, measuring-text) before writing that part.
- Pin tool versions in commands (`npx hyperframes@<version>`, `npx create-video@<version>`) and say in one line what
  gets installed. Remotion's license is free only below a company-size limit: check remotion.dev/license before commercial use.
- Avatars: Marketing Studio UGC presenters (Higgsfield, set up), HeyGen (best lip-sync, MCP, not set up) or Synthesia
  (corporate). Not for founder-authentic content or UI walkthroughs.
- Repurposing chain: clean up (Descript) -> auto-clip (Opus Clip) -> captions/styling (CapCut) -> schedule. Virality
  Predictor can score the cut's hook before posting; it is an attention proxy, not a sales result.

### Generative art [algorithmic-art]
1. Write the algorithmic philosophy (named movement, 4-6 paragraphs) as `.md`; weave in one quiet conceptual reference.
2. Read `templates/viewer.html` and build on it: seed section (display, prev/next, random, jump) and actions
   (regenerate, reset) stay; algorithm, params object and parameter controls change.
3. Seeded everything (`randomSeed(seed); noiseSeed(seed)`); same seed must give identical output; params are
   quantities, scales, probabilities, ratios, angles, thresholds. Thoughtful palettes, real-time performance.
4. Single self-contained HTML; p5.js from `cdnjs.cloudflare.com/ajax/libs/p5.js/1.7.0/p5.min.js` (allowed by the
   Artifact page policy).
5. Published as an Artifact, the page cannot start downloads: drop the Download PNG button or use the artifact file
   hand-off capability (`artifact-capabilities` skill). In a local HTML file the button works.

### GIFs [slack-gif-creator]
- Slack: emoji 128 x 128 (under 3 s), message GIF 480 x 480; 10-30 fps; 48-128 colors.
- Build frames with Pillow primitives through `core.gif_builder.GIFBuilder`; ease motion with `core.easing.interpolate`
  (ease_out, bounce_out, back_out, elastic_out); check with `core.validators.is_slack_ready`.
- Make it look crafted: lines width >= 2, gradient backgrounds, layered shapes, glows, contrasting outlines; no emoji fonts.
- Motion recipes in the member: shake, pulse/heartbeat, bounce, spin/wobble, fade, slide with overshoot, zoom,
  particle burst; combine two for richer loops.
- Optimize only when asked: fewer frames, fewer colors, smaller size, `remove_duplicates=True`, `optimize_for_emoji=True`.
- Setup: Pillow is on `python3.12`; `imageio` and `numpy` are not, so install them pinned into a scratchpad venv and say
  so. Import the helpers with `sys.path.insert(0, "<abs path of members/slack-gif-creator>")`; run from the scratchpad.
- Photoreal or illustrated animated GIFs the builder can't draw: `gpt_image_2_6 --output_format gif` (paid), then
  validate size and colors with the same validators.

## When members disagree

| Between | Conflict | Rule |
|---|---|---|
| imagegen vs Claude Code reality | imagegen prefers a built-in `image_gen` tool and allows its CLI only "when explicitly asked" | Claude Code has no built-in image tool, so the CLI is the OpenAI path. "Explicitly asked" becomes "the user approved this paid call" |
| imagegen script vs OpenAI retirements | script defaults to `gpt-image-1.5` (retires 2026-12-01); fal-ai-media's note still offers `gpt-image-1` (retired 2026-10-23) | Always pass `--model gpt-image-2.5-sunburst` after checking OpenAI's page; treat any `gpt-image-1` mention as stale |
| higgsfield-generate vs the user's spend rule | vendor: don't pre-estimate cost or offer cheaper models unless asked | Keep the quality default model, but always run the free cost check and ask once per batch; offer the cheap draft as an option, never swap silently |
| higgsfield-generate vs product-photoshoot vs banana-pro vs the user's autonomy rule | one question at a time / up to 4 labeled questions / a pre-prompt check every prompt / ask only blockers | One message: defaults as labeled options + pre-prompt bullets (references first) + the cost line. Skip it for small tweaks on an approved prompt |
| product members vs "never AI-generate the product" | product-photoshoot, marketplace-cards and product-360 generate the product | Allowed only when conditioned on the real product photo; verify against the real product; text-only product renders never ship |
| higgsfield-generate auto-pick vs banana-pro-director-30 | vendor: character sheets -> Seedream 5.0 Pro, Nano Banana Pro only when named; director: Banana Pro for face lock and sheets | Inside the director pipeline its models count as named (its prompts are written for them); one-shot face sheets from photos -> `seedream_v5_pro` |
| banana-pro-director-30 internal | "cinema stack closes Modes 0-5" vs "flat grade, no exceptions"; Mode 4 beauty lighting; 6-panel three-point light; Mode 0 "white background" | Every reference plate gets the flat 18% gray grade; the cinema stack only on finished stills (Mode 3 prose, Mode 4 as a deliverable, white-card stills) |
| banana-pro-director-30 internal | "no @image tags" vs the locked Mode 5 prompt using @image1/@image2 | Mode 5 is the one exception; pass the outfit reference first and prove the order on a count-1 run |
| banana-pro-director-30 vs higgsfield prompt safety | real brand names allowed vs avoid trademarks (`ip_detected`) | the user's own brands fine; third-party names only when the user asks; otherwise use original designs |
| seedance-product-360 vs media-studio video rules | text overlays and 20-28 s single prompts inside Seedance; Seedance "5-60 s" | Overlays in post; one shot per prompt under ~200 tokens; respect 4-30 s (2.5) and 4-15 s (2.0) |
| seedance-product-360 vs evidence | ray tracing, particle systems, text animation, "Higgsfield logo fine on Amazon" | Dropped as unsourced; platform rules checked on the platform |
| higgsfield delivery vs imagegen delivery | URLs only, no ids vs local path, prompt, provider, cost | Both: URL + downloaded local file + model + credits spent; no enhanced prompt unless asked |
| higgsfield bootstrap vs the user's security rules | run the vendor curl-pipe-sh installer when the CLI is missing | install the CLI from Homebrew; never run the installer; upgrades only with the user's OK |
| product-photoshoot vs prompt schema | "never write the GPT Image 2 prompt yourself" vs the shared schema | Schema for direct model calls; enhancer commands take a short intent line |
| banner-design vs imagegen | banner: generated visuals carry no text; imagegen: quote exact text in the prompt | HTML-composed assets: no text in pixels. Flat raster pieces where text must be baked in (poster, sticker): 3-5 words, verbatim, use a text-strong model, verify spelling |
| image vs brand-studio's design member vs Recraft on Higgsfield | image: AI logos are poor; design: generate logos with Gemini in 55 styles | AI makes logo concepts only (paid, ask); finals are hand-built SVG in brand-studio |
| imagegen vs image | imagegen: do not add details the user did not imply; image: always add style, lighting, aspect | Always add format and style words; add creative content (objects, brands, palettes) only if implied |
| algorithmic-art vs the user's brands | keep Anthropic colors and fonts in the viewer | Keep the template's structure and controls; for the user's brand work, swap the UI colors/fonts for the project's tokens. Keep Anthropic styling for neutral exploration |
| video vs remotion-video-creation | Hyperframes "recommended for agents" vs Remotion rules | Choose by the rule in Core rules > Video; don't port an existing Remotion project to Hyperframes |
| banner-design vs the user's autonomy rule | gather 6 answers via questions first | Ask only blockers; default the rest and list assumptions in the delivery |
| imagegen vs banner-design vs brand | output paths `output/imagegen/` vs `assets/banners/<campaign>/` vs brand asset naming | Project convention first; then the asset-type default; drafts in the scratchpad |
| fal-ai-media vs reality | "unified media via fal MCP" | fal is not set up and Higgsfield covers its models; recommend only if a model is missing |
| image-enhancer vs honesty | promises "upscaled to 4K, enhanced clarity" | Upscaling adds no detail; re-capture when possible and report what was actually done |
| code-drawn site imagery vs AI photos/video | banana-pro and seedance notes favour code-drawn scenes; Higgsfield allows AI imagery | Follow the user's brand: code-drawn scenes can stay the signature, AI hero loops, lifestyle, try-on and 360 are allowed, each batch cost-checked |

## Combine with

- Built-in skills: `anthropic-skills:canvas-design` (posters, static art), `anthropic-skills:algorithmic-art` (same as
  the member), `artifact-design` before publishing any page, `artifact-capabilities` for file hand-off or stored picks,
  `frontend-design:frontend-design` for type-led banners, `dataviz` when an image carries a chart.
- Superpowers: `superpowers:brainstorming` before a new visual direction, campaign or recurring character;
  `superpowers:dispatching-parallel-agents` for large variant sets (one agent per size or style; paid jobs still go
  through one approval); `superpowers:verification-before-completion` before "done".
- Agent prompts (`~/.claude/skill-library/agents/voltagent/`):
  `06-developer-experience/visual-asset-generator.md` (asset checklist for app icons, favicons, OG, social banners; skip
  its `npm install -g prompt-to-asset` step, that package is unreviewed), `01-core-development/ui-designer.md` (visual
  polish of composed assets), `01-core-development/frontend-developer.md` (Remotion or Hyperframes builds),
  `08-business-product/content-marketer.md` (what the asset should say and where it goes),
  `05-data-ai/prompt-engineer.md` (tighten a long prompt template under the ~200-token limit).
- Other super-skills: brand-studio (logo, palette, tokens), ads-and-measurement (ad creative strategy and ad specs),
  copy-and-content (headlines on the asset), conversion-lab (hero image placement, A/B tests of creatives), commerce-pro
  (uploading product media and listings to Shopify or marketplaces).

## House rules (the user)

- Paid generators ask first: Higgsfield credits (every job, incl. Virality Predictor and Soul training), OpenAI images,
  Gemini, fal, ElevenLabs, HeyGen, Runway and any AI upscaler. One question per batch with route, model, count, settings
  and the estimate; the dry run, `account status` and `generate cost` are free.
- Use the API or CLI route (scripts, Higgsfield CLI, Chrome headless, Playwright MCP) before clicking through a web UI;
  if a browser is truly needed, say why in one line.
- Keep keys in one credentials file outside any repo; export `GEMINI_API_KEY` only for the one command that needs it; never print or paste a
  key and never open `~/.config/higgsfield/`.
- Uploads to Higgsfield (product photos, design files, faces, videos, product or brand URLs) only for files the user approved
  for that batch; URL imports only from the user's own store or site.
- Faces: Soul ID, face locks, custom avatars and outfit swaps use only the user's own face with their say-so or a person's clear
  written OK; never recreate a real person's likeness. Soul training needs a paid Higgsfield plan (check the plan with `higgsfield account status`).
- Anything that publishes, posts or uploads an asset to a live store, marketplace, site or social account asks the user first;
  label AI-made content where TikTok, Meta or Amazon require it and check marketplace image rules before a listing upload.
- Store and conversion work: every visual must help a visitor buy. Real product imagery near the buy button, no explainer graphics; cost-check each batch.
- Installing a new tool (fal MCP, Hyperframes, imageio, a Higgsfield upgrade) means a reviewed source, a pinned version
  and one line telling the user; no curl-pipe-bash installers. Members without an upstream license are for personal use only; never republish their text.

## Members

| Member | Best at | Path |
|---|---|---|
| imagegen | OpenAI GPT Image CLI (generate/edit/batch, masks, transparency), use-case taxonomy, prompt schema, invariant-first editing, save-path hygiene | `members/imagegen/SKILL.md`, `references/{prompting,sample-prompts,cli,image-api}.md`, `scripts/image_gen.py` |
| imagen | Gemini image helper (stdlib only, PNG validation, no auto-retry of billable calls) | `members/imagen/SKILL.md`, `scripts/generate_image.py` |
| fal-ai-media | One API for image, video and audio models; seeds; cost estimation; model discovery | `members/fal-ai-media/SKILL.md` |
| image | Marketing image production: model-choice tree, placement workflows (hero, social, mockups, banners), web optimization, OG tags, OpenAI retirement dates | `members/image/SKILL.md`, `members/image/references/ai-image-prompting.md` |
| banner-design | Multi-option banner process, 22 art directions, safe zones, CTA and type rules, print specs, export naming | `members/banner-design/SKILL.md`, `members/banner-design/references/banner-sizes-and-styles.md` |
| video | Video approach choice (programmatic, AI, avatar, repurpose), AI video model table, edit-anatomy beat sheet, scripted demo recording | `members/video/SKILL.md`, `references/{ai-video-prompting,edit-anatomy,product-demo-recording}.md` |
| remotion-video-creation | 28 Remotion rule files (animation, sequencing, captions, audio, fonts, transitions, 3D, charts) | `members/remotion-video-creation/SKILL.md`, `rules/*.md` |
| algorithmic-art | Philosophy-first p5.js generative art with seeded variation and an interactive viewer template | `members/algorithmic-art/SKILL.md`, `templates/viewer.html` |
| slack-gif-creator | Slack GIF limits, GIFBuilder, easing, validators, animation recipes | `members/slack-gif-creator/SKILL.md`, `core/*.py` |
| image-enhancer | Enhancement intent (screenshots for docs, social, slides; keep originals); the concrete method is in Core rules | `members/image-enhancer/SKILL.md` |
| higgsfield-generate | Higgsfield CLI: model catalog and auto-picks, media flags, cost commands, Marketing Studio ads, DTC ads, brand kits, workflows, Virality Predictor, 3D, audio, errors | `members/higgsfield-generate/SKILL.md`, `references/{model-catalog,media-inputs,workflows,marketing-*,prompt-engineering,troubleshooting}.md`; merged in `references/higgsfield.md` |
| higgsfield-product-photoshoot | 10 product-photo modes with a backend prompt enhancer, mode tie-breakers, short labeled interview | `members/higgsfield-product-photoshoot/SKILL.md` |
| higgsfield-marketplace-cards | Marketplace main, secondary and A+ image sets by scope or asset list | `members/higgsfield-marketplace-cards/SKILL.md` |
| higgsfield-soul-id | Face identity training: photo rules, variants, use with Soul models | `members/higgsfield-soul-id/SKILL.md`, `references/{photo-guide,troubleshooting}.md` |
| banana-pro-director-30 | Photoreal character pipeline (face lock, outfit plates, 3-panel sheets, outfit swap), flat-grade reference plates, cinema-prose scene plates, anti-AI-look render rules | `members/banana-pro-director-30/SKILL.md`; merged in `references/higgsfield-prompt-craft.md` |
| seedance-product-360 | Product video craft: hooks, hero angles, light per category and material, rotation and camera library, multi-angle photo plans, overlay timing, review checklist | `members/seedance-product-360/SKILL.md`; corrected and merged in `references/product-360.md` |

If a member folder is missing (not installed), work from this file alone.
