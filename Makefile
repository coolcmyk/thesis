# Tools
ENGINE ?= tectonic
TECTONIC ?= tectonic
LATEXMK ?= latexmk
WATCHEXEC ?= watchexec
BROWSER_SYNC ?= browser-sync
RM = rm -fr	

ifeq ($(ENGINE),tectonic)
COMPILE = $(TECTONIC) -Z "shell-escape-cwd=$(CURDIR)" --synctex -o out $(DOCNAME).tex
else ifeq ($(ENGINE),latexmk)
COMPILE = $(LATEXMK) -synctex=1 -pdf -shell-escape -outdir=out -file-line-error $(DOCNAME)
else
$(error Unsupported ENGINE '$(ENGINE)'; use tectonic or latexmk)
endif

# Project-specific settings
DOCNAME = thesis

# Targets
all: doc
doc: pdf
pdf: $(DOCNAME).pdf

# Synchronize the generated Obsidian paragraph notes before every document build.
$(DOCNAME).pdf: sync-obsidian

sync-obsidian:
	@python3 scripts/sync_obsidian_paragraphs.py

sync-obsidian-watch:
	@$(MAKE) --no-print-directory sync-obsidian
	$(WATCHEXEC) --watch src/01-body --exts tex -- $(MAKE) --no-print-directory sync-obsidian

# Rules
%.pdf: %.tex
	@mkdir -p out
	$(COMPILE)

mostlyclean:
	$(RM) $(DOCNAME).aux $(DOCNAME).bbl $(DOCNAME).blg $(DOCNAME).loe
	$(RM) $(DOCNAME).lof $(DOCNAME).log $(DOCNAME).lol $(DOCNAME).lot
	$(RM) $(DOCNAME).nlo $(DOCNAME).out $(DOCNAME).toc $(DOCNAME).xdv
	$(RM) $(DOCNAME).fls $(DOCNAME).fdb_latexmk $(DOCNAME).run.xml
	$(RM) $(DOCNAME).synctex.gz out/$(DOCNAME).synctex.gz _minted-$(DOCNAME) *.d

clean: mostlyclean
	$(RM) out

# Build once before BrowserSync opens, then watch source files with watchexec.
serve: pdf
	@set -e; \
		trap 'kill "$$watcher_pid" 2>/dev/null || true' EXIT INT TERM; \
		$(WATCHEXEC) --postpone --watch thesis.tex --watch settings.tex --watch istilah.tex \
			--watch singkatan.tex --watch pustaka.bib --watch acknowledgement.txt \
			--watch src --watch _internals --watch assets -- \
			$(MAKE) --no-print-directory sync-obsidian && $(COMPILE) & \
		watcher_pid=$$!; \
		$(BROWSER_SYNC) start --server out --files "out/$(DOCNAME).pdf" \
			--startPath "$(DOCNAME).pdf" --no-notify

.PHONY: all clean doc mostlyclean pdf serve sync-obsidian sync-obsidian-watch

# Include auto-generated dependencies
-include *.d

# Local, subscription-backed AI thesis reviewer.
REVIEW_DIR ?= .review
COARSE ?= $(REVIEW_DIR)/.venv/bin/coarse-review
REVIEW_SOURCE ?= $(REVIEW_DIR)/thesis-for-review.tex
REVIEW_OUTPUT ?= $(REVIEW_DIR)/output
REVIEW_HOST ?= codex
REVIEW_EFFORT ?= high
REVIEW_LANGUAGE ?= Indonesian
REVIEW_MODEL ?=

# Flatten the multi-file thesis before review because Coarse accepts one source
# document and does not recursively resolve LaTeX \input directives.
review-source:
	@mkdir -p $(REVIEW_DIR)
	@python3 scripts/flatten_thesis_for_review.py thesis.tex $(REVIEW_SOURCE)

review: review-source
	@test -x "$(COARSE)" || { echo "Coarse is not installed at $(COARSE)." >&2; exit 1; }
	$(COARSE) $(REVIEW_SOURCE) --host $(REVIEW_HOST) --effort $(REVIEW_EFFORT) --language "$(REVIEW_LANGUAGE)" --output-dir $(REVIEW_OUTPUT) $(if $(REVIEW_MODEL),--model $(REVIEW_MODEL))

# Start a review in the background; inspect progress with `make review-follow`.
review-detached: review-source
	@test -x "$(COARSE)" || { echo "Coarse is not installed at $(COARSE)." >&2; exit 1; }
	$(COARSE) $(REVIEW_SOURCE) --host $(REVIEW_HOST) --effort $(REVIEW_EFFORT) --language "$(REVIEW_LANGUAGE)" --output-dir $(REVIEW_OUTPUT) --detach --log-file $(REVIEW_DIR)/coarse.log $(if $(REVIEW_MODEL),--model $(REVIEW_MODEL))

review-follow:
	@test -x "$(COARSE)" || { echo "Coarse is not installed at $(COARSE)." >&2; exit 1; }
	$(COARSE) --attach $(REVIEW_DIR)/coarse.log

.PHONY: review review-detached review-follow review-source
