# CB Overlay-Only Default Rule

For an existing Workbench repo, a Capture Back should produce a named overlay zip that can be unzipped over the current working tree. The overlay should contain only the changed or added files needed for the CB.

Do not also provide a full repo pack by default.

Full packs are appropriate only when:
- creating a brand-new Workbench
- explicitly asked by the user
- producing a release/archive artifact
- recovering from a broken or missing local repo

The response should emphasize the overlay artifact and apply command. It should not distract with a full-pack alternative unless needed.

## Why this matters

The learner’s repo is an ongoing Workbench. Repeated full packs create ambiguity: the user may apply the wrong artifact, overwrite local work, or think a CB landed when only an older pack was downloaded. Overlay-only CBs keep the apply path narrow and auditable.

## Default assistant behavior

When the user asks to CB a change in `italian-learning-li`:
1. Create one named overlay zip.
2. Put only changed/new files in that overlay.
3. Provide the apply command for the existing repo.
4. Do not generate or link a full pack unless the user explicitly asks.
5. Verify the overlay outcome using `make verify` and `make pack` after application.
