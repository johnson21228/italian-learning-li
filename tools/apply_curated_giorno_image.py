from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
data_path = root / "site/js/vocabulary-data.js"
css_path = root / "site/css/app.css"
image_path = root / "site/images/vocabulary/curated/giorno.png"

if not data_path.exists():
    raise SystemExit("Expected site/js/vocabulary-data.js not found.")
if not image_path.exists():
    raise SystemExit("Expected curated giorno image not found at site/images/vocabulary/curated/giorno.png.")

text = data_path.read_text()
new_entry = '{ italian: "giorno", english: "day", icon: "🌅", image: "images/vocabulary/curated/giorno.png", imageAlt: "warm daytime landscape", note: "time", curated: true, imageEssence: "morning sunlight, clear sky, and the feeling of a new day", imagePrompt: "Create a simple, warm, square vocabulary image for the Italian noun giorno meaning day. It should convey the essence of daytime: morning sunlight, clear sky, and the feeling of a new day. No text in the image. Clean friendly style suitable for a language-learning flashcard website. Square format." }'
pattern = re.compile(r'\{ italian: "giorno"[^\n]*\}')
text2, count = pattern.subn(new_entry, text, count=1)
if count != 1:
    raise SystemExit("Expected exactly one giorno vocabulary entry to patch.")
data_path.write_text(text2)

css_add = """

/* Curated vocabulary images: larger review-friendly display. */
.vocab-card img,
.vocabulary-card img,
.card-image,
.vocab-image,
.term-image {
  width: min(100%, 220px);
  height: 220px;
  object-fit: cover;
  border-radius: 18px;
}
"""
css = css_path.read_text() if css_path.exists() else ""
if "Curated vocabulary images: larger review-friendly display" not in css:
    css_path.write_text(css.rstrip() + css_add)

print("Patched giorno to use curated site image and larger vocabulary image display.")
