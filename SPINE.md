# Italian Learning LI Spine

## Purpose

Help the learner acquire Italian by becoming able to participate in simple first-person conversation.

## Governing idea

Language begins as a social act: I want, I notice, I ask, I answer, I do not understand, I try again.

## Boundary

This Workbench is not a complete Italian curriculum yet. It is a durable starting structure for learning Italian through conversation, repetition, listening, and lived need.

## First outcome

The first useful outcome is not grammatical completeness. The first useful outcome is a small set of Italian utterances the learner can hear, repeat, understand, and use.

## Learning stance

The learner begins like a child:

- close to the body
- close to the room
- close to other people
- close to desire and attention
- close to naming and asking
- close to repair when communication breaks


## Practice loop

The first durable practice loop is:

```text
Hear → Imitate → Answer → Repair → Capture
```

This loop is governed by `li/practice/hear_imitate_answer_repair_loop.md` and `li/domain/conversation_before_grammar_rule.md`.

The learner should enter conversation before studying grammar. Grammar may clarify a pattern after the learner has heard, imitated, answered, repaired, and captured useful Italian.

## Corpus stance

The Workbench should preserve encountered language. A phrase becomes important because it was heard, needed, spoken, misunderstood, repaired, or reused.


## First class corpus spine

The first copied class slides become the first external corpus seed for the Workbench. They should be used as conversation material first:

```text
Ciao.
Come ti chiami?
Mi chiamo Steve.
Come stai?
Sto bene.
A presto.
```

The first class corpus is governed by:

```text
li/corpus/first_class_greetings_and_essere_stare.md
li/practice/greeting_response_loop.md
li/practice/formal_informal_choice_loop.md
li/practice/name_exchange_loop.md
```

Grammar from the slides, especially `essere`, `stare`, `tu`, `Lei`, and `voi`, is allowed only as clarification after the learner has spoken a small exchange.

## LLM continuity snapshot

The Workbench preserves one stable LLM-readable repo history file:

```text
outputs/history/repo_history_for_llm.md
```

This file is a continuity surface, not Git history itself. It is overwritten with the latest snapshot by `tools/export_repo_history_for_llm.py`.


## Class material image assets

Images that correspond with class slides, class phrases, or generated visual aids are governed by:

```text
li/assets/class_material_image_asset_rule.md
li/corpus/come_si_chiama_image_corpus_entry.md
assets/class_material/first_class/come_si_chiama_poster.jpeg
cards/005_class_material_image_assets_card.md
```

A class image must support a phrase family, a first-person learner line, pronunciation, repair, and personal corpus capture. The first image asset supports `Come ti chiami?`, `Mi chiamo Steve.`, and `Come si chiama questo?`.



## Uploaded learning resources

Uploaded PDFs and learning materials are source resources, governed by:

```text
li/source/uploaded_resource_custody_rule.md
source/resources/italian_learning_resource_index.md
source/resources/piacere_resource_summary.md
source/resources/cortina_conversational_italian_resource_summary.md
source/resources/basic_italian_traveler_resource_summary.md
cards/006_register_uploaded_italian_learning_resources_card.md
```

These resource summaries let future conversations see the value of each source quickly:

- `Piacere!` supplies a modern open elementary curriculum map;
- `Cortina Conversational Italian in 20 Lessons` supplies old-school conversational and phonetic drill patterns;
- `Basic Italian for Travelers` supplies practical need-to-speak travel phrase families.

The Workbench should use these resources to create small first-person conversations, pronunciation drills, repair loops, and personal corpus entries. It should not copy full copyrighted PDFs into generated packs.

## Italian-first chat mode

Future conversations should be able to resume the Workbench in Italian-first mode using:

```text
li/workflow/italian_first_chat_mode_rule.md
li/prompts/start_chat_in_italian_mode_with_pack.md
cards/007_start_italian_first_chat_mode_card.md
```

The mode is Italian-first, not Italian-only. The assistant defaults to simple Italian as much as possible, asks for the current `italian-learning-li` pack when repo state is missing, allows English for clarity, repo work, source custody, terminal commands, or explanation, and then returns to Italian.


## CB008 — Overlay-only default artifact

`li/workflow/cb_overlay_only_default_rule.md` governs Capture Back artifact shape for this existing Workbench. Future CBs should provide named overlay zips and should not also provide full repo packs by default. Full packs remain valid for brand-new Workbench creation, explicit requests, release/archive artifacts, or broken/missing local repos.

CB008 card: `cards/008_cb_overlay_only_default_artifact_card.md`

## Phrase flashcards and categories

The website supports phrase flashcards as first-class practice objects. New flashcards are governed by:

```text
li/domain/phrase_flashcard_metadata_rule.md
cards/012_phrase_flashcard_metadata_card.md
```

The first phrase flashcard is `Come si chiama?`, using the class image at:

```text
site/images/vocabulary/curated/come-si-chiama.jpg
```

Each new flashcard should have exact `speak` text, an image, a `curated` flag, and language-instruction categories. Categories should describe communicative use: `conversation-primitive`, `question`, `name-exchange`, `object-labeling`, `speaking-practice`, `listening-practice`, and `class-1`.

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

- CB014 records that Class 1 screenshot notes become FCs with controlled Class 1 note categories.

CB014 authority files: `li/domain/class1_note_flashcard_category_rule.md` and `cards/014_class1_screenshot_flashcards_card.md`.
