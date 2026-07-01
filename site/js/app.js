const state = {
  activeFilter: "all",
  voices: [],
  selectedVoiceURI: localStorage.getItem("italianVoiceURI") || "",
};

const cardsEl = document.getElementById("cards");
const showEnglishEl = document.getElementById("showEnglish");
const voiceSelectEl = document.getElementById("voiceSelect");
const voiceStatusEl = document.getElementById("voiceStatus");
const filterBarEl = document.getElementById("filterBar");
const activeFilterLabelEl = document.getElementById("activeFilterLabel");

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
  if (category === "all") return "All";
  return category.split("-").map((part) => part ? part[0].toUpperCase() + part.slice(1) : part).join(" ");
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
    img.src = item.image || "images/vocabulary/placeholders/word-placeholder.svg";
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
    const categoryList = document.createElement("ul");
    categoryList.className = "categories";
    categoryList.setAttribute("aria-label", "Flashcard categories");
    categoriesFor(item).slice(0, 5).forEach((category) => {
      const chip = document.createElement("li");
      chip.textContent = category;
      categoryList.appendChild(chip);
    });
    card.append(icon, italian, english, categoryList);
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

if ("speechSynthesis" in window) {
  refreshVoices();
  speechSynthesis.addEventListener?.("voiceschanged", refreshVoices);
  window.setTimeout(refreshVoices, 250);
  window.setTimeout(refreshVoices, 1000);
} else {
  voiceStatusEl.textContent = "Speech synthesis is not available in this browser.";
  voiceSelectEl.disabled = true;
}

renderFilters();
renderCards();
