const state = {
  activeFilter: "all",
  currentPage: 1,
  cardsPerPage: 12,
  voices: [],
  selectedVoiceURI: localStorage.getItem("italianVoiceURI") || "",
};

const cardsEl = document.getElementById("cards");
const showEnglishEl = document.getElementById("showEnglish");
const voiceSelectEl = document.getElementById("voiceSelect");
const voiceStatusEl = document.getElementById("voiceStatus");
const filterChipsEl = document.getElementById("filterChips");
const resultStatusEl = document.getElementById("resultStatus");
const prevPageEl = document.getElementById("prevPage");
const nextPageEl = document.getElementById("nextPage");

const FILTERS = [
  { id: "all", label: "All", match: () => true },
  { id: "needs-image", label: "Needs image", match: (item) => !item.curated || !item.image || !item.image.startsWith("images/vocabulary/curated/") },
  { id: "curated", label: "Curated", match: (item) => item.curated === true && item.image && item.image.startsWith("images/vocabulary/curated/") },
  { id: "noun", label: "Nouns", match: (item) => item.partOfSpeech === "noun" },
  { id: "verb", label: "Verbs", match: (item) => item.partOfSpeech === "verb" },
  { id: "phrase", label: "Phrases", match: (item) => item.partOfSpeech === "phrase" },
  { id: "grammar", label: "Grammar", match: (item) => item.semanticHints.includes("grammar") || item.partOfSpeech === "grammar-word" },
  { id: "people", label: "People", match: (item) => item.semanticHints.includes("person") || item.semanticHints.includes("people") },
  { id: "time", label: "Time", match: (item) => item.semanticHints.includes("time") || item.semanticHints.includes("day cycle") },
  { id: "classroom", label: "Classroom", match: (item) => item.semanticHints.includes("classroom") || item.semanticHints.includes("learning") },
  { id: "identity", label: "Identity", match: (item) => item.semanticHints.includes("identity") || item.semanticHints.includes("self identification") },
  { id: "conversation", label: "Conversation", match: (item) => item.semanticHints.includes("conversation") || item.semanticHints.includes("conversation primitive") },
  { id: "repair", label: "Repair", match: (item) => item.semanticHints.includes("repair") || item.semanticHints.includes("repair phrase") },
  { id: "essere", label: "Essere", match: (item) => item.semanticHints.includes("essere") || item.verbFamily === "essere" },
  { id: "learning", label: "Learning", match: (item) => item.semanticHints.includes("learning") || item.studyUse.includes("learning") },
];

function wordsFrom(value) {
  return String(value || "")
    .toLowerCase()
    .split(/[^a-zàèéìòù]+/i)
    .filter(Boolean);
}

function unique(values) {
  return Array.from(new Set(values.filter(Boolean)));
}

function inferPartOfSpeech(item, sourceList) {
  const note = String(item.note || "").toLowerCase();

  if (item.partOfSpeech) return item.partOfSpeech;
  if (sourceList === "verbs") {
    return String(item.italian || "").includes(" ") ? "phrase" : "verb";
  }
  if (note.includes("grammar word")) return "grammar-word";
  if (sourceList === "nowns") return "noun";
  if (sourceList === "other") return "other";
  return "other";
}

function inferSemanticHints(item, sourceList, partOfSpeech) {
  const term = String(item.italian || "").toLowerCase();
  const note = String(item.note || "").toLowerCase();
  const english = String(item.english || "").toLowerCase();
  const hints = [
    ...(item.semanticHints || []),
    ...wordsFrom(note),
    partOfSpeech,
    sourceList,
  ];

  if (sourceList === "nowns") hints.push("noun");
  if (sourceList === "verbs") hints.push("verb");
  if (sourceList === "other") hints.push("other");

  if (/person|people|gentleman|lady|student|teacher|professor|friend/.test(`${note} ${english}`)) {
    hints.push("person", "people");
  }
  if (/time|day|evening|night|giorno|sera|notte/.test(`${note} ${english} ${term}`)) {
    hints.push("time", "day cycle");
  }
  if (/school|class|classroom|student|teacher|professor|learning|book/.test(`${note} ${english}`)) {
    hints.push("classroom", "learning");
  }
  if (/name|identity|called|sono|sei|siamo|siete|essere|to be/.test(`${note} ${english} ${term}`)) {
    hints.push("identity", "self identification", "being", "presence");
  }
  if (/conversation|question|answer|greeting|say|saying|phrase|sentence/.test(`${note} ${english}`)) {
    hints.push("conversation", "conversation primitive", "speaking");
  }
  if (/repair|understand|repeat|capire|ripetere/.test(`${note} ${english} ${term}`)) {
    hints.push("repair", "repair phrase");
  }
  if (/grammar|pronoun|verb|adjective/.test(`${note} ${english}`)) {
    hints.push("grammar");
  }
  if (/essere|io sono|tu sei|lui è|lei è|noi siamo|voi siete/.test(term)) {
    hints.push("essere");
  }

  return unique(hints);
}

function inferSemanticDomain(item, hints) {
  if (item.semanticDomain) return item.semanticDomain;
  const priority = ["identity", "people", "person", "time", "classroom", "learning", "conversation", "repair", "grammar", "place", "object", "language"];
  return priority.find((hint) => hints.includes(hint)) || "general";
}

function inferStudyUse(item, hints) {
  const use = [...(item.studyUse || []), "recognition", "speaking"];
  if (hints.includes("conversation")) use.push("conversation practice");
  if (hints.includes("repair")) use.push("repair phrase support");
  if (hints.includes("grammar")) use.push("grammar support");
  if (hints.includes("identity")) use.push("introduction practice");
  if (hints.includes("learning")) use.push("classroom practice");
  return unique(use);
}

function inferVerbFamily(item) {
  if (item.verbFamily) return item.verbFamily;
  const term = String(item.italian || "").toLowerCase();
  if (["essere", "io sono", "tu sei", "lui è", "lei è", "noi siamo", "voi siete"].includes(term)) return "essere";
  if (["stare", "sto", "stai", "sta"].includes(term)) return "stare";
  if (term.includes("chiam")) return "chiamarsi";
  if (["andare", "va"].includes(term)) return "andare";
  if (term.includes("cap")) return "capire";
  if (term.includes("ripet")) return "ripetere";
  if (term.includes("dire") || term.includes("dice")) return "dire";
  return "";
}

function normalizeItem(item, sourceList, index) {
  const partOfSpeech = inferPartOfSpeech(item, sourceList);
  const semanticHints = inferSemanticHints(item, sourceList, partOfSpeech);
  const semanticDomain = inferSemanticDomain(item, semanticHints);
  const studyUse = inferStudyUse(item, semanticHints);

  return {
    ...item,
    sourceList,
    displayIndex: index,
    partOfSpeech,
    semanticDomain,
    semanticHints,
    studyUse,
    classIntroduced: item.classIntroduced || "class-1",
    verbFamily: inferVerbFamily(item),
  };
}

function allVocabulary() {
  const vocab = window.ITALIAN_CLASSROOM_VOCABULARY || {};
  const groups = ["nowns", "verbs", "other"];
  const flattened = [];

  groups.forEach((sourceList) => {
    (vocab[sourceList] || []).forEach((item) => {
      flattened.push(normalizeItem(item, sourceList, flattened.length));
    });
  });

  return flattened;
}

function activeFilter() {
  return FILTERS.find((filter) => filter.id === state.activeFilter) || FILTERS[0];
}

function filteredVocabulary() {
  const filter = activeFilter();
  return allVocabulary().filter(filter.match);
}

function maxPage(total) {
  return Math.max(1, Math.ceil(total / state.cardsPerPage));
}

function pagedVocabulary(items) {
  const max = maxPage(items.length);
  if (state.currentPage > max) state.currentPage = max;
  if (state.currentPage < 1) state.currentPage = 1;
  const start = (state.currentPage - 1) * state.cardsPerPage;
  return items.slice(start, start + state.cardsPerPage);
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

  speechSynthesis.cancel();
  speechSynthesis.speak(utterance);
}

function renderFilterChips() {
  filterChipsEl.innerHTML = "";

  FILTERS.forEach((filter) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "filter-chip";
    button.dataset.filter = filter.id;
    button.textContent = filter.label;
    button.setAttribute("aria-pressed", String(filter.id === state.activeFilter));
    button.addEventListener("click", () => {
      state.activeFilter = filter.id;
      state.currentPage = 1;
      renderFilterChips();
      renderCards();
    });
    filterChipsEl.appendChild(button);
  });
}

function renderStatus(total) {
  const max = maxPage(total);
  const start = total === 0 ? 0 : (state.currentPage - 1) * state.cardsPerPage + 1;
  const end = Math.min(total, state.currentPage * state.cardsPerPage);
  resultStatusEl.textContent = `${activeFilter().label}: showing ${start}–${end} of ${total}`;

  prevPageEl.disabled = state.currentPage <= 1;
  nextPageEl.disabled = state.currentPage >= max;
}

function renderCards() {
  const filtered = filteredVocabulary();
  const pageItems = pagedVocabulary(filtered);
  cardsEl.innerHTML = "";
  renderStatus(filtered.length);

  if (!pageItems.length) {
    const empty = document.createElement("p");
    empty.className = "empty";
    empty.textContent = "No cards match this filter.";
    cardsEl.appendChild(empty);
    return;
  }

  pageItems.forEach((item) => {
    const card = document.createElement("article");
    card.className = "card";
    card.dataset.partOfSpeech = item.partOfSpeech;
    card.dataset.semanticDomain = item.semanticDomain;
    card.dataset.sourceList = item.sourceList;

    const icon = document.createElement("div");
    icon.className = "icon";
    if (item.image) {
      const img = document.createElement("img");
      img.src = item.image;
      img.alt = item.imageAlt || item.italian;
      img.loading = "lazy";
      icon.appendChild(img);
    } else {
      icon.textContent = item.icon || "🇮🇹";
    }

    const italian = document.createElement("div");
    italian.className = "italian";
    italian.lang = "it";
    italian.textContent = item.italian;

    const english = document.createElement("div");
    english.className = "english";
    english.textContent = item.english || "";

    const note = document.createElement("div");
    note.className = "note";
    note.textContent = item.note || item.semanticDomain || "";

    const meta = document.createElement("div");
    meta.className = "meta-chips";

    [item.partOfSpeech, item.semanticDomain, item.curated ? "curated" : "needs image"].forEach((label) => {
      const chip = document.createElement("span");
      chip.className = "meta-chip";
      chip.textContent = label;
      meta.appendChild(chip);
    });

    const speak = document.createElement("button");
    speak.type = "button";
    speak.className = "speak";
    speak.textContent = "🔊 Speak";
    speak.addEventListener("click", () => speakItalian(item.italian));

    card.append(icon, italian, english, note, meta, speak);
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

prevPageEl.addEventListener("click", () => {
  state.currentPage = Math.max(1, state.currentPage - 1);
  renderCards();
});

nextPageEl.addEventListener("click", () => {
  state.currentPage += 1;
  renderCards();
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

renderFilterChips();
renderCards();
