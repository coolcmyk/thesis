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

Pushes and pull requests build the document automatically. Download the `thesis-pdf` artifact from the workflow run to retrieve `out/thesis.pdf`.

### Versioned releases

To publish an immutable, versioned PDF, tag the thesis commit and create a GitHub Release from that tag:

```sh
git tag -a v1.0.0 -m "Thesis v1.0.0"
git push origin v1.0.0
gh release create v1.0.0 --title "Thesis v1.0.0" --generate-notes
```

When the release is published, the release workflow checks out that exact tag, builds the document, and attaches `thesis-v1.0.0.pdf` to the release. Create a new tag and release whenever you want to publish a newly edited version.
