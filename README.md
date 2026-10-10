# OCR Scanner – PDF & Text

Static product website for Android package `com.chandra.ocr.offline`. The existing on-device engine supports 13 languages. The cloud-capable 1.4.0 update is in preparation; Datalab cloud processing is **not currently available**. Public remote advertising mode for supported releases is temporarily **TEST**: Native, App Open and Interstitial use Google test ads, and production ads are disabled. Ad display still depends on applicable privacy choices, confirmed Pro status and service availability.

**Website:** https://metosapps.github.io/ocr-scanner-website/

**Public support:** chennoufo11@gmail.com

## Pages and source

- `dist/index.html`: landing page, on-device features, planned optional cloud workflow, screenshots, FAQ and availability.
- `dist/privacy.html`: document handling, optional uploads, Google sign-in, Cloudflare/Datalab, expiry, purchases, ads and hosting; French/Arabic summaries.
- `dist/terms.html`: use, recognition limits, Free/Pro and optional cloud availability.
- `dist/support.html`: how-to, cloud setup unavailable, troubleshooting, purchases and data deletion.
- `dist/licenses.html`: notices synchronized from the app’s bundled component/model notices.
- `dist/404.html`: error page with the same current support content.

Public files in `dist/` are the editable source and deployment artifact. There is no generator or build step. The layout uses local approved images, system fonts and plain HTML/CSS/JavaScript. Earlier screenshots illustrate on-device flows; they do not demonstrate active Datalab processing. No fabricated ratings, testimonials, download counts or store URLs are used.

## Preview and checks

```sh
python3 -m http.server 4182 --directory dist
node --check dist/app.js
python3 verify.py
```

Open http://localhost:4182/. `verify.py` checks structure, local assets and links, and key current-mode disclosures. It does not verify a live cloud job or store purchase.

## Publication

The existing `Publish website` workflow validates JavaScript and pages, uploads only `dist/` and publishes through GitHub Pages after a push to `main`. Pages is configured with **GitHub Actions** as the source. No other hosting provider is involved. Edit `dist/`, validate, commit and push to `main`; verify the completed deployment and served public bytes before recording publication as complete.

Keep canonical URLs, sitemap, robots and hosting disclosures consistent. Provider credentials, Android binaries, signing material and backend source do not belong in this repository. The website contains no ad SDK, analytics, document uploader, sign-in form or payment form.

## App scope

On-device OCR, image/PDF import, page editing, local history/search/favorites and TXT export remain available offline. Interface and local OCR support EN, FR, AR, ES, DE, IT, PT, TR, RU, HI, Simplified Chinese, JA and KO. Arabic supports RTL. Local recognition gives simple text/formatting; manual crop/rotate/grayscale are supported. PDF/searchable-PDF export and automatic edge detection are not claimed.

Optional Datalab will require internet, Google sign-in and explicit document upload confirmation. Prepared pages go to the publisher’s Cloudflare server and authenticated Datalab API. Cloud document languages are detected automatically. A failed cloud request will not silently switch engines. Our content expires 24 hours after job creation, with scheduled cleanup that may be delayed; minimal quota/idempotency metadata is scheduled for removal 48 hours after expiry. This does not guarantee Datalab-side deletion. The public copy must continue saying cloud is unavailable until end-to-end setup is verified.

Free allows 3 pages per document. Pro allows 25 on-device or 10 cloud pages, Markdown/HTML exports and ad suppression, purchased once through Samsung IAP. Cloud quotas/concurrency/service availability still apply; Pro is not unlimited cloud access. Galaxy Store is authoritative for local price and purchase availability. Purchases use a Samsung account; cloud authentication uses Google, as distinct services.

## Cloud activation boundary for maintainers

Before consumer cloud activation, verify the publisher’s applicable Datalab service agreement permits delivering OCR outputs to app users and establish any required personal-data processing arrangement. Review the current [Datalab service agreement](https://www.datalab.to/terms/end-user-terms), especially personal-data and output-use provisions, and [Privacy Policy](https://www.datalab.to/terms/privacy). A configured API key alone does not establish these permissions. Use synthetic documents while setup and the appropriate agreement are unverified. Do not claim a provider retention period, training opt-out or consumer availability without evidence from the applicable account agreement and controls.

## Advertising

Native, App Open and Interstitial are configuration controlled. The current public remote mode is temporarily TEST for supported releases: Native, App Open and Interstitial use Google test ads; production ads are disabled. Bundled defaults remain disabled until a valid remote or cached configuration is accepted. Earlier clients using the legacy configuration remain OFF. Configuration enablement does not guarantee that an ad will be served. Confirmed Pro and required privacy choices gate ad requests. Document content and OCR language are not used for ad targeting. Remote settings downloaded from package-specific GitHub endpoints do not include documents or receipts. This website does not itself control app advertising or trigger a forced update; the app-specific remote configuration determines the active mode.

## Policy synchronization

The Android app’s bundled privacy/terms fragments are the content baseline for the website legal pages. Keep public HTML wrappers, navigation and canonical URLs. The backend static mirror is synchronized separately in the Android/backend workspace; deployment of this website does not deploy the backend. Both bundled and hosted copies must describe the same local/cloud distinction, current service status and retention semantics.

OCR Scanner is independent of Samsung, Google and Datalab. Their names and marks remain theirs; website artwork/text are not assigned an open-source license. Third-party notices apply to their respective components.
