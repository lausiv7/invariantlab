# DoraHacks Mantle Turing Test Submission

## Project

```text
InvariantLab
```

## One-liner

```text
DeFi invariant checker for autonomous on-chain agents.
```

## Fit

Mantle Turing Test Phase II focuses on autonomous agents, on-chain strategy, AI data, RWA, AI DevTools, and agentic wallets. InvariantLab fits best under AI DevTools and AI x RWA risk management. It does not execute trading strategies itself; it verifies whether a strategy or vault interaction is safe before execution.

## Description

InvariantLab helps autonomous agents avoid unsafe DeFi actions. The tool represents known exploit classes as economic invariants, runs a verification test, and reports concrete risk signals such as attacker profit, stuck assets, or accounting divergence.

The MVP demonstrates a vault launch invariant. If a vault accepts an external first share before setup is complete, later NAV can be misallocated. InvariantLab turns that pattern into a reproducible test result and a patch recommendation.

## Demo

```bash
python3 scripts/invariantlab_demo.py --sample --json
```

Sample output fields:

```text
tests
reported_protocol_nav
attacker_profit_excluding_1_wei
stuck_cached_total_assets
patch_recommendation
```

## Mantle-Oriented Extension

For Mantle, the next adapter would check agent actions against Mantle DeFi/RWA primitives before execution:

```text
agent strategy proposal
target protocol state
known invariant patterns
fork or local simulation
risk decision
```

## Tracks

```text
AI DevTools
AI Trading & Strategy safety
AI x RWA risk management
Agentic Wallets & Economy
```
