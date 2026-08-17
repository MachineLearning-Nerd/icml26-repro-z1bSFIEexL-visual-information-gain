# Audit report

## Result

Overall verdict: INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOY.

This repository is a trustworthy source-pinned audit, not a full reproduction. C1 has bounded formula evidence. C2–C6 are explicitly unverified. Full-paper publication is disabled by publication_allowed=false.

## What is verified

- The paper identity, OpenReview ID, arXiv version, and canonical repository are recorded.
- The source PDF and source archive are checksum-pinned.
- The source archive inventory is deterministic and contains no executable files.
- The VIG log-perplexity identity is exercised on fixed synthetic token probabilities.
- Matching, partial, conflicting, and weak-visual toy controls have deterministic signs and ordering.
- The final repository has one canonical main branch and MachineLearning-Nerd attribution on reachable canonical commits.
- EVIDENCE_MANIFEST.json hashes every tracked audit artifact except the manifest and mutable state file.

## What is not verified

No local artifact supports an independent claim about LVLM forward passes, blurred-image controls, real images, MS-COCO, tokenizers, selective training, checkpoints, active-token counts, benchmark scores, hallucination, or language-bias mitigation.

## Reproduction decision

The bounded toy is the appropriate reproducible scope under the available local environment. A future end-to-end attempt would need identified checkpoints, datasets, preprocessing, model code, scoring/training scripts, logs, and benchmark evaluators before any result could be labeled reproduced.
