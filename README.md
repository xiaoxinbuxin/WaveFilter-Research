# WaveFilter Research

[![Public demo CI](https://github.com/xiaoxinbuxin/WaveFilter-Research/actions/workflows/public-demo.yml/badge.svg)](https://github.com/xiaoxinbuxin/WaveFilter-Research/actions/workflows/public-demo.yml)

**Research on causal market-state filtering, volatility risk, and robust validation in financial time series.**

I started WaveFilter as a visual oscillator for tracking directional pressure. As I kept testing it, the project became less about adding signals and more about deciding which ideas were actually reliable enough to keep.

This repository is the public research record for that process. It shows the methodology, validation framework, selected results, synthetic demonstrations, and examples of the visible indicator. The production implementation, exact formulas, calibrated parameters, and private research pipeline are not public.

## What I am studying

The main question is:

> **Can a market-state filter respond to meaningful structural change without becoming overly sensitive to short-lived noise?**

A second question became just as important during development: when a new feature looks better on a chart, does it still help after causal testing, cross-asset validation, execution assumptions, and a sealed holdout?

That led me to use a **Champion / Challenger** workflow. A stable version is kept as the Champion, while each new idea is tested separately as a Challenger. If an idea does not survive the same validation process, it is rejected rather than added to the indicator.

## How the project started

My first version was not a separate market-state system. I began by combining indicators I already used, especially **SKDJ, RSI, and Stochastic RSI**, because I expected agreement between several momentum indicators to produce cleaner signals.

The main problem was delay. Waiting for several indicators to confirm the same move often meant that part of the move had already happened. Adding more confirmation reduced some noise, but it also made the signal slower and the logic more complicated.

That pushed me away from indicator voting and toward building my own state logic around directional pressure, evidence, and structural change. I also began separating the responsive visible wave from the more conservative internal state so that every small fluctuation would not automatically become a formal reversal.

The full development story, including how my approach changed from chart tuning to systematic testing, is in [`docs/development_story.md`](docs/development_story.md).

## Selected results

| Research component | Result | Decision |
|---|---:|---|
| Core wave-state filter | Stable across repeated challenger tests | **Champion retained** |
| Standard volatility warning | High-volatility rate increased from **31.2% to 65.4%** in one sealed-holdout study | **Retained as non-directional risk information** |
| Volatility-warning stability | Positive lift across all 9 evaluated folds in that study | **Retained** |
| Multi-timeframe confirmation | Development evidence did not survive execution-cost / holdout requirements | **Rejected** |
| Divergence trading extensions | Promising visually, but not robust enough in sealed validation | **Not promoted to trading logic** |
| Adaptive-threshold / acceleration experiments | Failed stability or regret guardrails | **Rejected** |

The negative results are intentional. They are part of the project because they explain why the final system is simpler than the full set of ideas I tested.

A compact decision record is available in [`results/validation_summary.csv`](results/validation_summary.csv), with more context in [`docs/experiment_history.md`](docs/experiment_history.md).

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
```

The visible wave and the internal structural state are treated separately. This lets the display respond more naturally without forcing every visual move to become a formal structural reversal.

Volatility warnings are also kept separate from directional claims. Their purpose is to identify a higher-volatility environment, not to predict whether price will rise or fall.

More detail is in [`docs/architecture.md`](docs/architecture.md).

## How I test new ideas

I use time-ordered data rather than random train/test shuffling. Events are evaluated from the bar where they become observable, not from an earlier pivot that can only be identified later.

For production-relevant changes, the typical sequence is:

```text
research idea
    ↓
development-only diagnostic
    ↓
separate Challenger implementation
    ↓
causal and platform-parity checks
    ↓
cross-asset / cross-timeframe tests
    ↓
freeze rules and pass/fail gates
    ↓
open sealed holdout once
    ↓
promote, restrict, or reject
```

Depending on the experiment, I also check MFE/MAE, regret or reversal rates, confirmation delay, remaining opportunity after confirmation, transaction costs, slippage, and block-bootstrap uncertainty.

The full public protocol is documented in [`docs/methodology.md`](docs/methodology.md) and [`docs/validation_framework.md`](docs/validation_framework.md).

## Real-market examples

These screenshots show visible output only. They are examples of how the indicator behaves on different markets and timeframes, not trading recommendations.

### Bitcoin / BTCUSDT perpetual — 1H

![BTCUSDT WaveFilter example](figures/btc_wavefilter_real.jpg)

### NVIDIA / NVDA — 4H

![NVDA WaveFilter example](figures/nvda_wavefilter_real.jpg)

### Gold / XAUUSD — 1H

![XAUUSD WaveFilter example](figures/xauusd_wavefilter_real.jpg)

Notes for the examples are in [`figures/real_examples.md`](figures/real_examples.md).

## Reproducible public demo

[`notebooks/public_demo.ipynb`](notebooks/public_demo.ipynb) is a small synthetic example of the research workflow. It demonstrates:

- causal feature construction without look-ahead
- a time-ordered development / holdout split
- non-directional volatility-risk evaluation
- block-bootstrap uncertainty analysis

It does not reproduce the private WaveFilter algorithm. The environment is listed in [`requirements.txt`](requirements.txt), and GitHub Actions executes the notebook automatically so that the public demo stays reproducible.

## Repository guide

```text
WaveFilter-Research/
├── README.md
├── NOTICE.md
├── requirements.txt
├── docs/          development story, research design, and validation notes
├── results/       public decision summary
├── figures/       architecture and chart examples
└── notebooks/     synthetic reproducible demo
```

Useful starting points:

- [`docs/development_story.md`](docs/development_story.md) — how the indicator developed from early oscillator combinations into the current research framework
- [`docs/architecture.md`](docs/architecture.md) — system design
- [`docs/methodology.md`](docs/methodology.md) — research workflow
- [`docs/validation_framework.md`](docs/validation_framework.md) — holdout and anti-overfitting rules
- [`docs/experiment_history.md`](docs/experiment_history.md) — retained and rejected directions
- [`docs/limitations.md`](docs/limitations.md) — scope and limitations

## Scope

Most documented experiments use cryptocurrency data across a limited set of assets, timeframes, periods, and exchange feeds. Results should not be assumed to generalize automatically to other markets.

This repository is for academic, research, and portfolio use. It does not provide automated trading instructions or guarantee profitability after costs, latency, slippage, and risk constraints.

The production Pine Script, exact parameterization, private AutoLab implementation, raw private datasets, and execution-specific rules remain private. See [`NOTICE.md`](NOTICE.md) for the public disclosure boundary.
