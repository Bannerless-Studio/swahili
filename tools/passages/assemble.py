#!/usr/bin/env python3
"""Assemble tools/passages/*.txt (hand-written passage sources) into
tools/passages_src.json for `packbuilder passages`.

Source format, one passage per block:
    @ A1 | Title | names: Juma, Dar es Salaam | oop: lemma=reason; ...
    S <Swahili sentence> | <English>
    Q tf | T or F | <sentence index> | lemma,lemma | <statement> | <English>
    Q mc | <sentence index> | lemma,lemma | <question> | <English> | <key> ;; <wrong> ;; <wrong> ;; <wrong>
The key is written first; the assembler cycles it through positions 0-3.
Prints the per-level share of mc keys that are the unique longest option."""
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
RULES = {"coverage": {"A1": 0.95, "A2": 0.95, "B1": 0.93},
         "budget": {"A1": ["A2", 3], "A2": ["B1", 3], "B1": [None, 0]},
         "words_per_passage": {"A1": [60, 90], "A2": [90, 120], "B1": [110, 150]},
         "questions": [4, 5]}


def parse(path):
    out, cur = [], None
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        tag, _, rest = line.partition(" ")
        f = [x.strip() for x in rest.split("|")]
        if tag == "@":
            cur = {"lv": f[0], "title": f[1], "oop": {}, "names": [], "sentences": [], "questions": []}
            for extra in f[2:]:
                k, _, v = extra.partition(":")
                if k.strip() == "names":
                    cur["names"] = [x.strip() for x in v.split(",") if x.strip()]
                elif k.strip() == "oop":
                    for kv in v.split(";"):
                        if kv.strip():
                            a, _, b = kv.partition("=")
                            cur["oop"][a.strip()] = b.strip()
            out.append(cur)
        elif tag == "S":
            cur["sentences"].append([f[0], f[1]])
        elif tag == "Q" and f[0] == "tf":
            cur["questions"].append({"q": f[4], "en": f[5], "type": "tf", "options": None,
                                     "answer": f[1] == "T", "words": f[3].split(","), "sentence": int(f[2])})
        elif tag == "Q" and f[0] == "mc":
            opts = [x.strip() for x in f[5].split(";;")]
            cur["questions"].append({"q": f[3], "en": f[4], "type": "mc", "options": opts, "answer": 0,
                                     "words": f[2].split(","), "sentence": int(f[1])})
        else:
            sys.exit(f"{path.name}:{n}: cannot parse {line!r}")
    return out


def main():
    passages = []
    for p in sorted(HERE.glob("*.txt")):
        passages += parse(p)
    pos = 0
    longest = Counter()
    mc = Counter()
    tf = Counter()
    for i, p in enumerate(passages, 1):
        p["id"] = f"p{i:04d}"
        for q in p["questions"]:
            if q["type"] == "mc":
                key, wrong = q["options"][0], q["options"][1:]
                opts = wrong[:]
                opts.insert(pos % 4, key)
                q["options"], q["answer"] = opts, pos % 4
                pos += 1
                mc[p["lv"]] += 1
                if all(len(key) > len(o) for o in wrong):
                    longest[p["lv"]] += 1
            else:
                tf[(p["lv"], q["answer"])] += 1
    order = ["id", "lv", "title", "oop", "names", "sentences", "questions"]
    src = {"rules": RULES, "passages": [{k: p[k] for k in order} for p in passages]}
    (HERE.parent / "passages_src.json").write_text(json.dumps(src, ensure_ascii=False, indent=1) + "\n")
    print(f"{len(passages)} passages", dict(Counter(p['lv'] for p in passages)))
    for lv in ("A1", "A2", "B1"):
        if mc[lv]:
            print(f"{lv}: key unique-longest {longest[lv]}/{mc[lv]} ({longest[lv] / mc[lv]:.0%}); "
                  f"tf true {tf[(lv, True)]} false {tf[(lv, False)]}")


if __name__ == "__main__":
    main()
