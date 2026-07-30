# Italian Learning LI Map

This map orients a human and an LLM inside the Italian Learning Workbench.

## Repository purpose

This repository is a Learning Intelligence Workbench for acquiring Italian through communicative need, first-person conversation, and a growing personal corpus.

## Read first

```text
LLM_READ_FIRST.md
SPINE.md
li/domain/italian_learning_principles.md
li/domain/childlike_language_acquisition_rule.md
li/domain/first_person_conversation_rule.md
li/domain/conversation_before_grammar_rule.md
li/corpus/first_class_greetings_and_essere_stare.md
li/practice/greeting_response_loop.md
li/practice/formal_informal_choice_loop.md
li/practice/name_exchange_loop.md
li/assets/class_material_image_asset_rule.md
li/corpus/come_si_chiama_image_corpus_entry.md
```

## Core domain LI

```text
li/domain/italian_learning_principles.md
li/domain/childlike_language_acquisition_rule.md
li/domain/first_person_conversation_rule.md
li/domain/conversation_before_grammar_rule.md
li/corpus/first_class_greetings_and_essere_stare.md
li/practice/greeting_response_loop.md
li/practice/formal_informal_choice_loop.md
li/practice/name_exchange_loop.md
li/assets/class_material_image_asset_rule.md
li/corpus/come_si_chiama_image_corpus_entry.md
```

These files define the learning posture: start like a child, stay inside conversation, and use grammar as pattern clarification rather than as the first doorway.

## Prompt LI

```text
li/prompts/start_italian_micro_conversation.md
li/prompts/build_from_need_to_speak.md
li/prompts/listen_repeat_respond_loop.md
li/prompts/enter_conversation_before_grammar.md
li/prompts/repair_misunderstanding_in_italian.md
li/prompts/capture_personal_corpus_entry.md
li/prompts/practice_first_class_dialogue.md
li/prompts/build_flashcards_from_first_class_slides.md
li/prompts/speak_first_class_italian_aloud.md
li/prompts/create_image_from_class_material.md
li/prompts/practice_with_class_image.md
```

These prompts begin the learning loop:

1. enter a tiny Italian conversation;
2. convert a need into a usable utterance;
3. listen, repeat, respond, and repair;
4. enter conversation before grammar explanation;
5. capture personal corpus entries after small exchanges.

## Continuity card

```text
cards/001_start_italian_learning_workbench_card.md
cards/002_enter_conversation_before_grammar_card.md
cards/003_first_class_corpus_greetings_card.md
cards/004_standardize_llm_repo_history_snapshot_card.md
cards/005_class_material_image_assets_card.md
```

The first card captures the initial Workbench direction and gives future cards a stable starting point.

The second card adds the conversation-before-grammar rule and the required practice loop:

```text
li/practice/hear_imitate_answer_repair_loop.md
Hear → Imitate → Answer → Repair → Capture
```

## First class corpus

Card 003 turns the copied first-class slides into usable corpus and practice material:

```text
li/corpus/first_class_greetings_and_essere_stare.md
li/practice/greeting_response_loop.md
li/practice/formal_informal_choice_loop.md
li/practice/name_exchange_loop.md
li/prompts/practice_first_class_dialogue.md
li/prompts/build_flashcards_from_first_class_slides.md
li/prompts/speak_first_class_italian_aloud.md
li/prompts/create_image_from_class_material.md
li/prompts/practice_with_class_image.md
```

The corpus covers greetings, leave-taking, `Come stai?`, `Come sta?`, `Come va?`, name exchange, `Tu / Lei / voi`, and first exposure to `essere` and `stare`.

## Class material image assets

Card 005 adds the rule that images from class material are corpus assets, not decoration. The standard location is:

```text
assets/class_material/
```

The first image asset is:

```text
assets/class_material/first_class/come_si_chiama_poster.jpeg
li/assets/class_material_image_asset_rule.md
li/corpus/come_si_chiama_image_corpus_entry.md
li/prompts/create_image_from_class_material.md
li/prompts/practice_with_class_image.md
```

This asset supports `Come ti chiami?`, `Mi chiamo Steve.`, `Come si chiama questo?`, and the repair phrase `Non capisco. Puoi ripetere lentamente?`.


## Uploaded learning resources

Card 006 registers uploaded Italian learning PDFs as source resources so future conversations can find their value without searching blindly:

```text
li/source/uploaded_resource_custody_rule.md
source/resources/italian_learning_resource_index.md
source/resources/piacere_resource_summary.md
source/resources/cortina_conversational_italian_resource_summary.md
source/resources/basic_italian_traveler_resource_summary.md
li/prompts/use_uploaded_resource_for_practice.md
li/prompts/map_resource_to_personal_corpus.md
li/prompts/start_chat_in_italian_mode_with_pack.md
cards/006_register_uploaded_italian_learning_resources_card.md
cards/007_start_italian_first_chat_mode_card.md
```

These summaries explain how `Piacere!`, `Cortina Conversational Italian in 20 Lessons`, and `Basic Italian for Travelers` contribute to the Workbench. The source PDFs themselves are not blindly copied into the repo; the WB preserves custody notes, value summaries, and practice maps.

## Italian-first session start

Card 007 adds a reusable prompt that asks for the current pack and places a future chat into Italian-first mode:

```text
li/workflow/italian_first_chat_mode_rule.md
li/prompts/start_chat_in_italian_mode_with_pack.md
cards/007_start_italian_first_chat_mode_card.md
```

The standard posture is: Italian-first, not Italian-only. The assistant should default to simple Italian as much as possible, allow English for clarity or repo/source work, and then return to Italian.

## Corpus outlook

The Workbench grows a personal corpus of encountered Italian:

- phrases heard
- phrases spoken
- phrases needed
- phrases misunderstood
- phrases repaired
- pronunciation notes
- situations where the phrase was useful

The personal corpus is treated as the learner's lived source material.

## Tools

```text
make verify
make pack
```

`make verify` checks the required Workbench files. `make pack` writes a session pack under `dist/`.

## Standard Workbench history snapshot

The canonical LLM-readable repo history snapshot is:

```text
outputs/history/repo_history_for_llm.md
```

It is governed by `li/workflow/llm_repo_history_snapshot_rule.md` and captured by `cards/004_standardize_llm_repo_history_snapshot_card.md`. `tools/export_repo_history_for_llm.py` overwrites this file on each history/pack run.


## CB008 — Overlay-only default artifact

- Card: `cards/008_cb_overlay_only_default_artifact_card.md`
- Rule: `li/workflow/cb_overlay_only_default_rule.md`
- Default: ongoing CB work in an existing Workbench repo should provide an overlay zip only.
- Required phrase: Do not also provide a full repo pack by default.

## Phrase flashcard metadata

Card 012 adds phrase flashcard metadata for the classroom notes website:

```text
li/domain/phrase_flashcard_metadata_rule.md
cards/012_phrase_flashcard_metadata_card.md
site/js/vocabulary-data.js
site/js/app.js
site/css/app.css
site/images/vocabulary/curated/come-si-chiama.jpg
```

New flashcards should include visible Italian text, exact `speak` text, image path, `curated` flag, and language-instruction categories such as `conversation-primitive`, `question`, `name-exchange`, `object-labeling`, `speaking-practice`, and `listening-practice`.

## CB013 — Flashcard category filters

Card 013 replaces rigid flashcard tabs with metadata-driven category filters.

```text
li/domain/flashcard_category_filter_rule.md
cards/013_flashcard_category_filter_ui_card.md
site/js/vocabulary-data.js
site/js/app.js
site/css/app.css
site/index.html
site/images/vocabulary/placeholders/word-placeholder.svg
```

Each FC should carry `speak`, `image`, `curated`, `partOfSpeech`, and `categories`. The site renders `All` plus category filters from flashcard metadata, so one card can belong to multiple learning paths.

- CB014: Class 1 screenshot phrase flashcards and Class 1 note category vocabulary. See `cards/014_class1_screenshot_flashcards_card.md` and `li/domain/class1_note_flashcard_category_rule.md`.

## July 22 Markdown lesson

The proposed screenshot-informed lesson reconstruction is:

```text
li/corpus/july_22_restaurant_places_and_movement_lesson.md
li/flashcards/july_22_visual_flashcards.md
assets/class_material/july_22/clips/
captures/CAPTURE_BACK_JULY_22_MARKDOWN_LESSON.md
```

It connects restaurant language, places, taxi phrases, `andare`, and `venire`
through short usable exchanges before conjugation clarification.

The reusable weekly protocol remains:

```text
li/workflow/weekly_screenshot_lesson_capture_rule.md
templates/weekly_screenshot_lesson/README.md
tools/verify_weekly_class_lessons.py
```

The published lesson index, dated lesson pages, lesson-only stylesheet, and
class-lesson image copies are removed from the focused flashcard site.
Workbench-custody Markdown and crops remain preserved.
## July 22 interactive flashcard correction

`captures/CAPTURE_BACK_JULY_22_INTERACTIVE_FLASHCARDS.md` proposes routing the
July 22 evidence into the site's real interactive flashcard data source so the
learner can see the image, read the Italian, and tap to hear it.

## July 17 screenshot flashcards

`captures/CAPTURE_BACK_JULY_17_CONVERSATION_AND_CONJUGATION_FLASHCARDS.md` proposes 23 interactive question and conjugation cards from the learner-identified July 17 class screenshots.

## Composable avere, bere, and mangiare flashcard pilot

`captures/CAPTURE_BACK_COMPOSABLE_BERE_FLASHCARD_PILOT.md` proposes runtime
assembly of labeled subject, reusable verb action, and labeled class-vocabulary object into
filterable tap-to-hear cards.

## Generative flashcard system

`li/domain/generative_flashcard_system_rule.md` governs the generator-only site projection. `captures/CAPTURE_BACK_GENERATIVE_FLASHCARD_SYSTEM.md` is proposed for review.

## Generative flashcard system

`li/domain/generative_flashcard_system_rule.md` governs the generator-only site projection. `captures/CAPTURE_BACK_GENERATIVE_FLASHCARD_SYSTEM.md` is proposed for review.

## Sensitive speech targets

`li/domain/generative_flashcard_system_rule.md` governs independent subject,
conjugated-verb, complement, and complete-sentence speech controls.
`captures/CAPTURE_BACK_SENSITIVE_SPEECH_TARGETS.md` is proposed for review.


## Published Lessons surface removal

`captures/CAPTURE_BACK_REMOVE_PUBLISHED_LESSONS_SURFACE.md` proposes removing
the Lessons navigation and published lesson artifacts while retaining lesson
knowledge and source custody inside the Workbench.

## Handout flashcard candidates

`source/resources/handout_flashcard_derivation_manifest.md` records external
source identity without storing PDFs. `li/flashcards/from_handouts_candidates.json`
holds transformed candidates. `captures/CAPTURE_BACK_HANDOUT_FLASHCARD_CANDIDATES.md`
is proposed for review.
