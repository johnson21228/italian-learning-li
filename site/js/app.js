const registry = window.ITALIAN_GENERATIVE_FLASHCARD_REGISTRY;
const state = {
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
      const italian = `${subject.italian} ${form.form} ${complement.phrase}.`;
      cards.push({
        id: `${verb.key}-${subject.key}-${complement.key}-round-${state.round}`,
        italian,
        english: `${form.english} ${complement.english}.`,
        speak: italian,
        verb: verb.infinitive,
        subject: subject.key,
        complement: complement.key,
        visualParts: [
          {role: "subject", image: subject.image, alt: `Subject ${subject.italian}`, speak: subject.italian},
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

function renderCards() {
  cardsEl.innerHTML = "";
  state.cards.forEach((item) => {
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
    cardsEl.append(card);
  });
  document.body.classList.toggle("hide-english", !showEnglishEl.checked);
  roundStatusEl.textContent = `Giro ${state.round}: ${state.cards.length} carte · ${registry.verbs.length} verbi attivi.`;
  pendingStatusEl.textContent = `${registry.pendingVerbs.length} verbi attendono paradigmi e complementi verificati.`;
}

function newRound() {
  state.round += 1;
  state.cards = buildRound();
  renderCards();
}

newRoundButtonEl.addEventListener("click", newRound);
showEnglishEl.addEventListener("change", renderCards);
voiceSelectEl.addEventListener("change", () => {
  state.selectedVoiceURI = voiceSelectEl.value;
  localStorage.setItem("italianVoiceURI", state.selectedVoiceURI);
});
speechSynthesis.onvoiceschanged = refreshVoices;
refreshVoices();
newRound();
