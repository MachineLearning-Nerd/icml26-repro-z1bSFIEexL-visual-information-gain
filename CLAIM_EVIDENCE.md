# Claim-to-evidence audit

This dossier separates what the paper claims, how the paper produces each claim, and what this repository actually verifies. The paper source is pinned by SHA-256 in SOURCE_AUDIT.md. Paper-reported numbers remain paper-reported unless the required model, data, procedure, logs, and metric calculation are independently available here.

## Paper identity

- Title: Focusing Where Vision Matters: Selective Training for Large Vision Language Models via Visual Information Gain
- Authors: Seulbi Lee and Sangheum Hwang
- arXiv: 2602.17186v2
- OpenReview: z1bSFIEexL
- Repository: https://github.com/MachineLearning-Nerd/icml26-visual-information-gain

## Claim ledger

### C1 — VIG definition

Paper claim: Visual Information Gain is a perplexity-based log-ratio measuring how much image conditioning reduces answer uncertainty.

Paper production path: Section 3.2 defines VIG as log(PPL(A|Q) / PPL(A|Q,I)), with a blurred image used as the no-visual control. The source then rewrites the quantity as the cross-entropy difference L(A|Q) - L(A|Q,I), and Section 3.3 expands it as the average of token-level loss differences. Source anchor: main.tex lines 223–280.

Local evidence: src/claim1_vig_definition_toy.py evaluates fixed synthetic token probabilities for matching, partial, conflicting, and weak-visual conditions. It records the four results under outputs/claim1_vig_definition_toy/ and checks the algebra, sign, and ordering.

Status: TOY_SOURCE_VIG_FORMULA. This is formula-level evidence only. No LVLM, visual encoder, blurred image, tokenizer, or real answer sample is used.

### C2 — sample/token decomposition and grounded-token analysis

Paper claim: VIG decomposes to sample and token levels and identifies visually grounded tokens such as colors, spatial relations, and attributes.

Paper production path: The paper computes token-wise loss differences on aligned LVLM instruction-tuning data, aggregates them to sample-level VIG, and analyzes token/POS distributions. Source anchor: main.tex lines 264–280 and 347–386.

Local evidence: The source archive preserves the paper’s equations, tables, and figures. The toy has synthetic token differences but no tokenizer, LVLM logits, corpus, or POS analysis.

Status: UNVERIFIED.

### C3 — matching, partial, and conflicting image behavior

Paper claim: MS-COCO examples produce positive VIG for matching images, smaller positive VIG for partially grounded images, and negative VIG for conflicting images.

Paper production path: The paper holds the question and answer fixed, varies the image, and evaluates an aligned LLaVA-v1.5 7B. Table 1 reports 0.923 for a match, 0.409 for a partial match, and -0.520 for a conflicting image. Source anchor: main.tex lines 288–330.

Local evidence: The toy reproduces only the qualitative sign/order pattern with synthetic probabilities: 1.0415, 0.5465, and -1.0415, plus a near-zero control. It does not contain the source images, checkpoint, or forward-pass logs.

Status: UNVERIFIED / qualitative toy only.

### C4 — token-level visual grounding

Paper claim: Visually grounded words have high positive loss differences while weakly visual function tokens are near zero or negative.

Paper production path: The paper compares token losses with and without visual conditioning on LLaVA-1.5 instruction-tuning data and analyzes scatter plots, examples, and POS groups. Source anchor: main.tex lines 347–386.

Local evidence: Only the pinned source figures/tables and the synthetic three-token toy are present. There is no tokenizer, instruction dataset, model logit output, or independently computed token analysis.

Status: UNVERIFIED.

### C5 — selective training

Paper claim: VIG-guided selective training prioritizes high-VIG samples and tokens, improving visual grounding while reducing supervision.

Paper production path: Section 3.4 ranks samples by VIG, retains the top p percent, reuses the threshold tau_p for token-level loss masking, and trains on selected token losses. The experiment uses p=70 and reports active-token reductions. Source anchor: main.tex lines 388–416 and 437–445.

Local evidence: No selected dataset, LVLM training implementation, checkpoint, loss trace, gradient mask, or training output is present.

Status: UNVERIFIED.

### C6 — benchmark and language-bias gains

Paper claim: VIG-guided selective training improves vision performance, data efficiency, and language-bias mitigation against full-data and existing baselines.

Paper production path: The paper trains/evaluates LLaVA-1.5 7B/13B, ShareGPT4V 7B, and Open-Qwen2VL 2B on vision-understanding, hallucination, and text-only benchmarks, then compares against baselines and ablations. Source anchor: main.tex lines 418–508, 510–558, 563–617, and 619–667.

Local evidence: The repository has no model checkpoints, datasets, training logs, benchmark predictions, metric scripts, or independent score tables.

Status: UNVERIFIED.

## Overall boundary

The local result is INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOY. The toy supports the finite VIG identity and expected behavior under hand-specified probabilities. It neither reproduces nor falsifies the paper’s LVLM, dataset, training, benchmark, data-efficiency, hallucination, or language-bias claims.
