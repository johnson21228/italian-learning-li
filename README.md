# Italian Learning LI

A minimal Learning Intelligence Workbench for learning Italian from first principles.

This Workbench starts with the human drive to communicate. It does not begin as a grammar course. It begins as a way to become able to be **in conversation** in Italian as a first-person speaker.

## Purpose

Build Italian through lived conversational need:

- greeting
- naming
- pointing
- asking
- answering
- wanting
- noticing
- refusing
- repairing misunderstanding
- listening and repeating

Grammar is welcome, but it enters later as pattern-clarification after the learner has encountered useful speech.

## First principle

Italian learning begins with the basic human drive to communicate. The learner is treated as a person trying to say something, not as a student trying to pass a grammar quiz.

## First files

```text
MAP.md
README.md
SPINE.md
li/domain/italian_learning_principles.md
li/domain/childlike_language_acquisition_rule.md
li/domain/first_person_conversation_rule.md
li/domain/conversation_before_grammar_rule.md
li/practice/hear_imitate_answer_repair_loop.md
li/prompts/start_italian_micro_conversation.md
li/prompts/build_from_need_to_speak.md
li/prompts/listen_repeat_respond_loop.md
li/prompts/enter_conversation_before_grammar.md
li/prompts/repair_misunderstanding_in_italian.md
li/prompts/capture_personal_corpus_entry.md
cards/001_start_italian_learning_workbench_card.md
cards/002_enter_conversation_before_grammar_card.md
li/corpus/first_class_greetings_and_essere_stare.md
li/practice/greeting_response_loop.md
li/practice/formal_informal_choice_loop.md
li/practice/name_exchange_loop.md
li/prompts/practice_first_class_dialogue.md
li/prompts/build_flashcards_from_first_class_slides.md
li/prompts/speak_first_class_italian_aloud.md
cards/003_first_class_corpus_greetings_card.md
```

## Card 002

Card 002 adds the conversation-before-grammar rule and the practice loop:

```text
Hear → Imitate → Answer → Repair → Capture
```

The learner first stays in a small exchange. Grammar enters later to clarify a pattern already used.

## Card 003

Card 003 captures the first copied Italian class slides as a starter corpus. It creates practice material for greetings, checking in, name exchange, formal/informal choice, and first exposure to `essere` and `stare`.

The useful speech comes first:

```text
Ciao.
Come ti chiami?
Mi chiamo Steve.
Come stai?
Sto bene.
A presto.
```

Then grammar may clarify patterns already used.

## Use

Ask the Workbench questions like:

```text
Start a tiny Italian conversation with me.
```

```text
Turn this English need into the simplest useful Italian: I want coffee.
```

```text
Make a personal corpus entry from today's Italian practice.
```

## Verification and packing

```bash
make verify
make pack
```

## LLM repo history snapshot

The standard continuity snapshot lives at:

```text
outputs/history/repo_history_for_llm.md
```

Run `make history` or `make pack` to overwrite it with the latest LLM-readable repo history. Repeated pack runs should not create timestamped history files.


## Class material image assets

This Workbench can capture images that correspond with class material. These images live under:

```text
assets/class_material/
```

The first image asset is:

```text
assets/class_material/first_class/come_si_chiama_poster.jpeg
```

It is governed by `li/assets/class_material_image_asset_rule.md` and connected to `li/corpus/come_si_chiama_image_corpus_entry.md`.



## Uploaded resource index

Uploaded Italian learning PDFs are registered under:

```text
source/resources/
```

Start with:

```text
source/resources/italian_learning_resource_index.md
```

This index summarizes what each uploaded resource contributes:

- `Piacere!` — modern elementary curriculum and class-aligned beginner sequence;
- `Cortina Conversational Italian in 20 Lessons` — conversational self-study and phonetic-pronunciation pattern source;
- `Basic Italian for Travelers` — practical travel phrasebook for immediate need-to-speak situations.

The custody rule is:

```text
li/source/uploaded_resource_custody_rule.md
```

The Workbench stores summaries and use maps, not full copied copyrighted sources.

## Start a future chat in Italian-first mode

Use this prompt when beginning a new conversation with the Workbench:

```text
li/prompts/start_chat_in_italian_mode_with_pack.md
```

It asks for the current `italian-learning-li` pack when needed and sets the default posture to Italian-first, not Italian-only. English remains allowed for clarity, repo work, source custody, terminal commands, or explanation.


## Overlay-only default artifact

For ongoing Capture Back work in this existing Workbench, the default apply artifact is a named overlay zip. The assistant should not also provide a full repo pack by default. Full packs are reserved for brand-new Workbench creation, explicit requests, release/archive artifacts, or recovery from a broken/missing local repo.

## Phrase flashcards

The classroom notes site can include phrases as flashcards, not only nouns and verbs. New flashcards should include:

- visible Italian text;
- exact `speak` text for speech synthesis;
- an image;
- a `curated` flag;
- language-learning categories.

The first phrase flashcard is `Come si chiama?` in the `Other` tab. It uses the approved class image at `site/images/vocabulary/curated/come-si-chiama.jpg` and is governed by `li/domain/phrase_flashcard_metadata_rule.md`.

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
