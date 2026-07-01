import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm";
import { ITALIAN_LEARNING_SUPABASE_PUBLIC_CONFIG } from "../config/supabase.public.js";

let sharedSupabaseClient = null;

function hasPlaceholder(value) {
  return /YOUR_PROJECT_REF|YOUR_PUBLISHABLE_KEY/i.test(String(value || ""));
}

function isSupabasePublicConfigReady(config = ITALIAN_LEARNING_SUPABASE_PUBLIC_CONFIG) {
  return Boolean(
    config
    && config.enabled === true
    && typeof config.supabaseUrl === "string"
    && config.supabaseUrl.startsWith("https://")
    && !hasPlaceholder(config.supabaseUrl)
    && typeof config.supabasePublishableKey === "string"
    && config.supabasePublishableKey.length > 0
    && !hasPlaceholder(config.supabasePublishableKey)
  );
}

function getSharedSupabaseClient(config = ITALIAN_LEARNING_SUPABASE_PUBLIC_CONFIG) {
  if (!isSupabasePublicConfigReady(config)) {
    return null;
  }

  if (!sharedSupabaseClient) {
    sharedSupabaseClient = createClient(config.supabaseUrl, config.supabasePublishableKey, {
      auth: {
        persistSession: true,
        autoRefreshToken: true,
        detectSessionInUrl: true,
      },
    });
  }

  return sharedSupabaseClient;
}

function requireSharedSupabaseClient(config = ITALIAN_LEARNING_SUPABASE_PUBLIC_CONFIG) {
  const client = getSharedSupabaseClient(config);
  if (!client) {
    throw new Error("Supabase public client is not configured.");
  }
  return client;
}

export {
  getSharedSupabaseClient,
  isSupabasePublicConfigReady,
  requireSharedSupabaseClient,
};
