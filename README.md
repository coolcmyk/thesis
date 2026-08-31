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

The main document is `thesis.tex`. Build it with [TeX Live](https://www.tug.org/texlive/) (or another LaTeX distribution) that includes `latexmk`, `minted`, and Pygments.

```sh
make
```

The generated PDF is written to `out/thesis.pdf`. The template enables `-shell-escape` because `minted` uses Pygments to render source-code listings.

To remove generated build files:

```sh
make mostlyclean  # keep the PDF
make clean        # remove all build output, including out/
```

### GitHub Actions

Pushes to `main` that modify thesis sources build the document automatically and publish the resulting PDF to a GitHub Release.

### Versioned releases

Every push to `main` that changes thesis sources creates a GitHub Release automatically. Releases use patch versions (`thesis v0.0.1`, then `thesis v0.0.2`, and so on) and contain a matching PDF such as `thesis-v0.0.1.pdf`. Changes to `.tex`, `.sty`, `.bib`, `assets/`, or the `Makefile` trigger a new versioned release.
