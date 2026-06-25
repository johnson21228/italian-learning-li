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
```

## Core domain LI

```text
li/domain/italian_learning_principles.md
li/domain/childlike_language_acquisition_rule.md
li/domain/first_person_conversation_rule.md
li/domain/conversation_before_grammar_rule.md
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
```

The first card captures the initial Workbench direction and gives future cards a stable starting point.

The second card adds the conversation-before-grammar rule and the required practice loop:

```text
li/practice/hear_imitate_answer_repair_loop.md
Hear → Imitate → Answer → Repair → Capture
```

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
