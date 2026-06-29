#!/usr/bin/env python3
import re
from pathlib import Path

text = Path("site/js/vocabulary-data.js").read_text()

for m in re.finditer(r'\{[^{}]*italian:\s*"([^"]+)"[^{}]*english:\s*"([^"]+)"[^{}]*\}', text):
    entry = m.group(0)
    italian = m.group(1)
    english = m.group(2)

    note = re.search(r'note:\s*"([^"]+)"', entry)
    image = re.search(r'image:\s*"([^"]+)"', entry)
    curated = re.search(r'curated:\s*true', entry)
    essence = re.search(r'imageEssence:\s*"([^"]+)"', entry)

    ok = curated and image and image.group(1).startswith("images/vocabulary/curated/")

    if not ok:
        print(f"Italian: {italian}")
        print(f"English: {english}")
        print(f"tab/kind: {note.group(1) if note else 'unknown'}")
        print(f"current image status: {image.group(1) if image else 'missing image'}; curated={'true' if curated else 'missing/false'}")
        print(f"proposed image essence: {essence.group(1) if essence else 'needs simple concrete visual essence'}")
        print()
        print(entry)
        break
else:
    print("All vocabulary entries appear curated.")
