# Environment and reproduction boundary

- Compute policy: local CPU/local GTX 1050 only.
- Remote, paid, upgraded-cloud, Hugging Face Jobs, and external GPU execution are out of scope.
- The bounded toy uses Python standard library only.
- No LVLM checkpoint, tokenizer, image dataset, text dataset, training code, or benchmark evaluator is included.
- The source PDF and source archive are pinned before any claim interpretation.
- Generated Python bytecode, macOS metadata, and pytest cache are ignored.
- The lightweight verifier uses Python 3, Git, JSON, tarfile, and SHA-256.

The environment is sufficient for the deterministic formula toy and audit checks. It is not sufficient evidence for the paper’s end-to-end LVLM training and benchmark claims.
