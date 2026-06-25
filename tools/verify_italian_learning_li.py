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
}


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
    ]:
        if token not in spine_text:
            print(f"SPINE.md missing expected orientation token: {token}")
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
