# Platform specs (merged)

One table set built from image, banner-design, design (social-photos), video, slack-gif-creator and the
visual-asset-generator agent prompt. Where members differed, the value used is noted. Platforms change specs: when a
size is business-critical (ad upload, store listing), confirm it on the platform's help page.

## Social posts and stories

| Platform | Type | Size (px) | Aspect | Notes |
|---|---|---|---|---|
| Instagram | Feed post | 1080 x 1080 | 1:1 | 1080 x 1350 (4:5) takes more feed space |
| Instagram | Carousel | 1080 x 1350 | 4:5 | |
| Instagram | Story / Reel | 1080 x 1920 | 9:16 | keep the central 80% clear of UI |
| Facebook | Post / link share | 1200 x 630 | 1.91:1 | same file works as OG image |
| Facebook | Story | 1080 x 1920 | 9:16 | |
| X (Twitter) | Post image | 1200 x 675 | 16:9 | |
| X (Twitter) | Card / ad | 800 x 418 | 1.91:1 | |
| LinkedIn | Feed image | 1200 x 627 | 1.91:1 | |
| LinkedIn | Article cover | 1200 x 644 | 1.86:1 | |
| Pinterest | Pin | 1000 x 1500 | 2:3 | |
| TikTok | Cover | 1080 x 1920 | 9:16 | |
| Threads | Post | 1080 x 1080 | 1:1 | |
| YouTube | Thumbnail | 1280 x 720 | 16:9 | |

## Covers, headers and profile banners

| Platform | Size (px) | Notes |
|---|---|---|
| Facebook cover | 820 x 312 desktop; 640 x 360 mobile | design for both crops |
| Facebook event cover | 1920 x 1080 | |
| X header | 1500 x 500 | lower-left is covered by the avatar |
| LinkedIn personal cover | 1584 x 396 | keep content centered |
| LinkedIn company cover | 1128 x 191 | LinkedIn accepts up to 4200 x 700 |
| YouTube channel art | 2560 x 1440 | all text and logos inside the 1546 x 423 safe area |
| GitHub social preview | 1280 x 640 | |
| Product Hunt gallery | 1270 x 760 | up to 6 images, real UI |
| G2 profile | 1280 x 720 | product screenshots |
| Google Play feature graphic | 1024 x 500 | required for the listing |
| App Store screenshots | per device | see the aso skill (seo-suite) |

## Display ads (Google Display Network)

| Name | Size (px) | Notes |
|---|---|---|
| Medium rectangle | 300 x 250 | highest CTR, make this one first |
| Large rectangle | 336 x 280 | |
| Leaderboard | 728 x 90 | |
| Billboard | 970 x 250 | desktop hero |
| Half page | 300 x 600 | |
| Wide skyscraper | 160 x 600 | |
| Mobile banner | 320 x 50 | |
| Large mobile | 320 x 100 | |

## Website and email

| Type | Size (px) | Notes |
|---|---|---|
| Full-width hero | 1920 x 600-1080 | serve responsive sizes, WebP, under ~200 KB |
| Section banner | 1200 x 400 | |
| Blog header / OG image | 1200 x 630 | banner-design said 1200 x 628; 1200 x 630 is the OG standard |
| Email header | 600 x 200 | many clients block images: the email must read without it |
| App icon master | 1024 x 1024 | transparent, simple silhouette, readable at 16 px |
| Favicon | 32 x 32 or 64 x 64 (plus SVG) | derive from the logo mark, never AI |

## Marketplace listing images (verify before every listing upload)

| Marketplace | Rule of thumb | Source |
|---|---|---|
| Amazon main image | pure white background, product fills about 85% of the frame, real product only, no added text or badges | higgsfield-marketplace-cards house note; check Seller Central |
| Amazon secondary / A+ | infographics, lifestyle, multi-angle, what's in the box; A+ modules via `--scope aplus` | higgsfield-marketplace-cards |
| TikTok Shop, Shopify, Etsy | each has its own main-image and AI-label rules | check the platform help page |

Product videos for listings and stores: see `product-360.md` (platform video notes).

## Video aspect

| Placement | Aspect | Notes |
|---|---|---|
| TikTok, Reels, Shorts, Stories | 9:16 (1080 x 1920) | vertical, captions burned in |
| Feed (IG, FB, LinkedIn) | 1:1 or 4:5 | |
| YouTube, website, sales deck | 16:9 (1920 x 1080) | |
| AI-generated clips | 16:9, 9:16 or 1:1 | about 5-10 s per generation; Kling goes longer |

Captions on every social video; text overlays programmatic, never AI-rendered.

## GIF

| Use | Size | FPS | Colors | Length |
|---|---|---|---|---|
| Slack emoji | 128 x 128 | 10-30 | 48-128 | under 3 s |
| Slack message GIF | 480 x 480 | 10-30 | 48-128 | short loop |

## Print

| Type | Size | Specs |
|---|---|---|
| Roll-up banner | 850 x 2000 mm | 150 DPI ok for large format |
| Step-and-repeat | 8 x 8 ft | |
| Vinyl outdoor | 6 x 3 ft | |
| Trade show | 33 x 78 in | |
| All print | | 300 DPI (150 large format), CMYK, 3-5 mm bleed, 1 pt type per foot of viewing distance |
