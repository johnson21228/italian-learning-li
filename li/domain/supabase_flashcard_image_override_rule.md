# Supabase Flashcard Image Override Rule

Supabase may hold curated flashcard image overrides.

Static flashcard metadata remains the fallback truth. A missing or unavailable
Supabase record must never break flashcard rendering.

Supabase image support is a runtime override layer:

- local `site/js/vocabulary-data.js` remains the flashcard corpus
- local `image` paths remain valid fallbacks
- Supabase `flashcard_images` rows may override card images at runtime
- Storage uploads require authenticated users and RLS
- public site code may use only a publishable browser key
- no service-role key may be checked into the repo

A flashcard image upload is a curation action, not a schema rewrite.
