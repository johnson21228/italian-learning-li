const state = {
  activeTab: "nowns",
  voices: [],
  selectedVoiceURI: localStorage.getItem("italianVoiceURI") || "",
};

const cardsEl = document.getElementById("cards");
const showEnglishEl = document.getElementById("showEnglish");
const voiceSelectEl = document.getElementById("voiceSelect");
const voiceStatusEl = document.getElementById("voiceStatus");

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

function renderCards() {
  const data = window.ITALIAN_CLASSROOM_VOCABULARY[state.activeTab] || [];
  cardsEl.innerHTML = "";

  if (!data.length) {
    const empty = document.createElement("p");
    empty.className = "empty";
    empty.textContent = `No ${state.activeTab} have been added yet. Add items to site/js/vocabulary-data.js.`;
    cardsEl.appendChild(empty);
    return;
  }

  data.forEach((item) => {
    const card = document.createElement("article");
    card.className = "card";

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
    note.textContent = item.note || "";

    const speak = document.createElement("button");
    speak.type = "button";
    speak.className = "speak";
    speak.textContent = "🔊 Speak";
    speak.addEventListener("click", () => speakItalian(item.italian));

    card.append(icon, italian, english, note, speak);
    cardsEl.appendChild(card);
  });
}

document.querySelectorAll(".tab").forEach((button) => {
  button.addEventListener("click", () => {
    state.activeTab = button.dataset.tab;
    document.querySelectorAll(".tab").forEach((tab) => tab.classList.toggle("active", tab === button));
    renderCards();
  });
});

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

renderCards();
