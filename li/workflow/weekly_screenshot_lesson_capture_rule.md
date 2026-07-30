# Weekly Screenshot Lesson Capture Rule

## Purpose

Turn each new week of Italian class screenshots into a durable, reviewable
lesson that works both inside the Workbench and on the learning site.

## Required weekly sequence

```text
receive screenshots and learner recollection
→ inspect current Workbench and existing dirty state
→ transcribe only clearly visible material
→ label reconstruction, inference, and learner recollection
→ create privacy-safe exact crops
→ write conversation-first Markdown lesson
→ write paired visual Markdown flashcards
→ update the governed generative flashcard inputs when appropriate
→ verify links, assets, and Workbench integrity
→ return complete diff and visual evidence
→ obtain human acknowledgment
→ commit
→ refresh pack
→ push only with separate authorization
```

## Source and interpretation boundary

Each weekly Capture Back must distinguish:

- exact visible slide text;
- obscured or uncertain material;
- direct learner recollection;
- standard-language reconstruction supplied by the II;
- new practice examples written to make the material usable.

Do not silently turn inference into classroom transcription.

## Image rule

- Prefer exact deterministic crops from supplied screenshots.
- Exclude participant video, names, meeting controls, URLs, tokens, and unrelated
  desktop material.
- AI-generated imagery must never be represented as a screenshot crop.
- Workbench custody lives under `assets/class_material/<week>/`.
- Classroom crops do not enter the published site merely because they exist.
- A separately reviewed flashcard visual may be promoted through the generative-card protocol.

## Learning rule

The lesson begins with a small useful exchange. Vocabulary and conjugation
tables follow as clarification after the learner has spoken.

Every lesson should include:

- one communicative center;
- useful first-person lines;
- pronunciation/speaking prompts;
- repair language;
- a short retrieval exercise;
- provenance notes.

## Published-site boundary

The published site is the focused generative flashcard practice surface. Weekly
Markdown lessons and privacy-safe crops remain governed Workbench material; they
do not create a Lessons button, lesson index, dated lesson page, lesson-only
stylesheet, or published class-lesson image directory.

Promotion of particular lesson evidence into generated flashcards requires its
own reviewed Capture Back and must preserve provenance.

## Capture Back boundary

Each week is one separately reviewable Capture Back. Verification does not
acknowledge it. Commit, pack refresh, publication, and push remain explicit
human-custody boundaries.
