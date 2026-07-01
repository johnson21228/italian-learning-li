# Repository History for LLM

Generated: 2026-07-01T11:50:36Z
Branch: main
Snapshot digest: 68b151f
Canonical path: outputs/history/repo_history_for_llm.md

This file is the stable Italian Learning Workbench continuity snapshot. It is not Git history itself; it is an LLM-readable export derived from the current repository state. The file is overwritten by `tools/export_repo_history_for_llm.py` on each history/pack run so future sessions have one standard place to recover recent direction, accepted LI changes, cards, prompts, and open workbench state.

## Current accepted direction

The Italian Learning LI starts from childlike language acquisition, first-person conversation, conversation before grammar, and a personal corpus of encountered Italian.

## Recent commits

```text
5e2b267 (HEAD -> main, origin/main) Add Come si chiama phrase flashcard metadata
b1ae1f4 Add Come si chiama phrase flashcard metadata
271e732 Add Come si chiama phrase flashcard metadata
c673bd9 Add curated scuola flashcard image
08d0540 Add curated amici flashcard image
03b76f4 Bust vocabulary asset cache
5c49c39 Wire amico curated image data
693232a Add curated amico flashcard image
ee28f81 Fix nouns spelling
e96653f Update flashcard speech instruction
9b2291d Update Italian learning pack artifact
d105912 Repair vocabulary data after sere curation
2c9762e Repair hidden flashcard note labels
4b89371 Remove selectable text banner sentence
6d78bca Hide flashcard note labels
dd37aa3 Make flashcard images speak Italian
982bd60 Add curated sere flashcard image
184de23 Harden Italian speech playback
788f57f Replace vocabulary tabs with filters and pagination
5c151aa Curate studente vocabulary image
b6773d5 Curate essere vocabulary image
ab32f60 Curate professoressa vocabulary image
900fac2 Add verb flashcard placeholders and curation study rule
f9592a1 Curate signore and signora vocabulary images
7b6a376 Curate name vocabulary image
cc7f393 Publish Italian learning site with GitHub Pages
6555615 Curate evening and night vocabulary images
568cd5c Render curated vocabulary images in site cards
3b73991 Add curated giorno vocabulary image
8686bba Add classroom vocabulary site and curation LI
194697b Add Italian-first mode and overlay-only CB rule
88bbfa4 Register uploaded Italian learning resources
83388d2 Add class material image asset practice
4c9240e Standardize LLM repo history snapshot
4b785ca Add first class Italian greetings corpus
d082d11 Add conversation-before-grammar Italian learning loop
5fcece7 Start Italian learning LI workbench
```

## Working tree status

```text
M site/index.html
```

## Tracked files

```text
.github/workflows/pages.yml
HOW_LI_RULES.md
LLM_READ_FIRST.md
MAP.md
Makefile
README.md
SPINE.md
assets/class_material/first_class/come_si_chiama_poster.jpeg
captures/CAPTURE_BACK_CLASSROOM_NOTES_VOCAB_SITE_LI.md
captures/CAPTURE_BACK_CLASSROOM_VOCABULARY_CURATION_CONTRACT.md
captures/CAPTURE_BACK_CURATED_GIORNO_IMAGE.md
cards/001_start_italian_learning_workbench_card.md
cards/002_classroom_notes_vocabulary_site_card.md
cards/002_enter_conversation_before_grammar_card.md
cards/003_first_class_corpus_greetings_card.md
cards/004_standardize_llm_repo_history_snapshot_card.md
cards/005_class_material_image_assets_card.md
cards/006_register_uploaded_italian_learning_resources_card.md
cards/007_start_italian_first_chat_mode_card.md
cards/008_cb_overlay_only_default_artifact_card.md
cards/009_classroom_vocabulary_curation_contract_card.md
cards/011_curated_giorno_image_card.md
cards/012_phrase_flashcard_metadata_card.md
dist/italian-learning-li.pack.zip
li/assets/class_material_image_asset_rule.md
li/corpus/come_si_chiama_image_corpus_entry.md
li/corpus/first_class_greetings_and_essere_stare.md
li/domain/childlike_language_acquisition_rule.md
li/domain/classroom_notes_vocabulary_site_goal.md
li/domain/classroom_vocabulary_curation_rule.md
li/domain/conversation_before_grammar_rule.md
li/domain/curated_vocabulary_image_path_rule.md
li/domain/first_person_conversation_rule.md
li/domain/italian_learning_principles.md
li/domain/phrase_flashcard_metadata_rule.md
li/domain/vocabulary_filter_metadata_rule.md
li/domain/vocabulary_image_curation_study_loop_rule.md
li/practice/formal_informal_choice_loop.md
li/practice/greeting_response_loop.md
li/practice/hear_imitate_answer_repair_loop.md
li/practice/name_exchange_loop.md
li/prompts/build_classroom_notes_vocabulary_site.md
li/prompts/build_flashcards_from_first_class_slides.md
li/prompts/build_from_need_to_speak.md
li/prompts/capture_personal_corpus_entry.md
li/prompts/create_image_from_class_material.md
li/prompts/curate_classroom_vocabulary_entry.md
li/prompts/enter_conversation_before_grammar.md
li/prompts/listen_repeat_respond_loop.md
li/prompts/map_resource_to_personal_corpus.md
li/prompts/practice_first_class_dialogue.md
li/prompts/practice_with_class_image.md
li/prompts/repair_misunderstanding_in_italian.md
li/prompts/speak_first_class_italian_aloud.md
li/prompts/start_chat_in_italian_mode_with_pack.md
li/prompts/start_italian_micro_conversation.md
li/prompts/use_uploaded_resource_for_practice.md
li/source/uploaded_resource_custody_rule.md
li/workflow/cb_overlay_only_default_rule.md
li/workflow/italian_first_chat_mode_rule.md
li/workflow/llm_repo_history_snapshot_rule.md
outputs/history/repo_history_for_llm.md
site/css/app.css
site/data/vocabulary-ledger.example.json
site/images/vocabulary/curated/amici.jpg
site/images/vocabulary/curated/amico.jpg
site/images/vocabulary/curated/come-si-chiama.jpg
site/images/vocabulary/curated/essere.jpg
site/images/vocabulary/curated/giorno.png
site/images/vocabulary/curated/nome.jpg
site/images/vocabulary/curated/notte.jpg
site/images/vocabulary/curated/professoressa.jpg
site/images/vocabulary/curated/scuola.jpg
site/images/vocabulary/curated/sera.jpg
site/images/vocabulary/curated/sere.jpg
site/images/vocabulary/curated/signora.jpg
site/images/vocabulary/curated/signore.jpg
site/images/vocabulary/curated/studente.jpg
site/images/vocabulary/placeholders/verb-placeholder.svg
site/index.html
site/js/app.js
site/js/vocabulary-data.js
source/resources/basic_italian_traveler_resource_summary.md
source/resources/cortina_conversational_italian_resource_summary.md
source/resources/italian_learning_resource_index.md
source/resources/piacere_resource_summary.md
tools/apply_curated_giorno_image.py
tools/clean_li_repo_artifacts.py
tools/export_repo_history_for_llm.py
tools/find_next_uncurated_vocabulary_image.py
tools/verify_italian_learning_li.py
```
