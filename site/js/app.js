const state = {
  activeFilter: "all",
  voices: [],
  selectedVoiceURI: localStorage.getItem("italianVoiceURI") || "",
  supabaseAuthMessage: "",
};

const cardsEl = document.getElementById("cards");
const showEnglishEl = document.getElementById("showEnglish");
const voiceSelectEl = document.getElementById("voiceSelect");
const voiceStatusEl = document.getElementById("voiceStatus");
const filterBarEl = document.getElementById("filterBar");
const activeFilterLabelEl = document.getElementById("activeFilterLabel");
const supabaseAuthStatusEl = document.getElementById("supabaseAuthStatus");
const supabaseAuthEmailEl = document.getElementById("supabaseAuthEmail");
const supabaseSignInButtonEl = document.getElementById("supabaseSignInButton");
const supabaseSignOutButtonEl = document.getElementById("supabaseSignOutButton");

function allFlashcards() {
  if (Array.isArray(window.ITALIAN_CLASSROOM_FLASHCARDS)) return window.ITALIAN_CLASSROOM_FLASHCARDS;
  const grouped = window.ITALIAN_CLASSROOM_VOCABULARY || {};
  return [...(grouped.nouns || grouped.nowns || []), ...(grouped.verbs || []), ...(grouped.other || [])];
}

function rankItalianVoice(voice) {
  const name = `${voice.name} ${voice.lang}`.toLowerCase();
  let score = 0;
  if (voice.lang === "it-IT") score += 100;
  else if (voice.lang && voice.lang.startsWith("it")) score += 75;
  if (/premium|enhanced|siri|neural|natural/i.test(name)) score += 30;
  if (/alice|elsa|paola|luca|ital/i.test(name)) score += 15;
  if (voice.localService) score += 5;
  return score;
}

function getItalianVoices() {
  return speechSynthesis.getVoices()
    .filter((voice) => voice.lang === "it-IT" || (voice.lang || "").startsWith("it"))
    .sort((a, b) => rankItalianVoice(b) - rankItalianVoice(a));
}

function selectedVoice() {
  const italian = getItalianVoices();
  if (!italian.length) return null;
  return italian.find((voice) => voice.voiceURI === state.selectedVoiceURI) || italian[0];
}

function refreshVoices() {
  state.voices = getItalianVoices();
  voiceSelectEl.innerHTML = "";
  if (!state.voices.length) {
    const option = document.createElement("option");
    option.textContent = "No Italian voice exposed";
    option.value = "";
    voiceSelectEl.appendChild(option);
    voiceSelectEl.disabled = true;
    voiceStatusEl.textContent = "No Italian voice is currently exposed by this browser/device. Speech will still request it-IT.";
    return;
  }
  voiceSelectEl.disabled = false;
  const best = selectedVoice();
  state.voices.forEach((voice, index) => {
    const option = document.createElement("option");
    option.value = voice.voiceURI;
    option.textContent = `${index === 0 ? "Best: " : ""}${voice.name} (${voice.lang})`;
    voiceSelectEl.appendChild(option);
  });
  voiceSelectEl.value = best.voiceURI;
  voiceStatusEl.textContent = `Using ${best.name} (${best.lang}).`;
}

function speakItalian(text) {
  if (!("speechSynthesis" in window)) {
    alert("Speech synthesis is not available in this browser.");
    return;
  }
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "it-IT";
  utterance.rate = 0.85;
  utterance.pitch = 1.0;
  const voice = selectedVoice();
  if (voice) utterance.voice = voice;
  window.__italianLearningLastUtterance = utterance;
  speechSynthesis.cancel();
  speechSynthesis.resume();
  window.setTimeout(() => speechSynthesis.speak(utterance), 0);
}

function speakTextFor(item) {
  return item.speak || item.spokenItalian || item.italian;
}

function supabaseImageStore() {
  return window.ItalianLearningSupabaseImages || null;
}

function flashcardKeyFor(item) {
  const store = supabaseImageStore();
  if (store?.cardKeyFor) return store.cardKeyFor(item);
  return String(item.key || item.slug || item.italian || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function imageUrlFor(item) {
  const store = supabaseImageStore();
  const supabaseUrl = store?.bestImageUrlForCard?.(item);
  return supabaseUrl || item.image || "images/vocabulary/placeholders/word-placeholder.svg";
}

function isSupabaseSignedIn() {
  const store = supabaseImageStore();
  return Boolean(store?.getCurrentUser?.());
}

function canPasteSupabaseImage() {
  const store = supabaseImageStore();
  return Boolean(store?.isConfigured?.() && store?.uploadClipboardImageForCard && isSupabaseSignedIn());
}

function renderSupabaseAuthStatus() {
  if (!supabaseAuthStatusEl) return;

  const store = supabaseImageStore();
  const configured = Boolean(store?.isConfigured?.());
  const user = store?.getCurrentUser?.() || null;

  if (!configured) {
    supabaseAuthStatusEl.textContent = "Supabase image uploads are not configured.";
    if (supabaseAuthEmailEl) supabaseAuthEmailEl.disabled = true;
    if (supabaseSignInButtonEl) supabaseSignInButtonEl.disabled = true;
    if (supabaseSignOutButtonEl) supabaseSignOutButtonEl.hidden = true;
    return;
  }

  if (user) {
    const email = user.email || "signed-in user";
    supabaseAuthStatusEl.textContent = `Signed in as ${email}. Paste image upload is enabled.`;
    if (supabaseAuthEmailEl) supabaseAuthEmailEl.hidden = true;
    if (supabaseSignInButtonEl) supabaseSignInButtonEl.hidden = true;
    if (supabaseSignOutButtonEl) {
      supabaseSignOutButtonEl.hidden = false;
      supabaseSignOutButtonEl.disabled = false;
    }
    return;
  }

  supabaseAuthStatusEl.textContent = state.supabaseAuthMessage || "Sign in to upload curated flashcard images.";
  if (supabaseAuthEmailEl) {
    supabaseAuthEmailEl.hidden = false;
    supabaseAuthEmailEl.disabled = false;
  }
  if (supabaseSignInButtonEl) {
    supabaseSignInButtonEl.hidden = false;
    supabaseSignInButtonEl.disabled = false;
  }
  if (supabaseSignOutButtonEl) supabaseSignOutButtonEl.hidden = true;
}

async function pasteSupabaseImageFor(item, button, imageElement) {
  const store = supabaseImageStore();
  if (!store?.uploadClipboardImageForCard) {
    alert("Supabase image upload is not configured yet.");
    return;
  }

  const oldText = button.textContent;
  button.textContent = "Pasting…";
  button.disabled = true;

  try {
    const row = await store.uploadClipboardImageForCard(item);
    if (row?.public_url && imageElement) {
      imageElement.src = row.public_url;
    }
    button.textContent = "Uploaded!";
  } catch (error) {
    console.error(error);
    alert(error?.message || String(error));
    button.textContent = oldText;
  } finally {
    window.setTimeout(() => {
      button.textContent = oldText;
      button.disabled = false;
    }, 1200);
  }
}

function imagePromptFor(item) {
  if (item.imagePrompt) return item.imagePrompt;

  const categories = categoriesFor(item).join(", ");
  const meaning = item.english ? `The image should support the meaning: "${item.english}".` : "";
  const note = item.note ? `Instructional note: ${item.note}.` : "";

  return [
    `Create a simple square Italian flashcard image for "${item.italian}".`,
    meaning,
    note,
    `The Italian word or phrase to support is: ${speakTextFor(item)}.`,
    categories ? `Categories: ${categories}.` : "",
    "Use a clear, friendly, beginner-language-learning style.",
    "No English text.",
    "Avoid clutter.",
    "Make the image useful for remembering and speaking the Italian."
  ].filter(Boolean).join("\n");
}

async function copyImagePromptFor(item, button) {
  const prompt = imagePromptFor(item);

  try {
    await navigator.clipboard.writeText(prompt);
  } catch {
    const box = document.createElement("textarea");
    box.value = prompt;
    document.body.appendChild(box);
    box.select();
    document.execCommand("copy");
    document.body.removeChild(box);
  }

  const oldText = button.textContent;
  button.textContent = "Copied!";
  button.disabled = true;
  window.setTimeout(() => {
    button.textContent = oldText;
    button.disabled = false;
  }, 1200);
}

function categoriesFor(item) {
  if (Array.isArray(item.categories) && item.categories.length) return item.categories;
  const fallback = [];
  if (item.partOfSpeech) fallback.push(item.partOfSpeech);
  if (item.communicativeFunction) fallback.push(item.communicativeFunction);
  if (item.note) fallback.push(item.note);
  if (item.curated) fallback.push("curated");
  return fallback;
}

function filterLabel(category) {
  const labels = {
    all: "All",
    "class-1": "Class 1",
    saluti: "Saluti",
    presentazioni: "Presentazioni",
    "come-stai": "Come stai",
    nome: "Nome",
    essere: "Essere",
    stare: "Stare",
    "tu-lei": "Tu / Lei",
    formale: "Formale",
    informale: "Informale",
    riparazione: "Riparazione",
    "frasi-utili": "Frasi utili",
    dialogo: "Dialogo",
    sostantivi: "Sostantivi",
    verbi: "Verbi",
    frasi: "Frasi",
    domande: "Domande",
    risposte: "Risposte",
    curated: "Curated",
    "needs-image": "Needs image"
  };
  return labels[category] || category.split("-").map((part) => part ? part[0].toUpperCase() + part.slice(1) : part).join(" ");
}

function categoryCounts() {
  const counts = new Map([["all", allFlashcards().length]]);
  allFlashcards().forEach((item) => categoriesFor(item).forEach((category) => counts.set(category, (counts.get(category) || 0) + 1)));
  return counts;
}

function orderedCategories() {
  const counts = categoryCounts();
  const preferred = window.ITALIAN_CLASSROOM_CATEGORY_ORDER || [];
  const ordered = preferred.filter((category) => counts.has(category));
  const extras = [...counts.keys()].filter((category) => !ordered.includes(category)).sort((a, b) => a.localeCompare(b));
  return [...ordered, ...extras];
}

function renderFilters() {
  const counts = categoryCounts();
  filterBarEl.innerHTML = "";
  orderedCategories().forEach((category) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "filter-chip";
    button.dataset.category = category;
    button.setAttribute("aria-pressed", String(category === state.activeFilter));
    button.textContent = `${filterLabel(category)} ${counts.get(category)}`;
    button.addEventListener("click", () => {
      state.activeFilter = category;
      renderFilters();
      renderCards();
    });
    filterBarEl.appendChild(button);
  });
}

function visibleFlashcards() {
  const cards = allFlashcards();
  if (state.activeFilter === "all") return cards;
  return cards.filter((item) => categoriesFor(item).includes(state.activeFilter));
}

function renderCards() {
  const data = visibleFlashcards();
  cardsEl.innerHTML = "";
  if (activeFilterLabelEl) activeFilterLabelEl.textContent = `${filterLabel(state.activeFilter)} · ${data.length} FC${data.length === 1 ? "" : "s"}`;
  if (!data.length) {
    const empty = document.createElement("p");
    empty.className = "empty";
    empty.textContent = `No flashcards match ${filterLabel(state.activeFilter)}.`;
    cardsEl.appendChild(empty);
    return;
  }
  data.forEach((item) => {
    const card = document.createElement("article");
    card.className = "card";
    const icon = document.createElement("button");
    icon.type = "button";
    icon.className = "icon image-speak-button";
    const speakText = speakTextFor(item);
    icon.setAttribute("aria-label", `Hear ${speakText}`);
    icon.title = `Hear ${speakText}`;
    icon.addEventListener("click", () => speakItalian(speakText));
    const img = document.createElement("img");
    img.src = imageUrlFor(item);
    img.alt = item.imageAlt || item.italian;
    img.loading = "lazy";
    icon.appendChild(img);
    const italian = document.createElement("div");
    italian.className = "italian";
    italian.lang = "it";
    italian.textContent = item.italian;
    const english = document.createElement("div");
    english.className = "english";
    english.textContent = item.english || "";
const actions = document.createElement("div");

    actions.className = "card-actions";


    const promptButton = document.createElement("button");

    promptButton.type = "button";

    promptButton.className = "card-action-button";

    promptButton.textContent = "Copy image prompt";

    promptButton.setAttribute("aria-label", `Copy image prompt for ${item.italian}`);

    promptButton.addEventListener("click", () => copyImagePromptFor(item, promptButton));


    actions.appendChild(promptButton);

    if (canPasteSupabaseImage()) {
      const pasteButton = document.createElement("button");
      pasteButton.type = "button";
      pasteButton.className = "card-action-button";
      pasteButton.textContent = "Paste Supabase image";
      pasteButton.setAttribute("aria-label", `Paste Supabase image for ${item.italian}`);
      pasteButton.addEventListener("click", () => pasteSupabaseImageFor(item, pasteButton, img));
      actions.appendChild(pasteButton);
    }



    card.append(icon, italian, english, actions);

    cardsEl.appendChild(card);
  });
}

showEnglishEl.addEventListener("change", () => {
  document.body.classList.toggle("hide-english", !showEnglishEl.checked);
});

voiceSelectEl.addEventListener("change", () => {
  state.selectedVoiceURI = voiceSelectEl.value;
  localStorage.setItem("italianVoiceURI", state.selectedVoiceURI);
  const voice = selectedVoice();
  voiceStatusEl.textContent = voice ? `Using ${voice.name} (${voice.lang}).` : "Using browser default for it-IT.";
});

supabaseSignInButtonEl?.addEventListener("click", async () => {
  const store = supabaseImageStore();
  if (!store?.signInWithEmail) {
    alert("Supabase sign-in is not ready yet. Reload the page and try again.");
    return;
  }

  const oldText = supabaseSignInButtonEl.textContent;
  supabaseSignInButtonEl.textContent = "Sending…";
  supabaseSignInButtonEl.disabled = true;

  try {
    await store.signInWithEmail(supabaseAuthEmailEl?.value || "");
    state.supabaseAuthMessage = "Check your email for the Supabase sign-in link.";
    renderSupabaseAuthStatus();
  } catch (error) {
    console.error(error);
    alert(error?.message || String(error));
  } finally {
    supabaseSignInButtonEl.textContent = oldText;
    supabaseSignInButtonEl.disabled = false;
  }
});

supabaseSignOutButtonEl?.addEventListener("click", async () => {
  const store = supabaseImageStore();
  if (!store?.signOut) return;

  supabaseSignOutButtonEl.disabled = true;
  try {
    await store.signOut();
    state.supabaseAuthMessage = "Signed out.";
    renderCards();
    renderSupabaseAuthStatus();
  } catch (error) {
    console.error(error);
    alert(error?.message || String(error));
  } finally {
    supabaseSignOutButtonEl.disabled = false;
  }
});

if ("speechSynthesis" in window) {
  refreshVoices();
  speechSynthesis.addEventListener?.("voiceschanged", refreshVoices);
  window.setTimeout(refreshVoices, 250);
  window.setTimeout(refreshVoices, 1000);
} else {
  voiceStatusEl.textContent = "Speech synthesis is not available in this browser.";
  voiceSelectEl.disabled = true;
}


window.addEventListener("italian-learning:supabase-images-updated", () => {
  renderSupabaseAuthStatus();
  renderCards();
});

renderFilters();
renderSupabaseAuthStatus();
renderCards();
