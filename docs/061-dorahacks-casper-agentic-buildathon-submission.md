# 061. DoraHacks Casper Agentic Buildathon Submission

## BUIDL Name

```text
InvariantLab
```

## BUIDL Logo

```text
docs/screenshots/063-invariantlab-logo-480.png
```

## Vision

```text
InvariantLab is an AI-assisted DeFi invariant verification tool. It helps developers and AI agents check whether a protocol action violates critical economic invariants before capital moves on-chain.

The current MVP demonstrates vault launch safety: a newly deployed vault should not accept the first external share before setup and activation are complete. InvariantLab turns that invariant into runnable evidence by parsing Foundry PoC output and returning pass count, attacker profit, stuck assets, and a patch recommendation.
```

## Category

```text
AI Agents / DeFi / Developer Tools / Risk Infrastructure
```

## Is this BUIDL an AI Agent?

```text
No
```

InvariantLab is currently an agent safety and verification tool, not a fully autonomous agent. It can later expose MCP/tools for agents.

## GitHub

```text
https://github.com/lausiv7/invariantlab
```

## Project Website

```text
https://github.com/lausiv7/invariantlab
```

## Demo Video

Upload this file to YouTube and paste the YouTube link:

```text
docs/screenshots/063-invariantlab-demo.mp4
```

## Social Link

```text
https://github.com/lausiv7
```

## Details

```text
InvariantLab converts DeFi security reasoning into runnable evidence. It models protocol-specific economic invariants, runs a Foundry PoC or verification test, parses measurable impact, and returns a patch recommendation.

For an agentic DeFi workflow, this becomes a pre-execution safety gate:

agent intent -> invariant check -> PoC/fork simulation -> risk result -> execute or block

The current demo uses a vault launch invariant:

a newly deployed vault should not accept the first external share before setup and activation are complete.

Run:

python3 scripts/invariantlab_demo.py --sample

Observed result:

tests: 5 passed
reported_protocol_nav: 1208925819614629174706176
attacker_profit_excluding_1_wei: 604462909807314587353087
stuck_cached_total_assets: 604462909807314587353088

The next version adds an MCP server interface:

check_invariant(repo_or_contract, action_context)
run_foundry_poc(target_repo, poc_file)
summarize_risk(test_output)

This lets agent frameworks call InvariantLab before executing DeFi actions.
```

## 수정 이력

2026-06-13: DoraHacks BUIDL 제출폼 필드 기준으로 재작성했다.
