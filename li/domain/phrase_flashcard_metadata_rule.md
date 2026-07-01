# Phrase flashcard metadata rule

The classroom notes website is not only a vocabulary list. It is a speaking-practice surface.

Every new flashcard entry should include enough metadata to support listening, speaking, image recall, and later filtering.

## Required flashcard fields for new entries

A new site flashcard should include:

- `italian`: visible Italian word or phrase
- `english`: short support meaning
- `speak`: the exact Italian word or phrase to be spoken aloud
- `image`: a site-owned image path
- `imageAlt`: short image description
- `curated`: true or false
- `categories`: a list of learning categories

The `speak` field is the speech source. It may match `italian`, but it exists so the site can speak exactly what the learner should hear and repeat.

## Category families

Use categories from language-instruction practice, not random tags. Good categories include:

- `conversation-primitive`
- `greeting`
- `question`
- `answer`
- `name-exchange`
- `repair-phrase`
- `first-person`
- `second-person`
- `third-person`
- `formal`
- `informal`
- `object-labeling`
- `identity`
- `class-1`
- `speaking-practice`
- `listening-practice`
- `pronunciation-practice`
- `image-supported`
- `curated`

These categories let future practice select flashcards by communicative purpose instead of only by grammar.

## Website behavior

The website should use `speak` when present and fall back to `italian` when `speak` is missing.

The website may display category chips, but the main learning focus stays on hearing, repeating, and using the Italian phrase.

## First phrase flashcard

The first phrase flashcard from the class image is:

- `italian`: `Come si chiama?`
- `speak`: `Come si chiama?`
- image: `images/vocabulary/curated/come-si-chiama.jpg`
- categories: `conversation-primitive`, `question`, `name-exchange`, `third-person`, `object-labeling`, `class-1`, `speaking-practice`, `listening-practice`, `image-supported`, `curated`
