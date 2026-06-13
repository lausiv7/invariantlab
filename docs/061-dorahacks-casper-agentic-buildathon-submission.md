# DoraHacks Casper Agentic Buildathon Submission

## Project

```text
InvariantLab
```

## One-liner

```text
AI safety layer for DeFi agents: verify economic invariants before capital moves on-chain.
```

## Fit

Casper Agentic Buildathon focuses on AI agents, Web3, DeFi, RWA, MCP, and agent payments. InvariantLab fits as a risk-checking agent layer. Before an autonomous agent executes a DeFi action, InvariantLab checks whether the target protocol state violates known economic invariants.

## Description

InvariantLab converts DeFi security reasoning into runnable evidence. It models protocol-specific economic invariants, runs a Foundry PoC or verification test, parses measurable impact, and returns a patch recommendation. The current MVP demonstrates a vault launch invariant: a newly deployed vault should not accept the first external share before setup and activation are complete.

For an agentic DeFi workflow, this becomes a pre-execution safety gate:

```text
agent intent -> invariant check -> PoC/fork simulation -> risk result -> execute or block
```

## Demo

```bash
python3 scripts/invariantlab_demo.py --sample
```

Expected result:

```text
tests: 5 passed
reported_protocol_nav: 1208925819614629174706176
attacker_profit_excluding_1_wei: 604462909807314587353087
stuck_cached_total_assets: 604462909807314587353088
```

## Tracks

```text
AI Agents
DeFi
MCP / agent tooling
Risk infrastructure
Developer tooling
```

## Roadmap For Casper

The next version adds an MCP server interface:

```text
check_invariant(repo_or_contract, action_context)
run_foundry_poc(target_repo, poc_file)
summarize_risk(test_output)
```

This lets agent frameworks call InvariantLab before executing DeFi actions.
