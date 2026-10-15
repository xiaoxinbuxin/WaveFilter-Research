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

The full development story, including how my approach changed from chart tuning to systematic testing, is in [`docs/development_story.md`](docs/development_story.md). A shorter stage-by-stage version is in [`docs/development_timeline.md`](docs/development_timeline.md).

## Current research milestone

The current public milestone is based on the **v21.8.24** WaveFilter line developed in September 2026. After additional audit, causal replay, and locked validation, the core wave-state framework remained the retained baseline. A simplified **single non-directional volatility-warning layer** was kept for its specific role, while several alternative predictive, multi-timeframe, divergence, and faster-response ideas were not promoted when they did not show sufficiently stable incremental value.

The public repository records that development decision without publishing the production Pine Script, private replay outputs, exact formulas, or calibrated parameters.

## Selected research decisions

The decisions below are author-reported summaries of private research. The public repository does not independently reproduce those studies. Previously published numerical claims and the limits of their public evidence are collected in [Private-study context](results/private_study_context.md). For directly inspectable output, see the separate [executed synthetic demo](results/public_demo_results.md).

| Research component | Result | Decision |
|---|---:|---|
| Core wave-state filter | Stable across repeated challenger tests | **Champion retained** |
| Standard volatility warning | Reported higher future-volatility frequency in a private study; public evidence is limited to a summary | **Retained as non-directional risk information** |
| Multi-timeframe confirmation | Development evidence did not survive execution-cost / holdout requirements | **Rejected** |
| Divergence trading extensions | Promising visually, but not robust enough in sealed validation | **Not promoted to trading logic** |
| Adaptive-threshold / acceleration experiments | Failed stability or regret guardrails | **Rejected** |

The negative results are intentional. They are part of the project because they explain why the final system is simpler than the full set of ideas I tested.

A compact decision record is available in [`results/validation_summary.csv`](results/validation_summary.csv), with more context in [`docs/experiment_history.md`](docs/experiment_history.md).

## System overview

![WaveFilter public research architecture](figures/research_architecture_v2.svg)

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

## Current Cross-Market Examples

These selected TradingView screenshots illustrate the current visible WaveFilter output across cryptocurrency, an equity ETF, an individual equity, and a commodity. They show visual state behavior in different market contexts; they do not establish strategy profitability or cross-market statistical validity and are not trading recommendations.

### Bitcoin / BTCUSD (CRYPTO) — 1H

![BTCUSD (CRYPTO), 1H — current WaveFilter chart example](figures/btcusd_crypto_1h_current.png)

The visible wave repeatedly occupies the lower extreme region during the sustained decline on the right of the chart, then rises as price rebounds. The snapshot illustrates lower-zone persistence and recovery in a cryptocurrency context.

### Invesco QQQ Trust / QQQ (NASDAQ ETF) — 4H

![QQQ (NASDAQ ETF), 4H — current WaveFilter chart example](figures/qqq_nasdaq_4h_current.png)

The ETF view spans an advance, repeated pullbacks, and a later decline with a rebound. The lower panel shows alternating wave states and repeated visits to both extreme regions across that sequence.

### NVIDIA / NVDA (NASDAQ) — 4H

![NVDA (NASDAQ), 4H — current WaveFilter chart example](figures/nvda_nasdaq_4h_current.png)

The individual-equity view shows repeated upper- and lower-zone episodes through advances, declines, and recoveries. Numbered annotations and shaded intervals provide visible context alongside the wave.

### Gold (TVC) — 1H

![TVC Gold, 1H — current WaveFilter chart example](figures/gold_tvc_1h_current.png)

The TVC Gold view covers an initial advance followed by a decline and several rebounds. The visible wave alternates between extreme regions and intermediate states as the price path changes.

Notes for the examples are in [`figures/real_examples.md`](figures/real_examples.md).

## Reproducible public demo

Read the [executed results snapshot](results/public_demo_results.md) for the actual synthetic sample counts, event rates, bootstrap interval, boundary audit, and chart. The [notebook](notebooks/public_demo.ipynb) also includes saved outputs, so it can be inspected without running code.

[`notebooks/public_demo.ipynb`](notebooks/public_demo.ipynb) is a small synthetic example of the research workflow. It demonstrates:

- causal feature construction without look-ahead
- complete future labels and a purged time-ordered development / holdout split
- non-directional volatility-risk evaluation
- block-bootstrap uncertainty analysis

It does not reproduce the private WaveFilter algorithm or the reported private-study numbers. The demo settings and seeds are retained from the original public example, including when outcomes are unfavorable. [Run instructions](notebooks/README.md) explain how to regenerate the saved artifacts. The environment is listed in [`requirements.txt`](requirements.txt), with the snapshot's exact versions in [`results/public_demo_run.json`](results/public_demo_run.json). GitHub Actions runs boundary regression checks and executes the notebook.

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

- [`docs/development_story.md`](docs/development_story.md) — narrative of how the indicator developed from early oscillator combinations into the current research framework
- [`docs/development_timeline.md`](docs/development_timeline.md) — stage-by-stage development path and current public milestone
- [`docs/architecture.md`](docs/architecture.md) — system design
- [`docs/methodology.md`](docs/methodology.md) — research workflow
- [`docs/validation_framework.md`](docs/validation_framework.md) — holdout and anti-overfitting rules
- [`docs/experiment_history.md`](docs/experiment_history.md) — retained and rejected directions
- [`docs/limitations.md`](docs/limitations.md) — scope and limitations

## Scope

Most documented experiments use cryptocurrency data across a limited set of assets, timeframes, periods, and exchange feeds. Results should not be assumed to generalize automatically to other markets.

This repository is for academic, research, and portfolio use. It does not provide automated trading instructions or guarantee profitability after costs, latency, slippage, and risk constraints.

The production Pine Script, exact parameterization, private AutoLab implementation, raw private datasets, and execution-specific rules remain private. See [`NOTICE.md`](NOTICE.md) for the public disclosure boundary.
