# Flashcard Adds Must Not Create Verifier Churn

Flashcard content additions are data changes, not verifier changes.

When adding ordinary flashcards, do not update `tools/verify_italian_learning_li.py`
just to list the new cards, phrases, images, or categories.

The verifier may check the flashcard data contract generically:

- the site exposes `window.ITALIAN_CLASSROOM_FLASHCARDS`
- every flashcard has `italian`
- every flashcard has `speak` or can fall back to `italian`
- every flashcard has `partOfSpeech`
- every flashcard has a non-empty `categories` array
- every flashcard has `curated` as a boolean
- every flashcard image path, when present, points to an existing file
- every flashcard can be rendered by the current app runtime

The verifier must not require specific lesson cards by name unless the CB is changing
a core LI invariant, site model, or runtime contract.

Update the verifier only when changing one of these:

- flashcard schema
- category registry contract
- rendering/runtime behavior
- required site files
- Workbench governance files
- source/custody rules

A normal flashcard CB should usually update only:

- `site/js/vocabulary-data.js`
- optional image assets under `site/images/vocabulary/...`
- optional source/custody notes under `assets/` or `source/`
- optional card/capture documentation if the change is important enough

This keeps FC curation fast and prevents every vocabulary addition from becoming a tooling change.
