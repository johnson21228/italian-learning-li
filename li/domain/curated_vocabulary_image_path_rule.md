# Curated Vocabulary Image Path Rule

Curated vocabulary images used by the website must live at stable site-owned paths.

Preferred path pattern:

- `site/images/vocabulary/curated/<term>.png`

The vocabulary data should reference the stable website path, not a temporary generated filename.

Example:

- `images/vocabulary/curated/giorno.png`

This allows future edits to replace the image file while keeping the website and vocabulary database references unchanged.

When a curated image is accepted:

1. Copy the image to the stable curated path.
2. Set the vocabulary entry `curated` flag to `true`.
3. Preserve the image prompt and image essence used to create or approve the image.
4. Keep the Italian term as selectable/speakable text separate from the image.
