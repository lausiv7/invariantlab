#!/usr/bin/env python3
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SAMPLE_OUTPUT = ROOT / "examples/sample_foundry_output.txt"
DEFAULT_TARGET_PATH = "test/unit-test/InvariantPoC.t.sol"


def run(cmd, cwd):
    proc = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, proc.stdout


def extract_int(label, text):
    match = re.search(rf"{re.escape(label)}:\s*([0-9]+)", text)
    return int(match.group(1)) if match else None


def parse_summary(output, log_path=None):
    pass_count = re.search(r"Suite result: ok\. ([0-9]+) passed; 0 failed; 0 skipped", output)
    summary = {
        "project": "InvariantLab",
        "demo": "vault launch invariant",
        "invariant": "a new vault must not accept first external shares before setup/activation",
        "tests": pass_count.group(1) + " passed" if pass_count else "not ok",
        "reported_protocol_nav": extract_int("reported protocol NAV", output),
        "attacker_profit_excluding_1_wei": extract_int("attacker profit excluding 1 wei principal", output),
        "stuck_cached_total_assets": extract_int("stuck cachedTotalAssets", output),
        "patch_recommendation": (
            "deploy vaults with deposits closed; open deposits only after roles, strategy, "
            "limits, and seed state are configured"
        ),
        "log": str(log_path) if log_path else None,
    }
    summary["agent_decision"] = agent_check(summary)
    return summary


def agent_check(summary):
    profit = summary.get("attacker_profit_excluding_1_wei") or 0
    stuck = summary.get("stuck_cached_total_assets") or 0
    if summary.get("tests") == "not ok":
        return {
            "decision": "REVIEW",
            "reason": "verification did not complete cleanly",
            "risk": "unknown",
        }
    if profit > 0 or stuck > 0:
        return {
            "decision": "BLOCK",
            "reason": "economic invariant violation detected before execution",
            "risk": "attacker profit or stuck accounting observed",
        }
    return {
        "decision": "ALLOW",
        "reason": "no measured invariant violation in the current run",
        "risk": "none observed",
    }


def print_summary(summary, as_json):
    if as_json:
        print(json.dumps(summary, indent=2))
        return
    print(f"{summary['project']} demo: {summary['demo']}")
    print(f"invariant: {summary['invariant']}")
    print(f"tests: {summary['tests']}")
    for key in ("reported_protocol_nav", "attacker_profit_excluding_1_wei", "stuck_cached_total_assets"):
        if summary[key] is not None:
            print(f"{key}: {summary[key]}")
    print(f"patch_recommendation: {summary['patch_recommendation']}")
    print(f"agent_decision: {summary['agent_decision']['decision']}")
    print(f"agent_reason: {summary['agent_decision']['reason']}")
    if summary["log"]:
        print(f"log: {summary['log']}")


def main():
    parser = argparse.ArgumentParser(description="InvariantLab DeFi invariant verification demo")
    parser.add_argument("--sample", action="store_true", help="run the bundled public sample output")
    parser.add_argument("--target-repo", help="Foundry repository root for a private PoC run")
    parser.add_argument("--poc-file", help="private PoC Solidity file to copy into the target repo")
    parser.add_argument("--match-path", default=DEFAULT_TARGET_PATH, help="Foundry match path inside target repo")
    parser.add_argument("--log", help="optional log output path")
    parser.add_argument("--json", action="store_true", help="print machine-readable summary")
    parser.add_argument("--agent-check", action="store_true", help="print only the agent execution decision")
    args = parser.parse_args()

    if args.sample:
        output = SAMPLE_OUTPUT.read_text(encoding="utf-8")
        summary = parse_summary(output)
        if args.agent_check:
            print(json.dumps(summary["agent_decision"], indent=2))
        else:
            print_summary(summary, args.json)
        return

    if not args.target_repo or not args.poc_file:
        raise SystemExit("use --sample or provide --target-repo and --poc-file")

    repo = Path(args.target_repo).resolve()
    poc = Path(args.poc_file).resolve()
    target = repo / args.match_path
    if not (repo / "foundry.toml").exists():
        raise SystemExit(f"not a Foundry repo: {repo}")
    if not poc.exists():
        raise SystemExit(f"missing PoC source: {poc}")

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(poc, target)

    command = ["forge", "test", "--match-path", args.match_path, "-vv"]
    code, output = run(command, repo)

    log_path = Path(args.log).resolve() if args.log else None
    if log_path:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(output, encoding="utf-8")

    summary = parse_summary(output, log_path)
    summary["repo"] = str(repo)
    summary["command"] = " ".join(command)
    if args.agent_check:
        print(json.dumps(summary["agent_decision"], indent=2))
    else:
        print_summary(summary, args.json)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
