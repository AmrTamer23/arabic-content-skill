# Writing Rules

## Contents
1. Translation smells (and fixes)
2. Addressing the user & gender
3. Sentence patterns by string type
4. Punctuation & typography
5. Tone calibration
6. Tone by situation (good news, neutral, bad news)
7. Accessibility & inclusive language

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

**Form placeholders & help text** — a placeholder is a hint, not a label (the label stays visible above the field). Three useful shapes:
- a direct question: `ما اسم المنتج؟`
- a realistic example: `مثال: أحمد العتيبي`، `name@example.com`
- a filter/sort cue: `ابحث بالاسم أو رقم الطلب`
Help text under a field is the shortest version that removes doubt: `8 أحرف على الأقل` rather than a full sentence repeating the label. Never put critical instructions only in a placeholder — it disappears when the user starts typing.

**Validation** — short, attached to the field: `هذا الحقل مطلوب`، `أدخل بريدًا إلكترونيًا صحيحًا`، `يجب أن تتكون كلمة المرور من 8 أحرف على الأقل`.

**Empty states** — treat them as the start of something, not a failure. Say what will appear here and offer the first action:
- `ستظهر طلباتك هنا` + `ابدأ التسوق` (better than a bare `لا توجد طلبات`)
- `لم تحفظ أي عنوان بعد` + `أضف عنوانًا`
- Search with no results is different — it *is* a dead end, so help the user recover: `لا توجد نتائج لـ «{query}»` + `جرّب كلمة أخرى أو تصفّح الأقسام`.
Never apologize in an empty state (`عذرًا، لا توجد…`) — nothing went wrong.

**Confirmations / toasts** — very short: `تم الحفظ`، `تمت الإضافة إلى السلة`، `تم نسخ الرابط`.

**Success screens** (not toasts — full screens or cards after a meaningful action) — confirm what happened in terms of the user's goal, then say what happens next:
- `تم استلام طلبك. سنرسل لك إشعارًا عند خروجه للتوصيل.`
- `أُرسلت الحوالة. ستصل إلى المستفيد خلال دقائق.` — only state timings the product actually guarantees (see "Don't add claims" in SKILL.md).
- Add one next action when there is a natural one: `تتبّع الطلب`، `العودة إلى الرئيسية`.

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

## 6. Tone by situation

The brand voice stays fixed; the tone shifts with what just happened to the user. Decide which of three situations a string belongs to before writing it.

| Situation | Examples | Do | Avoid |
|---|---|---|---|
| **Good news** — success, welcome, milestone | order placed, payment done, first login | Warm and brief; credit the user, not the product; point to the next step | Self-congratulation (`نجحنا في…`), over-celebration on routine actions, stacking `!` |
| **Neutral** — information, instructions | form labels, settings, explanations | Direct and confident; tie the action to its benefit (`فعّل الإشعارات لتعرف موعد وصول طلبك`) | Hedging (`يمكنك إن أردت…`), commanding without a reason, piling on politeness |
| **Bad news** — errors, failures, declines, cancellations | payment failed, session expired, item unavailable | Honest and calm: what happened → what to do now; one apology at most, only when the product is at fault | Blaming the user (`أدخلت رقمًا خاطئًا`), vague errors (`حدث خطأ` alone), jokes, emoji, technical codes in the main message |

Bad-news patterns:
- Product's fault → brief apology + recovery: `عذرًا، تعذّر إتمام الدفع. حاول مرة أخرى أو اختر طريقة دفع أخرى.`
- User input issue → no apology, no blame, describe the fix: `يتكون الرمز من 6 أرقام` rather than `الرمز الذي أدخلته خاطئ`.
- External cause (bank declined, no network) → name the cause plainly, then the options: `رفض البنك العملية. تحقّق من بيانات البطاقة أو تواصل مع البنك.`

## 7. Accessibility & inclusive language

**Plain language** — everything in this guide already pushes toward it: short sentences, common words, one idea per sentence, the most important information first. This matters more in Arabic UI because many users read in their second-best script on small screens.

**Disability language** — use person-first, respectful terms:

| Use | Avoid |
|---|---|
| `ذوو الإعاقة` / `الأشخاص ذوو الإعاقة` (neutral, formal) | `المعاقون`، `العاجزون` |
| `أصحاب الهمم` (UAE official term) / `ذوو الهمم` (common in Egypt) | — use only when the market or brand already does; `ذوو الإعاقة` is the safe default |
| `مستخدمو قارئ الشاشة` | `المكفوفون` when you mean screen-reader users generally |
| `يستخدم كرسيًا متحركًا` | `مُقعد`، `حبيس الكرسي` |

**Alt text and accessible labels** — write them in Arabic, describe the purpose not the file:
- Image alt: `صورة: غلاف كتاب «موسم الهجرة إلى الشمال»` not `image.jpg` or `صورة`.
- Decorative images: empty alt (`alt=""`), not a description.
- Icon-only buttons need an accessible label in Arabic: `aria-label="إغلاق"`، `aria-label="إضافة إلى المفضلة"` — the visible icon doesn't speak.
- Don't repeat the role (`زر إغلاق`) — screen readers announce "button" already.
- Links say where they go: `اعرف المزيد عن رسوم التحويل` beats a bare `اضغط هنا` when the link stands alone.

**Don't encode meaning only in color or emoji** — `✓` or a green border needs text too (`تم الحفظ`).

