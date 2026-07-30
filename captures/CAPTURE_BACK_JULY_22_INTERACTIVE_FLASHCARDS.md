# Capture Back: July 22 Interactive Flashcard Correction

## Status

Acknowledged by the human custodian on 2026-07-30.

## Observation

The acknowledged July 22 Capture Back created a detailed Markdown visual deck
and a browsable lesson page, but it did not append July 22 entries to the site's
actual `ITALIAN_CLASSROOM_FLASHCARDS` data source.

Consequently, the intended practice loop—see an image, read the Italian, and
tap the image to hear Italian—was not available for the July 22 material.

## Proposal

Add a bounded July 22 card set to the existing interactive flashcard surface.
Reuse the exact privacy-safe classroom crops already held by the Workbench and
site. Add July 22 topic filters and verifier coverage.

Grouped vocabulary and conjugation cards intentionally speak a short ordered
list. Communicative phrase cards speak the exact visible Italian phrase.

## Provenance

- Visible classroom wording remains classroom evidence.
- The `venire` conjugation and example exchange remain explicitly reconstructed
  from learner recollection plus standard Italian.
- The `venire` cards reuse the places image as a movement prompt; they do not
  represent that image as a visible `venire` table.

## Boundary

This correction does not remove the Markdown lesson or reading page. It does
not acknowledge itself, commit, rebuild the pack, publish, or push.


## Generated venire practice image

The proposed interactive set includes one newly generated mnemonic image of
people coming toward a shared destination. It is stored at the stable curated
site path `site/images/vocabulary/curated/venire-coming.png`.

The image is reused across six separate conjugation cards—`vengo`, `vieni`,
`viene`, `veniamo`, `venite`, and `vengono`—so each retrieval and speech action
is short. The image is labeled as generated practice material and is never
represented as classroom evidence.


## First curated verb-image batch

At the learner's direction, this proposal also includes the first bounded
eight-image verb-curation batch:

- `stare`
- `chiamarsi`
- `andare`
- `capire`
- `ripetere`
- `dire`
- `guardare`
- `ascoltare`

Each image was generated from the prompt exposed by the site, with a final
subject-specific visual clarification. The complete prompt and image essence
are preserved on its flashcard. Each accepted candidate moves from
`needs-image` to `curated` and uses a stable site-owned path.
