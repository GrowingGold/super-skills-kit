# Higgsfield operating guide (merged)

Built from higgsfield-generate (SKILL.md + 12 references), higgsfield-product-photoshoot, higgsfield-marketplace-cards and
higgsfield-soul-id (all vendor skills v0.14.0). Model ids and params drift: the live schema
(`higgsfield model get <id> --json`, `higgsfield workflow get <name> --json`) beats anything written here. Full vendor
detail stays in `members/higgsfield-generate/references/<file>.md`.

## Setup checklist (check locally, nothing called)

| Need | State | How to confirm or fix |
|---|---|---|
| Account | your workspace and plan | `higgsfield account status` shows plan and credits; it spends nothing |
| CLI | `higgsfield` from Homebrew (`brew install higgsfield`, check the vendor docs) | Never run the vendor curl-pipe-sh installer; upgrade with `brew upgrade higgsfield` only after the user says yes |
| Auth | Logged in once; a credentials file exists under `~/.config/higgsfield/` | Never open or print that folder. On `Session expired` / `Not authenticated` / "Stored credentials are for ..." ask the user to run `higgsfield auth login` themselves (interactive) |
| MCP | The claude.ai Higgsfield connector may or may not load in Claude Code | Use the CLI when no Higgsfield tools load; it is the documented route |
| Helpers | `jq` reads `--json` output | `brew install jq` |
| Soul ID | Needs Basic plan or higher; free plan fails with `Minimum Basic plan required` | Upgrade is the user's call |

## Spend rules (the user's house rules beat the vendor's "don't pre-estimate cost")

1. `higgsfield account status`: plan and credit balance.
2. Estimate for free:
   - models: `higgsfield generate cost <model_id> <same flags as the real run>`
   - workflows: `higgsfield generate cost workflow <name> <flags>` (not `generate workflow cost`)
   - DTC ads: `higgsfield marketing-studio dtc-ads generate <flags> --cost-only`
   - product-photoshoot, marketplace-cards and soul-id document no cost flag: check `<command> --help`; if there is none,
     say "credits unknown until a count-1 run" and compare the balance before and after that run.
3. Ask the user once per batch with model, count, settings and credits (template in SKILL.md). Keep the quality default model;
   offer the cheap draft option (count 1, lower resolution, Z Image / Lite / Turbo) instead of silently downgrading.
4. Never auto-retry a failed or timed-out paid job. Check `higgsfield generate list --json` / `generate get <id> --json`
   first: a timeout on our side can still be a finished, billed job (rejoin with `generate wait <id>`).
5. Every local path passed to a media flag is uploaded to Higgsfield's servers. Send only files the user approved for that batch.

## Model ids (vendor catalog v0.14.0; confirm with `higgsfield model list --json`)

| Job | Id | Notes |
|---|---|---|
| General image, design, UI, on-image text, edits | `gpt_image_2_6` (GPT Image 2.6 Sunburst) | Vendor default. `--output_format` png, jpeg, webp, gif or svg; `--resolution 2k`; Flare is the separate id `gpt_image_2_6_flare`, never a `--variant` |
| Animated GIF / SVG | `gpt_image_2_6 --output_format gif` / `svg` | Set the format before the first job; GIF defaults `--size 288x288 --frame_count 9 --frame_duration_ms 200`; SVG takes no reference images |
| Cartoon / illustrated character, heavy texture | `nano_banana_flash` (Nano Banana 2) | `nano_banana_2` is an ALIAS FOR NANO BANANA PRO, not Nano Banana 2 |
| Top-fidelity Nano Banana (Banana Pro) | `nano_banana_pro` | Used by the character pipeline (prompt-craft reference) |
| Cheap reference edits / drafts | `nano_banana_2_lite` (up to 14 refs) / `z_image` (fastest, prompt-only) | Only when cheaper/faster is wanted |
| New original photoreal person (UGC, editorial, fashion) | `text2image_soul_v2` | `--quality 1.5k` or `2k`; presets `higgsfield preset list soul-v2` -> `--style_id` (not with `--image`); `--soul-id <ref>` for a trained Soul |
| Cinematic still | `soul_cinematic` | Same quality tiers, adds 21:9; `soul_cinema_studio` is a different model with `style_id` + `enhance_prompt` |
| Face sheet / face edit from reference photos | `seedream_v5_pro` | Up to 10 refs, resolution `1k`, `1.5k` or `2k` |
| Environment, no people | `soul_location` | Prompt-only, fixed size per aspect |
| Vector, icon, logo concept, controlled palette | `recraft_v4_1 --model_type vector` | Prompt-only; logo finals belong to brand-studio |
| Product brand visuals | `higgsfield product-photoshoot create` (enhancer on GPT Image 2) | Do not call `gpt_image_2` directly for product shots: it skips the enhancer |
| Marketplace listing images | `higgsfield marketplace-cards create` (enhancer on Nano Banana 2) | |
| Branded ad image | `marketing_studio_image` or `marketing-studio dtc-ads generate` | |
| Video default | `seedance_2_5` | 4-30 s, 480p/720p/1080p; modes `t2v` (no media) / `omni_reference` (any refs incl. start/end frames) / `video_edit` / `video_extension` |
| Native 4K video | `seedance_2_0` | 4-15 s, `480p..4k`, native audio on by default (`generate_audio`); say why you switched |
| Cheaper / faster video (only when asked) | `kling3_0_turbo`, Veo 3.1 Lite, Seedance 1.5 Pro | Kling 3.0 Turbo: 3-15 s, one start frame |
| Named video models | `cinematic_studio_video_4_0`, `kling3_0`, `veo3_1` (4/6/8 s, 16:9 or 9:16), `grok_video_v15` (needs one start image, 2-15 s), `gemini_omni_flash_1_1` | Cinema Studio ids do not appear in `model list`; use `model get` |
| Ad video (UGC, unboxing, try-on, review, TV spot) | `marketing_studio_video` | See Marketing Studio below |
| Audio: SFX, ambience, foley, voice-style, music bed | `seed_audio` | `sonilo_music` / `mirelo_text_to_audio` only when named (need `--duration`) |
| 3D mesh (GLB) from product photos | `multi_image_to_3d` | 1-4 `--image`, `--should_texture true`; a "3D-looking picture" is an image job |
| Score a finished video | `brain_activity` (Virality Predictor) | `--video` only, no prompt; returns a text report |

Guards: don't invent ids (`unknown model` error); don't downgrade because another schema looks simpler; prompt-only models
(Z Image, Recraft, Soul Cast, Soul Location) reject media flags; a model the user names stays for follow-ups on that work.

## Generic generation

```bash
higgsfield generate create <id> --prompt "..." [media flags] [param flags] --wait [--wait-timeout 20m] [--json]
```
- Media flags take a local path (auto-uploaded) or a UUID (upload id or previous job id): `--image`, `--start-image`,
  `--end-image`, `--video`, `--audio`; reference-array models use `--image-references`, `--video-references`,
  `--audio-references`. Accepted roles per model: `members/higgsfield-generate/references/media-inputs.md`.
- Check params once with `higgsfield model get <id> --json` and pass only what's needed. The server coerces a bad enum to
  the nearest allowed value ("adjustments") and rejects unknown params.
- Prompt from stdin: `echo "..." | higgsfield generate create z_image --wait`.

## Product photoshoot (`higgsfield product-photoshoot create`)

```bash
higgsfield product-photoshoot create --mode <mode> --prompt "<short intent>" --image <real product photo> [--count 1-10] [--aspect_ratio <ratio>]
```
| Mode | For | Pick when the request says |
|---|---|---|
| `product_shot` | neutral studio / catalog | white, clean, studio, catalog, Shopify |
| `lifestyle_scene` | product in a real place | in use, kitchen, outdoor, cafe, gym |
| `closeup_product_with_person` | hands / partial face | holding, applying, demonstrating |
| `moodboard_pin` | vertical 2:3 Pinterest aesthetic | Pinterest, pin |
| `hero_banner` | wide site / email / campaign header | hero, banner, header, landing page |
| `social_carousel` | 3-10 linked slides | carousel, swipeable (count = slides) |
| `ad_creative_pack` | coordinated static ad variants | ads, paid social (count = variants) |
| `virtual_model_tryout` | worn by an AI model | model wearing, try-on, lookbook |
| `conceptual_product` | surreal / CGI / levitating / splash | floating, splash, sculptural |
| `restyle` | new mood or season for an existing image | redo, Christmas version, change vibe |

- Tie-breakers: the more specific mode wins (Pinterest pin of a kitchen scene -> `moodboard_pin`; hero showing it in use
  -> `hero_banner`; carousel of scenes -> `social_carousel`).
- The backend writes the GPT Image 2 prompt: pass only a short intent line (product, use, mood, platform). Never paste the
  enhanced prompt back.
- `--count` variants vary preset, light, angle and palette; for carousel and ad pack the backend locks one visual system.
- Aspect: the backend picks per mode; override only on request (`1:1 4:5 5:4 3:4 4:3 2:3 3:2 9:16 16:9`). Resolution 2k.
- Questions (folded into the one cost message, labeled options): count `[1/3/5]`; style `[clean studio / lifestyle /
  conceptual / with a model]`; placement `[Shopify / Instagram / Pinterest / paid ads / site hero]`; brand colors if not
  known. Restyle: aesthetic, season, what to keep. Try-on: model archetype, environment, framing. No product photo: ask
  for one first (much higher fidelity).

## Marketplace cards (`higgsfield marketplace-cards create`)

| `--scope` | Creates |
|---|---|
| `main` | 1 main image |
| `product-images` | main + 5 secondary |
| `aplus` | main + 7 A+ modules |
| `full-set` | main + 5 secondary + 7 A+ |

Custom subsets: repeat `--asset` from `main_image infographic multi_angle detail_shot lifestyle whats_in_box
aplus_hero_banner aplus_pain_points aplus_features aplus_ingredients aplus_efficacy aplus_how_to_use aplus_endorsement`.
Context flags: `--product_context`, `--brand_context`, `--category`, `--visual_style`; reuse a finished main image with
`--main-job <job_id>`. The vendor keeps its compliance templates private, so still check the target marketplace's current
image rules yourself (Amazon main image: pure white background, product fills about 85%; TikTok Shop has its own rules).
A full set is 13 jobs: cost it as 13.

## Marketing Studio (ads)

- Concepts: avatar (preset, or custom from uploaded photos), product (from a URL or uploaded images), hook (opening angle,
  prepended to the prompt), setting (scene), ad reference (an inspiration video), brand kit (fetched from a site URL),
  ad format (DTC image templates). List what exists: `higgsfield marketing-studio <avatars|products|hooks|settings|ad-references|brand-kits|ad-formats> list --json`.
- Video modes (`--mode`, default `ugc`): `ugc`, `ugc_how_to`, `ugc_unboxing`, `product_showcase`, `product_review`,
  `tv_spot`, `wild_card`, `ugc_virtual_try_on`, `virtual_try_on`. `--hook_id` / `--setting_id` only on `ugc`,
  `ugc_how_to`, `ugc_unboxing`, `product_review`, `ugc_virtual_try_on`, and only on `marketing_studio_video`.
- An ad reference video and hook/setting blocks are mutually exclusive: offer one approach, never both.
- `--product_ids` and `--avatars` are JSON arrays passed as `@file.json` (never a bare UUID); aspect
  `auto|21:9|16:9|4:3|1:1|3:4|9:16`; resolution up to 720p or 1080p per the live schema; `--generate-audio true` for
  sound; `--wait-timeout 30m` for long runs. With a hook, pass products too (hooks pivot into a product).
- Click-to-Ad: `marketing-studio products fetch --url <url> --wait`, then `generate create marketing_studio_video --url <same url> ...`.
  Only the user's own store URLs; brand kits only from the user's own sites.
- DTC ads image: `marketing-studio dtc-ads generate --prompt ... --format-id <id> [--brand-kit-id] [--avatar] [--product]
  [--media <id>[:role]] [--aspect-ratio] [--resolution 1k|2k|4k] [--quality low|medium|high] [--batch-size 1-20] --wait`.
  The format is mandatory and the user picks it from `ad-formats list`; resolution, quality and batch size change cost, so
  confirm them; no auto-retry.
- Custom avatars and UGC presenters: consented faces only (house rules).

## Soul ID (identity training)

- Photos: 5-20 (8-12 best), one person, sharp, about 1024 px or more, JPEG/PNG; vary angle (front, 3/4 both sides, slight
  up/down), light, expression and distance. No group shots, sunglasses, hats over the face, costumes, heavy unusual makeup,
  repeated poses, or video files.
- `higgsfield soul-id create --name "<one word>" --soul-2 --image ... ` (`--soul-cinematic` for cinematic/video use),
  then `soul-id wait <id>` (30 min default, `--timeout 60m`), `soul-id list`, `soul-id get <id>`.
- Use: `generate create text2image_soul_v2 --soul-id <ref> --quality 2k` or `soul_cinematic`.
- `Training failed` -> fewer than 5 or too-uniform photos, occlusion, group photos, or video uploads.

## Workflows, analysis, 3D

- `higgsfield workflow list` / `workflow get <name>`; run with `higgsfield generate workflow <name> ... --wait`:
  `reframe --video in.mp4 --aspect-ratio 9:16 --resolution 720p [--mode std|pro]`;
  `draw_to_video --video in.mp4 --sketch frame.png --timestamp 3.2 --prompt "make the jacket red"`.
- Virality Predictor: `generate create brain_activity --video ./ad.mp4 --wait`. Report overall score, peak hook second,
  sustain, strongest/weakest region and the Open report link; lower Default Mode is better (less mind-wandering). It is an
  attention proxy, not a sales test: real A/B tests live in conversion-lab.
- 3D: `generate create multi_image_to_3d --image front.png --image side.png --should_texture true --wait`.

## Prompts (vendor basics, merged with the craft reference)

- Subject + setting + style, then camera (lens, angle, motion) and light; under about 200 tokens: models distort on long
  prompts.
- Image-to-image: describe the change, not the input. Image-to-video: the start frame is fixed, describe the motion.
- Phrase positively ("tack sharp", "uninhabited landscape"); most models have no negative prompt.
- Content policy ends jobs as `nsfw` or `ip_detected`: no real public figures, sexual content or third-party
  trademarked characters.

## Errors

| Message | Fix |
|---|---|
| `Missing required params: prompt` | ask for the prompt |
| `Missing required params: medias` (Virality) | pass exactly one `--video` |
| `Invalid values: x=y (allowed: ...)` | pick from the list |
| `Unknown params: x` | `model get <id>`; for `hook_id`/`setting_id` the mode or model doesn't support them |
| `failed`, `nsfw`, `ip_detected` | rephrase; ask the user before spending again |
| `Timeout after 10m` | `generate wait <id>` (the job may still finish and bill) |
| HTTP 429 | back off |
| HTML body with captcha-delivery | anti-bot; wait 30 s, retry once |

## Delivery

Vendor style: no raw ids or JSON in chat. The user's style adds the rest: result URL, the downloaded local file (scratchpad for
drafts, project asset folder for picks), model and settings, credits spent (balance before vs after), and what was checked.
No enhanced prompt text unless the user asks.
