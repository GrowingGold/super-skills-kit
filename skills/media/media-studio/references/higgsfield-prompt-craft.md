# Photoreal character and scene prompt craft (merged)

Condensed from banana-pro-director-30 (1,127 lines), with its internal contradictions resolved and the Higgsfield CLI
mapping added. The member keeps the verbatim locked templates: open `members/banana-pro-director-30/SKILL.md` at the
named section when you need the exact wording. The member has no upstream license: personal use only,
never republish its text.

## Tool names -> Higgsfield ids

| Director says | Higgsfield id | Role |
|---|---|---|
| Banana Pro / Nano Banana | `nano_banana_pro` (alias `nano_banana_2`) | default for face lock, outfit plates, sheets, scene plates, outfit swap |
| GPT-2 | GPT Image 2 family: use `gpt_image_2_6` unless the user names GPT Image 2 | chest-up / face detail only, costs more credits |
| Soul Cinema | `soul_cinematic` | cheap, loose face exploration; outfit-on-bland-model step |

Inside this pipeline the director's model choices count as "named" models, so they override the Higgsfield auto-pick
(which would send character sheets to `seedream_v5_pro`). For a one-shot face sheet or face edit from photos, outside the
pipeline, use `seedream_v5_pro`. Aspect ratio goes in `--aspect_ratio`, never in the prompt text. Reference images go in
`--image` flags in the order the prompt names them. Prompt-only delivery (the user pastes into the Higgsfield web UI) is free;
a CLI run is paid and goes through the spend gate.

## The pipeline (strict order, one step at a time)

0. **Existing or new character?** Existing: read the reference images, mirror back a locked spec (face, bone structure,
   skin tone, hair color and texture, identity markers, proportions), wait for a yes. New: write a text spec first
   (apparent age register by build, never a number; face; hair; body; default makeup; default expression; identity
   markers), iterate until the user locks it.
1. **Mode 0 face lock (new characters only).** Identity only: 3:4 headshot, forehead to upper chest, body squared,
   neutral closed-lip expression, plain black thin-strap camisole (women) or plain black ribbed tank (men), no jewelry,
   logos or graphics. Tool fork, offered once: Banana Pro single pass (default); GPT Image single pass (highest fidelity,
   chest-up only, more credits; mention the cost once per conversation); Soul Cinema two-pass (Step 0.1 lean face plate
   with essentials only, then Step 0.2 Banana Pro 3:4 lock using that plate plus every fine marker).
2. **Mode 1 base outfit plate.** First image of every new outfit, before any sheet. Tool fork: Banana Pro writes the
   styling from the prompt (simpler outfits, one shot); Soul Cinema two-step builds the fit on a bland slim model
   (straight-on, arms relaxed, neutral face, medium-brown hair, gender-matched to the outfit), then composites it onto the
   locked character with a two-line prompt ("Place the face and body from reference image 1 onto the outfit from
   reference image 2" + the flat backdrop/light lines; no styling, character or cinema text). Pose default: cocked hip,
   body 15-30 degrees off camera, full body. Vary one parameter per extra shot (pose, framing, expression); never the face.
3. **Mode 2A 3-panel sheet (default sheet).** Only after an approved base plate. One horizontal frame, three equal panels:
   LEFT full-body front with the head removed (not cropped: full headroom kept); CENTER full-body rear with head; RIGHT
   tight chest-up face lock (collarbones up; if it drifts to waist-up the sheet is useless). Headless variant by neckline:
   A "ghost mannequin" hollow for structured necklines (tees, tanks, collars, hoods, keyholes: empty dark opening, inner
   back of the fabric faintly visible); B "clean neck cut" mannequin edge for strapless, halter, spaghetti strap, plunging
   or scooped necklines. Both: hair goes with the head, no blur, fade, wisps, stump, anatomy or gore at the cut. Identity
   and wardrobe described once at the top; each panel only says what differs; label panels LEFT / CENTER / RIGHT; the
   skin-tone consistency clause is mandatory (rear panels drift darker without it).
   **Mode 2B 6-panel (3x2)** only when the user names it: warn once that six cells starve the face panels of resolution.
4. **Mode 3 scene plates** (character in a world, or pure environment). Only when asked; often the start frame for a
   Seedance video, so match the camera language to the planned video.
5. **Mode 4 detail portrait** (chest-up or face) only on explicit request, on GPT Image.
6. **Mode 5 outfit replacement**: outfit-and-pose reference first, character reference second; the locked prompt is
   "Replace the character in @image1 with the character in @image2. Keep the outfit and pose from @image1 exactly. Match
   the face, bone structure, body type, skin tone, and hair from @image2." + clean mid-gray seamless, soft large-source
   light, true skin and outfit tone, natural grain, full body. Its `@image` tags are the one exception to "no image tags";
   prove the order on a count-1 run before a batch. To place the result in a scene, run Mode 3 on the Mode 5 output.

## Pre-prompt check (every new prompt; skip for minor tweaks)

One line "Pre-prompt check:", then bullets in this order: **References attached** (every uploaded image by a short visual
descriptor, or "none, pure text composition"), **Character**, **Outfit/styling**, **Backdrop or environment**,
**Framing** (only if non-default). Close with one short question. A missing reference in the list means the prompt is being
composed wrong. Skip the check for a small delta on a prompt approved in this thread (framing, pose, light nudge, one
garment swap); run it again for a new character, a full outfit swap, a new mode or a new environment. For CLI runs this
check is folded into the single paid-call request.

## Reference plates: the locked flat grade (Modes 0, 1, 2, 5, and Mode 4 when it feeds later work)

Why: plates are references, not finished frames. Any shadow, key direction or backdrop falloff baked in gets inherited
and amplified by every later generation, and pure white or black grounds create the high-contrast edges where video models
halo and "breathe". Mid-gray lowers that contrast.
Three things every flat close states (drop one and modelling comes back):
1. **Flat backdrop**: one even 18% neutral gray value corner to corner; no seam, gradient, hotspot, vignette or falloff.
   Neutral, never warm-shifted. White only when the user asks for a white card, and the flatness stays.
2. **Shadowless light**: one enormous soft frontal source at camera position, matched equal fill left, right, above and
   below; no key-to-fill ratio, shadow side, cheek triangle, nose or under-chin shadow, rim, hair light, kicker or hotspot.
3. **Zero cast shadow**: nothing on the background, no contact or drop shadow, no ambient occlusion under feet or hem.
Plus: skin matte and velvety (no T-zone shine), skin and wardrobe at their true natural color "never pale, washed-out or
cool-shifted by the background", fine even pore texture and peach fuzz, 50 mm prime, soft natural grain, "photographed not
generated". Verbatim block: member section "18% GRAY SEAMLESS + FLAT GRADE".

## Finished stills: the cinema stack (Mode 3 prose close, Mode 4 as a deliverable, white-card standalone stills)

Five render rules fight the AI look: real skin (fine, even pores, peach fuzz, subsurface scattering, no retouch or
dewy/glass skin), strand-level hair that reacts to the scene (matte by default), real lens character (clean 50 mm prime
for portraits; vintage 2x anamorphic for scenes: oval bokeh, edge falloff, light diffusion bloom), real light physics
(atmospheric haze between planes, filmic highlight roll-off, lifted but open blacks), real grain (color-negative film look,
fine 35 mm grain everywhere). The five strongest phrases:
- "atmospheric perspective with visible haze and air density between planes" (kills the flat "video game" staging)
- "shadow falloff into the neck, jawline, ear shadow, nostril shadow" (kills the uniformly lit AI face)
- "subsurface scattering at ear edges, nostrils, and around the eye sockets with warm undertone bleed"
- "highlights rolled off gently in a filmic curve, never clipping to pure white"
- "photographed not generated, captured on a real camera by a real cinematographer on a real set"
Environment-only plates drop the skin, hair and anatomy lines. Verbatim block: member section "THE CINEMA STACK".
Mode 4 deliverable lighting: soft key above camera-left at about 35 degrees, chest-level fill camera-right, subtle hair
light, soft under-bounce lifting the eye sockets.

## Flattering-realism ceiling (all faces)

Realism never means unflattering: no acne, blemishes, spots, scars (unless an identity marker), enlarged or cratered pores
or clinical macro texture. Matte carries the anti-plastic look; fine-and-even carries the flattering look. When they
conflict, resolve toward flattering.

## Lean prompts on strong references

References carry identity and geometry. Give each subject one distinguishing handle ("the woman with platinum-blonde hair
in the white unitard") and spend the words on what only the prompt can say: composition, pose, hands, expression, light,
plate-specific styling, then the close. Cut any sentence that re-describes an attached reference. Banana Pro weighs the
front of the prompt most; a 2,500-character prompt with strong references beats a 5,000-character one.

## Reading reference images (visual facts only, never invented)

Capture per character: hair (exact color nuance, length, texture, parting, styling, accessories), makeup (finish, brows,
eyes, lashes, lips, cheeks; freckles or marks only if visible), every garment top to bottom (fabric, color, fit,
construction, neckline, hem, layering, visible branding), every jewelry piece and accessory, visible piercings, tattoos,
nails, and pose/energy. Missing wardrobe for a new scene: ask, don't invent.

## Scene plates (Mode 3): the cinema-prose register

- Pick the cinema mode by scene: M1 narrative (street, kitchen, car, bar), M2 studio/editorial, M3 action/combat/chase,
  M4 performance/concert, M5 atmospheric/empty. Describe its look in plain words in the last paragraph; never camera,
  lens or film-stock brand names (the models don't parse them).
- Think silently in six buckets (shot DNA, subject + placement, visible detail, world, light + atmosphere, camera +
  finish), then write five unlabeled paragraphs: (1) one long opening sentence: medium, framing, subject, camera position,
  mood; (2) character as observed facts, pose, gaze, props, "carrying identically from the attached character reference";
  (3) world as ambience, not architecture, anchored to the attached world plate; (4) the focal anchor (screen, second car,
  horizon) or fold into 3; (5) camera spec + finish in plain words + the realism close ("Real photographic frame captured
  on a real cinema camera ... no CGI, no rendered look, no plastic surfaces, no AI smoothness, no skin smoothing, no glossy
  highlights").
- Resolution-aware detail: before each detail ask whether a real lens at this distance, motion blur and light level would
  resolve it; if not, drop it (a car at 200 ft and 120 mph shows silhouette, color blocks and lights, not decals).
- Placement in words, never coordinates: rule-of-thirds anchors ("anchored on the left third", "horizon at the upper
  third", "in the deeper background camera-left"); leave lead room in the direction of motion. The member's X/Y library
  is a planning aid only.
- No labeled blocks, no CRITICAL/MUST lines, no negations except the closing quality filter; write what IS there ("sleeves
  cut off cleanly at the shoulder seam") instead of what isn't.
- Night scenes: mostly dark with hard practical light cutting through (headlights, sodium lamps, neon, dash glow), haze
  catching the beams, rim light defining subjects, skin warm against cool ambient. Open-country night: practicals only,
  sky near-black, at most a faint distant horizon glow. Urban/interior night: teal-amber split only where practical sources
  motivate it. Never bright-night or teal-everywhere.

## Universal prompt rules

1. No proper names for characters: visual descriptors survive across prompts, names don't.
2. No ages or age words (boy, girl, teen, young, old, middle-aged): describe by role, build and clothing.
3. Brand names only for the user's own brands, or third-party ones the user asks for, always with the visual description; expect
   `ip_detected` on third-party marks. Prefer original designs.
4. No aspect ratios, internal production context, meta-commentary or negative-prompt blocks in the prompt text.
5. Default expression: neutral to a slight closed-lip smirk; no teeth-showing smile unless asked.
6. One prompt per fenced code block; several shots = several numbered blocks after one pre-prompt check.
7. Photoreal is the default; stylized (anime, illustration, painterly) only when the user asks.
