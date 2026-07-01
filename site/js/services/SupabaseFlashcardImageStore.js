import { ITALIAN_LEARNING_SUPABASE_PUBLIC_CONFIG } from "../config/supabase.public.js";
import { getSharedSupabaseClient, isSupabasePublicConfigReady } from "./SupabaseClient.js";

const UPDATED_EVENT = "italian-learning:supabase-images-updated";
const imageRowsByCardKey = new Map();

function slugify(value) {
  return String(value || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 96);
}

function cardKeyFor(item = {}) {
  return item.key || item.slug || item.cardKey || slugify(item.italian || item.speak || item.imageAlt || "flashcard");
}

function configured() {
  return isSupabasePublicConfigReady(ITALIAN_LEARNING_SUPABASE_PUBLIC_CONFIG);
}

function client() {
  return getSharedSupabaseClient(ITALIAN_LEARNING_SUPABASE_PUBLIC_CONFIG);
}

function bucketName() {
  return ITALIAN_LEARNING_SUPABASE_PUBLIC_CONFIG.imageBucket || "flashcard-images";
}

function tableName() {
  return ITALIAN_LEARNING_SUPABASE_PUBLIC_CONFIG.imageTable || "flashcard_images";
}

function dispatchUpdated() {
  window.dispatchEvent(new CustomEvent(UPDATED_EVENT));
}

function bestImageUrlForCard(item = {}) {
  const key = cardKeyFor(item);
  const row = imageRowsByCardKey.get(key);
  return row?.public_url || row?.publicUrl || "";
}

async function loadActiveImageRows() {
  const supabase = client();
  if (!supabase) return [];

  const { data, error } = await supabase
    .from(tableName())
    .select("id, card_key, italian, storage_path, public_url, status, created_at")
    .eq("status", "active")
    .order("created_at", { ascending: false });

  if (error) throw error;

  imageRowsByCardKey.clear();
  for (const row of data || []) {
    if (!imageRowsByCardKey.has(row.card_key)) {
      imageRowsByCardKey.set(row.card_key, row);
    }
  }

  dispatchUpdated();
  return data || [];
}

async function readClipboardImageBlob() {
  if (!navigator.clipboard?.read) {
    throw new Error("Clipboard image read is not available in this browser. Use Chrome or another browser that supports clipboard image reads on HTTPS.");
  }

  const items = await navigator.clipboard.read();
  for (const item of items) {
    const imageType = item.types.find((type) => type.startsWith("image/"));
    if (imageType) {
      return await item.getType(imageType);
    }
  }

  throw new Error("No image was found on the clipboard.");
}

async function convertImageBlobToJpeg(blob, quality = 0.9) {
  const bitmap = await createImageBitmap(blob);
  const canvas = document.createElement("canvas");
  canvas.width = bitmap.width;
  canvas.height = bitmap.height;

  const context = canvas.getContext("2d");

  // JPEG has no transparency. Flatten transparent PNG/WebP pixels onto white.
  context.fillStyle = "#ffffff";
  context.fillRect(0, 0, canvas.width, canvas.height);
  context.drawImage(bitmap, 0, 0);

  bitmap.close?.();

  return await new Promise((resolve, reject) => {
    canvas.toBlob((jpegBlob) => {
      if (!jpegBlob) {
        reject(new Error("Could not convert clipboard image to JPEG."));
        return;
      }
      resolve(jpegBlob);
    }, "image/jpeg", quality);
  });
}

async function uploadClipboardImageForCard(item = {}) {
  const supabase = client();
  if (!supabase) {
    throw new Error("Supabase image upload is not configured.");
  }

  const { data: userData, error: userError } = await supabase.auth.getUser();
  if (userError) throw userError;

  const user = userData?.user;
  if (!user) {
    throw new Error("Sign in before uploading flashcard images.");
  }

  const clipboardBlob = await readClipboardImageBlob();
  const jpegBlob = await convertImageBlobToJpeg(clipboardBlob, 0.9);

  const key = cardKeyFor(item);
  const ext = "jpg";
  const storagePath = `${user.id}/vocabulary/${key}/${Date.now()}.${ext}`;
  const file = new File([jpegBlob], `${key}.${ext}`, { type: "image/jpeg" });

  const { error: uploadError } = await supabase.storage
    .from(bucketName())
    .upload(storagePath, file, {
      contentType: file.type,
      upsert: false,
    });

  if (uploadError) throw uploadError;

  const { data: publicData } = supabase.storage
    .from(bucketName())
    .getPublicUrl(storagePath);

  const publicUrl = publicData?.publicUrl || "";

  await supabase
    .from(tableName())
    .update({ status: "superseded" })
    .eq("card_key", key)
    .eq("status", "active");

  const { data: inserted, error: insertError } = await supabase
    .from(tableName())
    .insert({
      card_key: key,
      italian: item.italian || "",
      storage_path: storagePath,
      public_url: publicUrl,
      status: "active",
      created_by: user.id,
    })
    .select("id, card_key, italian, storage_path, public_url, status, created_at")
    .single();

  if (insertError) throw insertError;

  imageRowsByCardKey.set(key, inserted);
  dispatchUpdated();

  return inserted;
}

window.ItalianLearningSupabaseImages = {
  UPDATED_EVENT,
  isConfigured: configured,
  cardKeyFor,
  bestImageUrlForCard,
  loadActiveImageRows,
  uploadClipboardImageForCard,
};

if (configured()) {
  loadActiveImageRows().catch((error) => {
    console.warn("Italian Learning Supabase image load failed:", error);
  });
}
