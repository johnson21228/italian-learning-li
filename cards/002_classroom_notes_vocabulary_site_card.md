# Card 002 — Classroom Notes Vocabulary Site

## Date

2026-06-29

## Context

The learner wants Italian class vocabulary to be easier to practice on iPhone and iPad. A PDF supports selectable text, but a web page can do more: tap a vocabulary card and hear the Italian word spoken.

## Decision

Add LI for a static classroom notes vocabulary site hosted on GitHub Pages.

The site should have tabs for:

- Nowns
- Verbs
- Other

The Nowns label preserves the learner's working term. The page should present Italian text as real selectable text, place a visual cue beside each item, optionally show English, and provide browser-based Italian speech.

## Speech decision

Use web speech synthesis with `it-IT`, choose the best available Italian voice exposed by the browser/device, provide a voice picker, and remember the learner's choice locally.

## Content decision

Vocabulary should be maintained as site data so classroom notes can be added over time without rewriting the page layout.

## Next implementation target

Create or maintain:

```text
site/index.html
site/js/vocabulary-data.js
site/js/app.js
site/css/app.css
```

The site must remain static and GitHub Pages compatible.
