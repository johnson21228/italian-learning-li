# Card 008 — CB Overlay-Only Default Artifact

## Purpose

Make overlay packs the default artifact for Capture Back changes against the existing Italian Learning Workbench.

## Decision

For an existing Workbench repo, a CB should produce a named overlay zip that can be unzipped over the current working tree. The overlay should contain only the changed or added files needed for the CB.

Do not also provide a full repo pack by default.

## Exceptions

Full packs are appropriate only when:
- creating a brand-new Workbench
- explicitly asked by the user
- producing a release/archive artifact
- recovering from a broken or missing local repo

## Applies to

- `italian-learning-li`
- future CB overlays for Italian learning prompts, corpus entries, image assets, source summaries, and practice loops

## Verification

`make verify` confirms this rule exists and is referenced from the Workbench map and spine.

## Rule file

- `li/workflow/cb_overlay_only_default_rule.md`
