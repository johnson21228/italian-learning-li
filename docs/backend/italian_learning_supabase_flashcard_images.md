# Supabase Flashcard Image Store

Italian Learning LI may use Supabase as a curated image override layer.

The static site data remains the fallback truth. Supabase image rows are optional
runtime overrides for flashcard images.

## Pattern

This follows the Bracketeering public-browser Supabase pattern:

- public config file
- shared Supabase browser client
- feature service seam
- SQL target under `source/sql`
- static rendering remains safe without Supabase

## Runtime behavior

For each flashcard:

1. Render the static/local image if present.
2. Ask the Supabase image store whether an active uploaded image exists.
3. If yes, prefer the uploaded image URL.
4. If Supabase is disabled, not configured, or unavailable, render the static site normally.

## Upload workflow

Admin/user workflow:

1. Copy image prompt from flashcard.
2. Generate an image.
3. Copy the generated image to clipboard.
4. Click `Paste Supabase image` on the flashcard.
5. Browser reads image from clipboard.
6. Image uploads to Supabase Storage.
7. A `flashcard_images` row records the active image override.
8. The card re-renders using the uploaded image.

## Safety

Uploads require Supabase Auth and Storage RLS.

The GitHub Pages site must not expose service-role keys. Only a publishable/anon
browser key belongs in `site/js/config/supabase.public.js`.
