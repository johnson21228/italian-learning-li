# Generative Flashcard System Rule

## Purpose

The site is a practice projection generated from governed Workbench truth. It
is not the authority for class evidence, verb paradigms, or vocabulary.

## Card invariant

Every admitted verb produces one six-card round:

```text
six subjects
× every conjugation exactly once
× a different compatible complement on every card
```

Objects, destinations, states, names, and phrases are all typed complements.
The generator may only pair a verb with complements explicitly admitted for
that verb.

## Growth rule

New class evidence may append:

- a reviewed verb paradigm;
- a typed complement with its exact phrase and article/preposition;
- a visual, label, gloss, and provenance;
- a compatibility link between verb and complement.

New material expands future rounds without requiring manually duplicated cards.
When a pool contains more than six compatible complements, rounds draw without
replacement so the larger pool compounds practice over time.

## Admission gate

A verb may appear on the generated site only when it has:

- six reviewed subject forms;
- at least six distinct compatible complements;
- exact sentence fragments;
- visual and spoken representations;
- source or reconstruction provenance;
- passing matrix verification.

Learned verbs that do not yet satisfy the gate remain in the pending registry.
Standard-language reconstruction may satisfy missing structure only when it is
explicitly labeled as reconstruction and reviewed through Capture Back. It
must never be represented as directly visible classroom evidence.

## Site boundary

The site shows only generated practice cards. Historical manually assembled
cards remain recoverable in Git history and their class evidence remains in LI,
assets, and Capture Backs.

Filters, image-prompt generation, and authenticated image mutation are outside
this focused practice projection.
