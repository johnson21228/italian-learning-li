# Capture Back: Composable Avere, Bere, and Mangiare Flashcard Pilot

## Status

Acknowledged by the human custodian on 2026-07-30.

## Intent

Test a scalable flashcard recipe:

```text
labeled subject icon + reusable verb action + labeled class-vocabulary object
→ visible Italian sentence + tap-to-hear speech
```

## Pilot

Six `avere`, six `bere`, and six `mangiare` cards reuse:

- six grammar-subject SVGs with Italian pronouns overlaid on the body;
- one generated, subject-neutral action image for each verb;
- reusable drink and pasta object SVGs derived from class vocabulary;
- eighteen complete contextual sentences.

The site overlays the infinitive on each verb action and the Italian noun on
each object. These labels are presentation metadata rather than burned-in image
content, keeping the assets reusable.

The exact visible class tables remain retained as source evidence and top-level
fallback metadata. The composable cards use simpler action mnemonics that work
unchanged with every conjugation.

The selected `avere` mnemonic follows the corpus emphasis on `avere fame`,
`avere sete`, `avere bisogno`, and possession. It groups an empty bowl, water
drop, and key without depicting physical holding; the earlier hand-and-key
candidate was rejected before acknowledgment.

The runtime assembles the three visual parts. It does not generate images or
call an external service while the learner studies.

## Filters

The pilot adds filters for grammatical subject, `Bevande`, and individual
drink objects.

## Provenance

The `avere`, `bere`, and `mangiare` tables are class evidence. Subject and object SVGs are
new deterministic practice graphics. The shared action mnemonics are generated
practice imagery, not classroom evidence; they intentionally contain no text,
person, gender, number, or grammatical-subject cue. Visible verb and object
labels are site-rendered metadata. Complete sentences are practice compositions
built from visible conjugations and class vocabulary.

## Boundary

This pilot does not acknowledge itself, commit, rebuild the pack, publish, or
push.
