# Manuscript revision audit: OpenVLA UAV adaptation

Historical audit of the initial OpenVLA-only reframing. The subsequent authorized manuscript revision selects OpenVLA + π₀-FAST; see `manuscript-revision-notes.md` for the current implementation record.

Date: 6 November 2026. Scope: title, bilingual abstracts, Chapters I–V, appendices, bibliography, and supporting terminology. This is a proposed revision plan, not a manuscript rewrite or a report of completed experiments.

## 1. Recommended argument and scope

Working research question:

> Does GRPO post-training improve held-out semantic UAV navigation performance beyond a LoRA-SFT-adapted OpenVLA policy, and under which tested conditions do gains or failures occur?

Treat improvement as a hypothesis. A positive conclusion must come from this project's experiments. The primary contrast is M2 versus M1, not M2 versus an unadapted manipulation policy.

Recommended identity: empirical VLA adaptation study. DroneVL remains the execution and evaluation framework. Its adapter, controller boundary, safety gate, and episode runner support experimental control. They need not disappear, but they should no longer dominate the research gap and claimed contribution.

Choose one main distinguishing experimental dimension before rewriting the gap: demonstration budget, semantic instruction composition, or execution conditions. The existing semantic mission suite makes instruction composition a plausible choice, but its readiness and separation from training must be established. Do not promise all three dimensions without resources to test them.

### Terminology decisions

| Term | Use in the revision |
| --- | --- |
| OpenVLA-7B | Exact pretrained policy under study; record checkpoint/revision. |
| OpenVLA-OFT | A distinct recipe/variant used by important prior work; do not silently equate it with the project's OpenVLA. |
| SFT | Supervised fine-tuning objective using UAV demonstrations. |
| LoRA | Parameter update mechanism, not a competing training objective. |
| M0 | Pre-UAV-SFT reference with an explicitly documented action interface; disclose any new initialization or calibration. |
| M1 | OpenVLA after UAV LoRA-SFT. |
| M2 | Exactly M1 followed by GRPO, with the updated parameter set specified. |
| Continued-SFT control | Additional supervised training initialized from M1; report data exposure, updates, and compute rather than implying every resource can be matched simultaneously. |
| DroneVL | Execution and experimental framework. Distinguish its software adapter from trainable LoRA adapters. |
| Generalization | Performance under a named withheld change, not merely performance on new random seeds. |
| Safety | Measured simulated collisions, violations, and interventions; distinguish policy proposals from assisted execution. |

## 2. Findings ranked by consequence

| Priority | Finding | Consequence and required response |
| --- | --- | --- |
| Critical | Title, abstracts, introduction, and Chapter II position the contribution around model-agnostic integration; Chapter III calls LoRA/GRPO the main objective. | Select one central question and align every contribution statement with it. |
| Critical | GRPO is described in one final methodological paragraph, with no fully specified objective, rollout procedure, or training evaluation design. | Expand the learning and experimental methods before running the main comparison. |
| Critical | M0's UAV tokenization/decoder initialization is ambiguous. | Define exactly what changes before SFT and what M0 can meaningfully measure. |
| Critical | Mission events and oracle access are inconsistent across chapters. | Draw the actual information paths and distinguish evaluator access from policy feedback. |
| Major | OpenVLA's actual input encoding is missing despite a rich canonical observation contract. | Document which fields the policy consumes, how each is encoded, and which serve only execution/evaluation. |
| Major | Chapter I limits evaluation to Blocks, while progress notes describe AirSimNH semantic development. | Define Blocks as integration testing if appropriate and identify the final semantic training/test environment explicitly. |
| Major | No inference across training seeds or explicit primary endpoint is specified. | Add paired evaluation, independent training seeds, uncertainty estimates, and a predefined aggregation rule. |
| Major | Literature positioning omits the closest VLA RL and UAV SFT-to-GRPO studies discussed in this session. | Rebuild related work and its comparison table around adaptation evidence and remaining scope. |
| Major | VLA action mapping lists motion actions but not a learned mechanism for target declaration/subgoal events. | Specify how a motion-token policy meets semantic completion requirements without outsourcing the claimed ability. |
| Structural | Chapters IV and V are placeholders. | Build question-driven outlines; do not write positive results in advance. |

## 3. Title and abstracts

Locations: `settings.tex:4`, `src/00-front_matter/06-abstrak.tex`, `src/00-front_matter/07-abstract.tex`.

The current title promises a model-agnostic VLM/VLA adapter. The abstracts spend much of their space listing six model backends and integration contracts. The closing expected output remains integration and a benchmark. This prepares the reader for a different thesis than the proposed adaptation study.

Suggested neutral title:

> Evaluasi Adaptasi OpenVLA dengan LoRA-SFT dan GRPO untuk Navigasi UAV Semantik

> Evaluating OpenVLA Adaptation with LoRA-SFT and GRPO for Semantic UAV Navigation

DroneVL can remain as a title prefix if desired. Avoid a finding-led title containing “improves” until results warrant it.

Rebuild both abstracts with matching content:

1. Semantic UAV navigation requires sequential visual decisions under partial observability.
2. State the specific uncertainty about additional GRPO benefit after UAV SFT.
3. Describe the fixed policy interface, M1/M2 contrast, and important controls.
4. Name the actual held-out conditions and primary outcome.
5. Insert measured findings only after evaluation; retain proposal language while results are unavailable.
6. State a bounded implication for the tested UAV policy and simulation conditions.

Remove the full backend inventory unless broad portability remains a primary contribution. Keywords should emphasize VLA, OpenVLA, SFT, LoRA, GRPO, UAV navigation, and evaluation; add platform terms only as useful.

## 4. Chapter I: Pendahuluan

### Keep

The opening need for semantic goals, visual grounding, spatial relations, and sequential feedback is relevant. Retain the insistence on closed-loop evaluation and bounded simulation claims.

### Rewrite the background's argument

Locations: `src/01-body/01-bab1.tex:19`, `:33`, `:35`.

Replace the current progression from heterogeneous API formats to adapter novelty with:

1. UAV semantic navigation needs perception-conditioned action sequences.
2. A manipulation-pretrained VLA requires explicit UAV embodiment adaptation.
3. SFT supplies initial flight behavior, but performance under policy-induced deviations and withheld conditions is an empirical question.
4. Prior VLA RL work motivates outcome-driven post-training; conflicting algorithm results discourage universal claims.
5. Existing UAV GRPO studies mean the gap cannot simply be “GRPO has not been used for drones.”
6. State the chosen remaining question, the controlled study, and its scope.

Compress CLIP/image-captioning history and vendor interface details. Move necessary integration specifics to Chapter III or appendices.

### Replace research questions and align objectives

Locations: `:41` and `:54`.

Recommended questions:

- RQ1: How effectively does UAV LoRA-SFT adapt the specified OpenVLA checkpoint under the selected action representation?
- RQ2: What additional effect does GRPO initialized from M1 have on held-out mission success and safety-related outcomes?
- RQ3: How does that effect vary under the selected withheld condition, such as unseen instruction compositions or layouts?

If continued SFT is included, incorporate that comparison explicitly in RQ2. Make learning cost a supporting analysis unless efficiency is a central research question. Remove size-versus-performance and six-backend ranking questions unless there is a corresponding controlled experiment.

Objectives should mirror these questions: construct the UAV data/action interface; train and compare the specified conditions; evaluate the selected generalization dimension; analyze learning behavior and failures. List framework implementation as an enabling objective.

### Benefits, scope, and chapter roadmap

Recast benefits around evidence on UAV adaptation and reproducible evaluation. Model replacement remains a software benefit, not necessarily the scientific result.

Fix the Blocks-only restriction at `:81`. Progress notes describe AirSimNH, but those notes do not themselves establish a completed test suite. Name the actual final environments and the role of each.

Specify model, observation, action horizon, low-level controller, language distribution, training data source, generalization split, and simulated evaluation boundary. Remove unsupported optional promises such as broad sensor/prompt ablations. Revise the roadmap so Chapter IV answers RQ1–RQ3.

## 5. Chapter II: Tinjauan Pustaka

Locations: `src/01-body/02-bab2.tex:24`, `:30`, `:52`, `:95`, `:108`, `:116`.

The relevant material exists, but selection of heterogeneous model interfaces occupies too much space. The final gap and contribution table still defend integration, not post-training.

Recommended organization:

1. Semantic UAV navigation and partial observability.
2. VLM planners versus learned VLA policies, including their control boundaries.
3. OpenVLA architecture, action discretization, embodiment dependence, and adaptation.
4. Behavior cloning/SFT, demonstration coverage, and distribution shift during execution.
5. LoRA and the exact role of quantization if used.
6. Policy-gradient post-training and GRPO for interactive trajectories.
7. Generalization evaluation: visual, semantic, and execution changes.
8. Related work synthesis and the precise study position.

Add mathematical background sufficient to understand Chapter III: the SFT action-token loss, trainable LoRA update, policy likelihood ratio, and group-relative advantage. Explain what changes when a “response” becomes an environment-interacting flight trajectory.

Prior work to add and distinguish:

- **What Can RL Bring to VLA Generalization?**: OpenVLA with LoRA; comparisons among PPO, GRPO, and DPO; useful generalization taxonomy and caution about algorithm rankings.
- **SimpleVLA-RL**: supervised initialization followed by GRPO-based interaction on OpenVLA-OFT; useful precedent for post-training and exploration design, not proof for this project's UAV policy.
- **AeroDASH**: direct UAV precedent for LoRA-SFT followed by GRPO, with a B-spline action representation and asynchronous executor.
- **Expert-Guided GRPO for aerial navigation**: distinguish ordinary GRPO from extra expert guidance during online optimization.
- Original OpenVLA and the relevant OpenVLA-OFT work: separate pretrained model identity from adaptations in subsequent papers.

Replace the current table comparing broad VLM work, ROS 2, and DroneVL with a paper-level table: embodiment, model, action representation, SFT initialization, RL algorithm, use of extra expert data, test shifts, safety measures, and the specific distinction of this study. Mark unavailable details as unreported; do not infer them.

Keep ROS 2 and AirSim background compact. Their technical role belongs in methods. Compress CognitiveDrone/OpenPI into contextual related work if their evaluation is removed. Do not claim VLA is inherently superior to VLM or uniquely compatible with GRPO.

## 6. Chapter III: Metodologi dan Perancangan Sistem

This is the largest revision. Current locations `src/01-body/03-bab3.tex:11` and `:71` establish the intended comparison but do not yet make it reproducible.

### 6.1 Task formulation and information access

Define observation, instruction, history, action, transition, trajectory, terminal condition, and evaluation outcome. Distinguish simulator state from policy observation. A canonical data container is not evidence that OpenVLA can consume all its fields.

Document how RGB, depth, pose, velocity, and mission progress are encoded, omitted, or used outside the policy. If state is inserted as text, give the exact encoding. If depth serves only the safety gate, say so rather than claiming depth-conditioned VLA inference. Keep this mapping fixed for M1/M2.

At `:39`, the mission manager verifies events through the oracle evaluator, while Chapter I's scope and Chapter II `:72` deny oracle access to the mission manager. Resolve this explicitly. Oracle-based scoring is permissible, but any progress signal returned to the policy must be disclosed. It changes whether the task tests autonomous subgoal tracking or navigation assisted by verified progress.

### 6.2 Action representation and M0

Specify action dimensions, token count, bins, normalization, clipping, coordinate frame, units, horizon, decoder, and controller conversion. Fit normalization/calibration only with permitted training information and disclose it.

Clarify whether the action vocabulary is reused, changed, or newly initialized. If the UAV decoder/head has been trained before M0, M0 is not an untouched pretrained reference. If it is untrained, low success measures an embodiment mismatch as well as model capability. Label this honestly and keep M1 versus M2 primary.

At `:45`, VLA outputs map only to motion/hover/abort, while semantic evaluation relies on declaration and subgoal events. Define whether those events are model outputs, a separately learned component, or deterministic evaluator logic. Avoid attributing externally supplied mission reasoning to OpenVLA.

### 6.3 Data and splits

Add trajectory provenance, expert/oracle behavior, instruction generation, counts, lengths, quality filtering, failed demonstrations, sensor synchronization, and labeling. Distinguish synthetic markers from natural object categories and bound any visual-generalization claim accordingly.

Define partitions before collecting overlapping episodes. Separate ID testing from named OOD conditions. New seeds in one layout are insufficient evidence for unseen-layout generalization. Withhold related trajectories/instruction templates as groups to avoid near-duplicate leakage. Do not change every factor at once if the intended conclusion attributes a gain to one factor.

### 6.4 Experimental conditions and controls

| Condition | Initialization | Training | Purpose |
| --- | --- | --- | --- |
| M0 | Documented base/reference policy | No UAV SFT, except explicitly disclosed interface preparation | Embodiment baseline |
| M1 | M0 | UAV LoRA-SFT | Supervised adaptation |
| Continued-SFT control | Matched M1 checkpoint | Additional SFT on permitted training demonstrations | Stronger supervised alternative |
| M2 | Same M1 checkpoint | GRPO using training-environment interaction | Incremental RL post-training |

Report additional compute and environment interaction for M2. Continued SFT helps assess whether more supervised optimization suffices; it does not by itself equalize all supervision and interaction resources. Choose a resource accounting rule appropriate to the claim and report the remaining differences.

PPO is optional if the claim is benefit over SFT. It becomes relevant if claiming GRPO is the better RL algorithm. A VLM planner and another VLA are contextual comparisons, not prerequisites for the narrow M1/M2 claim.

### 6.5 SFT specification

Provide the action-token training objective, supervised targets, loss masking, selected modules, LoRA rank/alpha/dropout, optimizer, learning rate, effective batch size, steps/epochs, precision, quantization, frozen modules, checkpoint rule, and seed handling. Specify any non-LoRA trainable projection/decoder parameters. Keep the distinction between LoRA and QLoRA precise.

### 6.6 GRPO specification

Provide pseudocode and the exact objective. Specify:

- Grouping of stochastic trajectories by instruction and initial state; simulator reset reproducibility.
- Action sampling, temperature, truncation, horizon, group size, and collection budget.
- Exact token log-probabilities and context, old-policy ratio, clipping, normalization, length weighting, and loss masking.
- Whether advantages are per episode, step, or action chunk.
- Reference-policy handling and KL, if used; reference checkpoint and old policy are distinct concepts.
- Whether M1's LoRA adapters continue training, are merged first, or are replaced; list frozen and trainable parameters.
- Reward terms, units, weights, temporal aggregation, and terminal penalties.
- Treatment of zero-variance groups and the fraction of discarded/uninformative rollouts.
- Policy versioning, update epochs, checkpoint selection, training termination, and failures.

Log sampled policy actions separately from safety-modified executed actions. Attach policy likelihoods to sampled actions; the environment transition reflects actual execution. Explain that the evaluated policy operates with this safety gate. A deterministic safety gate does not remove the need to define this interaction carefully.

### 6.7 Metrics, inference, and costs

Define primary endpoint: episode mission success. Predefine aggregation across mission families. Report M2-minus-M1 in percentage points with uncertainty, retaining per-family results and independent training-seed variability.

Use paired evaluation episodes across conditions. Do not count frames, action tokens, or correlated decisions as independent mission trials. Use an inference procedure that respects repeated episodes and training seeds; select sample sizes from a pilot precision/power target and available budget, not an invented fixed number.

Secondary outcomes: collision/violation rates, intervention rates, completion time, subgoal completion, trajectory efficiency, invalid actions, inference latency, training GPU-hours, environment steps, and all rollout collection cost. Successful-only efficiency is conditional and should not hide failures; pair it with success-weighted efficiency where a valid reference path exists, or state the limitation plainly.

The current grounding accuracy at `:65` needs an explicit opportunity denominator and treatment of abstentions/missing declarations. A policy that never declares a target must not look accurate by avoiding evaluation.

Add development-based hyperparameter/checkpoint selection; no test-based reward or prompt tuning. An adaptation comparison needs multiple independently trained runs if its conclusion is intended to extend beyond one checkpoint.

### 6.8 Supporting system description

Retain the useful controller boundary, safety gate, terminal rules, timestamps, and raw logs. Shorten repeated API schema fields in the main chapter and place full schemas/examples in appendices. Identify simulator pause behavior during inference: stop-and-wait versus continuous flight changes the meaning of closed-loop latency and execution robustness.

Suggested order: task → data/splits → policy/action adaptation → SFT → GRPO → comparisons → evaluation/statistics → supporting implementation.

## 7. Chapter IV: Pengujian dan Evaluasi

Current `src/01-body/04-bab4.tex:5` still promises a VLM backend comparison. The chapter contains only two placeholder sections; it requires a results structure rather than sentence edits.

Recommended sections and planned evidence:

| Section | Question answered | Evidence to report |
| --- | --- | --- |
| Experimental realization | What actually ran? | Final data/split counts, checkpoints, parameter sets, budgets, hardware, deviations from protocol. |
| Integration validation | Does the execution/evaluator pipeline behave as expected? | Brief oracle/controller and replay consistency checks; keep separate from learned-policy evidence. |
| UAV supervised adaptation | Does M1 acquire useful behavior? | M0/M1 performance, SFT learning diagnostics, embodiment-related failures. |
| Main GRPO comparison | Does M2 improve beyond M1 and continued SFT? | Success, uncertainty, paired outcome differences, safety/intervention results, independent seeds. |
| Generalization | Which withheld changes retain the gains? | ID versus specifically defined OOD results; no pooling that conceals regressions. |
| Learning behavior and cost | When does GRPO learn or stall? | Evaluation success versus interactions/compute, reward variance, informative-group rate, resource use. |
| Targeted ablation and failures | What qualifies the main interpretation? | One or two justified design ablations; representative failures and their frequency. |
| Discussion and limitations | What does the study add? | Synthesis against prior work, plausible alternative explanations, boundaries. |

Do not replace mission evaluation with static image inference, oracle-only flights, a single LoRA update, or training reward curves. Those are useful development checks, not evidence for the main claim.

Keep main comparison, generalization boundary, and safety tradeoffs in the main text. Put full per-episode logs, long schema tables, extra videos, and non-central engineering checks in appendices. Do not relocate contradictory findings away from the main interpretation.

## 8. Chapter V: Penutup

Current `src/01-body/05-bab5.tex` is a placeholder. Plan its logic now, but write conclusions after results.

Answer RQ1–RQ3 directly with the smallest decisive evidence. State whether GRPO improved, did not improve, or had condition-dependent effects. Improvement in training reward is not sufficient. If success improves but collisions/interventions worsen, report a tradeoff rather than an unqualified superiority claim.

Bound conclusions to the tested checkpoint, dataset, action representation, controller/safety system, instruction distribution, and simulator. A single-model study does not establish that all VLAs benefit or that GRPO dominates PPO/VLM planners. Simulation alone does not establish real-flight transfer.

Replace generic future work about adding more backends with experiments that resolve observed uncertainty: PPO comparison if GRPO stalls, stronger initial SFT if exploration fails, unseen environments if layout transfer fails, or real-world validation if simulation evidence is strong enough to motivate it.

## 9. Supporting content and consistency

- `pustaka.bib`: add verified entries for close VLA RL/UAV studies; distinguish preprints from accepted conference versions. There are many legacy template entries unrelated to this thesis. Check whether cited before removing them; their presence alone is not evidence of a citation error.
- `singkatan.tex`: add VLA, SFT, RL, and relevant evaluation/optimization abbreviations actually used. VLA and SFT are currently absent.
- `src/00-front_matter/daftar-notasi.tex`: replace generic template symbols with the actual policy, trajectory, return, advantage, ratio, LoRA, and action notation.
- `src/99-back_matter/lampiran.tex`: replace example Python/table material with data schema, representative instruction/trajectory, split manifest, SFT/GRPO hyperparameters, reward specification, reproducibility instructions, and extended results.
- `README.md`, `progress.md`: align the project description with the chosen primary study while retaining factual progress distinctions.
- `obsidian/`: LaTeX is canonical. Update linked notes after actual manuscript edits using the existing synchronization procedure rather than treating notes as a separate competing manuscript.
- Both abstracts, title declarations, chapter-opening summaries, research questions, objectives, contribution table, metrics, and conclusion must use the same study identity.

## 10. Claim–evidence map

| Proposed claim | Evidence required | Status from the reviewed manuscript/progress notes |
| --- | --- | --- |
| Framework integrates sensor, controller, and evaluator | Integration runs and reproducible artifacts | Progress notes report development evidence; implementation artifacts were not re-audited here. |
| LoRA-SFT enables semantic UAV navigation | Completed M1 training and held-out closed-loop evaluation | Needs evidence. |
| GRPO improves beyond M1 | Matched initialization, completed RL, paired held-out comparisons, independent training runs | Needs evidence. |
| GRPO improves over continued SFT | Explicit control and documented resource/data differences | Not specified in current methods. |
| Gains generalize | Named withheld condition with separated data and evaluation | Planned generally; concrete experimental partitions missing. |
| Policy is safer | Measured safety outcomes and proposed/executed/intervention accounting | Needs evidence; fixed gate alone cannot establish policy safety. |
| GRPO is better than PPO or VLM planning | Directly relevant controlled comparisons | Unsupported and unnecessary for the recommended scope. |
| Study is first to apply SFT then GRPO to UAV VLA | Exhaustive defensible novelty assessment | Do not claim; close UAV precedents exist. |

Latest local progress notes describe static inference and very small adaptation checks, and explicitly leave full training and frozen-test comparisons unfinished. This audit does not certify the external implementation repository or infer later work from those notes.

## 11. Revision sequence

1. Freeze the central question, primary comparison, and one distinguishing evaluation dimension.
2. Resolve action/tokenization, observation encoding, mission events, and oracle-feedback boundaries.
3. Specify data/splits, learning procedures, controls, resource accounting, and statistical evaluation in Chapter III.
4. Rebuild Chapter II around the actual closest prior work and the remaining question.
5. Rewrite Chapter I and align its objectives/scope with that protocol.
6. Establish the Chapter IV reporting structure and execute the missing experiments.
7. Write Chapter V from observed outcomes; finalize the bilingual abstracts and any finding-led title last.

The original audit did not change the manuscript. A subsequent authorized revision on 6 November 2026 implemented the argument, chapter, and supporting-content changes. See `manuscript-revision-notes.md` for the implementation record; no main experimental results were invented.

## Sources consulted for literature positioning

- Author project page: [What Can RL Bring to VLA Generalization?](https://rlvla.github.io/). Reports PPO/GRPO/DPO with LoRA and stronger PPO performance in its setting.
- Primary manuscript: [SimpleVLA-RL, arXiv v1](https://arxiv.org/html/2509.09674v1). SFT-to-GRPO precedent and exploration/failure considerations; use the final conference version when preparing bibliography entries.
- Primary preprint: [AeroDASH](https://arxiv.org/html/2610.25407v1). Direct LoRA-SFT-to-GRPO UAV precedent with a different action/execution design.
- Primary preprint: [Towards Precise Intent-Aligned VLA Aerial Navigation via Expert-Guided GRPO](https://arxiv.org/html/2606.02313v1). Separates ordinary GRPO improvement from expert-guided optimization.
