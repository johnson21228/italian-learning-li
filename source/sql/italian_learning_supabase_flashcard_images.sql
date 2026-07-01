-- Italian Learning LI — Supabase flashcard image curation support
--
-- Apply this in the Supabase SQL editor for the Italian Learning project.
-- This creates:
--   - public flashcard image metadata
--   - public read for active image rows
--   - authenticated-only image writes
--   - a public Storage bucket for image display
--   - authenticated Storage upload policy scoped to the user's own folder

create extension if not exists pgcrypto;

insert into storage.buckets (id, name, public)
values ('flashcard-images', 'flashcard-images', true)
on conflict (id) do update set public = excluded.public;

create table if not exists public.flashcard_images (
  id uuid primary key default gen_random_uuid(),
  card_key text not null,
  italian text not null default '',
  storage_path text not null,
  public_url text not null default '',
  status text not null default 'active' check (status in ('active', 'superseded', 'rejected')),
  created_by uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now()
);

create index if not exists flashcard_images_card_key_status_created_idx
  on public.flashcard_images (card_key, status, created_at desc);

alter table public.flashcard_images enable row level security;

drop policy if exists "Active flashcard images are public read" on public.flashcard_images;
create policy "Active flashcard images are public read"
  on public.flashcard_images
  for select
  using (status = 'active');

drop policy if exists "Authenticated users can insert flashcard images" on public.flashcard_images;
create policy "Authenticated users can insert flashcard images"
  on public.flashcard_images
  for insert
  to authenticated
  with check (auth.uid() = created_by);

drop policy if exists "Authenticated users can update own flashcard images" on public.flashcard_images;
create policy "Authenticated users can update own flashcard images"
  on public.flashcard_images
  for update
  to authenticated
  using (auth.uid() = created_by)
  with check (auth.uid() = created_by);

drop policy if exists "Flashcard image files are public read" on storage.objects;
create policy "Flashcard image files are public read"
  on storage.objects
  for select
  using (bucket_id = 'flashcard-images');

drop policy if exists "Authenticated users can upload own flashcard image files" on storage.objects;
create policy "Authenticated users can upload own flashcard image files"
  on storage.objects
  for insert
  to authenticated
  with check (
    bucket_id = 'flashcard-images'
    and (storage.foldername(name))[1] = auth.uid()::text
  );

drop policy if exists "Authenticated users can update own flashcard image files" on storage.objects;
create policy "Authenticated users can update own flashcard image files"
  on storage.objects
  for update
  to authenticated
  using (
    bucket_id = 'flashcard-images'
    and (storage.foldername(name))[1] = auth.uid()::text
  )
  with check (
    bucket_id = 'flashcard-images'
    and (storage.foldername(name))[1] = auth.uid()::text
  );
