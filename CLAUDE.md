# Swahili trainer: agent notes

```
kaikki (Wiktionary sw) + en->sw translation tables ─┐
Tatoeba swh/eng, OPUS GlobalVoices en-sw, FLORES-200 ┼─> packbuilder build --lang sw (langs/sw.py, rule tagger)
                                                     │    tools/gloss_overrides.json, forced_a1.txt,
                                                     │    generated_examples.tsv, bad_sentences.txt, id_map_v1.json
                                                     v
                         pack/*.json + tools/REPORT.md
tools/passages/{a1,a2,b1}.txt -> assemble.py -> tools/passages_src.json
                         -> packbuilder passages -> pack/passages.json + tools/REPORT_passages.md
                         pack/*.json --engine/tools/jsonify_pack.py--> pack/*.js
                                                     v
                   build.sh (engine/build.sh) -> index.html + sw.js
progress lives in localStorage key vocab_sw
```

Why it is built this way: a single-file site with a service worker works offline. The engine is a git submodule, so every language ships the same drills. Word ids are frozen in `tools/id_map_v1.json`, so learner progress survives rebuilds. Swahili rules (tokeniser, lemmatiser, noun classes) are code in vocab-engine `tools/packbuilder/langs/sw.py`, not here.

## State

- No remote and not published (user decision 2026-09-27). Never create a remote or push without a new instruction.
- The engine submodule pin (e15c378) predates `langs/sw.py`. That spec and the base `tools/bad_sentences.txt` hook sit on vocab-engine branch engine-sw (commit 6e72e4c) and are not on main yet. Until the submodule is bumped, every packbuilder command needs `PYTHONPATH` or `PACKBUILDER_PATH` pointed at a vocab-engine checkout that has them.

## Commands (pinned)

`VE` is a vocab-engine `tools` dir with the Swahili spec, e.g. `../vocab-engine-sw/tools`. Python is `.venv/bin/python`.

```sh
PYTHONPATH=$VE .venv/bin/python -m packbuilder build --lang sw --repo .   # pack/*.json + tools/REPORT.md
.venv/bin/python tools/passages/assemble.py                               # passages txt -> tools/passages_src.json
PYTHONPATH=$VE .venv/bin/python -m packbuilder passages --lang sw .       # pack/passages.json; --check = report only
python3 engine/tools/jsonify_pack.py pack                                 # pack/*.js from pack/*.json
./build.sh                                                                # index.html + sw.js
PACKBUILDER_PATH=$VE ./check.sh                                           # packbuilder check, validate_pack, stale-build guard
PYTHONPATH=$VE .venv/bin/python -m packbuilder passages --lang sw --check .   # check.sh does not run this; run it too
```

`packbuilder passages` refuses to run when a fresh build would give a different `pack/words.json`. Build first, then run passages.

## Always

- Commit index.html and sw.js together. The stale-build guard in check.sh passes only after that commit.
- Run passages after every pack build that changes the word list, then jsonify and build.
- Fix sentences through builder inputs only: `tools/bad_sentences.txt` drops a corpus sentence by exact text. `tools/generated_examples.tsv` adds or rewrites written sentences. `tools/gloss_overrides.json` fixes glosses.
- Keep new passages and sentences inside the content policy in README.md "Data".
- Stage by path: engine, index.html, sw.js, pack/, tools/, README.md, CLAUDE.md, TODO.md, LICENSE, .gitignore.
- Bump the engine submodule only to a vocab-engine main sha, and rebuild after the bump.

## Never

- Hand-edit pack/*.json, pack/*.js, index.html or sw.js. They are generated.
- Renumber word ids or edit `tools/id_map_v1.json`.
- Delete a published sw.js. Use engine/engine/sw.disable.js as the kill switch.
- Commit .venv, .cache, tools/cache or source dumps.
- Edit engine/ here. Engine and spec changes go to vocab-engine.

## Republish rule

Any change that alters pack/*.json is a republish. Rebuild the pack, the passages, the .js files and index.html, run check.sh and the passages check, then commit index.html and sw.js together. vocab-engine's flagoff goldens do not read this repo yet. Once they do, run `flagoff_snapshot.js --check` there after each republish.

## Where things are

README.md is for end users. tools/README.md lists every builder input. TODO.md holds residuals and the next data wave. tools/REPORT.md and tools/REPORT_passages.md are build reports; their manual sections are kept across runs.
