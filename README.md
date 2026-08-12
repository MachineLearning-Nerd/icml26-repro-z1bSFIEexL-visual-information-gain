# Visual Information Gain: Source-Pinned ICML 2026 Reproduction Audit

This repository is a claim-by-claim audit of **“Focusing Where Vision Matters: Selective Training for Large Vision Language Models via Visual Information Gain.”** It pins the paper source, records the exact VIG definition and selective-training path, and executes a finite synthetic-probability toy for the metric. The local toy is intentionally not presented as LVLM, image, MS-COCO, or benchmark evidence.

> **Current status:** Claim 1 has a **formula-level toy**. Claims 2–6 remain **unverified locally** because this repository contains no LVLM checkpoint, image/text dataset, model forward-pass logs, training run, or benchmark output generated independently here.

## Paper and resources

- Paper: [arXiv:2602.17186](https://arxiv.org/abs/2602.17186)
- OpenReview: [z1bSFIEexL](https://openreview.net/forum?id=z1bSFIEexL)
- Pinned paper PDF: `evidence/source/arxiv.pdf`
- Pinned paper source: `evidence/source/arxiv_source.tar.gz`
- Contracted claims: `contract/live_claims.json`

The canonical arXiv record identifies this as an ICML 2026 paper by Seulbi Lee and Sangheum Hwang. The local source artifact is arXiv `2602.17186v2` dated 20 May 2026; its PDF and source archive are checksum-pinned. The source archive includes the paper’s figures and `main.tex`, but no runnable LVLM training implementation or dataset.

## What the paper does

The paper addresses language bias in large vision-language models (LVLMs): a model may answer from textual priors without using the image. Its claim-production path is:

1. For an image/question/answer tuple `(I, Q, A)`, evaluate the answer-token likelihood with visual conditioning and without visual cues. The paper implements the latter using a blurred image.
2. Define sample-level Visual Information Gain (VIG) as
   `VIG = log(PPL(A | Q) / PPL(A | Q, I))`.
   Because perplexity is the exponential of mean token cross-entropy, this is equivalently the mean token loss difference `L(A|Q) - L(A|Q,I)`.
3. Decompose VIG over answer tokens. Positive token-level values indicate that the visual input lowers loss for that token; near-zero or negative values indicate weak or counterproductive visual contribution.
4. Analyze VIG on aligned models such as LLaVA-v1.5 7B using MS-COCO and other vision benchmarks. The paper reports high positive VIG for matching images, smaller positive VIG for partial matches, and negative VIG for conflicting images, plus higher values for visually grounded words such as colors and spatial attributes.
5. Rank multimodal training samples by sample-level VIG and retain the top `p%`. At `p=70`, use the same threshold `tau_70` to mask the instruction-tuning loss so only selected visually informative tokens contribute gradients; text-only samples are left unchanged.
6. Compare vanilla and VIG-guided training for LLaVA-1.5 7B/13B, ShareGPT4V 7B, and Open-Qwen2VL 2B on vision-understanding benchmarks (LLaVA-W, MMVet, MMBench, CV-Bench, DocVQA) and hallucination benchmarks (POPE, CHAIR, MMHal), with additional text-only and language-bias analyses.

The paper reports benchmark improvements and reduced active-token supervision, but those are paper-reported results. They are not independently reproduced by this repository.

## Repository status

| Area | Current state |
| --- | --- |
| Compute | Local CPU / local GTX 1050 only |
| Primary source | arXiv `2602.17186v2`, SHA-256 pinned |
| Claim 1 | Synthetic probability toy checks the log-PPL and token-loss-difference algebra |
| Claims 2–6 | Unverified locally |
| LVLM checkpoints | Not present |
| Images/datasets | Not present |
| Training implementation | Not present |
| Independent benchmark logs | Not present |
| Publication of benchmark results | Not allowed without model, data, protocol, logs, and metric evidence |

## Contents

| Path | Purpose |
| --- | --- |
| `contract/live_claims.json` | Six paper claims and verification labels |
| `evidence/source/` | Pinned arXiv PDF/source archive and checksums |
| `src/claim1_vig_definition_toy.py` | Finite formula-level VIG calculation |
| `outputs/claim1_vig_definition_toy/` | Synthetic inputs, CSV results, summary, and checksums |
| `.trackio/logbook/pages/claim-1-vig-definition/page.md` | Existing experiment log page |
| `tests/test_claim1_vig.py` | Algebra and sign/order checks for the toy |
| `tests/test_contract.py` | Contract metadata check |
| `STATUS.md` | Human-readable phase and next action |
| `AUTONOMOUS_STATE.json` | Machine-readable evidence boundary and run state |

## Branch inventory

| Branch | Role | State |
| --- | --- | --- |
| `main` | Published source-pinned audit, documentation, and bounded VIG toy | Current default branch |

The old `master` branch was a stale pre-toy snapshot. It is preserved locally as `backup/pre-main-branch-cleanup` and is removed from the published repository after `main` is made the default branch.

## Claim-to-evidence ledger

The authoritative claim text is preserved in `contract/live_claims.json`. The table below separates the paper’s production path from the evidence currently available here.

| Claim | How the paper produces it | Evidence in this repository | Status |
| --- | --- | --- | --- |
| 1. VIG is a perplexity-based log-ratio measuring how much image conditioning reduces answer uncertainty. | Run the same aligned LVLM on the same answer with visual input and with a blurred/no-visual image; calculate `log(PPL_text/PPL_image)`, equivalently the mean token cross-entropy difference. | `src/claim1_vig_definition_toy.py` uses fixed synthetic probabilities and records matching `1.0415`, partial `0.5465`, conflicting `-1.0415`, and weak-visual `0.000278` VIG. It checks algebra and sign behavior only; no LVLM forward pass occurs. | **Toy only** |
| 2. VIG decomposes to sample and token levels and highlights visually grounded tokens. | Compute each token’s loss difference and average it over the answer; inspect the distribution/POS categories and examples in the aligned LVLM. | The formula and source tables are pinned in `main.tex`; the toy has three synthetic tokens per condition but no tokenizer, model, image, or corpus analysis. | **Unverified** |
| 3. MS-COCO examples produce high positive VIG for matching images, smaller positive VIG for partial matches, and negative VIG for conflicting images. | Evaluate LLaVA-v1.5 7B on fixed question/answer text while varying the image; compare the resulting sample-level VIG values. | The paper source reports example values such as `0.923`, `0.409`, and `-0.520`. The local toy reproduces the qualitative signs with synthetic probabilities, not the source images or model. | **Unverified / qualitative toy only** |
| 4. Token-level analysis gives high positive loss differences to visually grounded words and near-zero/negative differences to weakly visual tokens. | Compute per-token loss differences on LLaVA instruction-tuning data and inspect token scatter/POS categories; the paper reports examples such as `white (3.59)`, `black (6.08)`, and function tokens near zero. | The source archive contains the reported tables/figures. No tokenizer, instruction data, model logits, or independent token-level analysis is present. | **Unverified** |
| 5. VIG-guided selective training improves visual grounding and reduces supervision. | Rank multimodal samples, retain the top `p%`, reuse `tau_p` to mask low-VIG tokens, fine-tune the LVLM, and compare with vanilla/random selection. | The source documents `p=70` and paper-reported model/table results. No selected dataset, masked training loop, checkpoint, loss trace, or evaluation output is present locally. | **Unverified** |
| 6. Experiments show gains over full-data and existing methods for vision performance, data efficiency, and language-bias mitigation. | Train/evaluate LLaVA-1.5, ShareGPT4V, and Open-Qwen2VL on the listed vision, hallucination, and text-only benchmarks, including corrupted-text and attention analyses. | The pinned source contains the benchmark protocols and tables. This repository has none of the required model/data/run artifacts for independent comparison. | **Unverified** |

### Toy evidence boundary

The local toy validates only the finite identity `log(exp(mean_text_loss) / exp(mean_image_loss)) = mean(text_loss - image_loss)` and its expected sign under hand-specified probabilities. It does not test blurred-image conditioning, LVLM visual encoders, tokenizer alignment, sample/token selection, gradient masking, training, data efficiency, hallucination, or language-bias mitigation.

## Reproduce the current local evidence

From the repository root:

~~~bash
python3 src/claim1_vig_definition_toy.py
python3 tests/test_claim1_vig.py
python3 tests/test_contract.py
python3 -m pytest -q tests/test_claim1_vig.py tests/test_contract.py
(cd evidence/source && sha256sum -c SHA256SUMS)
(cd outputs/claim1_vig_definition_toy && sha256sum -c SHA256SUMS)
~~~

The toy uses only Python’s standard library. If `pytest` is unavailable, the direct Python checks still exercise the recorded evidence.

## Reproduction policy

- A paper-reported benchmark score or token-reduction percentage is not an independently reproduced result.
- A **toy** is evidence only for its finite inputs, formula, output, and declared boundary.
- A claim becomes **reproduced** only when the required checkpoint, images/text data, preprocessing, model forward/training procedure, logs, and metric calculation are available and independently checked.
- Resource limits are part of this record: local CPU/local GTX 1050 only; no paid, remote, or upgraded cloud compute.
- VIG requires additional model forward passes for scoring; the paper itself identifies this computational overhead even though scores can be reused across training runs.

## Citation

~~~bibtex
@misc{lee2026focusing,
  title         = {Focusing Where Vision Matters: Selective Training for Large Vision Language Models via Visual Information Gain},
  author        = {Seulbi Lee and Sangheum Hwang},
  year          = {2026},
  eprint        = {2602.17186},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV},
  url           = {https://arxiv.org/abs/2602.17186}
}
~~~

## Thank you

Thank you to Seulbi Lee and Sangheum Hwang for introducing a clear sample- and token-level measure of visual contribution and for documenting the selective-training protocol and benchmark analyses. This audit is intended to credit the original work while making the boundary between paper-reported LVLM results, pinned source artifacts, and the local formula toy explicit.
