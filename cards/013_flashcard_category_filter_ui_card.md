# Card 013 — Flashcard Category Filter UI

## Intent

Replace the rigid `Nouns / Verbs / Other` tab model with a category-filtered flashcard model.

## Capture

The site now treats flashcards as one flat set of FCs. Each FC carries metadata for speech, image, curation, part of speech, and multiple learning categories.

## Site changes

```text
site/js/vocabulary-data.js
site/js/app.js
site/css/app.css
site/index.html
site/images/vocabulary/placeholders/word-placeholder.svg
```

## LI changes

```text
li/domain/flashcard_category_filter_rule.md
cards/013_flashcard_category_filter_ui_card.md
```

## Acceptance

```text
No visible Nouns / Verbs / Other tab UI remains.
All FCs live in window.ITALIAN_CLASSROOM_FLASHCARDS.
Every FC has speak, image, curated, partOfSpeech, and categories metadata.
The filter UI is generated from categories.
All shows every FC.
Clicking class-1, noun, verb, phrase, question, name-exchange, curated, or needs-image filters the visible FCs.
Come si chiama? appears in All, class-1, phrase, question, conversation-primitive, name-exchange, image-supported, and curated filters.
```

## Why

Italian learning cards should be usable by instructional purpose, not just by a single grammar bucket. A card can belong to several practice paths at once.
