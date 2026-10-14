# Formatting & Technical Correctness

## Contents
1. Numbers, currency, dates
2. Mixed Arabic/Latin text (bidi)
3. Placeholders & plurals in i18n files
4. File-format notes
5. RTL layout notes for developers

---

## 1. Numbers, currency, dates

**Numerals.** Most modern GCC and Egyptian apps use Western digits (0–9) in UI, prices, and OTPs — it matches card numbers, phone keypads, and user expectations. Eastern Arabic digits (٠–٩) appear in some government, editorial, and traditional contexts. Follow the `numerals` setting; never mix both in one product.

**Currency** — follow the market. Reference brands put the Arabic unit **after** the number (`19 د.إ`, `250 جنيه`); formal bank/gov text spells it out (`10,000 ريال سعودي`); Microsoft's store is an exception (`ر.س.‏ 42.99/الشهر`). Default to number-then-unit:

| Market | Common Arabic forms | Example |
|---|---|---|
| SA | `ر.س` / `ريال` (new Riyal symbol ⃁ exists but has limited font support — use only if the project's font supports it) | `49.99 ر.س` |
| AE | `د.إ` / `درهم` | `120 د.إ` |
| EG | `ج.م` / `جنيه` | `250 جنيه` |
| KW | `د.ك` | `3.500 د.ك` |
| QA | `ر.ق` | `75 ر.ق` |
| BH | `د.ب` | |
| OM | `ر.ع` | |
| JO | `د.أ` | |

Many apps also show the ISO code (`SAR 49.99`, `AED 120`) — acceptable if the project already does it; be consistent. Use the platform formatter (`Intl.NumberFormat('ar-SA', {style:'currency', currency:'SAR', numberingSystem:'latn'})`) in code rather than hardcoding when generating code.

**Percentages**: `20%` (sign after the digits) is what the reference brands use; `%20` also appears (Google Workspace) — follow existing project usage, default `20%`. Discounts: `خصم 20%`، `وفّر 30%`.

**Dates**: `14 أكتوبر 2026` (Egypt/Levant month names are also used in GCC: يناير، فبراير، مارس، أبريل، مايو، يونيو، يوليو، أغسطس، سبتمبر، أكتوبر، نوفمبر، ديسمبر). Iraqi/Levantine month names (كانون الثاني…) — only if targeting those markets. Saudi gov contexts may show Hijri alongside Gregorian (`1448/04/22 هـ`). Prefer relative time in feeds: `الآن`، `قبل 5 دقائق`، `أمس`.

**Calendar gotcha in code**: `Intl.DateTimeFormat('ar-SA')` (and `toLocaleDateString('ar-SA')`) defaults to the **Hijri (islamic-umalqura) calendar** and Eastern digits. For Gregorian dates with Western digits use `'ar-SA-u-ca-gregory-nu-latn'`, or `ar-AE`/`ar-EG` with `-u-nu-latn`. Mention this whenever you hand over date formatting code or a locale config for Saudi Arabia.

**Time**: `9:30 ص` / `9:30 م`.

**Phone numbers**: always Western digits, LTR, with country code `+966 5X XXX XXXX`, `+20 10 XXXX XXXX`.

## 2. Mixed Arabic/Latin text (bidi)

- Brand names, product names, code, URLs, emails: keep in Latin script. Sentences can contain them: `حمّل تطبيق Careem`.
- In HTML, wrap embedded LTR runs in `<bdi>` or `<span dir="ltr">` when they include punctuation or numbers at the edges, otherwise punctuation can jump to the wrong side.
- A placeholder that may contain Latin text (a username, product name) should be wrapped with Unicode isolates in plain-text formats if the UI renders raw strings: `⁨{name}⁩` (FSI…PDI). Only add these if the project already does, or mention them as a recommendation.
- Don't start a string with a Latin word if avoidable — it can flip paragraph direction in naive renderers. `Apple Pay متاح الآن` → `ادفع الآن عبر Apple Pay`.

## 3. Placeholders & plurals

**Placeholders**: keep them byte-identical — `{name}`, `{{count}}`, `%s`, `%@`, `%1$s`, `$t(key)`, `<0>…</0>`, HTML tags. Move them to where Arabic grammar wants them; don't preserve English position.

**Plurals** — Arabic CLDR categories:

| Category | Numbers | Example (`item` = منتج) |
|---|---|---|
| zero | 0 | `لا توجد منتجات` |
| one | 1 | `منتج واحد` |
| two | 2 | `منتجان` |
| few | 3–10 (and x03–x10) | `{count} منتجات` |
| many | 11–99 (and x11–x99) | `{count} منتجًا` |
| other | 100, 101, 102, … | `{count} منتج` |

ICU example:
```
{count, plural,
  zero {لا توجد منتجات}
  one {منتج واحد}
  two {منتجان}
  few {# منتجات}
  many {# منتجًا}
  other {# منتج}
}
```

If the source string has a count but the format/library doesn't support plurals, either restructure to avoid agreement (`عدد المنتجات: {count}`) or flag it.

**Gendered variables**: if a placeholder is a person and the format supports `select`, use it; otherwise write neutrally.

## 4. File-format notes

- **JSON (i18next, next-intl, react-intl)**: same keys, same nesting; escape `"` inside values. Don't reorder keys.
- **ARB (Flutter)**: keep `@key` metadata blocks untouched; translate only values; ICU plurals as above.
- **iOS `Localizable.strings`**: `"key" = "value";` — keep semicolons; plurals go in `.stringsdict` or String Catalogs (`.xcstrings`) with `zero/one/two/few/many/other`.
- **Android `strings.xml`**: escape apostrophes `\'` (rare in Arabic) and `&` as `&amp;`; plurals via `<plurals>` with all six quantities.
- **gettext `.po`**: fill `msgstr`; `Plural-Forms: nplurals=6; plural=(n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5);`
- **Markdown/MDX/CMS content**: translate prose; keep code blocks, links' URLs, and frontmatter keys.

## 5. RTL layout notes (mention only when relevant)

When the task includes building or reviewing UI, not just text:
- `<html lang="ar" dir="rtl">`; use CSS logical properties (`margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `text-align: start`).
- Mirror directional icons (back/forward arrows, chevrons, progress) — don't mirror logos, media play buttons, clocks, checkmarks, or charts' time axes unless the design calls for it.
- Arabic needs more line-height (~1.6–1.8 for body) and slightly larger font size than Latin at the same visual weight. Good UI fonts: IBM Plex Sans Arabic, Noto Sans Arabic, Cairo, Tajawal, Almarai, Readex Pro, Rubik (Arabic subset), SF Arabic (Apple).
- Don't apply `letter-spacing` to Arabic — it breaks letter joining.
- Truncation: test with real Arabic strings; Arabic words are often shorter than English but taller.
