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
    "li/prompts/start_italian_micro_conversation.md",
    "li/prompts/build_from_need_to_speak.md",
    "li/prompts/listen_repeat_respond_loop.md",
    "cards/001_start_italian_learning_workbench_card.md",
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
}


def main() -> int:
    missing = [p for p in REQUIRED if not Path(p).exists()]
    if missing:
        print("Missing required Italian Learning LI files:")
        for path in missing:
            print(f"- {path}")
        return 1

    for path_text, tokens in TOKENS.items():
        text = Path(path_text).read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                print(f"{path_text} missing required token: {token}")
                return 1

    map_text = Path("MAP.md").read_text(encoding="utf-8")
    for token in ["corpus", "li/prompts/start_italian_micro_conversation.md", "make verify"]:
        if token not in map_text:
            print(f"MAP.md missing expected orientation token: {token}")
            return 1

    print("Italian Learning LI verification passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
