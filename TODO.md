# TODO

These are the residuals from the sentence review, passages round and QA fix wave of 2026-09-29. Counts and examples are in tools/REPORT.md, under "Sentence review 2026-09-29" and "Fix wave 2026-09-29", and in tools/REPORT_passages.md.

## Before publishing

- Get a native-speaker review. No native speaker has read the sentences, glosses or passages.

## Sentences

- Republish 7b8c173 (port wave 2): `packbuilder enrich` adds `ft` + the generic flag block + `eta` (tools/eta.json, measured 600 sessions at 85%, seeds 5/6/7); no words, sentences or passages changed. check.sh now runs `enrich --check`. No device voice is the common case: listening passes and sound pairs stay off without one.
- Migration proof: rollback hash 973d2741b00a080e0fdd2eda2b9ce8563a020701; previous live md5 index 1d2b806ba87373e8e2a6c55983cad1f2, sw d90aa0b9d36e6831a65b11b57043d75a; new local md5 index 11d9edda2a32b82875b2bda8c8245cb0, sw ec521695e5045f1c61f303747cbe7753. Storage: new fields day/sn/t/u/f/p/pm/pv/pause/read.done s,ls/today.tw on first use; boot writes nothing; previous build ef44c6e carries them (migration [port] 9/9).
- Live proof 1e55782 (2026-10-08) KEEP, voiceless: 12-session seed from 973d274 byte-equal after boot/reload/Progress open (leaving Progress adds only prog.pv); one Today session writes w/s/sets/sessions/sn/day/pm; that record boots on 973d274 byte-equal (boot + reload), one key vocab_sw, a session runs there; back on live byte-equal; 0 console errors, 0 failed requests. Today shows "≈ 140 sessions".
- Republish 09e90bc: sentence spans (18870/18945 linked words placed in sentences, 5358/5358 in passages); inflected forms now cloze targets. kuwa na/kuna own their tokens (76 sentences, 25 passage sentences).
- Republish ef44c6e: no words moved; deleted override keys itwa|verb, kanda|noun, maslahi|adj, mdogo|noun, mhanga|noun, taratibu|noun (none reached a record; pack/*.json byte-identical with and without them); set-counter and no-voice planner fixes.
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

There is no recorded Swahili audio, and Tatoeba has no permissively licensed Swahili clips. The app uses browser TTS (`sw-KE`), which Android Chrome supports (owner-verified on a phone 2026-09-29: speaker taps produce sound) and most desktop and Apple browsers do not. No audio work is planned until a licensed source turns up.
- Migration proof on engine 8745de1 (placement early stop, placed level drives reading/patterns/estimates, gender gaps, session estimates recalibrated): rollback hash 5625d11d1abc0cc0e4fb0b81907094d7457ae31b (engine 7b8c173). Live md5 before: index.html 11d9edda2a32b82875b2bda8c8245cb0, sw.js ec521695e5045f1c61f303747cbe7753. New build: index.html f62a4496e552309e4f4c8c1333c7afd0, sw.js d6cadf850c6a32c4967e97adabfe72e7. Pack diff: pack.json gains placedKnown, placedRead, placementEarlyStop, placementWhole (+ eta). Storage: boot writes nothing; 12-session seed from the previous build boots byte-equal on the new build (boot, reload, Progress; only pv added on leaving Progress), after one session boots on the previous build byte-equal with no backup keys and runs a session, and back on the new build byte-equal (scratch 13/13, KEEP).
