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
