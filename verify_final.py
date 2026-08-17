import csv
import hashlib
import json
import pathlib
import subprocess
import tarfile


ROOT = pathlib.Path(__file__).resolve().parent
REPOSITORY = "https://github.com/MachineLearning-Nerd/icml26-visual-information-gain"
FORMER_REPOSITORY = "https://github.com/MachineLearning-Nerd/icml26-repro-z1bSFIEexL-visual-information-gain"
IDENTITY = "MachineLearning-Nerd"
EMAIL = "37579156+MachineLearning-Nerd@users.noreply.github.com"
OVERALL = "INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOY"
EXPECTED_STATUSES = {
    "C1": "TOY_SOURCE_VIG_FORMULA",
    "C2": "UNVERIFIED",
    "C3": "UNVERIFIED",
    "C4": "UNVERIFIED",
    "C5": "UNVERIFIED",
    "C6": "UNVERIFIED",
}


def run(*args):
    result = subprocess.run(args, cwd=ROOT, check=True, capture_output=True, text=True)
    return result.stdout


def fail(message):
    print("FINAL_AUDIT=FAILED " + message)
    raise SystemExit(1)


def load(relative):
    try:
        return json.loads((ROOT / relative).read_text())
    except Exception as exc:
        fail("invalid_json=" + relative + ":" + str(exc))


def require_files():
    required = [
        ".gitignore",
        "README.md",
        "STATUS.md",
        "AUTONOMOUS_STATE.json",
        "CLAIM_EVIDENCE.md",
        "SOURCE_AUDIT.md",
        "ENVIRONMENT.md",
        "REPORT.md",
        "AUTHOR_THANK_YOU.md",
        "CITATION.cff",
        "BRANCH_AUDIT.md",
        "branch-audit.md",
        "claims.json",
        "contract/live_claims.json",
        "evidence/source/SHA256SUMS",
        "evidence/source/arxiv.pdf",
        "evidence/source/arxiv_source.tar.gz",
        ".trackio/logbook/pages/claim-1-vig-definition/page.md",
        "src/claim1_vig_definition_toy.py",
        "tests/test_claim1_vig.py",
        "tests/test_contract.py",
        "outputs/claim1_vig_definition_toy/README.md",
        "outputs/claim1_vig_definition_toy/SHA256SUMS",
        "outputs/claim1_vig_definition_toy/config.json",
        "outputs/claim1_vig_definition_toy/raw_probabilities.json",
        "outputs/claim1_vig_definition_toy/results.csv",
        "outputs/claim1_vig_definition_toy/summary.json",
        "EVIDENCE_MANIFEST.json",
        "verify_final.py",
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    if missing:
        fail("missing=" + ",".join(missing))


def check_git():
    if run("git", "branch", "--show-current").strip() != "main":
        fail("branch_is_not_main")
    remote = run("git", "remote", "get-url", "origin").strip().removesuffix(".git")
    if remote != REPOSITORY:
        fail("remote=" + remote)
    branches = run("git", "for-each-ref", "refs/heads", "--format=%(refname:short)").splitlines()
    if branches != ["main"]:
        fail("local_branches=" + ",".join(branches))
    original_refs = run("git", "for-each-ref", "refs/original", "--format=%(refname)").strip()
    if original_refs:
        fail("original_refs_present")
    if int(run("git", "rev-list", "--count", "main").strip()) < 4:
        fail("canonical_history_too_short")
    for line in run("git", "log", "main", "--format=%H%x00%an%x00%ae%x00%cn%x00%ce%x00%s").splitlines():
        parts = line.split("\x00", 5)
        if len(parts) != 6 or parts[1] != IDENTITY or parts[2] != EMAIL or parts[3] != IDENTITY or parts[4] != EMAIL:
            fail("noncanonical_commit_identity=" + line)
    if "Co-authored-by:" in run("git", "log", "main", "--format=%B"):
        fail("coauthor_trailer_present")


def check_json_contract():
    state = load("AUTONOMOUS_STATE.json")
    if state["github_repository"] != REPOSITORY or state["former_github_repository"] != FORMER_REPOSITORY:
        fail("state_repository_mismatch")
    if state["phase"] != "published_and_verified" or state["branch_set"] != ["main"]:
        fail("state_phase_or_branches")
    if state["overall_verdict"] != OVERALL or state["publication_allowed"] is not False:
        fail("state_verdict")
    if state["claim_statuses"] != EXPECTED_STATUSES:
        fail("state_claim_statuses")
    claims = load("claims.json")
    if claims["repository"] != REPOSITORY or claims["former_repository"] != FORMER_REPOSITORY:
        fail("claims_repository_mismatch")
    if claims["overall_verdict"] != OVERALL or claims["publication_allowed"] is not False:
        fail("claims_verdict")
    if {item["id"]: item["status"] for item in claims["claims"]} != EXPECTED_STATUSES:
        fail("claims_statuses")
    contract = load("contract/live_claims.json")
    if contract["orid"] != "z1bSFIEexL" or contract["arxiv"] != "2602.17186" or contract["claim_count"] != 6:
        fail("contract_identity")
    if len(contract["claims"]) != 6:
        fail("contract_claim_count")


def check_checksum_file(relative):
    checksum_path = ROOT / relative
    for line in checksum_path.read_text().splitlines():
        if not line.strip():
            continue
        expected, name = line.split(maxsplit=1)
        name = name.lstrip("*")
        target = checksum_path.parent / name
        if not target.is_file():
            fail("checksum_target_missing=" + str(target.relative_to(ROOT)))
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            fail("checksum_mismatch=" + str(target.relative_to(ROOT)))


def check_source():
    check_checksum_file("evidence/source/SHA256SUMS")
    check_checksum_file("outputs/claim1_vig_definition_toy/SHA256SUMS")
    archive = ROOT / "evidence/source/arxiv_source.tar.gz"
    with tarfile.open(archive, "r:gz") as handle:
        members = handle.getmembers()
        if len(members) != 45 or sum(item.isfile() for item in members) != 44 or sum(item.isdir() for item in members) != 1:
            fail("source_archive_inventory")
        if any(item.issym() or (item.isfile() and item.mode & 0o111) for item in members):
            fail("source_archive_permissions")
        if "main.tex" not in {item.name for item in members}:
            fail("main_tex_missing")


def check_toy():
    config = load("outputs/claim1_vig_definition_toy/config.json")
    if config["metric"] != "VIG=log(PPL(A|Q)/PPL(A|Q,I))=mean_t(CE_text-CE_image)":
        fail("toy_metric")
    if "no VLM" not in config["scope"]:
        fail("toy_scope")
    summary = load("outputs/claim1_vig_definition_toy/summary.json")
    if summary["verdict"] != "toy" or "no VLM" not in summary["scope"]:
        fail("toy_summary_scope")
    values = {item["condition"]: item["vig"] for item in summary["results"]}
    required = {"matching-grounded", "partial-grounded", "conflicting-grounded", "weak-visual"}
    if set(values) != required:
        fail("toy_conditions")
    if not values["matching-grounded"] > values["partial-grounded"] > 0 > values["conflicting-grounded"]:
        fail("toy_sign_order")
    if abs(values["weak-visual"]) >= 0.02:
        fail("toy_weak_control")
    for item in summary["results"]:
        if abs(item["vig"] - sum(item["token_loss_differences"]) / len(item["token_loss_differences"])) >= 1e-12:
            fail("toy_token_identity=" + item["condition"])
    with (ROOT / "outputs/claim1_vig_definition_toy/results.csv").open(newline="") as handle:
        if {row["condition"] for row in csv.DictReader(handle)} != required:
            fail("toy_csv_conditions")


def check_manifest():
    manifest = load("EVIDENCE_MANIFEST.json")
    if manifest["schema_version"] != 1:
        fail("manifest_schema")
    tracked = [path for path in run("git", "ls-files", "-z").split("\x00") if path]
    expected = sorted(path for path in tracked if path not in {"AUTONOMOUS_STATE.json", "EVIDENCE_MANIFEST.json"})
    entries = manifest["files"]
    actual = sorted(item["path"] for item in entries)
    if actual != expected:
        fail("manifest_paths")
    for item in entries:
        target = ROOT / item["path"]
        if hashlib.sha256(target.read_bytes()).hexdigest() != item["sha256"] or target.stat().st_size != item["bytes"]:
            fail("manifest_hash=" + item["path"])


def main():
    require_files()
    check_git()
    check_json_contract()
    check_source()
    check_toy()
    check_manifest()
    print("FINAL_AUDIT=VERIFIED branches=1 claims=C1:toy_source_vig_formula,C2:unverified,C3:unverified,C4:unverified,C5:unverified,C6:unverified publication_allowed=false")


if __name__ == "__main__":
    main()
