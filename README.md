# DroneVL: Evaluating GRPO after LoRA-SFT for Instruction-Conditioned UAV Navigation

DroneVL is a thesis project designed to evaluate OpenVLA-7B and π₀-FAST adaptation for semantic UAV navigation in CoSyS-AirSim. Its main question is whether Group Relative Policy Optimization (GRPO), continued after Low-Rank Adaptation supervised fine-tuning (LoRA-SFT), improves mission success on held-out episodes.

For each model, the planned study compares M0 (base model with a UAV interface calibrated on training data), M1 (LoRA-SFT), M2 (GRPO continued from M1), and a continued-SFT control starting from the same M1 checkpoint. DroneVL defines the observation and action contracts, controller boundary, safety gate, episode runner, and evaluator. The main comparison is M2 versus M1 within each model; M2 versus continued SFT tests the value of additional supervised optimization.

UAV-Flow-Sim demonstrations are planned for LoRA-SFT. GRPO rollouts and final evaluation are planned in separate CoSyS-AirSim AirSimNH partitions, making the M2 result an adaptation across simulators rather than zero-shot transfer. Tasks cover primitive flight intents, landmark-relative maneuvers, and held-out compositions of trained maneuvers. Policy inputs are limited to front RGB imagery, instructions, UAV state, and verified progress counts; the π₀-FAST input mapping remains to be implemented. OpenVLA predicts four motion tokens per decision. The planned π₀-FAST path predicts compressed action-chunk tokens, with its UAV processor, tokenizer, and execution horizon still to be specified and validated. Depth is used by the safety gate, while evaluator target identities and coordinates are withheld from the policy.

Evaluation is planned on paired mission episodes, separating episodes from the training distribution from withheld instruction combinations. Mission success is the primary outcome; collisions, safety interventions, efficiency, and learning cost are also reported. Cross-model comparisons include differences in pretraining, input processing, and action representation, so they cannot isolate the effect of tokenization. Final splits, training budgets, seed counts, and test counts remain to be set.

Current evidence covers OpenVLA integration, limited training and inference checks, oracle validation, and initial development missions. Full M1 and M2 training, held-out comparisons, and π₀-FAST UAV integration remain unfinished. The thesis therefore does not yet establish a GRPO benefit.

Experiment implementation: `/home/kyo/ws/robotics/thesis`. Chapter IV and the appendix distinguish documented development evidence from unfinished main experiments. See [the revision audit](research-direction-revision-audit.md) for the rationale behind the revised scope.

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
