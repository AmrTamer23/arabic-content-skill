# Writing Rules

## Contents
1. Translation smells (and fixes)
2. Addressing the user & gender
3. Sentence patterns by string type
4. Punctuation & typography
5. Tone calibration

---

## 1. Translation smells

These are the patterns that make Arabic read as machine-translated. Each has a native alternative.

| Smell | Example (avoid) | Native |
|---|---|---|
| `قم بـ` + verbal noun | قم بإدخال رمز التحقق | أدخل رمز التحقق |
| `الخاص بك / الخاصة بك` | البريد الإلكتروني الخاص بك | بريدك الإلكتروني |
| Passive `يتم/تم` for actions the product does | يتم معالجة طلبك | نجهّز طلبك الآن / طلبك قيد التجهيز |
| `هل أنت متأكد أنك تريد…؟` | هل أنت متأكد أنك تريد حذف هذا العنصر؟ | حذف هذا العنصر؟ / هل تريد حذف العنصر؟ |
| Literal idioms | احصل على البدء / أنت جاهز تماماً للذهاب | ابدأ الآن / كل شيء جاهز |
| English word order (adjective piles) | تجربة تسوق سريعة سهلة آمنة جديدة | تسوّق بسرعة وأمان |
| `من خلال` / `عن طريق` everywhere | ادفع من خلال استخدام البطاقة | ادفع بالبطاقة |
| `بنجاح` on every success | تم تحديث الملف الشخصي بنجاح | تم تحديث ملفك الشخصي ✓ (`بنجاح` is fine occasionally, not on every toast) |
| Overused `عزيزي العميل` | عزيزي العميل، طلبك في الطريق | طلبك في الطريق |
| Possessive chains (إضافة × 4) | زر تأكيد عملية دفع الطلب | تأكيد الدفع |
| Calqued "please" in every string | من فضلك أدخل اسمك من فضلك | أدخل اسمك (`يُرجى` only for formal/gov) |
| `عفواً! حدث خطأ ما` style "Oops" | عفواً! حدث خطأ ما! | حدث خطأ، حاول مرة أخرى |
| Exclamation stacking | !!! | One `!` at most, mostly none |
| Translating "you" as `أنت` at sentence start | أنت يمكنك الآن تتبع طلبك | يمكنك الآن تتبع طلبك |
| Capital-letter emphasis rendered as quotes | اضغط على "التالي" | اضغط **التالي** (or no marking) |
| Literal "Click here" | انقر هنا لمعرفة المزيد | اعرف المزيد |

Also watch for:
- **Over-formal MSA in casual products** (`نودّ إحاطتكم علماً بأنه…` in a food app). Match the profile.
- **Classical vocabulary nobody uses in apps** (`الولوج` for login, `الحاسوب` where `الكمبيوتر` is standard in the market). Prefer the term the reference brands use (see glossary).
- **Demonyms that collide with common words.** Some city/country adjectives already mean something else: `الرياضيون` reads as "athletes", not "Riyadh people". Use `أهل الرياض` / `سكان الرياض` / `في الرياض` instead. Re-read every coined demonym or nisba (`ـي/ـيون`) for a second meaning.
- **Inconsistent hamza/tā' marbūṭa** (`انشاء` vs `إنشاء`, `مكافاة` vs `مكافأة`). Write correct hamzas: `إنشاء، أضف، إلغاء، مكافأة، اسأل، مسؤول`.
- **Tanween on alif placement**: write `أيضًا / شكرًا / مجانًا` (tanween on the letter before alif) consistently — or omit diacritics entirely (`أيضا`). Pick one per project; modern brands mostly include it on common words.

## 2. Addressing the user & gender

Arabic verbs and pronouns are gendered. The project setting `address` decides the strategy:

- **masculine** (most common in Gulf consumer apps and big tech): masculine singular imperatives and pronouns — `ابدأ`، `حسابك`، `يمكنك`. This is accepted as the generic form.
- **plural** (formal, gov, banks, some brands): `ابدؤوا`، `حسابكم`، `يمكنكم`. Respectful but heavier; good for gov-fintech and email salutations.
- **neutral**: avoid gendered forms where possible:
  - Verbal nouns for buttons and labels: `تسجيل الدخول`، `إضافة إلى السلة`، `متابعة`
  - Unvocalized `ـك` is gender-ambiguous on the page (`حسابك` reads as both) — fine to use.
  - `يمكنك` / `بإمكانك` instead of an imperative.
  - First-person plural from the product: `سنرسل لك رمزًا` instead of `استلم رمزًا`.
  - Nouns as headings: `طلباتك`، `المفضلة`.
  - Avoid imperatives in body text where possible; in buttons prefer verbal nouns.

Whatever the setting, never mix (e.g. `ابدئي` on one screen and `ابدأ` on another), and don't use `انت/انتي` slash forms (`سجّل/ي`) in product UI — it looks bureaucratic.

The product refers to itself as `نحن` (implicit in verbs: `سنرسل`، `أرسلنا`) — not in the third person (`سيقوم التطبيق بإرسال`).

## 3. Sentence patterns by string type

**Buttons / CTAs** — 1–3 words. Imperative or verbal noun, one convention per product.
`ابدأ الآن`، `اطلب الآن`، `متابعة`، `حفظ`، `إلغاء`، `اعرف المزيد`، `حمّل التطبيق`

**Titles / headers** — noun phrases: `طلباتك`، `طرق الدفع`، `الإشعارات`.

**Headlines (marketing)** — short, benefit-first, often two beats:
- Verb + benefit: `اطلب أكلك المفضل في دقائق`
- Noun + promise: `تسوّق اليوم، وادفع لاحقاً`
- Contrast/parallelism works well in Arabic (rhythm and near-rhyme are valued): `أسرع، وأسهل، وأوفر`
Avoid pure literal versions of English puns; find an Arabic rhythm instead (or drop the pun).

**Errors** — say what happened + what to do, no blame, no "Oops":
`رقم الجوال غير صحيح. تأكد منه وحاول مرة أخرى.`
`انتهت الجلسة. سجّل الدخول من جديد.`
`تعذّر الاتصال بالإنترنت.` (`تعذّر` is the idiomatic "couldn't")

**Validation** — short, attached to the field: `هذا الحقل مطلوب`، `أدخل بريدًا إلكترونيًا صحيحًا`، `يجب أن تتكون كلمة المرور من 8 أحرف على الأقل`.

**Empty states** — reassure + next step: `لا توجد طلبات بعد` + `ابدأ التسوق`.

**Confirmations / toasts** — very short: `تم الحفظ`، `تمت الإضافة إلى السلة`، `تم نسخ الرابط`.

**Destructive confirmations** — question title + clear verbs on buttons (not "Yes/No"):
title `حذف العنوان؟` body `لن تتمكن من استعادته.` buttons `حذف` / `إلغاء`.

**Push notifications** — title ≤ ~30 chars, body ≤ ~90 chars; this is where dialect and emoji (if the brand uses them) belong.

**Legal / policy** — formal MSA, full sentences, `يُرجى`، `يحق لـ`، `وفقًا لـ`. Don't simplify legal meaning for style.

## 4. Punctuation & typography

- Arabic comma `،`, semicolon `؛`, question mark `؟`. Period and exclamation are the same glyphs `.` `!`.
- Quotation marks: `«…»` (formal/editorial) or `"…"`; pick one per project.
- No space before punctuation; one space after.
- Don't use Latin-style ALL CAPS emphasis or italics — Arabic has no case and italic Arabic looks broken. Use weight (bold) or color.
- Kashida/tatweel (`ـــ`) to stretch words: not in UI by default (Thmanyah uses it as a brand signature in short labels — only if the project opts into that look).
- Diacritics (tashkeel): only where needed to disambiguate or for the shadda on short imperatives that would otherwise misread (`حمّل`، `فعّل`، `سجّل`). Don't fully vocalize UI text.
- Ellipsis `…` single glyph: `جارٍ التحميل…`
- Loading states: `جارٍ التحميل…` / `جاري التحميل…` — `جارٍ` is correct MSA; `جاري` is very common in apps. Pick one.

## 5. Tone calibration

| Profile | Feels like | Avoid |
|---|---|---|
| super-app | Friendly, quick, confident, benefit-led | Bureaucratic MSA, long sentences |
| big-tech | Clean, precise, calm, helpful | Slang, hype, exclamation marks |
| gov-fintech | Clear, respectful, reassuring, exact | Jokes, emoji, vague promises |
| egyptian | Warm, witty, conversational | Dialect in legal/payment/error-critical text |
| editorial | Sober, curious, confident, analytical | Hype, clichés, `تم`/`قام بـ`, italics |
