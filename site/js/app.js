const registry = window.ITALIAN_GENERATIVE_FLASHCARD_REGISTRY;
const handoutRegistry = window.ITALIAN_HANDOUT_FLASHCARD_CANDIDATES;
const day7Registry = window.ITALIAN_DAY7_FLASHCARDS || [];
const state = {
  activeView: "class",
  activeCategory: "all",
  round: 0,
  cards: [],
  complementDecks: new Map(),
  selectedVoiceURI: localStorage.getItem("italianVoiceURI") || "",
};

const cardsEl = document.getElementById("cards");
const showEnglishEl = document.getElementById("showEnglish");
const voiceSelectEl = document.getElementById("voiceSelect");
const voiceStatusEl = document.getElementById("voiceStatus");
const roundStatusEl = document.getElementById("roundStatus");
const pendingStatusEl = document.getElementById("pendingStatus");
const newRoundButtonEl = document.getElementById("newRoundButton");
const classTabEl = document.getElementById("classTab");
const handoutTabEl = document.getElementById("handoutTab");
const filterPanelEl = document.getElementById("filterPanel");
const filterBarEl = document.getElementById("filterBar");
const activeFilterLabelEl = document.getElementById("activeFilterLabel");

const categoryOrder = ["all", "class-1", "restaurant-travel", "day-7", "hotel", "body-pain", "health", "pharmacy", "without-pronouns", "avere", "fare"];
const categoryLabels = {
  all: "All lessons",
  "class-1": "Class 1",
  "restaurant-travel": "Restaurant & travel",
  "day-7": "Day 7",
  hotel: "Hotel",
  "body-pain": "Body & pain",
  health: "Health",
  pharmacy: "Pharmacy",
  "without-pronouns": "Without pronouns",
  avere: "Avere",
  fare: "Fare",
};

function shuffled(items) {
  const result = [...items];
  for (let index = result.length - 1; index > 0; index -= 1) {
    const swap = Math.floor(Math.random() * (index + 1));
    [result[index], result[swap]] = [result[swap], result[index]];
  }
  return result;
}

function drawDistinctComplements(verb) {
  let deck = state.complementDecks.get(verb.key) || [];
  if (deck.length < registry.subjects.length) {
    const retained = new Set(deck.map((item) => item.key));
    deck = [...deck, ...shuffled(verb.complements.filter((item) => !retained.has(item.key)))];
  }
  if (deck.length < registry.subjects.length) {
    throw new Error(`${verb.infinitive} lacks six distinct compatible complements.`);
  }
  const selected = deck.slice(0, registry.subjects.length);
  state.complementDecks.set(verb.key, deck.slice(registry.subjects.length));
  return shuffled(selected);
}

function buildRound() {
  const cards = [];
  registry.verbs.forEach((verb) => {
    const complements = drawDistinctComplements(verb);
    registry.subjects.forEach((subject, index) => {
      const form = verb.forms[index];
      const complement = complements[index];
      const italian = `${form.form} ${complement.phrase}.`;
      const provenance = `${verb.provenance || ""} ${complement.provenance || ""}`;
      const categories = ["without-pronouns", verb.key];
      if (/class 1|first class|name exchange|greeting/i.test(provenance)) categories.push("class-1");
      if (/july 22|restaurant|taxi|places|movement/i.test(provenance)) categories.push("restaurant-travel");
      if (/day 7/i.test(provenance) || verb.key === "fare") categories.push("day-7");
      if (/hotel|prenotazione/i.test(provenance)) categories.push("hotel");
      cards.push({
        id: `${verb.key}-${subject.key}-${complement.key}-round-${state.round}`,
        italian,
        english: `${form.english} ${complement.english}.`,
        speak: italian,
        verb: verb.infinitive,
        subject: subject.key,
        complement: complement.key,
        categories: [...new Set(categories)],
        visualParts: [
          {role: "verb", image: verb.image, icon: verb.icon, alt: `Conjugated verb ${form.form}`, label: form.form, speak: form.form},
          {role: "object", icon: complement.icon, alt: complement.label, label: complement.label, speak: complement.phrase},
        ],
      });
    });
  });
  return cards;
}

function italianVoices() {
  return speechSynthesis.getVoices()
    .filter((voice) => (voice.lang || "").startsWith("it"))
    .sort((a, b) => (b.lang === "it-IT") - (a.lang === "it-IT"));
}

function refreshVoices() {
  const voices = italianVoices();
  voiceSelectEl.innerHTML = "";
  if (!voices.length) {
    voiceSelectEl.append(new Option("Browser default (it-IT)", ""));
    voiceStatusEl.textContent = "Speech will request it-IT.";
    return;
  }
  voices.forEach((voice) => voiceSelectEl.append(new Option(`${voice.name} (${voice.lang})`, voice.voiceURI)));
  const selected = voices.find((voice) => voice.voiceURI === state.selectedVoiceURI) || voices[0];
  voiceSelectEl.value = selected.voiceURI;
  voiceStatusEl.textContent = `Using ${selected.name} (${selected.lang}).`;
}

function speakItalian(text) {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "it-IT";
  utterance.rate = 0.85;
  const voice = italianVoices().find((item) => item.voiceURI === voiceSelectEl.value);
  if (voice) utterance.voice = voice;
  speechSynthesis.cancel();
  speechSynthesis.speak(utterance);
}

function renderPart(part) {
  const cell = document.createElement("button");
  cell.type = "button";
  cell.className = `visual-part ${part.role}`;
  cell.setAttribute("aria-label", `Hear ${part.speak}`);
  cell.addEventListener("click", () => speakItalian(part.speak));
  if (part.image) {
    const image = document.createElement("img");
    image.src = part.image;
    image.alt = part.alt;
    cell.append(image);
  } else {
    const icon = document.createElement("span");
    icon.className = "object-icon";
    icon.setAttribute("aria-label", part.alt);
    icon.textContent = part.icon;
    cell.append(icon);
  }
  if (part.label) {
    const label = document.createElement("span");
    label.className = "visual-label";
    label.textContent = part.label;
    cell.append(label);
  }
  return cell;
}

function handoutVisualParts(item) {
  return [{role: "object", icon: item.icon, alt: item.italian, label: item.italian, speak: item.italian}];
}

function day7Cards() {
  return day7Registry.map((item) => ({
    ...item,
    visualParts: [{role: "object", image: item.image, icon: item.icon, alt: item.imageAlt || item.italian, speak: item.speak}],
  }));
}

function activeCards() {
  if (state.activeView === "handouts") {
    return handoutRegistry.cards.map((item) => ({
      ...item,
      speak: item.italian,
      visualParts: handoutVisualParts(item),
    }));
  }
  return [...state.cards, ...day7Cards()];
}

function visibleCards() {
  const cards = activeCards();
  if (state.activeView === "handouts" || state.activeCategory === "all") return cards;
  return cards.filter((item) => (item.categories || []).includes(state.activeCategory));
}

function renderFilters() {
  if (!filterBarEl) return;
  const cards = [...state.cards, ...day7Cards()];
  filterBarEl.innerHTML = "";
  categoryOrder.forEach((category) => {
    const count = category === "all" ? cards.length : cards.filter((item) => (item.categories || []).includes(category)).length;
    if (!count) return;
    const button = document.createElement("button");
    button.type = "button";
    button.className = "filter-chip";
    button.setAttribute("aria-pressed", String(state.activeCategory === category));
    button.textContent = `${categoryLabels[category]} ${count}`;
    button.addEventListener("click", () => {
      state.activeCategory = category;
      renderFilters();
      renderCards();
    });
    filterBarEl.append(button);
  });
  if (activeFilterLabelEl) activeFilterLabelEl.textContent = categoryLabels[state.activeCategory];
}

function renderCards() {
  cardsEl.innerHTML = "";
  visibleCards().forEach((item) => {
    const card = document.createElement("article");
    card.className = "card";
    const visual = document.createElement("div");
    visual.className = "visual";
    item.visualParts.forEach((part) => visual.append(renderPart(part)));
    const italian = document.createElement("button");
    italian.type = "button";
    italian.className = "italian sentence-speak";
    italian.lang = "it";
    italian.setAttribute("aria-label", `Hear complete sentence: ${item.italian}`);
    italian.addEventListener("click", () => speakItalian(item.speak));
    const speaker = document.createElement("span");
    speaker.className = "speaker-affordance";
    speaker.setAttribute("aria-hidden", "true");
    speaker.textContent = "🔊";
    const sentence = document.createElement("span");
    sentence.textContent = item.italian;
    italian.append(speaker, sentence);
    const english = document.createElement("p");
    english.className = "english";
    english.textContent = item.english;
    card.append(visual, italian, english);
    if (item.source) {
      const source = handoutRegistry.sources.find((entry) => entry.key === item.source);
      const provenance = document.createElement("p");
      provenance.className = "source-note";
      provenance.textContent = `${source.title} · PDF p. ${item.page} · ${item.derivation}`;
      card.append(provenance);
    }
    cardsEl.append(card);
  });
  document.body.classList.toggle("hide-english", !showEnglishEl.checked);
  if (state.activeView === "handouts") {
    roundStatusEl.textContent = `${handoutRegistry.cards.length} candidate da tre handout.`;
    pendingStatusEl.textContent = "PDF esterni · frasi brevi o trasformate · provenienza visibile.";
  } else {
    roundStatusEl.textContent = `Giro ${state.round}: ${visibleCards().length} carte visibili · ${registry.verbs.length} verbi attivi.`;
    pendingStatusEl.textContent = `Pronome omesso · ascolta la forma verbale · ${registry.pendingVerbs.length} verbi in attesa.`;
  }
}

function newRound() {
  state.round += 1;
  state.cards = buildRound();
  renderFilters();
  renderCards();
}

function setView(view) {
  state.activeView = view;
  const handouts = view === "handouts";
  classTabEl.classList.toggle("active", !handouts);
  handoutTabEl.classList.toggle("active", handouts);
  classTabEl.setAttribute("aria-pressed", String(!handouts));
  handoutTabEl.setAttribute("aria-pressed", String(handouts));
  newRoundButtonEl.hidden = handouts;
  if (filterPanelEl) filterPanelEl.hidden = handouts;
  renderCards();
}

classTabEl.addEventListener("click", () => setView("class"));
handoutTabEl.addEventListener("click", () => setView("handouts"));
newRoundButtonEl.addEventListener("click", newRound);
showEnglishEl.addEventListener("change", renderCards);
voiceSelectEl.addEventListener("change", () => {
  state.selectedVoiceURI = voiceSelectEl.value;
  localStorage.setItem("italianVoiceURI", state.selectedVoiceURI);
});
speechSynthesis.onvoiceschanged = refreshVoices;
refreshVoices();
newRound();
