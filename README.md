# OCR Scanner – PDF & Text

A professional static website for the on-device Android app `com.chandra.ocr.offline`, prepared release 1.2.1 (8).

**Website:** https://metosapps.github.io/ocr-scanner-website/

**Public support:** chennoufo11@gmail.com

## Pages

- [Landing page](https://metosapps.github.io/ocr-scanner-website/): features, simple how-to, six screenshot posters, FAQ and availability.
- [Privacy](https://metosapps.github.io/ocr-scanner-website/privacy.html): on-device data handling, website hosting, English with French and Arabic summaries.
- [Terms](https://metosapps.github.io/ocr-scanner-website/terms.html): usage terms and recognition limitations.
- [Support](https://metosapps.github.io/ocr-scanner-website/support.html): contact, troubleshooting and data deletion.
- [Open-source notices](https://metosapps.github.io/ocr-scanner-website/licenses.html): notices included with the Android release.

## Preview and checks

```sh
python3 -m http.server 4182 --directory dist
node --check dist/app.js
python3 verify.py
```

Open http://localhost:4182/. Public files are all in `dist/`. The layout uses local images, system fonts and plain HTML/CSS/JavaScript. No installation or build step is needed.

## Publication

The `Publish website` workflow validates links and JavaScript, uploads only `dist/`, then publishes to GitHub Pages after every push to `main`. Repository Settings → Pages uses **GitHub Actions** as the source. The workflow can also be started manually from Actions.

Edit the files in `dist/`, run the checks above, commit and push to `main`. Keep canonical URLs, `sitemap.xml`, `robots.txt` and privacy hosting disclosures consistent if the domain changes. See [GitHub's Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Content scope

The website describes camera capture, image/PDF import, multi-page drafts, manual crop/rotate/grayscale, English/French/Arabic on-device OCR, text/Markdown/formatted results, local history/search/favorites and TXT/Markdown/HTML exports. It does not advertise cloud OCR, automatic edge detection, table/image reconstruction or PDF export.

The Galaxy Store download link will be added once the listing is publicly available. No fabricated ratings, testimonials or download counts are used. The screenshot posters and app captures match the approved app materials.

Only website assets are included. Android binaries, backend source, signing material and provider credentials do not belong in this repository. No advertising, analytics, document uploads, contact form backend or external font scripts are added.

The app remains an independent product; Samsung Galaxy Store and third-party component trademarks belong to their respective owners. Website text and artwork have not been assigned an open-source license; third-party notices apply to their original components.

## Free and Pro

From 1.1.0: Free allows 3 pages per document and TXT export. Pro allows 25 pages, Markdown/HTML file exports and suppresses ads, purchased once through Samsung IAP. Approved proposed base price: USD 4.99; Galaxy Store is authoritative for local prices. Buying and restoring require internet and a Samsung account; OCR remains on-device. The app release and IAP product must be available before purchases can occur.

## Advertising and public configuration

Prepared version 1.2.1 supports Google AdMob Native, App Open and Interstitial placements with remote TEST / PRODUCTION / OFF selection. Current mode is OFF: test and commercial ads are disabled through the public remote configuration. The release supports future production selection; debug remains demo-only. Production activation requires this exact app to be live, explicit user authorization, applicable UMP messages and current Data Safety disclosures. Test requests still contact Google and can transmit advertising identifiers, connection metadata, interactions and diagnostics. UMP privacy choices gate ad requests; Settings exposes Ad privacy choices when required. Confirmed Pro suppresses ad loading. No document content or OCR language is used as ad targeting information.

The Android app also downloads package-specific public configuration from GitHub over HTTPS and caches it locally. GitHub receives normal connection metadata; documents and purchase receipts are not sent. See the [Privacy Policy](https://metosapps.github.io/ocr-scanner-website/privacy.html#ads). The website itself still contains no ad SDK, analytics or document uploads.
