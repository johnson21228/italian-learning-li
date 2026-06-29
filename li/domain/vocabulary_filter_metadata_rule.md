# Vocabulary Filter Metadata Rule

The classroom vocabulary site should treat vocabulary as one study list, not as separate tab-only lists.

The source data may remain grouped as `nowns`, `verbs`, and `other` for compatibility, but the runtime should flatten those groups into one list and attach filter metadata.

Every flashcard should support these metadata concepts, either explicitly in `site/js/vocabulary-data.js` or derived at runtime:

- `partOfSpeech`: noun, verb, phrase, grammar-word, other
- `sourceList`: nowns, verbs, other
- `semanticDomain`: people, time, classroom, identity, grammar, conversation, repair, place, object, language, learning, etc.
- `semanticHints`: expandable array of study/filter hints
- `studyUse`: expandable array describing how the card is used in study
- `classIntroduced`: class-1, class-2, etc.
- `curated`: true/false image curation status

Semantic hints are expandable. Adding new hints later must not break older cards.

The UI should show one combined flashcard list with filter chips at the top. Nouns, verbs, and other must remain easy filters.

Large lists should not render all cards at once. The UI should show a fixed number of cards per page and provide Previous / Next controls while preserving the active filter.
