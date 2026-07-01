# Card 012 — Phrase Flashcard Metadata

## Capture

The learner asked whether the `Come si chiama?` class image could become a flashcard and whether each website flashcard should have additional attributes.

## Decision

Yes. The website should support phrase flashcards as first-class learning objects, not only isolated nouns and verbs.

New flashcards should carry:

- visible Italian text;
- English support text;
- exact `speak` text for Italian speech synthesis;
- an image path;
- an image alt description;
- a `curated` flag;
- learning categories.

## Why

The learner is practicing conversation primitives after class 1. `Come si chiama?` is not merely a grammar phrase. It is a usable question for asking what a person, animal, or object is called.

The metadata makes future practice possible by category:

- questions;
- name exchange;
- object labeling;
- speaking practice;
- listening practice;
- class 1 review;
- image-supported recall.

## Files

- Rule: `li/domain/phrase_flashcard_metadata_rule.md`
- Website data: `site/js/vocabulary-data.js`
- Website runtime: `site/js/app.js`
- Website style: `site/css/app.css`
- Image asset: `site/images/vocabulary/curated/come-si-chiama.jpg`

## Result

The `Other` tab now includes a curated flashcard for `Come si chiama?` with exact speak text and language-instruction categories.
