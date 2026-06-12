# Architecture

InvariantLab is a compact DeFi security research pipeline.

```mermaid
flowchart LR
    A[Target DeFi Repo] --> B[Invariant Definition]
    B --> C[Foundry PoC Runner]
    C --> D[Evidence Parser]
    D --> E[Patch Recommendation]
```

The first supported invariant class is vault launch safety. A vault should not accept the first external share before roles, limits, strategy configuration, and activation state are complete.

```mermaid
sequenceDiagram
    participant O as Operator
    participant F as Factory
    participant V as New Vault
    participant A as Attacker
    participant S as Strategy

    O->>F: create vault
    F->>V: deploy with initial state
    A->>V: deposit first dust share
    O->>V: configure roles and strategy
    S-->>V: report NAV
    A->>V: redeem first share
    V-->>A: profit above principal
    V-->>V: stuck accounting remains
```

The MVP does not claim fully autonomous auditing. It packages a human-reviewed invariant into a repeatable verification loop.
