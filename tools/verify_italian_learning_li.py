#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

REQUIRED = [
    "LLM_READ_FIRST.md", "SPINE.md", "MAP.md", "HOW_LI_RULES.md",
    "li/domain/generative_flashcard_system_rule.md",
    "captures/CAPTURE_BACK_GENERATIVE_FLASHCARD_SYSTEM.md",
    "site/index.html", "site/js/app.js", "site/js/vocabulary-data.js",
    "site/css/app.css",
]

def load_registry():
    script = """
const fs=require('fs'),vm=require('vm');
const ctx={window:{}}; vm.createContext(ctx);
vm.runInContext(fs.readFileSync('site/js/vocabulary-data.js','utf8'),ctx);
console.log(JSON.stringify(ctx.window.ITALIAN_GENERATIVE_FLASHCARD_REGISTRY));
"""
    result = subprocess.run(["node", "-e", script], text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    return json.loads(result.stdout)

def main():
    missing = [path for path in REQUIRED if not Path(path).is_file()]
    if missing:
        print("Missing required generative Workbench files:", *missing, sep="\n- ")
        return 1
    index = Path("site/index.html").read_text()
    app = Path("site/js/app.js").read_text()
    forbidden = ["filterBar", "supabase", "Copy image prompt", "imagePromptFor"]
    combined = (index + app).lower()
    for token in forbidden:
        if token.lower() in combined:
            print(f"Removed site surface remains: {token}")
            return 1
    for token in ["Nuovo giro", "buildRound", "drawDistinctComplements", "speakItalian", "20260730-generative-system-v1"]:
        if token not in index + app:
            print(f"Generative runtime token missing: {token}")
            return 1
    registry = load_registry()
    if registry.get("schema") != "italian-generative-flashcards/v1":
        print("Generative registry schema mismatch.")
        return 1
    subjects = registry["subjects"]
    if len(subjects) != 6 or len({item["key"] for item in subjects}) != 6:
        print("Exactly six unique subjects are required.")
        return 1
    expected_verbs = {
        "essere", "stare", "chiamarsi", "andare", "capire", "ripetere",
        "dire", "guardare", "ascoltare", "parlare", "scrivere", "abitare",
        "provare", "mangiare", "lavorare", "venire", "avere", "bere",
    }
    verbs = registry["verbs"]
    if {verb["key"] for verb in verbs} != expected_verbs:
        print("Admitted verb set mismatch.")
        return 1
    for subject in subjects:
        if not Path("site", subject["image"]).is_file():
            print(f"Subject image missing: {subject['image']}")
            return 1
    for verb in verbs:
        if len(verb["forms"]) != 6:
            print(f"Verb lacks six forms: {verb['key']}")
            return 1
        complements = verb["complements"]
        keys = [item["key"] for item in complements]
        if len(complements) < 6 or len(keys) != len(set(keys)):
            print(f"Verb lacks six distinct complements: {verb['key']}")
            return 1
        if bool(verb.get("image")) == bool(verb.get("icon")):
            print(f"Verb must have exactly one visual representation: {verb['key']}")
            return 1
        if verb.get("image") and not Path("site", verb["image"]).is_file():
            print(f"Verb image missing: {verb['image']}")
            return 1
        if not verb.get("provenance"):
            print(f"Verb provenance missing: {verb['key']}")
            return 1
        round_sentences = {
            f"{subjects[index]['italian']} {verb['forms'][index]['form']} {complements[index]['phrase']}."
            for index in range(6)
        }
        if len(round_sentences) != 6:
            print(f"Round does not yield six unique cards: {verb['key']}")
            return 1
        for item in complements:
            for field in ["key", "label", "phrase", "english", "icon", "provenance"]:
                if not item.get(field):
                    print(f"Complement metadata missing: {verb['key']}:{field}")
                    return 1
    pending = registry["pendingVerbs"]
    if pending:
        print("All learned verbs should be admitted in this Capture Back.")
        return 1
    print("Italian generative flashcard verification passed.")
    print(f"admitted verbs: {len(verbs)}")
    print(f"cards per round: {len(verbs) * len(subjects)}")
    print(f"pending verbs: {len(pending)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
