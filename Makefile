REPO_NAME := $(notdir $(CURDIR))
PACK_PATH := dist/$(REPO_NAME).pack.zip

.PHONY: verify history clean-li pack read-first

verify:
	python3 tools/verify_italian_learning_li.py

history:
	python3 tools/export_repo_history_for_llm.py

clean-li:
	python3 tools/clean_li_repo_artifacts.py

pack: verify history clean-li
	mkdir -p dist
	rm -f "$(PACK_PATH)"
	zip -r "$(PACK_PATH)" . \
		-x ".git/*" \
		-x ".git/**" \
		-x "dist/*.zip" \
		-x "__pycache__/*" \
		-x "*/__pycache__/*" \
		-x ".DS_Store" \
		-x "__MACOSX/*"
	@echo "Wrote $(PACK_PATH)"

read-first:
	@cat LLM_READ_FIRST.md
