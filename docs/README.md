# Research Documentation

The documentation is organized so a reviewer can move from how the project developed to the system design and validation logic without needing access to proprietary implementation details.

## Recommended reading order

1. [`development_story.md`](development_story.md) — how the project moved from combining SKDJ, RSI, and Stochastic RSI to a separate market-state filter and a more systematic research process.
2. [`architecture.md`](architecture.md) — what the research system represents and how responsibilities are separated.
3. [`methodology.md`](methodology.md) — how hypotheses are formed, implemented, and evaluated causally.
4. [`validation_framework.md`](validation_framework.md) — how holdouts, parity checks, robustness tests, and promotion gates are handled.
5. [`experiment_history.md`](experiment_history.md) — selected retained, rejected, and not-validated research directions.
6. [`limitations.md`](limitations.md) — scope, generalization limits, non-stationarity, and interpretation boundaries.

## Public / private boundary

These documents describe the development process, research responsibilities, evaluation logic, and non-proprietary findings. They intentionally omit production formulas, calibrated parameters, private AutoLab code, raw private datasets, and execution-specific trading rules.

For the portfolio overview, return to the [repository README](../README.md). For compact public decisions, see [`../results/validation_summary.csv`](../results/validation_summary.csv).
