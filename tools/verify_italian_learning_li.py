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
    "cards/013_flashcard_category_filter_ui_card.md", "li/workflow/llm_repo_history_snapshot_rule.md", "li/workflow/italian_first_chat_mode_rule.md",
    "li/workflow/cb_overlay_only_default_rule.md", "li/domain/phrase_flashcard_metadata_rule.md", "li/domain/flashcard_category_filter_rule.md",
    "site/index.html", "site/js/vocabulary-data.js", "site/js/app.js", "site/css/app.css",
    "site/images/vocabulary/curated/come-si-chiama.jpg", "site/images/vocabulary/placeholders/word-placeholder.svg",
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
    for token in ["filterBar", "activeFilterLabel", "Flashcard category filters", "20260701-category-filters"]:
        if token not in index:
            print(f"site/index.html missing filter UI token: {token}")
            return 1
    for token in ["activeFilter", "function allFlashcards", "ITALIAN_CLASSROOM_FLASHCARDS", "function renderFilters", "function visibleFlashcards", "filter-chip",
        "PAGE_SIZE",
        "currentPage",
        "pager-button",
        "Showing", "aria-pressed", "function speakTextFor", "item.speak", "function imagePromptFor", "copyImagePromptFor", "Copy image prompt"]:
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
    for category in ["class-1", "phrase", "question", "conversation-primitive", "name-exchange", "image-supported", "curated"]:
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
    for category in ["class-1", "noun", "verb", "phrase", "curated", "needs-image", "speaking-practice", "listening-practice"]:
        if category not in all_categories:
            print(f"Expected category missing from flashcard set: {category}")
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
        "MAP.md": ["cards/013_flashcard_category_filter_ui_card.md", "li/domain/flashcard_category_filter_rule.md", "category filters"],
        "README.md": ["CB013", "Flashcard category filters", "speak", "curated", "categories"],
        "SPINE.md": ["CB013", "li/domain/flashcard_category_filter_rule.md", "cards/013_flashcard_category_filter_ui_card.md"],
        "li/domain/flashcard_category_filter_rule.md": ["Each flashcard", "Required flashcard metadata", "All` shows every flashcard", "Tabs are not the source of truth"],
        "cards/013_flashcard_category_filter_ui_card.md": ["Replace the rigid", "ITALIAN_CLASSROOM_FLASHCARDS", "Come si chiama? appears"],
        "li/domain/phrase_flashcard_metadata_rule.md": ["speak", "image", "curated", "categories"],
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
