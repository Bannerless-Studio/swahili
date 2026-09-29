# Swahili A1-B1 vocab trainer

A free vocabulary trainer for Swahili, A1 through B1. It has 2000 words with short English glosses and example sentences. It also has 60 short reading passages with comprehension questions.

**Status:** published at https://bannerless-studio.github.io/swahili/.

**Scope note:** this app gives the vocabulary base for B1. A B1 exam also needs grammar, writing and speaking practice, which this app does not teach.

## Using the trainer

- **Today** runs one daily session: review, learn new words, listen, recall, sentence practice, and a reading passage when one is due. A stage skips itself when there is not enough material yet.
- **Words** lets you browse and search the word list, and drill any set on demand.
- **Test** has a placement test, to skip words you already know, plus free tests.
- **Progress** shows your stats and lets you export, import or reset your progress.
- **Reading passages** come in 20 short texts at each of A1, A2 and B1, with multiple-choice and true/false questions. A level's passages unlock once you have learned 70% of that level's words. Tap any word in a passage for its gloss. Missed questions feed their words back into review.
- **Offline:** the app is one page with a service worker. Once loaded, it keeps working offline.
- **Audio:** there is no recorded Swahili audio. The trainer speaks words and sentences with the browser's `sw-KE`/`sw-TZ` voice where one exists. Verified 2026-09-29 on Android Chrome (Google TTS speaks Swahili); most desktop browsers and Apple devices have no Swahili voice, so the speaker buttons are hidden there.
- **Progress** is kept only in this browser's local storage. Export it from the Progress tab to move it to another device.

## Data

This is a data pack (`key: "sw"`) for the shared [vocab-engine](https://github.com/Bannerless-Studio/vocab-engine), included as a git submodule at `engine/`. The word list is ranked by frequency over a tagged corpus. Glosses come from Wiktionary. Example sentences and levels are assigned by rule.

- **Words:** 2000 in all: A1 600, A2 700, B1 700. Levels are frequency bands with a forced A1 core, not an official CEFR list.
- **Tagger:** Swahili has no ready statistical tagger. A rule-based tokeniser and lemmatiser over the Wiktionary data does the tagging at build time (vocab-engine `tools/packbuilder/langs/sw.py`).
- **Sentences:** 2,777 in all (A1 522, A2 976, B1 1,279). Every word has at least 2. Most come from Tatoeba, OPUS GlobalVoices and FLORES-200; 678 are written for this pack and marked `"src": "gen"`.
- **Sentence review:** every level was read by hand across three QA rounds, each fixing what the last one's fresh sample turned up, plus a re-QA pass. The last confirming samples (20% of A2 and B1, freshly drawn) found under 1% content defects. The tables and counts are in `tools/REPORT.md`.
- **Content policy:** passages and sentences keep to everyday East African life and respect Islamic principles. They leave out alcohol, dating and romance, music and dancing as entertainment, gambling and pork.
- **Reading passages:** the 60 passages were written for this pack. They were checked by an automated QA pass, not by a native speaker. In-pack word coverage is at least 95% at A1/A2 and 93% at B1. Numbers per passage are in `tools/REPORT_passages.md`.

No native Swahili speaker has reviewed the pack yet. Known residuals are in `TODO.md`.

### Sources and licences

| Data | Source | Licence | Used for |
|---|---|---|---|
| Glosses, part of speech, noun classes | [kaikki.org](https://kaikki.org) Swahili Wiktionary extract | CC BY-SA 3.0 / GFDL (Wiktionary) | English glosses, POS, lemmatiser data |
| English-to-Swahili translation tables | [Wiktionary](https://en.wiktionary.org) | CC BY-SA 3.0 / GFDL | extra headwords and glosses |
| Example sentences and translations | [Tatoeba](https://tatoeba.org) Swahili-English | CC BY 2.0 FR | sentences; contributors listed in `pack/attribution.json` |
| Parallel news sentences | [OPUS GlobalVoices](https://opus.nlpl.eu/GlobalVoices.php) en-sw v2018q4 | CC BY 3.0 | frequency corpus and short example sentences (`"src": "gv"`) |
| Benchmark sentences | [FLORES-200](https://github.com/facebookresearch/flores) swh_Latn | CC BY-SA 4.0 | frequency corpus and short example sentences (`"src": "flores"`) |
| Written sentences and passages | written for this pack | CC BY-SA 4.0 | examples where the corpus had none; all 60 passages |
| Word frequency (fallback surfaces) | [`wordfreq`](https://github.com/rspeer/wordfreq) Python package | CC BY-SA 4.0 | word ranking for surfaces outside the tagged corpus |
| UI font | [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans) via Google Fonts | SIL Open Font License 1.1 | interface typeface |
| Audio | none | - | browser TTS only |

Licence: code MIT, pack data CC BY-SA 4.0. See LICENSE.

## Rebuild

`CLAUDE.md` has the rebuild and check commands. `tools/README.md` describes every file under `tools/`.
