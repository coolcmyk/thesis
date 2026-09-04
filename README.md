# DroneVL

DroneVL is a thesis project on a model-agnostic adapter for semantic UAV navigation in CoSyS-AirSim and ROS 2.

It compares GPT-5.6, Qwen3.6, and Gemini Robotics through one canonical observation/action contract:

```text
model backend → DroneVL adapter → parser + safety gate → fixed flight controller
```

The repository contains the LaTeX thesis, bibliography, figures, and linked Obsidian literature notes.

## Requirements

- [Tectonic](https://tectonic-typesetting.github.io/)
- Python 3
- [Pygments](https://pygments.org/) (`pygmentize`) for `minted` listings

Optional for live preview:

- [watchexec](https://github.com/watchexec/watchexec)
- [BrowserSync](https://browsersync.io/)

## Build

```sh
make pdf
```

The PDF is generated at `out/thesis.pdf`.

`make pdf` also synchronizes marked citation paragraphs from `src/01-body/` into `obsidian/Paragraphs/`.

## Obsidian citation notes

The LaTeX source is canonical. Edit a paragraph in `.tex`, then run:

```sh
make sync-obsidian
```

To continuously regenerate paragraph notes while editing:

```sh
make sync-obsidian-watch
```

Open `obsidian/00-Graph-Start.md` in Obsidian to navigate the graph:

```text
chapter → cited paragraph → paper note → local PDF
```

## Live preview

```sh
make serve
```

This watches thesis sources and opens `out/thesis.pdf` through BrowserSync.

## AI review (Coarse)

Coarse provides a local, subscription-backed review pass over a flattened copy of the thesis. After its one-time setup in `.review/`, run:

```sh
make review
```

The report is written to `.review/output/`. Use `make review-detached` for a background run and `make review-follow` to follow it. The review workspace and generated reports are ignored by Git.

## Clean

```sh
make mostlyclean  # remove intermediate files
make clean        # remove out/
```
