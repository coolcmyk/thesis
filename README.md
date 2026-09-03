# UI Style

LaTeX configuration for report/thesis/dissertation according to [University Indonesia](http://www.ui.ac.id/) standard. Originally made by Andreas Febrian and available for download [here](http://komunitas.ui.ac.id/pg/file/andreas.febrian/read/12945/template-latex-untuk-laporan-skripsithesisdisertasi)

## Original author & contributors

Author: Andreas Febrian

Contributors:

1. Lia Sadita
2. Andre Tampubolon
3. Erik Dominikus
4. Fahrurrozi Rahman

## Updates

- Alternative bibliography management
- Handling multiline source code
- Additional math symbols

---

## Modifications

- Restructure project
- Add code listings with [minted](https://github.com/gpoore/minted)
- Makefile
- Modify to latest (2017) standard according to _KEPUTUSAN REKTOR UNIVERSITAS INDONESIA NOMOR 2143/SK/R/Ul/2017_.
- Use eps for UI logo

## Building the thesis

The main document is `thesis.tex`. Build it with [Tectonic](https://tectonic-typesetting.github.io/) and [Pygments](https://pygments.org/). Tectonic downloads required LaTeX packages automatically; Pygments renders the `minted` source-code listings.

```sh
make
```

The generated PDF is written to `out/thesis.pdf`. The build enables Tectonic's shell escape because `minted` uses Pygments to render source-code listings.

### Live browser preview

The preview uses the same two-process workflow as `mml-solutions`: `watchexec` rebuilds the document when a source file changes and `browser-sync` serves and reloads the generated PDF. Install those tools if needed:

```sh
cargo install watchexec-cli
npm install -g browser-sync
```

Start the watcher and browser preview with:

```sh
make serve
```

BrowserSync opens the PDF (normally at <http://localhost:3000/thesis.pdf>) and reloads it after each successful build. Stop both processes with <kbd>Ctrl</kbd>+<kbd>C</kbd>.

The watcher invokes Tectonic with shell escape enabled so `minted` can run Pygments. A local `pdflscape` compatibility fallback is included for Tectonic's XeTeX engine.

To remove generated build files:

```sh
make mostlyclean  # keep the PDF
make clean        # remove all build output, including out/
```

### GitHub Actions

Pushes to `main` that modify thesis sources build the document automatically and publish the resulting PDF to a GitHub Release.

### Versioned releases

Every push to `main` that changes thesis sources creates a GitHub Release automatically. Releases use patch versions (`thesis v0.0.1`, then `thesis v0.0.2`, and so on) and contain a matching PDF such as `thesis-v0.0.1.pdf`. Changes to `.tex`, `.sty`, `.bib`, `assets/`, or the `Makefile` trigger a new versioned release.
