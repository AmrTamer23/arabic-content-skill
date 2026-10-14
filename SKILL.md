---
name: arabic-content
description: Write native-quality Arabic content for apps and websites — UI strings, buttons, onboarding, errors, notifications, landing pages, app-store listings, emails, blog posts, newsletters, podcast descriptions, and i18n/locale files (ar.json, ar.arb, Localizable.strings, strings.xml, .po). Writes in the style of leading Arabic products (Careem, Talabat, Noon, Tamara, Tabby, Apple/Google/Microsoft Arabic, Absher, Al Rajhi, Emirates NBD, Vodafone Egypt, InstaPay, Breadfast, and Thmanyah for editorial content) instead of literal machine translation, with configurable dialect (MSA, Egyptian, Gulf). Use this skill whenever the user asks to translate, localize, or write anything in Arabic for a product, adds Arabic/RTL support, creates or fills an `ar` locale file, asks for "Arabic version" of copy, or mentions Arabic-speaking markets (Saudi, UAE, Egypt, GCC, MENA) for app or web content — even if they just say "translate this to Arabic".
---

# Arabic Content

Write Arabic the way the best Arabic products already do — not the way a translation engine would. The goal is copy that a native user would assume was written in Arabic first.

## The core idea: write, don't translate

Machine translation maps English words onto Arabic words and keeps English sentence structure. The result is grammatical but instantly recognizable as foreign: `قم بتحميل التطبيق الخاص بك` instead of `حمّل التطبيق`. Arabic users notice this immediately and it makes a product feel cheap or untrustworthy.

So for every string:
1. Ask what the string *does* for the user (label an action? reassure? explain an error? sell a benefit?).
2. Ask how a reference product in the same category would say that thing in Arabic.
3. Write that — even if it shares few words with the source. Shorter is usually better.

The source English is a brief, not a template.

## Workflow

### 1. Load the project settings

Look for `.claude/arabic-style.yml` in the project root. If present, follow it. Format:

```yaml
dialect: msa            # msa | egyptian | gulf
profile: super-app      # super-app | big-tech | gov-fintech | egyptian | editorial (comma-separate to blend)
address: masculine      # masculine | plural | neutral  — how to address the user
numerals: western       # western (0-9) | eastern (٠-٩)
market: SA              # SA | AE | EG | KW | QA | ... (drives currency/date defaults)
brand_terms:            # terms that must stay as-is or use a fixed Arabic form
  Pro: Pro
  Wallet: المحفظة
notes: "Brand voice is playful but never sarcastic."
```

If the file is missing, infer sensible settings from context (product type, target country, existing Arabic strings in the repo — existing strings always win for consistency). Default to `dialect: msa`, `address: masculine`, `numerals: western`. State the settings you chose in one line and offer to save them to `.claude/arabic-style.yml` so the next session is consistent.

### 2. Pick the reference profile

Match the product category to the profile whose style to imitate, then read **`references/style-profiles.md`** for that profile:

| Product type | Profile |
|---|---|
| Delivery, e-commerce, ride-hailing, BNPL, lifestyle, consumer apps | `super-app` |
| SaaS, dev tools, devices, productivity, settings-heavy software | `big-tech` |
| Banking, payments, government, insurance, health, legal, telecom billing | `gov-fintech` |
| Egyptian consumer market (any category above, targeting Egypt) | `egyptian` (blend with the category profile) |
| Articles, blogs, newsletters, podcast/video descriptions, about & careers pages, long-form landing copy, content/media products | `editorial` (Thmanyah) — for the prose; keep the category profile for the functional UI |

A product can blend: a Saudi neobank's marketing site might be `super-app` for headlines and `gov-fintech` for the account-opening flow.

### 3. Pick the register per surface

Dialect is a setting, but not every surface should use it. Even brands that market in dialect keep critical surfaces in MSA:

| Surface | Register |
|---|---|
| Legal, terms, privacy, payments confirmation, security/fraud warnings, settings | Always MSA, clear and formal-light |
| Errors, validation, empty states, form labels, buttons | MSA (simple). Dialect only if `dialect` ≠ msa **and** the brand voice is casual |
| Onboarding, push notifications, promos, headlines, social-style CTAs | The configured dialect |

When `dialect` is `egyptian` or `gulf`, read **`references/dialects.md`** for markers and the MSA↔dialect switch rules.

### 4. Use the glossary

Read **`references/ui-glossary.md`** before writing UI strings. It has the established Arabic terms for common UI concepts (sign in, checkout, settings, OTP, etc.) and notes where reference brands differ. Pick one term per concept and use it everywhere — inconsistency (`تسجيل الدخول` on one screen, `دخول` on the next) reads as sloppy.

### 5. Write

Follow the rules in **`references/writing-rules.md`** (translation smells, gender-neutral techniques, sentence patterns, punctuation). The highest-impact rules, in brief:

- **No `قم بـ` + verbal noun.** `قم بتحديث التطبيق` → `حدّث التطبيق`.
- **No `الخاص بك`/`الخاصة بك`.** Attach the pronoun: `حسابك`, `طلباتك`.
- **Limit `يتم`/`تم` passives.** `يتم إرسال الرمز إلى هاتفك` → `سنرسل الرمز إلى هاتفك` or `أرسلنا الرمز إلى رقمك`. Keep `تم` only for short confirmations where it's idiomatic (`تم الحفظ`).
- **Buttons are 1–3 words**: imperative (`ابدأ الآن`) or verbal noun (`تسجيل الدخول`) — pick one convention per product and keep it.
- **Don't translate idioms literally.** "Get started" ≠ `احصل على البدء`; "You're all set" ≠ `أنت كلك مضبوط`.
- **Don't add claims the source doesn't make.** Adapting style is your job; adding facts isn't. A licence line ("regulated by the Central Bank"), "no hidden fees", a certification, a delivery time — these are legal/marketing commitments the user must own. If a section would benefit from one, suggest it in the notes after the copy, not inside it.
- **Use the domain noun, not the generic one.** "Item" in a food cart is `صنف` or `طبق`, in retail `منتج`, in a file manager `ملف` — `عنصر` only when the thing really is generic. This matters most in plural strings, where the noun is repeated across six forms.
- **Keep brand and product names in their official form** (usually Latin script), and don't translate feature names that are trademarks.
- **Arabic punctuation**: `،` `؛` `؟`. No Latin comma or question mark in Arabic text.

### 6. Formatting & technical correctness

Read **`references/formatting.md`** when the output includes numbers, prices, dates, phone numbers, mixed Arabic/English text, or goes into code (i18n files, HTML, CSS). Key points:
- Preserve every placeholder exactly (`{name}`, `%s`, `%1$d`, `{{count}}`, `<b>…</b>`) and position it where Arabic grammar wants it.
- Arabic has **six plural forms** (zero, one, two, few, many, other). When a string has a count, produce full ICU/ARB/stringsdict plural forms — never `{count} عناصر` for every number.
- Keep keys, file structure, and escaping identical to the source file.

### 7. Self-check before delivering

When the output is a file (or long enough to save to one), run the bundled linter — it catches the mechanical problems (translation smells, Latin punctuation, missing Arabic plural categories, dropped keys/placeholders):

```bash
python3 ~/.claude/skills/arabic-content/scripts/lint_arabic.py <ar-file> [--source <en-file>] [--eastern-digits]
```

Then read your Arabic back as if you'd never seen the English. Fix anything that:
- uses a pattern from the "smells" list in `writing-rules.md`,
- would not fit the UI element (long button, wrapped tab label),
- mixes registers inside one screen,
- uses the wrong tone for the situation (celebrating a routine action, blaming the user in an error, apologizing in an empty state),
- leaves an icon-only button or image without an Arabic accessible label/alt text (when you're writing UI code),
- uses a different term for a concept already used elsewhere in the project,
- breaks a placeholder or plural.

## Output

- **Single strings / short copy**: give the Arabic, and when there's a real choice (e.g. dialect vs MSA, two valid terms), give the recommended version first plus one alternative with a few words on when to use it.
- **i18n files**: write the full file in the same format as the source; don't add comments into the file unless the format supports them and they help translators.
- **Long-form (landing pages, store listings)**: write the Arabic directly, structured like the source but adapted — reorder or merge sentences where Arabic reads better.
- If the user writes in English and may not read Arabic, add a short English back-gloss for headlines or anything with a meaningful creative choice, so they can review intent. Skip it for routine UI labels unless asked.
- Flag anything you couldn't resolve (ambiguous source meaning, a term that needs a brand decision) in one line each after the content.
