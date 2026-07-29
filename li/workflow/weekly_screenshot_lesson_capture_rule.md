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
→ create/update static site lesson
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
- Site copies live under `site/images/class-lessons/<YYYY-MM-DD>/`.
- Derived site copies must match their Workbench-custody source bytes.

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

## Site rule

Create:

```text
site/lessons/<YYYY-MM-DD>.html
```

Add one entry to:

```text
site/lessons/index.html
```

The page must work as static HTML under the existing GitHub Pages deployment.
It must not require a server or build step.

## Capture Back boundary

Each week is one separately reviewable Capture Back. Verification does not
acknowledge it. Commit, pack refresh, publication, and push remain explicit
human-custody boundaries.
