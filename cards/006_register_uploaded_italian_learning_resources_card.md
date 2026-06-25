# Card 006 — Register Uploaded Italian Learning Resources

## Purpose

Register the uploaded Italian learning PDFs as source resources for future WB sessions, without turning the Workbench into a PDF archive or a grammar-first course.

## Why this card exists

The learner uploaded three useful Italian resources:

1. `Piacere-1669134974._print.pdf`
2. `Cortina Conversational Italian in 20 Lessons.pdf`
3. `Basic Italian Traveler Text.pdf`

Future conversations should know where these resources fit, what value they provide, and how to use them without losing the Workbench's core stance: conversation first, grammar as clarification, and personal corpus capture.

## Added LI and source files

```text
li/source/uploaded_resource_custody_rule.md
source/resources/italian_learning_resource_index.md
source/resources/piacere_resource_summary.md
source/resources/cortina_conversational_italian_resource_summary.md
source/resources/basic_italian_traveler_resource_summary.md
li/prompts/use_uploaded_resource_for_practice.md
li/prompts/map_resource_to_personal_corpus.md
```

## Resource placement rule

Uploaded PDFs and other course resources are registered under:

```text
source/resources/
```

The Workbench should preserve a summary and use map for each resource. It should not blindly copy full copyrighted resources into the repo. When a resource is open or permissively licensed, the license should still be recorded and respected.

## Value added by the resources

### Piacere!

A modern open educational elementary Italian textbook. It contributes an organized curricular map, especially useful for first-class topics such as greetings, introductions, alphabet, numbers, subject pronouns, `avere`, `essere`, vocabulary, conversations, readings, and exercises.

### Cortina Conversational Italian in 20 Lessons

A conversation-centered older course. It contributes a useful historical/self-study pattern: lessons, phonetic pronunciation support, and conversational framing. Because it is an all-rights-reserved scanned book, the Workbench should treat it as a user-supplied reference only, not as material to copy into generated packs.

### Basic Italian for Travelers

A compact phrasebook for practical travel needs. It contributes immediate need-to-speak phrase families: greetings, introductions, pronunciation, social niceties, numbers, food and drink, taxis, hotels, communication strategies, shopping, emergencies, telephone etiquette, signs, and travel/cultural appendices.

## Operational rule

When future WB conversations ask for practice, the LLM should consult the resource index before inventing lesson sequence. It should use the resources as support for practice loops:

```text
Hear → Imitate → Answer → Repair → Capture
```

The resources should be converted into:

- small conversations;
- phrase families;
- pronunciation drills;
- repair loops;
- personal corpus entries;
- learner-facing flashcards;
- class-corresponding image or audio practice prompts.

## Verification

`make verify` should confirm that the resource index, summaries, custody rule, prompts, and this card exist and are referenced by MAP and SPINE.
