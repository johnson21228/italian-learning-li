#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    "li/workflow/weekly_screenshot_lesson_capture_rule.md",
    "templates/weekly_screenshot_lesson/README.md",
    "li/corpus/july_22_restaurant_places_and_movement_lesson.md",
    "li/flashcards/july_22_visual_flashcards.md",
    "assets/class_material/july_22/clips",
    "captures/CAPTURE_BACK_REMOVE_PUBLISHED_LESSONS_SURFACE.md",
]
for name in required:
    if not (ROOT / name).exists():
        errors.append(f"missing Workbench-custody material: {name}")

for name in [
    "site/lessons",
    "site/images/class-lessons",
    "site/css/lesson.css",
]:
    if (ROOT / name).exists():
        errors.append(f"published lesson surface remains: {name}")

home = ROOT / "site/index.html"
home_text = home.read_text() if home.is_file() else ""
for token in ["lessons/index.html", ">Lessons<"]:
    if token in home_text:
        errors.append(f"Lessons navigation remains: {token}")

rule = (ROOT / "li/workflow/weekly_screenshot_lesson_capture_rule.md").read_text()
for token in [
    "Source and interpretation boundary",
    "privacy-safe exact crops",
    "human acknowledgment",
    "published site is the focused generative flashcard practice surface",
]:
    if token not in rule:
        errors.append(f"weekly custody rule missing: {token}")

source_images = sorted((ROOT / "assets/class_material/july_22/clips").glob("*.png"))
if len(source_images) != 9:
    errors.append(f"expected 9 July 22 custody images; found {len(source_images)}")

if errors:
    print("Weekly class custody verification failed.")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Weekly class custody verification passed.")
print(f"custody images: {len(source_images)}")
print("published lesson surfaces: 0")
