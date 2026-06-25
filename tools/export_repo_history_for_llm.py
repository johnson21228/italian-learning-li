#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path

out_dir = Path("outputs/history")
out_dir.mkdir(parents=True, exist_ok=True)
stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
out = out_dir / f"repo_history_for_llm_{stamp}.md"
out.write_text(
    "# Repo History for LLM\n\n"
    "This initial pack was generated from a Workbench template pattern for italian-learning-li.\n\n"
    "Current accepted direction: childlike language acquisition, first-person conversation, and personal corpus.\n",
    encoding="utf-8",
)
print(f"Wrote {out}")
