# Card 015 — Flashcard Adds Must Not Create Verifier Churn

## Decision

Ordinary flashcard additions are content/data updates. They must not require changes
to `tools/verify_italian_learning_li.py`.

## Why

The flashcard site is expected to grow quickly from class notes, curated images,
and practice phrases. Verification should protect the data contract and runtime,
not force every new card to become a tool-maintenance event.

## Rule

Use a generic flashcard data-contract verifier. Do not add per-card verifier tokens
for each new FC.

## Acceptance

- Adding a new FC can pass verification without editing the verifier.
- The verifier checks schema and asset existence generically.
- Verifier changes are reserved for schema/runtime/governance changes.
