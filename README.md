# WaveFilter Research

[![Public demo CI](https://github.com/xiaoxinbuxin/WaveFilter-Research/actions/workflows/public-demo.yml/badge.svg)](https://github.com/xiaoxinbuxin/WaveFilter-Research/actions/workflows/public-demo.yml)

**Causal market-state filtering, volatility-risk detection, and systematic validation across financial time series.**

WaveFilter Research is a graduate-application research portfolio documenting the design and validation of a proprietary market-state filtering framework. The public repository focuses on research questions, experimental design, reproducibility, validation discipline, and non-proprietary findings. Production source code, calibrated parameters, private AutoLab infrastructure, and execution-specific rules are intentionally withheld.

## At a glance

| Area | Public scope |
|---|---|
| Research problem | Robust market-state filtering under non-stationary financial data |
| Core methodology | Causal event construction, time-ordered validation, sealed holdouts, Champion / Challenger governance |
| Strongest retained extension | Non-directional volatility-risk warning |
| Rejected extensions | Several visually attractive ideas that failed robustness, cost, or holdout requirements |
| Reproducibility | Synthetic public notebook + automated CI execution |
| Proprietary boundary | No production Pine source, exact formulas, calibrated parameters, or private AutoLab code |

## Research question

Technical indicators can look convincing in hindsight while failing under new market regimes, execution costs, or strict causal evaluation. This project studies a narrower and more testable problem:

> **Can a market-state filter remain responsive to meaningful structural change while reducing short-lived reversals, avoiding look-ahead bias, and preserving robustness across assets and timeframes?**

The project evolved from a visual oscillator into a research framework with explicit **Champion / Challenger governance**, cross-asset tests, sealed holdouts, platform-parity audits, and systematic rejection of extensions that did not survive out-of-sample validation.

## Selected results

| Research component | Public result | Decision |
|---|---:|---|
| Core wave-state filter | Stable across repeated challenger tests | **Champion retained** |
| Standard volatility warning | High-volatility rate increased from **31.2% to 65.4%** in one sealed-holdout study | **Validated as non-directional risk information** |
| Volatility-warning stability | Positive lift across all 9 evaluated folds in the cited study | **Retained** |
| Multi-timeframe confirmation | Development evidence did not survive execution-cost / holdout requirements | **Rejected** |
| Divergence trading extensions | Visually promising but not robust enough under sealed validation | **Not promoted to trading logic** |
| Adaptive-threshold / acceleration experiments | Failed stability or regret guardrails | **Rejected** |

These are research findings, not claims of future trading profitability. A fuller public decision record is available in [`results/validation_summary.csv`](results/validation_summary.csv) and [`docs/experiment_history.md`](docs/experiment_history.md).

## System architecture

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

The public architecture intentionally communicates responsibilities and validation interfaces rather than implementation details. See [`docs/architecture.md`](docs/architecture.md).

## Validation discipline

A candidate is not accepted because it improves a few selected charts. The research workflow is designed to separate visual appeal from evidence:

```text
Research hypothesis
    ↓
Freeze current Champion
    ↓
Development-only opportunity diagnostic
    ↓
Implement separate Challenger
    ↓
Causal / platform-parity audit
    ↓
Cross-asset and cross-timeframe robustness checks
    ↓
Freeze rules and pass/fail gates
    ↓
Open sealed holdout once
    ↓
Promote, restrict, or reject
```

Core practices include:

- causal, non-repainting event construction
- time-ordered development / holdout splits
- sealed holdouts opened only after rules are frozen
- cross-asset and cross-timeframe evaluation
- TradingView / Pine ↔ Python parity checks for production-relevant modules
- dependence-aware bootstrap analysis where appropriate
- transaction-cost and execution-delay stress tests for trading applications
- retention of negative results instead of cherry-picking
- explicit Champion / Challenger version governance

See [`docs/methodology.md`](docs/methodology.md) and [`docs/validation_framework.md`](docs/validation_framework.md) for the detailed public protocol.

## Real-market examples

The screenshots below show only visible chart output. They do **not** disclose the production implementation and are not presented as trading recommendations.

### Bitcoin / BTCUSDT perpetual — 1H

![BTCUSDT WaveFilter example](figures/btc_wavefilter_real.jpg)

### NVIDIA / NVDA — 4H

![NVDA WaveFilter example](figures/nvda_wavefilter_real.jpg)

### Gold / XAUUSD — 1H

![XAUUSD WaveFilter example](figures/xauusd_wavefilter_real.jpg)

Context for these figures is documented in [`figures/real_examples.md`](figures/real_examples.md).

## Reproducible public demo

[`notebooks/public_demo.ipynb`](notebooks/public_demo.ipynb) provides a synthetic, non-proprietary demonstration of the research workflow. It includes:

- causal event construction using historical information only
- time-ordered development / holdout splitting
- non-directional volatility-risk evaluation
- block-bootstrap uncertainty analysis
- explicit separation between research evidence and trading claims

The notebook does **not** reproduce the production WaveFilter algorithm. Dependencies are listed in [`requirements.txt`](requirements.txt), and GitHub Actions executes the notebook automatically to verify that the public demonstration remains reproducible.

## What the project demonstrates

- quantitative time-series analysis
- Python research-pipeline design
- Pine Script / TradingView deployment
- causal event labeling and anti-leakage design
- cross-asset robustness testing
- sealed-holdout methodology
- bootstrap-based uncertainty analysis
- transaction-cost and execution-delay evaluation
- research versioning and Champion / Challenger governance
- reproducible computational research
- communication of proprietary quantitative work without disclosing protected implementation details

## Repository map

```text
WaveFilter-Research/
├── README.md
├── NOTICE.md
├── requirements.txt
├── .gitignore
├── .github/
│   └── workflows/
│       └── public-demo.yml
├── docs/
│   ├── README.md
│   ├── architecture.md
│   ├── methodology.md
│   ├── validation_framework.md
│   ├── experiment_history.md
│   └── limitations.md
├── results/
│   ├── README.md
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

## Documentation

Start with [`docs/README.md`](docs/README.md), then use the topic-specific documents:

- [`docs/architecture.md`](docs/architecture.md) — conceptual system design
- [`docs/methodology.md`](docs/methodology.md) — research workflow and causal evaluation
- [`docs/validation_framework.md`](docs/validation_framework.md) — anti-overfitting and holdout protocol
- [`docs/experiment_history.md`](docs/experiment_history.md) — accepted and rejected research directions
- [`docs/limitations.md`](docs/limitations.md) — scope, non-stationarity, and interpretation limits

## Public disclosure boundary

The following are intentionally excluded:

- production Pine Script source code
- proprietary formulas and exact parameterization
- private AutoLab implementation
- raw private research datasets
- execution-specific trading rules
- credentials, API keys, account information, and private reports

The goal is to make the **research process auditable without disclosing proprietary implementation details**. See [`NOTICE.md`](NOTICE.md) for the repository's use and intellectual-property notice.

## Limitations and disclaimer

The documented experiments focus primarily on cryptocurrency market data and a limited set of assets, timeframes, and exchange feeds. Results should not be assumed to generalize automatically to other markets. Statistically useful information is not necessarily directly tradable after costs, latency, slippage, and risk constraints.

This repository is for academic, research, and portfolio purposes only. Nothing here constitutes investment advice, a recommendation, or a guarantee of financial performance.
