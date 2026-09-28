# TODO

These are the residuals from the sentence review and passages round of 2026-09-29. Counts and examples are in tools/REPORT.md, under "Sentence review 2026-09-29", and in tools/REPORT_passages.md.

## Before publishing

- Commit `langs/sw.py` and the base `tools/bad_sentences.txt` hook to vocab-engine main. Both are on branch engine-sw at 6e72e4c. Then bump `engine/` to that main sha, rebuild, and run check.sh without `PACKBUILDER_PATH`.
- Create the GitHub repo and publish only on a new user instruction. The user decision of 2026-09-27 is to hold.
- Get a native-speaker review. No native speaker has read the sentences, glosses or passages.

## Sentences

- 59 A1 sentences carry a relative form (-ye-, -cho-, amba-), which is above the A1 register. They were kept because a sentence's level follows its word, and dropping them would leave A1 words with no easy sentence. Fixing this needs a register-aware level rule, or written A1 sentences for those words.
- The B1 corpus sentences were scanned for policy words and punctuation damage, not read line by line.
- 41 words have exactly one sentence. The list is in tools/REPORT.md.
- Some sensitive words stay in the pack, each with one neutral sentence: pombe, kingono, uchi, kimapenzi, mpenzi, dansi, mwanamuziki. Dropping a word outright needs a word-level exclusion input, which the builder lacks.
- The rule tagger links some homographs to the wrong word, for example basi ("well") for "bus", chuma (iron) for kuchuma (pick), and unga (to join) for "flour". The passages were reworded around these. Corpus sentences were dropped only where the review found the problem. A homograph table in `langs/sw.py` would fix the whole class at once.

## Passages

- The declared out-of-pack lemmas are muuguzi, kiyoyozi, meneja, saruji, fidia and malaria. They are common words the frequency list misses. A later word-list pass could take them in.
- Moshi, a town in p0039, is also a pack word ("smoke"). It is declared as a name, but a learner may still read it as the word.

## Next data wave: culture-native sources

These come from vocab-engine docs/LANGUAGES.md, under "Swahili", and docs/scouts/story-sources-2026-09-27.md. They are aligned learner-register text that could replace written sentences and passages.

- African Storybook: about 280 aligned stories out of 628 Kiswahili books, CC BY 4.0.
- StoryWeaver: 260 books, 82 of them at level 2. They are CC BY 4.0, and most have an English twin.
- Bloom Library: 241 books (235 `swh` and 6 `sw`), under CC BY, BY-SA or CC0, with English.
- VOA Swahili: public-domain text up to 2024-12-31. The site is frozen, with no new text.

StoryWeaver aligns reliably only at page level. Align pages first, then split sentences within each page.

## Audio

There is no recorded Swahili audio, and Tatoeba has no permissively licensed Swahili clips. The app uses browser TTS (`sw-KE`), which Android Chrome supports and most desktop and Apple browsers do not. No audio work is planned until a licensed source turns up.
