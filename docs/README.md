# Research Documentation

The documentation is organized so a reviewer can move from the system concept to the validation logic without needing access to proprietary implementation details.

## Recommended reading order

1. [`architecture.md`](architecture.md) — what the research system represents and how responsibilities are separated.
2. [`methodology.md`](methodology.md) — how hypotheses are formed, implemented, and evaluated causally.
3. [`validation_framework.md`](validation_framework.md) — how holdouts, parity checks, robustness tests, and promotion gates are handled.
4. [`experiment_history.md`](experiment_history.md) — selected retained, rejected, and not-validated research directions.
5. [`limitations.md`](limitations.md) — scope, generalization limits, non-stationarity, and interpretation boundaries.

## Public / private boundary

These documents describe research responsibilities, evaluation logic, and non-proprietary findings. They intentionally omit production formulas, calibrated parameters, private AutoLab code, raw private datasets, and execution-specific trading rules.

For the portfolio overview, return to the [repository README](../README.md). For compact public decisions, see [`../results/validation_summary.csv`](../results/validation_summary.csv).
