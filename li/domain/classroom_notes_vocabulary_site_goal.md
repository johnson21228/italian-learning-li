# Classroom Notes Vocabulary Site Goal

## Goal

Create and maintain a small GitHub Pages web site for Italian classroom notes.

The site should turn class notes into a learner-friendly, tap-to-hear vocabulary surface. It begins with the first class vocabulary and grows as new notes are added.

## Primary learner outcome

The learner can open the site on iPhone, iPad, or desktop Chrome and practice Italian vocabulary from class:

- see an image or visual cue for each item;
- see the Italian word as selectable text;
- optionally show or hide the English meaning;
- tap a Speak button to hear the word in Italian;
- choose the best available Italian spoken voice exposed by the browser/device.

## Required tabs

The site must keep classroom vocabulary in three learner-facing tabs:

1. **Nowns** — the learner's classroom noun list. The tab label intentionally preserves the learner's working spelling, while the internal LI may also call these nouns/sostantivi.
2. **Verbs** — verbs and action words from class.
3. **Other** — greetings, phrases, pronouns, questions, answers, or classroom notes that are useful but are not simple nouns or verbs.

## Site-maintained content

Vocabulary should be maintained as site data, not hard-coded only in layout markup. A future LLM or human should be able to add classroom vocabulary by editing a data file, while the page rendering stays stable.

Each vocabulary item should support:

- Italian text;
- English meaning;
- category or tab;
- visual cue/image/icon;
- optional note;
- optional source note identifying the class, date, repo file, or classroom note where it came from.

## Speech rule

The site should use browser speech synthesis when available.

The speech behavior must:

- set Italian language explicitly with `it-IT`;
- rank available Italian voices and choose the best available voice automatically;
- offer a voice picker when multiple Italian voices are exposed;
- remember the selected voice locally when possible;
- fall back gracefully when no Italian voice is exposed by the browser/device.

The site cannot guarantee a premium Italian voice unless the browser/device exposes one. The correct behavior is to do the best available in web technology and show the current voice status to the learner.

## English visibility rule

The site must provide an option to show or hide English meanings. Italian remains the primary visible text. English is support, not the learning center.

## Hosting rule

The site should be static and hostable on GitHub Pages. It should not require a server, database, authentication, build step, or paid service.
