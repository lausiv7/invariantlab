# 062. DoraHacks Mantle Turing Test Submission

## BUIDL Name

```text
InvariantLab
```

## BUIDL Logo

```text
invariantlab/assets/invariantlab-logo-480.png
```

## Vision

```text
InvariantLab is an AI-assisted DeFi invariant verification agent for autonomous on-chain systems. It checks whether a proposed DeFi action violates critical economic invariants before capital moves on-chain, then returns an execution decision such as `ALLOW`, `BLOCK`, or `REVIEW`.

For the Mantle Turing Test, InvariantLab is positioned as an AI DevTool and risk layer for agentic wallets, trading agents, and RWA/DeFi strategy agents. The current MVP demonstrates vault launch safety: a newly deployed vault should not accept the first external share before setup and activation are complete.
```

## Category

```text
AI DevTools / DeFi / AI Trading & Strategy Safety / RWA Risk Infrastructure
```

## Is this BUIDL an AI Agent?

```text
Yes
```

InvariantLab acts as a pre-execution risk agent. It does not trade or move funds by itself; it evaluates a proposed DeFi action and returns an execution decision based on invariant evidence.

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
invariantlab/demo/invariantlab-demo.mp4
```

## Social Link

```text
https://github.com/lausiv7
```

## Technology Stack Used

```text
Python 3
Foundry
Solidity
GitHub
Pillow
FFmpeg
Agent decision CLI
```

## Details

```text
InvariantLab helps autonomous agents avoid unsafe DeFi actions. The agent represents known exploit classes as economic invariants, runs a verification test, and returns ALLOW/BLOCK/REVIEW based on concrete risk signals such as attacker profit, stuck assets, or accounting divergence.

For Mantle, the intended use case is a pre-execution safety check for agentic wallets, AI trading agents, and RWA/DeFi strategy agents:

agent strategy proposal -> target protocol state -> known invariant patterns -> local/fork simulation -> risk decision

The current demo uses a vault launch invariant:

a newly deployed vault should not accept the first external share before setup and activation are complete.

Run:

python3 scripts/invariantlab_demo.py --sample --json

Agent decision mode:

python3 scripts/invariantlab_demo.py --sample --agent-check

Observed output fields:

tests
reported_protocol_nav
attacker_profit_excluding_1_wei
stuck_cached_total_assets
patch_recommendation
agent_decision

The next Mantle-oriented extension would add adapters for Mantle DeFi/RWA primitives and expose a callable risk-check interface for agents before execution.
```

## 수정 이력

2026-06-13: 061 제출폼 구조에 맞춰 Mantle용 062를 재작성했다.
