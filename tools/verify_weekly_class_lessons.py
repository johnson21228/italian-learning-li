#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    "li/workflow/weekly_screenshot_lesson_capture_rule.md",
    "templates/weekly_screenshot_lesson/README.md",
    "li/corpus/july_22_restaurant_places_and_movement_lesson.md",
    "li/flashcards/july_22_visual_flashcards.md",
    "site/lessons/index.html",
    "site/lessons/2026-07-22.html",
    "site/css/lesson.css",
]
for name in required:
    if not (ROOT / name).is_file():
        errors.append(f"missing: {name}")

custody = ROOT / "assets/class_material/july_22/clips"
site_images = ROOT / "site/images/class-lessons/2026-07-22"
custody_names = sorted(path.name for path in custody.glob("*.png"))
site_names = sorted(path.name for path in site_images.glob("*.png"))
if custody_names != site_names:
    errors.append("Workbench-custody and site lesson image sets differ")

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

for name in sorted(set(custody_names) & set(site_names)):
    if digest(custody / name) != digest(site_images / name):
        errors.append(f"site image differs from custody source: {name}")

lesson = ROOT / "site/lessons/2026-07-22.html"
if lesson.is_file():
    text = lesson.read_text()
    image_refs = re.findall(r'src="\.\./images/class-lessons/2026-07-22/([^"]+)"', text)
    for name in image_refs:
        if not (site_images / name).is_file():
            errors.append(f"lesson image link missing: {name}")
    for token in (
        "Vieni al ristorante?",
        "Cosa ordini da mangiare e da bere?",
        "Vado al mercato.",
        "vengo",
        "vengono",
        "Ho bisogno di un taxi.",
    ):
        if token not in text:
            errors.append(f"July 22 site lesson missing: {token}")

index = ROOT / "site/lessons/index.html"
if index.is_file() and 'href="2026-07-22.html"' not in index.read_text():
    errors.append("lesson index does not link July 22 lesson")

home = ROOT / "site/index.html"
if home.is_file() and 'href="lessons/index.html"' not in home.read_text():
    errors.append("site home does not link lesson index")

rule = ROOT / "li/workflow/weekly_screenshot_lesson_capture_rule.md"
if rule.is_file():
    text = rule.read_text()
    for token in (
        "Source and interpretation boundary",
        "privacy-safe exact crops",
        "human acknowledgment",
        "push only with separate authorization",
    ):
        if token not in text:
            errors.append(f"weekly rule missing: {token}")

if errors:
    print("Weekly class lesson verification failed.")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Weekly class lesson verification passed.")
print(f"lesson images: {len(site_names)}")
print("site lessons: 1")
