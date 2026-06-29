# Classroom Vocabulary Curation Rule

The vocabulary site must maintain a class-introduced vocabulary ledger.

The ledger is not a generic dictionary. It must reflect Italian words that have actually been introduced through class notes, class images, classroom dialogue, or learner practice derived from class material.

Each vocabulary entry must belong to exactly one tab:

- Nowns
- Verbs
- Other

Each entry must carry:

- `term`: the Italian word or phrase
- `english`: optional English gloss
- `kind`: `nown`, `verb`, or `other`
- `introducedBy`: class note, image, dialogue, or practice source
- `curated`: boolean
- `image`: website image path or placeholder
- `imagePrompt`: prompt used or intended for generating an image
- `imageEssence`: short description of what the image should convey

`curated: false` means the entry has been captured from class but its image concept has not yet been reviewed.

`curated: true` means the term, meaning, category, and image essence have been reviewed enough that an LLM may generate or refine an image that best conveys the essence of the term.

The website must not require every entry to have a final generated image before it appears. It may show a placeholder until the entry is curated and an image exists.

The image must support recall of the Italian word. It should convey meaning visually without turning the site into an English-first translation table.
