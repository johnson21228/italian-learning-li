#!/usr/bin/env python3
from pathlib import Path

REQUIRED = [
    "MAP.md",
    "README.md",
    "SPINE.md",
    "LLM_READ_FIRST.md",
    "HOW_LI_RULES.md",
    "li/domain/italian_learning_principles.md",
    "li/domain/childlike_language_acquisition_rule.md",
    "li/domain/first_person_conversation_rule.md",
    "li/domain/conversation_before_grammar_rule.md",
    "li/practice/hear_imitate_answer_repair_loop.md",
    "li/prompts/start_italian_micro_conversation.md",
    "li/prompts/build_from_need_to_speak.md",
    "li/prompts/listen_repeat_respond_loop.md",
    "li/prompts/enter_conversation_before_grammar.md",
    "li/prompts/repair_misunderstanding_in_italian.md",
    "li/prompts/capture_personal_corpus_entry.md",
    "cards/001_start_italian_learning_workbench_card.md",
    "cards/002_enter_conversation_before_grammar_card.md",
    "cards/003_first_class_corpus_greetings_card.md",
    "cards/004_standardize_llm_repo_history_snapshot_card.md",
    "li/workflow/llm_repo_history_snapshot_rule.md",
    "li/corpus/first_class_greetings_and_essere_stare.md",
    "li/practice/greeting_response_loop.md",
    "li/practice/formal_informal_choice_loop.md",
    "li/practice/name_exchange_loop.md",
    "li/prompts/practice_first_class_dialogue.md",
    "li/prompts/build_flashcards_from_first_class_slides.md",
    "li/prompts/speak_first_class_italian_aloud.md",
    "li/assets/class_material_image_asset_rule.md",
    "li/corpus/come_si_chiama_image_corpus_entry.md",
    "li/prompts/create_image_from_class_material.md",
    "li/prompts/practice_with_class_image.md",
    "cards/005_class_material_image_assets_card.md",
    "assets/class_material/first_class/come_si_chiama_poster.jpeg",
    "li/source/uploaded_resource_custody_rule.md",
    "li/workflow/italian_first_chat_mode_rule.md",
    "li/prompts/start_chat_in_italian_mode_with_pack.md",
    "cards/007_start_italian_first_chat_mode_card.md",
    "li/workflow/cb_overlay_only_default_rule.md",
    "cards/008_cb_overlay_only_default_artifact_card.md",
]

REPAIR_PHRASES = [
    "Non capisco.",
    "Puoi ripetere?",
    "Più lentamente, per favore.",
    "Che significa?",
    "Come si dice in italiano?",
]

TOKENS = {
    "li/domain/italian_learning_principles.md": [
        "human drive to communicate",
        "personal corpus",
        "grammar",
    ],
    "li/domain/childlike_language_acquisition_rule.md": [
        "Approach Italian like a child",
        "Non capisco",
    ],
    "li/domain/first_person_conversation_rule.md": [
        "first-person speaker",
        "io",
        "tu",
    ],
    "li/domain/conversation_before_grammar_rule.md": [
        "Conversation Before Grammar",
        "Grammar is a clarification layer",
        "Non capisco.",
    ],
    "li/practice/hear_imitate_answer_repair_loop.md": [
        "Hear → Imitate → Answer → Repair → Capture",
        "phrase heard",
        "next phrase wanted",
    ],
    "li/prompts/enter_conversation_before_grammar.md": [
        "Do not begin with grammar",
        "Hear → Imitate → Answer → Repair → Capture",
    ],
    "li/prompts/repair_misunderstanding_in_italian.md": REPAIR_PHRASES,
    "li/prompts/capture_personal_corpus_entry.md": [
        "phrase heard",
        "phrase spoken",
        "repair needed",
        "next phrase wanted",
    ],
    "cards/002_enter_conversation_before_grammar_card.md": [
        "Enter Conversation Before Studying Grammar",
        "Hear → Imitate → Answer → Repair → Capture",
        "li/domain/conversation_before_grammar_rule.md",
    ] + REPAIR_PHRASES,
    "cards/003_first_class_corpus_greetings_card.md": [
        "First Class Corpus",
        "Greetings and Being in Conversation",
        "li/corpus/first_class_greetings_and_essere_stare.md",
        "li/practice/greeting_response_loop.md",
    ],
    "li/corpus/first_class_greetings_and_essere_stare.md": [
        "Come stai?",
        "Come sta?",
        "Come va?",
        "Mi chiamo Steve.",
        "Tu / Lei / voi",
        "essere vs stare",
        "phrase heard",
        "next phrase wanted",
    ],
    "li/practice/greeting_response_loop.md": [
        "Greeting Response Loop",
        "Come stai?",
        "Sto bene.",
        "Hear → Imitate → Answer → Repair → Capture",
    ],
    "li/practice/formal_informal_choice_loop.md": [
        "Formal / Informal Choice Loop",
        "Ciao. Come stai?",
        "Buona sera. Come sta?",
        "Tu  = one person",
        "Lei = one person",
    ],
    "li/practice/name_exchange_loop.md": [
        "Name Exchange Loop",
        "Come ti chiami?",
        "Mi chiamo Steve.",
        "Come si chiama?",
        "Sono il signore Johnson.",
    ],
    "li/prompts/practice_first_class_dialogue.md": [
        "practice the first class dialogue",
        "Ask me one question at a time",
        "personal corpus entry",
    ],
    "li/prompts/build_flashcards_from_first_class_slides.md": [
        "Build a small flashcard deck",
        "formal/informal note",
        "spoken example",
    ],
    "li/prompts/speak_first_class_italian_aloud.md": [
        "Italian speaking coach",
        "Speak each phrase slowly",
        "Mi chiamo Steve.",
    ],
    "li/assets/class_material_image_asset_rule.md": [
        "class material image assets",
        "assets/class_material/",
        "Hear → Imitate → Answer → Repair → Capture",
    ],
    "li/corpus/come_si_chiama_image_corpus_entry.md": [
        "assets/class_material/first_class/come_si_chiama_poster.jpeg",
        "Come ti chiami?",
        "Mi chiamo Steve.",
        "Non capisco. Puoi ripetere lentamente?",
    ],
    "li/prompts/create_image_from_class_material.md": [
        "Create an Italian learning image",
        "Do not make a generic poster",
        "Hear → Imitate → Answer → Repair → Capture",
    ],
    "li/prompts/practice_with_class_image.md": [
        "Use the Italian Learning LI",
        "li/corpus/come_si_chiama_image_corpus_entry.md",
        "Ask one Italian question at a time",
    ],
    "cards/005_class_material_image_assets_card.md": [
        "Class Material Image Assets",
        "assets/class_material/first_class/come_si_chiama_poster.jpeg",
        "Come si chiama questo?",
    ],

    "li/source/uploaded_resource_custody_rule.md": [
        "source/resources/",
        "Do not extract long passages",
        "conversation before grammar",
    ],
    "source/resources/italian_learning_resource_index.md": [
        "Piacere!",
        "Cortina Conversational Italian in 20 Lessons",
        "Basic Italian for Travelers",
        "source/resources/piacere_resource_summary.md",
    ],
    "source/resources/piacere_resource_summary.md": [
        "Creative Commons Attribution-NonCommercial-ShareAlike 4.0",
        "Saluti e presentazioni",
        "Conversazione: Mi presento",
    ],
    "source/resources/cortina_conversational_italian_resource_summary.md": [
        "Conversational Italian in 20 Lessons",
        "phonetic-pronunciation support",
        "copyright-caution",
    ],
    "source/resources/basic_italian_traveler_resource_summary.md": [
        "Basic Italian for Travelers",
        "communication strategies",
        "survival/travel speech",
    ],
    "li/prompts/use_uploaded_resource_for_practice.md": [
        "source/resources/italian_learning_resource_index.md",
        "Hear → Imitate → Answer → Repair → Capture",
        "Choose the best resource",
    ],
    "li/prompts/map_resource_to_personal_corpus.md": [
        "resource",
        "phrase heard",
        "next phrase wanted",
    ],
    "cards/006_register_uploaded_italian_learning_resources_card.md": [
        "Register Uploaded Italian Learning Resources",
        "source/resources/italian_learning_resource_index.md",
        "The Workbench should preserve a summary and use map",
    ],

    "li/workflow/italian_first_chat_mode_rule.md": [
        "Italian-first",
        "not Italian-only",
        "current `italian-learning-li` pack",
        "Hear → Imitate → Answer → Repair → Capture",
    ],
    "li/prompts/start_chat_in_italian_mode_with_pack.md": [
        "ask me to upload the current `italian-learning-li` pack",
        "Italian-first mode",
        "allow English",
        "Ciao Steve. Cominciamo in italiano semplice. Come stai?",
    ],
    "cards/007_start_italian_first_chat_mode_card.md": [
        "Start Italian-First Chat Mode",
        "Italian-first, not Italian-only",
        "li/prompts/start_chat_in_italian_mode_with_pack.md",
    ],

    "li/workflow/cb_overlay_only_default_rule.md": [
        "Do not also provide a full repo pack by default",
        "creating a brand-new Workbench",
        "overlay zip",
    ],
    "cards/008_cb_overlay_only_default_artifact_card.md": [
        "CB Overlay-Only Default Artifact",
        "li/workflow/cb_overlay_only_default_rule.md",
        "Do not also provide a full repo pack by default",
    ],
}


def require_curated_sere_flashcard() -> int:
    vocab_path = Path("site/js/vocabulary-data.js")
    image_path = Path("site/images/vocabulary/curated/sere.jpg")
    text = vocab_path.read_text(encoding="utf-8")
    required_tokens = [
        'italian: "sere"',
        'english: "evenings"',
        'image: "images/vocabulary/curated/sere.jpg"',
        'imageAlt: "Italian after-work aperitivo evenings in a warm piazza"',
        'curated: true',
        'imageEssence: "Italian after-work aperitivo evenings',
        'imagePrompt: "Create a simple square flashcard image for the Italian word “sere,” meaning “evenings.”',
    ]
    for token in required_tokens:
        if token not in text:
            print(f"site/js/vocabulary-data.js missing curated sere token: {token}")
            return 1
    if not image_path.exists():
        print("Missing curated sere image: site/images/vocabulary/curated/sere.jpg")
        return 1
    if image_path.read_bytes()[:3] != b"\xff\xd8\xff":
        print("Curated sere image is not a JPEG file")
        return 1
    return 0


def require_no_selectable_text_banner() -> int:
    index = Path("site/index.html").read_text(encoding="utf-8")
    forbidden = "The Italian words are real selectable text."
    if forbidden in index:
        print("site/index.html still contains selectable-text banner sentence")
        return 1
    return 0


def require_flashcard_notes_hidden() -> int:
    app = Path("site/js/app.js").read_text(encoding="utf-8")
    forbidden_tokens = [
        'note.className = "note"',
        'note.textContent = item.note || ""',
        'card.append(icon, italian, english, note);',
    ]
    required_token = 'card.append(icon, italian, english);'
    for token in forbidden_tokens:
        if token in app:
            print(f"site/js/app.js still renders flashcard note text: {token}")
            return 1
    if required_token not in app:
        print("site/js/app.js missing note-free card append")
        return 1
    return 0


def require_flashcard_image_speaks() -> int:
    app = Path("site/js/app.js").read_text(encoding="utf-8")
    css = Path("site/css/app.css").read_text(encoding="utf-8")
    required_app_tokens = [
        'document.createElement("button")',
        'className = "icon image-speak-button"',
        'icon.addEventListener("click", () => speakItalian(item.italian))',
        'card.append(icon, italian, english);',
    ]
    forbidden_app_tokens = [
        'textContent = "🔊 Speak"',
        'className = "speak"',
        'card.append(icon, italian, english, note);',
    ]
    for token in required_app_tokens:
        if token not in app:
            print(f"site/js/app.js missing image-speak token: {token}")
            return 1
    for token in forbidden_app_tokens:
        if token in app:
            print(f"site/js/app.js still has visible Speak button token: {token}")
            return 1
    if ".image-speak-button" not in css:
        print("site/css/app.css missing image-speak-button styling")
        return 1
    return 0


def require_tokens(path: str, tokens: list[str]) -> int:
    text = Path(path).read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            print(f"{path} missing required token: {token}")
            return 1
    return 0


def main() -> int:
    missing = [p for p in REQUIRED if not Path(p).exists()]
    if missing:
        print("Missing required Italian Learning LI files:")
        for path in missing:
            print(f"- {path}")
        return 1

    for path_text, tokens in TOKENS.items():
        if require_tokens(path_text, tokens):
            return 1

    map_text = Path("MAP.md").read_text(encoding="utf-8")
    for token in [
        "corpus",
        "li/prompts/start_italian_micro_conversation.md",
        "li/domain/conversation_before_grammar_rule.md",
        "li/practice/hear_imitate_answer_repair_loop.md",
        "cards/002_enter_conversation_before_grammar_card.md",
        "cards/003_first_class_corpus_greetings_card.md",
        "cards/004_standardize_llm_repo_history_snapshot_card.md",
        "cards/005_class_material_image_assets_card.md",
        "li/assets/class_material_image_asset_rule.md",
        "li/corpus/come_si_chiama_image_corpus_entry.md",
    "li/workflow/llm_repo_history_snapshot_rule.md",
        "li/corpus/first_class_greetings_and_essere_stare.md",
        "li/practice/greeting_response_loop.md",
        "li/prompts/practice_first_class_dialogue.md",
        "cards/006_register_uploaded_italian_learning_resources_card.md",
        "li/source/uploaded_resource_custody_rule.md",
        "li/workflow/italian_first_chat_mode_rule.md",
        "li/prompts/start_chat_in_italian_mode_with_pack.md",
        "li/workflow/cb_overlay_only_default_rule.md",
        "cards/008_cb_overlay_only_default_artifact_card.md",
        "cards/007_start_italian_first_chat_mode_card.md",
        "cards/008_cb_overlay_only_default_artifact_card.md",
        "li/workflow/cb_overlay_only_default_rule.md",
        "make verify",
    ]:
        if token not in map_text:
            print(f"MAP.md missing expected orientation token: {token}")
            return 1

    spine_text = Path("SPINE.md").read_text(encoding="utf-8")
    for token in [
        "li/domain/conversation_before_grammar_rule.md",
        "li/practice/hear_imitate_answer_repair_loop.md",
        "Hear → Imitate → Answer → Repair → Capture",
        "li/corpus/first_class_greetings_and_essere_stare.md",
        "li/practice/formal_informal_choice_loop.md",
        "li/assets/class_material_image_asset_rule.md",
        "li/corpus/come_si_chiama_image_corpus_entry.md",
        "li/workflow/italian_first_chat_mode_rule.md",
        "li/prompts/start_chat_in_italian_mode_with_pack.md",
        "li/workflow/cb_overlay_only_default_rule.md",
        "cards/008_cb_overlay_only_default_artifact_card.md",
    ]:
        if token not in spine_text:
            print(f"SPINE.md missing expected orientation token: {token}")
            return 1


    history_rule = Path("li/workflow/llm_repo_history_snapshot_rule.md").read_text(encoding="utf-8")
    exporter = Path("tools/export_repo_history_for_llm.py").read_text(encoding="utf-8")
    cleaner = Path("tools/clean_li_repo_artifacts.py").read_text(encoding="utf-8")
    for label, text in [("history rule", history_rule), ("exporter", exporter), ("cleaner", cleaner), ("MAP", map_text), ("SPINE", spine_text)]:
        if "outputs/history/repo_history_for_llm.md" not in text:
            print(f"{label} missing canonical LLM history path")
            return 1
    if "repo_history_for_llm_" in exporter:
        print("exporter still writes timestamped repo_history_for_llm files")
        return 1

    if require_curated_sere_flashcard():
        return 1

    if require_flashcard_image_speaks():
        return 1

    if require_flashcard_notes_hidden():
        return 1

    if require_no_selectable_text_banner():
        return 1

    combined = "\n".join(Path(path).read_text(encoding="utf-8") for path in REQUIRED if Path(path).suffix == ".md")
    for phrase in REPAIR_PHRASES:
        if phrase not in combined:
            print(f"Required Italian repair phrase missing from LI: {phrase}")
            return 1

    print("Italian Learning LI verification passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
