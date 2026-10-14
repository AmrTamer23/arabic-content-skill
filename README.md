# arabic-content

A Claude Code skill for writing native-quality Arabic content for apps and websites — UI strings, locale files, landing pages, store listings, newsletters — in the style of leading Arabic products instead of literal machine translation.

## Install

```bash
npx skills add AmrTamer23/arabic-content-skill
```

Or manually:

```bash
git clone https://github.com/AmrTamer23/arabic-content-skill.git ~/.claude/skills/arabic-content
```

Claude Code picks it up automatically in new sessions. Invoke explicitly with `/arabic-content`.

## Per-project settings

Add `.claude/arabic-style.yml` to a project:

```yaml
dialect: msa            # msa | egyptian | gulf
profile: super-app      # super-app | big-tech | gov-fintech | egyptian | editorial
address: masculine      # masculine | plural | neutral
numerals: western       # western | eastern
market: SA
```

## Contents

- `SKILL.md` — workflow
- `references/` — style profiles (distilled from Careem, Talabat, Tamara, Tabby, Apple, Google, Microsoft, Absher, Al Rajhi, Emirates NBD, Breadfast, InstaPay, valU, Thmanyah — observed October 2026), UI glossary, dialects, writing rules, formatting
- `scripts/lint_arabic.py` — linter for translation smells, punctuation, Arabic plurals, keys and placeholders

```bash
python3 scripts/lint_arabic.py ar.json --source en.json
```

- `evals/evals.json` — test prompts
