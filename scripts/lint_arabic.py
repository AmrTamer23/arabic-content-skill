#!/usr/bin/env python3
"""Lint Arabic copy for common machine-translation smells and formatting issues.

Usage: python3 lint_arabic.py <file> [--source <en-file>] [--eastern-digits]
Works on any text file; for JSON locale files pass --source to also check keys/placeholders.
Exit code 1 if any issue is found.
"""
import json, re, sys, argparse

SMELLS = [
    (r"قم\s+ب", "`قم بـ` + verbal noun — use a direct imperative (أدخل، حدّث، حمّل)"),
    (r"قومي\s+ب|قوموا\s+ب", "`قومي/قوموا بـ` — use a direct imperative"),
    (r"ال\w+\s+الخاص(?:ة)?\s+(?:بك|بكم|بكِ)", "`X الخاص بك` — attach the pronoun (حسابك)"),
    (r"هل\s+أنت\s+متأكد\s+(?:من\s+)?(?:أنك|أن)", "`هل أنت متأكد أنك…` — shorten (حذف العنصر؟ / هل تريد…؟)"),
    (r"احصل\s+على\s+البد", "literal 'get started' — use ابدأ الآن"),
    (r"انقر\s+هنا", "'click here' — use a descriptive link/CTA"),
    (r"!{2,}", "stacked exclamation marks"),
    (r"عفواً?!|عفوًا!|عذراً?!", "'Oops!' calque — state what happened instead"),
    (r"[؀-ۿ]\s*\?", "Latin '?' after Arabic text — use ؟"),
    (r"[؀-ۿ]\s*,\s*[؀-ۿ]", "Latin ',' between Arabic words — use ،"),
    (r"[؀-ۿ]\s*;", "Latin ';' after Arabic text — use ؛"),
    (r"ـ{2,}", "tatweel/kashida stretching"),
]
PH = re.compile(r"\{\{?\s*[\w.]+\s*\}?\}|%(?:\d+\$)?[sd@fi]|<\/?\w+[^>]*>|\$t\([^)]*\)")
ICU_PLURAL = re.compile(r"\{\s*\w+\s*,\s*plural\s*,")
AR_CATS = ["zero", "one", "two", "few", "many", "other"]

def strings(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items(): yield from strings(v, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj): yield from strings(v, f"{path}[{i}]")
    elif isinstance(obj, str): yield path, obj

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file"); ap.add_argument("--source"); ap.add_argument("--eastern-digits", action="store_true")
    a = ap.parse_args()
    text = open(a.file, encoding="utf-8").read()
    issues = []
    try:
        data = json.loads(text); items = list(strings(data))
    except Exception:
        data = None; items = [(f"line {i+1}", l) for i, l in enumerate(text.splitlines())]
    for loc, s in items:
        for pat, msg in SMELLS:
            if re.search(pat, s): issues.append(f"{loc}: {msg}  →  {s.strip()[:80]}")
        if a.eastern_digits and re.search(r"[0-9]", re.sub(PH, "", s)): issues.append(f"{loc}: Western digits but project uses Eastern")
        if not a.eastern_digits and re.search(r"[٠-٩]", s): issues.append(f"{loc}: Eastern Arabic digits — project default is Western 0-9")
        if ICU_PLURAL.search(s):
            missing = [c for c in AR_CATS if not re.search(rf"\b{c}\s*\{{", s)]
            if missing: issues.append(f"{loc}: ICU plural missing Arabic categories: {', '.join(missing)}")
    if a.source and data is not None:
        src = dict(strings(json.load(open(a.source, encoding="utf-8"))))
        tgt = dict(items)
        for k in src.keys() - tgt.keys(): issues.append(f"{k}: missing key")
        for k in tgt.keys() - src.keys(): issues.append(f"{k}: extra key not in source")
        for k in src.keys() & tgt.keys():
            sp = {p for p in PH.findall(src[k])} | set(re.findall(r"\{\s*(\w+)\s*,\s*plural", src[k]))
            for p in sp:
                if p not in tgt[k]: issues.append(f"{k}: placeholder {p} missing")
    for i in issues: print(i)
    print(f"\n{len(issues)} issue(s)" if issues else "OK — no issues found")
    sys.exit(1 if issues else 0)

if __name__ == "__main__": main()
