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
			$(COMPILE) & \
		watcher_pid=$$!; \
		$(BROWSER_SYNC) start --server out --files "out/$(DOCNAME).pdf" \
			--startPath "$(DOCNAME).pdf" --no-notify

.PHONY: all clean doc mostlyclean pdf serve

# Include auto-generated dependencies
-include *.d
