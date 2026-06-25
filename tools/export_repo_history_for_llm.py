#!/usr/bin/env python3
"""Export the Italian Learning LI stable LLM-readable history snapshot."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import subprocess

OUT_DIR = Path('outputs/history')
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / 'repo_history_for_llm.md'


def run(cmd):
    try:
        return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT).strip()
    except Exception as e:
        return f"[command failed: {' '.join(cmd)}]\n{e}"


status = run(['git', 'status', '--short'])
log = run(['git', 'log', '--oneline', '--decorate', '--max-count=40'])
branch = run(['git', 'branch', '--show-current'])
files = run(['git', 'ls-files'])
generated = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
digest = hashlib.sha1((status + log + files).encode('utf-8')).hexdigest()[:7]

OUT.write_text(f"""# Repository History for LLM

Generated: {generated}
Branch: {branch or '[unknown]'}
Snapshot digest: {digest}
Canonical path: outputs/history/repo_history_for_llm.md

This file is the stable Italian Learning Workbench continuity snapshot. It is not Git history itself; it is an LLM-readable export derived from the current repository state. The file is overwritten by `tools/export_repo_history_for_llm.py` on each history/pack run so future sessions have one standard place to recover recent direction, accepted LI changes, cards, prompts, and open workbench state.

## Current accepted direction

The Italian Learning LI starts from childlike language acquisition, first-person conversation, conversation before grammar, and a personal corpus of encountered Italian.

## Recent commits

```text
{log or '[no git log available]'}
```

## Working tree status

```text
{status or '[clean]'}
```

## Tracked files

```text
{files or '[no tracked files available]'}
```
""", encoding='utf-8')
print(f'Wrote {OUT}')
