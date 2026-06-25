# LLM Repo History Snapshot Rule

The Italian Learning Workbench has one canonical LLM-readable repo history snapshot:

```text
outputs/history/repo_history_for_llm.md
```

This file is not Git history itself. Git history remains in `.git/`. The snapshot is a readable continuity export derived from the current repo state and recent Git log so a future LLM session can recover direction, accepted cards, LI changes, prompts, and current workbench state quickly.

## Required behavior

- `tools/export_repo_history_for_llm.py` writes `outputs/history/repo_history_for_llm.md`.
- The script overwrites that stable file on each run.
- `make history` and `make pack` update the stable file.
- The default history export must not create timestamped `repo_history_for_llm.md` files.
- Legacy timestamped files are treated as stale generated artifacts and may be removed.

## Why this matters

The history snapshot is a standard Workbench continuity surface. It gives humans and LLMs one known place to look before continuing a Workbench loop.
