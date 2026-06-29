# Vocabulary Image Curation Study Loop Rule

Vocabulary image curation is a fundamental part of study in this LI.

When adding or extending classroom vocabulary, new flashcard entries may start with a placeholder image and `curated: false`.

The repeatable curation loop is:

1. Inspect `site/js/vocabulary-data.js` directly.
2. Find the first display-order entry where:
   - `curated` is missing or false, or
   - `image` is missing, or
   - `image` does not point to `images/vocabulary/curated/`.
3. Present exactly one next item:
   - Italian term
   - English gloss
   - tab/kind
   - current image status
   - proposed image essence
4. Provide exactly one image-generation prompt.
5. After the user approves or asks to CB the image:
   - save the generated image as `site/images/vocabulary/curated/<italian>.jpg`
   - update that vocabulary entry with:
     - `image`
     - `imageAlt`
     - `curated: true`
     - `imageEssence`
     - `imagePrompt`
   - run `make verify`
   - show `git status --short`

Do not infer the next vocabulary image from memory or prior chat. Always inspect the current repo data.

For abstract verbs, prefer adding concrete learner-facing phrase/form cards when that supports study better than a single abstract infinitive image.
