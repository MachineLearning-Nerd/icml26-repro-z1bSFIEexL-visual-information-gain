# Status

- Repository: https://github.com/MachineLearning-Nerd/icml26-visual-information-gain
- Former name: icml26-repro-z1bSFIEexL-visual-information-gain
- Paper: Focusing Where Vision Matters: Selective Training for Large Vision Language Models via Visual Information Gain
- Authors: Seulbi Lee and Sangheum Hwang
- OpenReview: z1bSFIEexL
- arXiv: 2602.17186v2
- Claims / maximum points: 6 / 12
- Branches: main only; canonical/default branch
- Commit identity: MachineLearning-Nerd
- Compute: local CPU/local GTX 1050 only; no remote/HF/paid compute.

| Claim | Local status |
| --- | --- |
| C1 — VIG log-PPL definition and token-loss identity | TOY_SOURCE_VIG_FORMULA |
| C2 — sample/token decomposition and grounded-token analysis | UNVERIFIED |
| C3 — matching/partial/conflicting MS-COCO VIG behavior | UNVERIFIED |
| C4 — visually grounded token loss-difference analysis | UNVERIFIED |
| C5 — VIG-guided selective training | UNVERIFIED |
| C6 — benchmark, data-efficiency, and language-bias gains | UNVERIFIED |

Overall verdict: INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOY. Publication of full-paper reproduction results is not allowed. The local evidence is limited to pinned paper artifacts, a deterministic formula toy, and lightweight audit checks.

Evidence: CLAIM_EVIDENCE.md, SOURCE_AUDIT.md, EVIDENCE_MANIFEST.json, outputs/claim1_vig_definition_toy/, evidence/source/, and contract/live_claims.json.
