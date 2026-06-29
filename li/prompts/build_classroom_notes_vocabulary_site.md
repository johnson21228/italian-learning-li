# Prompt: Build Classroom Notes Vocabulary Site

Use this prompt when adding or updating the Italian classroom notes vocabulary site.

## Goal

Build or update a static GitHub Pages site that presents classroom Italian vocabulary in learner-facing tabs:

- Nowns
- Verbs
- Other

The site should help the learner practice on iPhone, iPad, and desktop Chrome.

## Requirements

1. Keep vocabulary in site-maintained data, separate from the rendering logic.
2. Render one card per vocabulary item.
3. Each card should include a visual cue, the Italian word as real selectable text, and a Speak button.
4. Provide a global option to show/hide English.
5. Provide Italian speech synthesis using `SpeechSynthesisUtterance` with `lang = "it-IT"`.
6. Choose the best available Italian voice from `speechSynthesis.getVoices()`.
7. Provide a visible voice picker/status when voices are available.
8. Remember the selected voice with `localStorage` when possible.
9. Keep the site static and GitHub Pages compatible.
10. Make the layout touch-friendly for iPhone and iPad.

## First content

Seed the Nowns tab with the Class 1 list:

```text
giorno
sera
notte
nome
signore
signora
professoressa
studente
studenti
amico
amici
classe
casa
scuola
libro
gatto
tavolo
città
Roma
Virginia
Italia
italiano
italiana
frase
parola
conversazione
domanda
risposta
saluto
pronome
verbo
```

## Acceptance check

After changes, verify that:

- `site/index.html` exists;
- the page has tabs for Nowns, Verbs, and Other;
- the page has a show-English option;
- the page has Italian voice selection/status;
- the Class 1 Nowns list is represented in site data;
- the site can run from static files and be hosted on Pages.
