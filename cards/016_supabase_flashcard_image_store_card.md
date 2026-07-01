# Card 016 — Supabase Flashcard Image Store

## Decision

Add a Supabase-backed curated flashcard image store modeled after the
Bracketeering Supabase browser-client seam.

## Why

The flashcard workflow now has per-card prompt generation. The next useful step
is to let a generated image be pasted back into the card and saved as a curated
runtime image override.

## Scope

- Add public Supabase config shell.
- Add shared Supabase browser client.
- Add flashcard image store service.
- Add SQL target for image metadata and Storage RLS.
- Add UI hook for clipboard image upload.
- Keep static images and placeholders as fallback truth.

## Acceptance

- Site runs normally when Supabase is disabled.
- When configured, active Supabase images override local card images.
- Clipboard upload writes to Supabase Storage and metadata table.
- No service-role secrets are committed.
