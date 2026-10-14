# Dialects

Read this when `dialect` is `egyptian` or `gulf`. MSA is always the fallback.

## The register split (applies to every dialect)

Every reference brand that uses dialect keeps a hard line between surfaces. Following this is what makes dialect copy look intentional instead of unprofessional.

| Dialect OK | Keep MSA |
|---|---|
| Hero headlines, taglines | Navigation labels, tab bars, settings |
| CTAs on marketing pages, app-download prompts | Form labels, validation, errors |
| Onboarding slides, empty-state *encouragement* | Payment, transfer & order confirmations |
| Push notifications, promo banners, emails' subject lines | Amounts, fees, limits, terms, privacy, legal |
| FAQ/support voice (Tamara-style), chat-like help | Security, OTP, fraud warnings |

Within a single screen, don't mix: a promo card can be dialect, but the button under a payment summary is MSA (`تأكيد الدفع`, not `أكّد الدفع يلا`).

Light dialect is better than heavy dialect. One or two markers per sentence (`دلوقتي`، `اللي`) give the flavor; a full colloquial paragraph is harder to read and ages faster. Don't write dialect phonetically beyond what brands do (no `ءاخد`, no Franco/Arabizi like `3ayez` — except as an existing product name).

---

## Egyptian (`dialect: egyptian`)

**Markers** (MSA → Egyptian):

| MSA | Egyptian | Notes |
|---|---|---|
| الآن | دلوقتي | Most common marker in CTAs |
| الذي / التي / ما | اللي | `كل اللي تحتاجه` |
| اجعل / دع | خلّي | `خلّي الأكل علينا` |
| لكي / لأن | عشان | |
| ليس | مش | |
| ليس لها | ملهاش | |
| أكثر | أكتر | |
| تستطيع / يمكنك | تقدر | `تقدر تحوّل في ثواني` |
| تريد | عايز | |
| كيف | إزاي | |
| ستجد | هتلاقي | `هـ` future prefix |
| فقط / لكن | بس | |
| هكذا | كده | |
| معًا | مع بعض | |
| بكم | بكام | |
| حمّل (التطبيق) | نزّل | `نزّل التطبيق` |
| ينمو / يكبر | بيكبر | `بـ` progressive prefix |
| أموالك | فلوسك | |
| جرّب بنفسك | جرّب بنفسك | Same; works in both |
| مجاني | ببلاش / مجانًا | `ببلاش` very casual |
| لا تقلق | متقلقش | |
| سريعًا | بسرعة | |

**Patterns**: imperative + object + `دلوقتي`; "leave it to us" (`علينا`); `من غير` + hassle (`من غير وجع دماغ`); `كل اللي` + promise.

**Loanwords natural in Egyptian copy**: `أوردر`، `كاش`، `كاش باك`، `باقة`، `رصيد`، `ميجا`، `شحن`، `بيزنس`، `دليفري`.

**Spelling conventions**: follow standard Arabic spelling of the colloquial words (`دلوقتي` not `دلوئتي`; `عايز`; `هتلاقي`). Use `ڤ` for /v/ in loanwords only if the brand does.

**Example** (food delivery hero):
- MSA: `اطلب طعامك المفضل وسيصلك خلال دقائق`
- Egyptian: `اطلب أكلك المفضل ويوصلك في دقايق`
- CTA: `اطلب دلوقتي` — Nav/checkout stays `السلة` / `إتمام الطلب`.

---

## Gulf / Saudi (`dialect: gulf`)

Gulf brands use dialect much more sparingly than Egyptian ones — usually in FAQs/support, push notifications, and social-style promos (Tamara is the model). Hero copy is often still light MSA. When in doubt, use MSA with a Gulf-friendly word choice rather than full dialect.

**Markers** (MSA → Gulf/Saudi):

| MSA | Gulf | Notes |
|---|---|---|
| ماذا | وش / ايش | `وش` Najdi/Saudi, `ايش` Hejazi; `شنو` Kuwaiti/Bahraini; pick per market |
| ماذا سيحدث إذا… | وش يصير إذا… | Tamara FAQ style |
| فقط / لكن | بس | |
| كن / ابقَ | خلّك | `بس خلّك منتبه` |
| تريد | تبي / تبغى | `تبي` Najdi/Gulf, `تبغى` Hejazi |
| الآن | الحين / الحين | |
| كثير | وايد (UAE/KW) / مرّة (SA) | Market-specific |
| جيد / جميل | زين / حلو | |
| لماذا | ليش | |
| كيف | كيف | Same |
| سوف / سـ | بـ / راح | `بيوصلك` |
| لا تقلق | لا تشيل هم | |
| هيا | يلا | Common in CTAs/push |
| أنت | إنت | Rarely written; Tabby uses `بطريقتك إنت` for emphasis |

**Market sensitivity**: Saudi, Emirati, and Kuwaiti dialects differ (`وش` vs `شنو`, `مرّة` vs `وايد`). If `market` is a single country, use its forms; if pan-GCC, prefer markers shared across the Gulf (`بس`، `يلا`، `خلّك`، `زين`) or stay in MSA.

**Example** (BNPL FAQ):
- MSA: `ماذا يحدث إذا تأخرت عن الدفع؟`
- Gulf: `وش يصير إذا تأخرت عن الدفع؟`
- Answer stays clear, mostly MSA, maybe one marker: `ما عليك رسوم تأخير، بس خلّك منتبه لموعد الدفعة القادمة.`

---

## Other dialects

If asked for Levantine, Maghrebi, Iraqi, etc., the same register split applies. Use only markers you are confident about, keep to light dialect, and flag that a native reviewer from that market should check it.
