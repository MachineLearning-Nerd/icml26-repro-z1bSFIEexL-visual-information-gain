# Status

- OpenReview ID: `z1bSFIEexL`
- Paper: *Focusing Where Vision Matters: Selective Training for Large Vision Language Models via Visual Information Gain*
- Claims / maximum points: 6 / 12
- Source: arXiv 2602.17186v2 PDF/source archive pinned in `evidence/source/SHA256SUMS`.
- Compute: local CPU/local GTX 1050 only; no remote/HF/paid compute.
- Claim 1: **toy** — fixed synthetic probabilities validate the VIG log-PPL identity and expected sign/order. It is not LVLM, image, MS-COCO, or benchmark evidence.
- Claims 2–6: **unverified** — no LVLM checkpoint, image/text data, forward-pass logs, selective-training run, or benchmark outputs are present.
- Next: independently review the VIG toy against the pinned definition, then assess whether an end-to-end LVLM reproduction is feasible under the local-only compute policy.

Evidence: `outputs/claim1_vig_definition_toy/`, `evidence/source/`, and `contract/live_claims.json`.
