# TODO

These are the residuals from the sentence review, passages round and QA fix wave of 2026-09-29. Counts and examples are in tools/REPORT.md, under "Sentence review 2026-09-29" and "Fix wave 2026-09-29", and in tools/REPORT_passages.md.

## Before publishing

- Get a native-speaker review. No native speaker has read the sentences, glosses or passages.

## Sentences

- 59 A1 sentences carry a relative form (-ye-, -cho-, amba-), which is above the A1 register. They were kept because a sentence's level follows its word, and dropping them would leave A1 words with no easy sentence. Fixing this needs a register-aware level rule, or written A1 sentences for those words.
- All A2 and B1 corpus sentences were read three times across the two fix waves, at a strict bar in fix wave 2. The last 20% samples found under 1% defects. No native speaker has checked the reading.
- ushoga stays in the pack (owner call, 2026-09-29). Its sentence is neutral news about a Ugandan bill; keep any replacement neutral.
- Every word has at least two sentences. 706 rows in tools/generated_examples.tsv write sentences for the pack (`"src": "gen"`, tools/generated_examples.tsv) and need the native-speaker review too. Fix wave 2 dropped 1,055 corpus rows, so the written share grew.
- A few linker gaps are handled only by dropping their one sentence: "Kulia kwa nyuki", ziwafikie, mitoko, Kizito, kivile, kulevya, dhamiri, zimepagawa, hisi and Karibia.
- Alcohol and music words stay in the pack, as in the other packs: pombe, dansi, mwanamuziki. Sexual and romance words (kimapenzi, kingono, uchi) are kept at B1 by sw.py `word_ceiling_re`. Each has one neutral sentence.
- Homograph context rules in `langs/sw.py` now cover karibu, basi, mpaka, huenda, have-forms (hazina, kina, wana), -ako (including the letter sign-off "Wako,"), -tumia/-tuma, kutoka, la, kuwa, ndiyo, noun/verb-stem imperatives, taratibu, the negative perfect -jawa and noun/adjective pairs. The shared-surface audit found 0 known mislinks. chuma (iron) for kuchuma (pick) has no rule yet, and the passages were reworded around it.

## Passages

- The declared out-of-pack lemmas are muuguzi, kiyoyozi, meneja, saruji, fidia and malaria. They are common words the frequency list misses. A later word-list pass could take them in.
- Juma, Zawadi, Upendo, Simba and Moshi are declared names that are also pack words. They are never linked, but a learner may still read them as the word.

## Next data wave: culture-native sources

These come from vocab-engine docs/LANGUAGES.md, under "Swahili", and docs/scouts/story-sources-2026-09-27.md. They are aligned learner-register text that could replace written sentences and passages.

- African Storybook: about 280 aligned stories out of 628 Kiswahili books, CC BY 4.0.
- StoryWeaver: 260 books, 82 of them at level 2. They are CC BY 4.0, and most have an English twin.
- Bloom Library: 241 books (235 `swh` and 6 `sw`), under CC BY, BY-SA or CC0, with English.
- VOA Swahili: public-domain text up to 2024-12-31. The site is frozen, with no new text.

StoryWeaver aligns reliably only at page level. Align pages first, then split sentences within each page.

## Audio

There is no recorded Swahili audio, and Tatoeba has no permissively licensed Swahili clips. The app uses browser TTS (`sw-KE`), which Android Chrome supports and most desktop and Apple browsers do not. No audio work is planned until a licensed source turns up.
