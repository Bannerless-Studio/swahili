# tools/: Swahili pack builder inputs (dev/agent notes)

This directory holds the data Swahili owns: hand-maintained overrides, written sentences, drop lists, passage sources, and the reports the builder writes back. Swahili rules (tokeniser, lemmatiser, noun classes, linking) are code in vocab-engine `tools/packbuilder/langs/sw.py`.

## Files

- `build_pack.py`: **glue.** Runs `packbuilder build --lang sw --repo .` against `engine/tools`, or `PACKBUILDER_PATH` if set.
- `requirements.txt`: **config.** The shared builder requirements. Swahili needs no tagger model.
- `gloss_overrides.json`: **hand-maintained.** Gloss fixes keyed `"lemma|pos"`, for senses Wiktionary ranks wrongly or glosses with one sense only.
- `forced_a1.txt`: **hand-maintained.** The A1 core list forced into A1.
- `generated_examples.tsv`: **hand-authored input.** Swahili TAB English sentences written for this pack, for words the corpus leaves without a usable sentence. They ship as `"src": "gen"`.
- `bad_sentences.txt`: **hand-maintained.** Corpus sentences dropped by exact text, one per line, each after a `# <id> <note>` comment. These are the sentence review drops of 2026-09-29, read by the base-spec hook (vocab-engine 6e72e4c).
- `id_map_v1.json`: **generated, frozen.** The `"lemma|pos"` to word id map. Never hand-edit or renumber it; it keeps learner progress across rebuilds.
- `langs_sw.py.snapshot`: **safekeeping copy** of vocab-engine `langs/sw.py` from before it was committed. The build does not read it.
- `passages/a1.txt`, `passages/a2.txt`, `passages/b1.txt`: **hand-authored input.** Passage sources, 20 per level. The format is in the assemble.py docstring.
- `passages/assemble.py`: **glue.** Turns the three .txt files into `passages_src.json`, cycles each mc key through positions 0-3, and prints the share of keys that are the unique-longest option.
- `passages_src.json`: **generated** by assemble.py. It is the input to `packbuilder passages`.
- `REPORT.md`: **generated**, with the manual section kept across runs. It covers tagging stats, the word-selection funnel and levels, and holds the "Sentence review 2026-09-29" table.
- `REPORT_passages.md`: **generated**, with the manual QA section kept across runs. It gives coverage, level budget and question counts per passage.

## Passages workflow

1. Edit `passages/{a1,a2,b1}.txt`. Each block is `@ LV | Title | names: ... | oop: lemma=reason; ...`, then `S` sentence lines and `Q` question lines. Sentence indexes are 0-based.
2. `.venv/bin/python tools/passages/assemble.py` writes `passages_src.json`.
3. `PYTHONPATH=$VE .venv/bin/python -m packbuilder passages --lang sw --check .` lists every passage with its word count, coverage, out-of-pack and higher-level lemmas, and the errors.
4. Fix until it reports 0 errors. The rules are 60-90 words at A1, 90-120 at A2 and 110-150 at B1, with coverage of at least 0.95/0.95/0.93. Each passage has 4-5 questions. Each question word must be linked in its sentence, and every out-of-pack lemma needs a reason.
5. Run again without `--check` to write `pack/passages.json` and `REPORT_passages.md`. Then run `python3 engine/tools/jsonify_pack.py pack` and `./build.sh`.

QA checks the checker does not make:
- Read every B1 span as a surface = lemma : gloss table, and reword homograph links (basi, chuma, unga, hesabu).
- Keep a true/false statement from copying 5 or more words of its sentence.
- Keep the key the unique-longest option in no more than 25% of mc items.
- Make every question answerable from the passage alone.

## Sentence review workflow

1. Rebuild the pack and list the A1/A2 sentences not yet read.
2. For each bad sentence, add its exact text to `bad_sentences.txt` under the class header, with a `# <id> <note>` line above it.
3. Rebuild. Drops pull in deeper candidates, so read the new A1/A2 sentences and repeat until none are left.
4. A word left with no sentence gives its slot to the next-ranked word (`refill_unexampled`), which changes the word list. Add a sentence to `generated_examples.tsv` when the word should stay.
