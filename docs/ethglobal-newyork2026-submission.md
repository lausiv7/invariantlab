# ETHGlobal New York 2026 Submission

## Project

```text
InvariantLab
```

## One-liner

```text
AI-assisted DeFi invariant discovery and Foundry-based exploit verification.
```

## Description

InvariantLab turns DeFi security reasoning into runnable evidence. It identifies an economic invariant, runs a Foundry PoC, parses the result, and reports attacker profit, stuck assets, and the recommended fix. The current MVP demonstrates a vault launch invariant: a newly deployed vault must not accept the first external share before setup and activation are complete.

## Tracks

```text
AI x Crypto
DeFi
Security
Developer Tools
Data / Risk Infrastructure
```

## Demo

```bash
python3 scripts/invariantlab_demo.py --sample
```

Private PoC mode:

```bash
python3 scripts/invariantlab_demo.py \
  --target-repo /path/to/foundry-repo \
  --poc-file /path/to/InvariantPoC.t.sol \
  --match-path test/unit-test/InvariantPoC.t.sol
```

## Demo Video Script

InvariantLab is a DeFi security research tool. Instead of generating generic audit text, it focuses on economic invariants that can be tested. In this demo, the invariant is that a new vault must not accept the first external share before setup is complete. The runner parses a Foundry test result and extracts the pass count, reported protocol NAV, attacker profit, stuck assets, and patch recommendation. The next step is mainnet-fork replay, which turns fast local hypothesis testing into production-state evidence.
