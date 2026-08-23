# WaveFilter Research

**Causal market-state filtering, volatility-risk detection, and systematic validation across financial time series.**

This repository is a graduate-application research portfolio documenting the design and validation of a proprietary market-state filtering framework. The production indicator source code, calibrated parameters, and private AutoLab implementation are intentionally withheld; the public repository focuses on research questions, experimental design, reproducibility, validation discipline, and non-proprietary findings.

## Research question

Technical indicators can look convincing in hindsight while failing under new market regimes, execution costs, or strict causal evaluation. This project studies a narrower and more testable problem:

> **Can a market-state filter remain responsive to meaningful structural change while reducing short-lived reversals, avoiding look-ahead bias, and preserving robustness across assets and timeframes?**

The project evolved from a visual oscillator into a research framework with explicit **Champion / Challenger governance**, cross-asset tests, sealed holdouts, platform-parity audits, and systematic rejection of extensions that did not survive out-of-sample validation.

## Key results

| Research component | Public result | Decision |
|---|---:|---|
| Core wave-state filter | Stable across repeated challenger tests | **Champion retained** |
| Standard volatility warning | High-volatility rate increased from **31.2% to 65.4%** in one sealed-holdout study | **Validated as non-directional risk information** |
| Volatility-warning stability | Positive lift across all 9 evaluated folds in the cited study | **Retained** |
| Multi-timeframe confirmation | Development evidence did not survive execution-cost / holdout requirements | **Rejected** |
| Divergence trading extensions | Visually promising but not robust enough under sealed validation | **Not promoted to trading logic** |
| Adaptive-threshold / acceleration experiments | Failed stability or regret guardrails | **Rejected** |

These results are research findings, not claims of future trading profitability.

## Why this project is different from a typical indicator demo

The main contribution is not a single chart signal. It is the **research process used to decide what should and should not be trusted**.

- causal, non-repainting event construction
- time-ordered development / holdout splits
- sealed holdout datasets opened only after rules were frozen
- cross-asset and cross-timeframe evaluation
- TradingView / Pine ↔ Python parity checks
- block-bootstrap uncertainty analysis
- transaction-cost and execution-delay stress tests
- negative-result retention instead of cherry-picking
- Champion / Challenger version governance

## System overview

![WaveFilter public research architecture](figures/research_architecture.svg)

```text
Market data
    ↓
Momentum & structural features
    ↓
Robust noise normalization
    ↓
Evidence accumulation
    ↓
Internal structural state
    ↓
Visible wave-state representation
    ↓
Independent research modules
(volatility risk, divergence studies, multi-timeframe context)
```

The public architecture intentionally omits formulas, implementation details, and calibrated parameter values.

## Real-market examples

### Bitcoin / BTCUSDT perpetual — 1H

![BTCUSDT WaveFilter example](figures/btc_wavefilter_real.jpg)

Crypto example showing repeated wave-state transitions, extreme-zone behavior, and divergence-style visual interpretation.

### NVIDIA / NVDA — 4H

![NVDA WaveFilter example](figures/nvda_wavefilter_real.jpg)

Equity example showing the same sub-chart framework applied to a large-cap technology stock over a higher timeframe.

### Gold / XAUUSD — 1H

![XAUUSD WaveFilter example](figures/xauusd_wavefilter_real.jpg)

Commodity example showing the framework during a sustained directional move with repeated upper-zone pressure and visible momentum deceleration.

These screenshots expose only visible chart output. They do **not** disclose the production implementation and are not presented as trading recommendations.

## Validation workflow

```text
Research idea
    ↓
Development-only opportunity diagnostic
    ↓
Candidate implementation
    ↓
Causal / parity audit
    ↓
Cross-dataset robustness checks
    ↓
Freeze rules and evaluation gates
    ↓
Open sealed holdout once
    ↓
Promote, restrict, or reject
```

A candidate is not accepted because it improves a few selected charts. It must survive the same protocol used for competing ideas.

## Selected research lessons

### 1. Better-looking signals are not necessarily better models

Several additions produced attractive historical examples but failed holdout, cost, or stability tests. Those modules were rejected rather than added to the production indicator.

### 2. Volatility information should not be confused with direction

The volatility-warning module is deliberately non-directional. Its role is to identify a higher-volatility regime, not predict whether price should rise or fall.

### 3. Visible responsiveness and structural confirmation can be separated

The framework distinguishes a visible wave-state representation from a more conservative internal structural state. This reduces the need to choose between an overly reactive display and an overly delayed structural filter.

### 4. Negative results are part of the research output

Failed ER acceleration, adaptive-threshold, divergence, warning, and multi-timeframe ideas are documented because they constrain what the final system is allowed to claim.

## Research timeline

| Stage | Main question | Outcome |
|---|---|---|
| Early baseline | Can a simple wave-state oscillator represent directional pressure? | Useful visually, but too sensitive to short-lived changes |
| Structural filtering | Can evidence accumulation reduce unnecessary reversals? | Improved stability; retained as core architecture |
| Dual-state design | Can the visible line remain responsive without forcing structural reversals? | Adopted |
| Adaptive recovery / resynchronization | Can visual lag be reduced without destabilizing structure? | Selective improvements retained |
| Volatility research | Can the framework identify future volatility risk without directional claims? | Standard warning validated |
| Divergence research | Do visual divergences add robust trading value? | Not validated as independent trading logic |
| Multi-timeframe research | Does higher/lower-timeframe confirmation add executable value? | Rejected after cost / holdout evaluation |
| Current stage | Preserve validated core and document the research process | Public portfolio + private production implementation |

## Reproducible public demo

[`notebooks/public_demo.ipynb`](notebooks/public_demo.ipynb) provides a synthetic, non-proprietary demonstration of the methodology. It includes:

- causal event construction using historical information only
- time-ordered development / holdout splitting
- non-directional volatility-risk evaluation
- block-bootstrap uncertainty analysis
- explicit separation between research evidence and trading claims

The notebook does **not** reproduce the production WaveFilter algorithm.

## Repository structure

```text
WaveFilter-Research/
├── README.md
├── NOTICE.md
├── .gitignore
├── docs/
│   ├── architecture.md
│   ├── methodology.md
│   ├── validation_framework.md
│   ├── experiment_history.md
│   └── limitations.md
├── results/
│   └── validation_summary.csv
├── figures/
│   ├── README.md
│   ├── real_examples.md
│   ├── research_architecture.svg
│   ├── synthetic_wave_state_demo.svg
│   ├── btc_wavefilter_real.jpg
│   ├── nvda_wavefilter_real.jpg
│   └── xauusd_wavefilter_real.jpg
└── notebooks/
    ├── README.md
    └── public_demo.ipynb
```

## Skills demonstrated

- quantitative time-series analysis
- Python research-pipeline design
- Pine Script / TradingView deployment
- causal event labeling and anti-leakage design
- cross-asset robustness testing
- sealed holdout methodology
- bootstrap-based uncertainty analysis
- transaction-cost and execution-delay evaluation
- research versioning and Champion / Challenger governance
- reproducibility and software-validation workflows
- communicating proprietary quantitative research without disclosing protected implementation details

## What is intentionally not public

The following are excluded from this repository:

- production Pine Script source code
- proprietary formulas and exact parameterization
- private AutoLab implementation
- raw private research datasets
- execution-specific trading rules
- credentials, API keys, account information, and private reports

The goal is to make the **research process auditable without disclosing proprietary implementation details**.

## Documentation

- [`docs/architecture.md`](docs/architecture.md) — conceptual system design
- [`docs/methodology.md`](docs/methodology.md) — research workflow
- [`docs/validation_framework.md`](docs/validation_framework.md) — anti-overfitting and holdout protocol
- [`docs/experiment_history.md`](docs/experiment_history.md) — accepted and rejected research directions
- [`docs/limitations.md`](docs/limitations.md) — scope and limitations
- [`figures/real_examples.md`](figures/real_examples.md) — real-market example notes
- [`notebooks/public_demo.ipynb`](notebooks/public_demo.ipynb) — synthetic public workflow demonstration

## Disclaimer

This repository is for academic, research, and portfolio purposes only. Nothing here constitutes investment advice, a recommendation, or a guarantee of financial performance.
