#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess

REQUIRED = [
    "MAP.md", "README.md", "SPINE.md", "LLM_READ_FIRST.md", "HOW_LI_RULES.md",
    "li/domain/italian_learning_principles.md", "li/domain/childlike_language_acquisition_rule.md", "li/domain/first_person_conversation_rule.md",
    "li/domain/conversation_before_grammar_rule.md", "li/practice/hear_imitate_answer_repair_loop.md",
    "li/prompts/start_italian_micro_conversation.md", "li/prompts/build_from_need_to_speak.md", "li/prompts/listen_repeat_respond_loop.md",
    "li/prompts/enter_conversation_before_grammar.md", "li/prompts/repair_misunderstanding_in_italian.md", "li/prompts/capture_personal_corpus_entry.md",
    "cards/001_start_italian_learning_workbench_card.md", "cards/002_enter_conversation_before_grammar_card.md", "cards/003_first_class_corpus_greetings_card.md",
    "cards/004_standardize_llm_repo_history_snapshot_card.md", "cards/005_class_material_image_assets_card.md", "cards/006_register_uploaded_italian_learning_resources_card.md",
    "cards/007_start_italian_first_chat_mode_card.md", "cards/008_cb_overlay_only_default_artifact_card.md", "cards/012_phrase_flashcard_metadata_card.md",
    "cards/013_flashcard_category_filter_ui_card.md", "cards/014_class1_screenshot_flashcards_card.md", "li/domain/class1_note_flashcard_category_rule.md", "li/workflow/llm_repo_history_snapshot_rule.md", "li/workflow/italian_first_chat_mode_rule.md",
    "li/workflow/cb_overlay_only_default_rule.md", "li/domain/phrase_flashcard_metadata_rule.md", "li/domain/flashcard_category_filter_rule.md",
    "site/index.html", "site/js/vocabulary-data.js", "site/js/app.js", "site/css/app.css",
    "site/images/vocabulary/curated/come-si-chiama.jpg", "site/images/vocabulary/placeholders/word-placeholder.svg",
    "site/images/vocabulary/class-notes/class1-name-exchange.png", "site/images/vocabulary/class-notes/class1-dialogo-valigie.png",
    "site/images/vocabulary/class-notes/class1-tu-o-lei.png", "site/images/vocabulary/class-notes/class1-come-stai-risposte.png",
    "site/images/vocabulary/class-notes/class1-dialogo-informale.png",
]

REPAIR_PHRASES = ["Non capisco.", "Puoi ripetere?", "Più lentamente, per favore.", "Che significa?", "Come si dice in italiano?"]

def require_tokens(path: str, tokens: list[str]) -> int:
    text = Path(path).read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            print(f"{path} missing required token: {token}")
            return 1
    return 0

def load_flashcards():
    script = """
const fs=require('fs');
const vm=require('vm');
const code=fs.readFileSync('site/js/vocabulary-data.js','utf8');
const ctx={window:{}};
vm.createContext(ctx);
vm.runInContext(code, ctx);
console.log(JSON.stringify({cards: ctx.window.ITALIAN_CLASSROOM_FLASHCARDS, legacy: ctx.window.ITALIAN_CLASSROOM_VOCABULARY, order: ctx.window.ITALIAN_CLASSROOM_CATEGORY_ORDER}));
"""
    result = subprocess.run(["node", "-e", script], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Unable to evaluate site/js/vocabulary-data.js with node")
        print(result.stderr)
        return None
    return json.loads(result.stdout)

def require_flashcard_category_model() -> int:
    index = Path("site/index.html").read_text(encoding="utf-8")
    app = Path("site/js/app.js").read_text(encoding="utf-8")
    css = Path("site/css/app.css").read_text(encoding="utf-8")
    vocab = Path("site/js/vocabulary-data.js").read_text(encoding="utf-8")
    for token in ["class=\"tab", "data-tab=", "Vocabulary tabs"]:
        if token in index:
            print(f"site/index.html still contains tab UI token: {token}")
            return 1
    for token in ["filterBar", "activeFilterLabel", "Flashcard category filters", "20260730-labeled-avere-bere-mangiare"]:
        if token not in index:
            print(f"site/index.html missing filter UI token: {token}")
            return 1
    for token in ["activeFilter", "function allFlashcards", "ITALIAN_CLASSROOM_FLASHCARDS", "function renderFilters", "function visibleFlashcards", "filter-chip", "aria-pressed", "function speakTextFor", "item.speak", "function imagePromptFor", "copyImagePromptFor", "Copy image prompt"]:
        if token not in app:
            print(f"site/js/app.js missing category filter runtime token: {token}")
            return 1
    for token in ["document.querySelectorAll(\".tab\")", "activeTab", "button.dataset.tab"]:
        if token in app:
            print(f"site/js/app.js still contains tab runtime token: {token}")
            return 1
    for token in [".filter-panel", ".filter-bar", ".filter-chip", ".image-speak-button", ".card-actions", ".card-action-button"]:
        if token not in css:
            print(f"site/css/app.css missing category filter styling token: {token}")
            return 1
    for token in ["ITALIAN_CLASSROOM_FLASHCARDS", "ITALIAN_CLASSROOM_CATEGORY_ORDER", "partOfSpeech", "categories", "curated", "speak"]:
        if token not in vocab:
            print(f"site/js/vocabulary-data.js missing flat flashcard token: {token}")
            return 1
    payload = load_flashcards()
    if payload is None:
        return 1
    cards = payload.get("cards")
    if not isinstance(cards, list) or not cards:
        print("window.ITALIAN_CLASSROOM_FLASHCARDS must be a non-empty list")
        return 1
    required_fields = ["id", "italian", "english", "speak", "image", "imageAlt", "partOfSpeech", "categories", "curated"]
    for card in cards:
        for field in required_fields:
            if field not in card:
                print(f"Flashcard {card.get('italian', '<unknown>')} missing required field: {field}")
                return 1
        if not isinstance(card["categories"], list) or not card["categories"]:
            print(f"Flashcard {card['italian']} must have non-empty categories")
            return 1
        if not isinstance(card["curated"], bool):
            print(f"Flashcard {card['italian']} curated must be boolean")
            return 1
        if not Path("site", card["image"]).exists():
            print(f"Flashcard image missing for {card['italian']}: {card['image']}")
            return 1
    matches = [card for card in cards if card["italian"] == "Come si chiama?"]
    if len(matches) != 1:
        print("Expected exactly one Come si chiama? flashcard")
        return 1
    come = matches[0]
    for category in ["class-1", "nome", "presentazioni", "tu-lei", "formale", "frasi", "domande", "curated"]:
        if category not in come["categories"]:
            print(f"Come si chiama? missing category: {category}")
            return 1
    if come["speak"] != "Come si chiama?":
        print("Come si chiama? speak field must be exact")
        return 1
    if come["image"] != "images/vocabulary/curated/come-si-chiama.jpg":
        print("Come si chiama? image path changed unexpectedly")
        return 1
    all_categories = {category for card in cards for category in card["categories"]}
    for category in ["class-1", "sostantivi", "verbi", "frasi", "domande", "risposte", "saluti", "presentazioni", "come-stai", "nome", "tu-lei", "formale", "informale", "dialogo", "curated", "needs-image"]:
        if category not in all_categories:
            print(f"Expected category missing from flashcard set: {category}")
            return 1

    allowed_categories = {"class-1", "class-july-17", "class-july-22", "cibo", "avere", "bere", "mangiare", "bevande", "io", "tu", "lui-lei-lei", "noi", "voi", "loro", "acqua", "te", "caffe", "succo-arancia", "vino", "pasta", "fame", "ristorante", "luoghi", "movimento", "taxi", "andare", "venire", "saluti", "presentazioni", "come-stai", "nome", "essere", "stare", "tu-lei", "formale", "informale", "riparazione", "frasi-utili", "dialogo", "sostantivi", "verbi", "frasi", "domande", "risposte", "curated", "needs-image"}
    for card in cards:
        unexpected = set(card["categories"]) - allowed_categories
        if unexpected:
            print(f"Flashcard {card['italian']} has non-Class-1 category/categories: {sorted(unexpected)}")
            return 1
    required_italian = [
        "Sono il signore ___.", "Sono la signora ___.", "Come ti chiami?", "Mi chiamo ___.", "Sono ___.",
        "Buon giorno, signore.", "Desidera qualcosa?", "Cerco le mie valigie.", "Come si chiama Lei?",
        "Dove abita?", "Abito negli Stati Uniti, a Chicago.", "Tu o Lei?", "Studente a studente: tu.",
        "Come stai?", "Come sta?", "Come va?", "Molto bene.", "Sto bene.", "Abbastanza bene.",
        "Non c’è male.", "Così così.", "Male.", "Ciao Marco. Come stai?", "Sto bene, grazie, e tu?",
        "Ti presento Giulia.", "Piacere, Giulia.", "Piacere."
    ]
    present = {card["italian"] for card in cards}
    for phrase in required_italian:
        if phrase not in present:
            print(f"Missing Class 1 screenshot FC: {phrase}")
            return 1
    july_22_required = [
        "il cameriere",
        "la cameriera",
        "Cosa ordini da mangiare e da bere?",
        "Vado al mercato.",
        "vado · vai · va · andiamo · andate · vanno",
        "Vieni con noi? Sì, vengo.",
        "Io vengo al ristorante.",
        "Tu vieni al ristorante.",
        "Lei viene al ristorante.",
        "Noi veniamo al ristorante.",
        "Voi venite al ristorante.",
        "Loro vengono al ristorante.",
        "Ho bisogno di un taxi.",
        "Quanto le devo?",
    ]
    for phrase in july_22_required:
        matches = [card for card in cards if card["italian"] == phrase]
        if len(matches) != 1:
            print(f"Expected exactly one July 22 interactive FC: {phrase}")
            return 1
        card = matches[0]
        if "class-july-22" not in card["categories"]:
            print(f"July 22 FC missing class-july-22 category: {phrase}")
            return 1
        if card["speak"] == "":
            print(f"July 22 FC has empty speech text: {phrase}")
            return 1
        venire_generated = phrase == "Vieni con noi? Sì, vengo." or phrase.endswith("al ristorante.") and any(
            form in phrase for form in ("vengo", "vieni", "viene", "veniamo", "venite", "vengono")
        )
        expected_prefix = "images/vocabulary/curated/venire-coming.png" if venire_generated else "images/class-lessons/2026-07-22/"
        if not card["image"].startswith(expected_prefix):
            print(f"July 22 FC image provenance/path mismatch: {phrase}")
            return 1
    curated_verb_batch = {
        "stare": "images/vocabulary/curated/stare.png",
        "chiamarsi": "images/vocabulary/curated/chiamarsi.png",
        "andare": "images/vocabulary/curated/andare.png",
        "capire": "images/vocabulary/curated/capire.png",
        "ripetere": "images/vocabulary/curated/ripetere.png",
        "dire": "images/vocabulary/curated/dire.png",
        "guardare": "images/vocabulary/curated/guardare.png",
        "ascoltare": "images/vocabulary/curated/ascoltare.png",
    }
    by_id = {card["id"]: card for card in cards}
    for card_id, expected_image in curated_verb_batch.items():
        card = by_id.get(card_id)
        if not card:
            print(f"Curated verb card missing: {card_id}")
            return 1
        if card["image"] != expected_image or not card["curated"] or "needs-image" in card["categories"]:
            print(f"Curated verb metadata mismatch: {card_id}")
            return 1
        if not card.get("imagePrompt") or not card.get("imageEssence"):
            print(f"Curated verb prompt provenance missing: {card_id}")
            return 1
    july_17_required = {
        "Quando è il tuo compleanno?": "images/class-lessons/2026-07-17/questions.png",
        "Che giorno è oggi?": "images/class-lessons/2026-07-17/questions.png",
        "Che giorni non lavori?": "images/class-lessons/2026-07-17/questions.png",
        "Dove abiti?": "images/class-lessons/2026-07-17/questions.png",
        "Quando studi l’italiano?": "images/class-lessons/2026-07-17/questions.png",
        "Io ho fame.": "images/class-lessons/2026-07-17/avere-table.png",
        "Tu hai fame.": "images/class-lessons/2026-07-17/avere-table.png",
        "Lei ha fame.": "images/class-lessons/2026-07-17/avere-table.png",
        "Noi abbiamo fame.": "images/class-lessons/2026-07-17/avere-table.png",
        "Voi avete fame.": "images/class-lessons/2026-07-17/avere-table.png",
        "Loro hanno fame.": "images/class-lessons/2026-07-17/avere-table.png",
        "Io bevo acqua.": "images/class-lessons/2026-07-17/bere-table.png",
        "Tu bevi il tè.": "images/class-lessons/2026-07-17/bere-table.png",
        "Lei beve il caffè.": "images/class-lessons/2026-07-17/bere-table.png",
        "Noi beviamo il succo d’arancia.": "images/class-lessons/2026-07-17/bere-table.png",
        "Voi bevete il vino.": "images/class-lessons/2026-07-17/bere-table.png",
        "Loro bevono acqua.": "images/class-lessons/2026-07-17/bere-table.png",
        "Io mangio la pasta.": "images/class-lessons/2026-07-17/mangiare-table.png",
        "Tu mangi la pasta.": "images/class-lessons/2026-07-17/mangiare-table.png",
        "Lei mangia la pasta.": "images/class-lessons/2026-07-17/mangiare-table.png",
        "Noi mangiamo la pasta.": "images/class-lessons/2026-07-17/mangiare-table.png",
        "Voi mangiate la pasta.": "images/class-lessons/2026-07-17/mangiare-table.png",
        "Loro mangiano la pasta.": "images/class-lessons/2026-07-17/mangiare-table.png",
    }
    for phrase, expected_image in july_17_required.items():
        matches = [card for card in cards if card["italian"] == phrase]
        if len(matches) != 1:
            print(f"Expected exactly one July 17 FC: {phrase}")
            return 1
        card = matches[0]
        if card["image"] != expected_image or card["speak"] == "" or "class-july-17" not in card["categories"]:
            print(f"July 17 FC metadata mismatch: {phrase}")
            return 1
    bere_recipe_ids = {
        "july17-bere-io-bevo",
        "july17-bere-tu-bevi",
        "july17-bere-lei-beve",
        "july17-bere-noi-beviamo",
        "july17-bere-voi-bevete",
        "july17-bere-loro-bevono",
    }
    by_id = {card["id"]: card for card in cards}
    for card_id in bere_recipe_ids:
        card = by_id.get(card_id)
        if not card or len(card.get("visualParts", [])) != 3:
            print(f"Composable bere recipe missing visual parts: {card_id}")
            return 1
        if [part.get("role") for part in card["visualParts"]] != ["subject", "verb", "object"]:
            print(f"Composable bere role order mismatch: {card_id}")
            return 1
        verb_part = card["visualParts"][1]
        if verb_part.get("image") != "images/vocabulary/curated/bere-action.png":
            print(f"Composable bere action image mismatch: {card_id}")
            return 1
        for part in card["visualParts"]:
            if not Path("site", part["image"]).is_file():
                print(f"Composable bere visual missing: {part['image']}")
                return 1
        if "bevande" not in card["categories"] or card.get("subject") not in card["categories"] or card.get("object") not in card["categories"]:
            print(f"Composable bere filter metadata mismatch: {card_id}")
            return 1
        if card["visualParts"][1].get("label") != "bere" or not card["visualParts"][2].get("label"):
            print(f"Composable bere visible labels missing: {card_id}")
            return 1
    avere_recipe_ids = {
        "july17-avere-io-ho",
        "july17-avere-tu-hai",
        "july17-avere-lei-ha",
        "july17-avere-noi-abbiamo",
        "july17-avere-voi-avete",
        "july17-avere-loro-hanno",
    }
    for card_id in avere_recipe_ids:
        card = by_id.get(card_id)
        if not card or len(card.get("visualParts", [])) != 3:
            print(f"Composable avere recipe missing: {card_id}")
            return 1
        if [part.get("role") for part in card["visualParts"]] != ["subject", "verb", "object"]:
            print(f"Composable avere role order mismatch: {card_id}")
            return 1
        if card["visualParts"][1].get("image") != "images/vocabulary/curated/avere-action.png":
            print(f"Composable avere action image mismatch: {card_id}")
            return 1
        if card["visualParts"][1].get("label") != "avere" or card["visualParts"][2].get("label") != "fame":
            print(f"Composable avere visible labels missing: {card_id}")
            return 1
        if card.get("subject") not in card["categories"] or "fame" not in card["categories"]:
            print(f"Composable avere filter metadata mismatch: {card_id}")
            return 1
        for part in card["visualParts"]:
            if not Path("site", part["image"]).is_file():
                print(f"Composable avere visual missing: {part['image']}")
                return 1
    mangiare_recipe_ids = {
        "july17-mangiare-io-mangio",
        "july17-mangiare-tu-mangi",
        "july17-mangiare-lei-mangia",
        "july17-mangiare-noi-mangiamo",
        "july17-mangiare-voi-mangiate",
        "july17-mangiare-loro-mangiano",
    }
    for card_id in mangiare_recipe_ids:
        card = by_id.get(card_id)
        if not card or len(card.get("visualParts", [])) != 3:
            print(f"Composable mangiare recipe missing: {card_id}")
            return 1
        if [part.get("role") for part in card["visualParts"]] != ["subject", "verb", "object"]:
            print(f"Composable mangiare role order mismatch: {card_id}")
            return 1
        if card["visualParts"][1].get("image") != "images/vocabulary/curated/mangiare-action.png":
            print(f"Composable mangiare action image mismatch: {card_id}")
            return 1
        if card["visualParts"][1].get("label") != "mangiare" or card["visualParts"][2].get("label") != "pasta":
            print(f"Composable mangiare visible labels missing: {card_id}")
            return 1
        if card.get("subject") not in card["categories"] or "pasta" not in card["categories"]:
            print(f"Composable mangiare filter metadata mismatch: {card_id}")
            return 1
        for part in card["visualParts"]:
            if not Path("site", part["image"]).is_file():
                print(f"Composable mangiare visual missing: {part['image']}")
                return 1
    for subject_name, expected_label in {
        "io": ">io<",
        "tu": ">tu<",
        "lui-lei-lei": ">lui<",
        "noi": ">noi<",
        "voi": ">voi<",
        "loro": ">loro<",
    }.items():
        subject_svg = Path("site/images/grammar-subjects", f"{subject_name}.svg").read_text()
        if expected_label not in subject_svg:
            print(f"Grammar subject body label missing: {subject_name}")
            return 1
    return 0

def main() -> int:
    missing = [p for p in REQUIRED if not Path(p).exists()]
    if missing:
        print("Missing required Italian Learning LI files:")
        for path in missing:
            print(f"- {path}")
        return 1
    checks = {
        "MAP.md": ["cards/013_flashcard_category_filter_ui_card.md", "cards/014_class1_screenshot_flashcards_card.md", "li/domain/class1_note_flashcard_category_rule.md", "category filters"],
        "README.md": ["CB013", "CB014", "Flashcard category filters", "speak", "curated", "categories"],
        "SPINE.md": ["CB013", "CB014", "li/domain/flashcard_category_filter_rule.md", "li/domain/class1_note_flashcard_category_rule.md", "cards/014_class1_screenshot_flashcards_card.md"],
        "li/domain/flashcard_category_filter_rule.md": ["Each flashcard", "Required flashcard metadata", "All` shows every flashcard", "Tabs are not the source of truth"],
        "cards/013_flashcard_category_filter_ui_card.md": ["Replace the rigid", "ITALIAN_CLASSROOM_FLASHCARDS", "Come si chiama? appears"],
        "li/domain/phrase_flashcard_metadata_rule.md": ["speak", "image", "curated", "categories"],
        "li/domain/class1_note_flashcard_category_rule.md": ["Controlled Class 1 categories", "saluti", "presentazioni", "come-stai", "tu-lei"],
        "cards/014_class1_screenshot_flashcards_card.md": ["Class 1 screenshot", "New FCs", "valigie", "Dove abita"],
    }
    for path, tokens in checks.items():
        if require_tokens(path, tokens):
            return 1
    combined = "\n".join(Path(path).read_text(encoding="utf-8") for path in REQUIRED if Path(path).suffix == ".md")
    for phrase in REPAIR_PHRASES:
        if phrase not in combined:
            print(f"Required Italian repair phrase missing from LI: {phrase}")
            return 1
    if require_flashcard_category_model():
        return 1
    print("Italian Learning LI verification passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
