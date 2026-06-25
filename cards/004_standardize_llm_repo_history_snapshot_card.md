# Card 004 — Standardize LLM Repo History Snapshot

## Capture Back

The Workbench now treats the repo history export as a standard continuity file instead of a timestamped artifact stream.

## Decision

Use one canonical file:

```text
outputs/history/repo_history_for_llm.md
```

The exporter overwrites this file each run. Repeated `make pack` runs should not create additional timestamped history files.

## LI added

```text
li/workflow/llm_repo_history_snapshot_rule.md
```

## Tools updated

```text
tools/export_repo_history_for_llm.py
tools/clean_li_repo_artifacts.py
tools/verify_italian_learning_li.py
```

## Reason

The file is important Workbench continuity. It is not Git history itself; it is an LLM-readable surface derived from the repo state. A stable path lets the Registry, template, humans, and LLMs all know where to look.
