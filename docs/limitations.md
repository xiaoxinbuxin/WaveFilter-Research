# Limitations

## Scope

The documented experiments focus primarily on cryptocurrency market data and a limited set of assets, timeframes, and exchange feeds. Results should not be assumed to generalize automatically to equities, futures, foreign exchange, other exchanges, or non-standard chart types.

Real-market screenshots from other asset classes are included as visual examples only and should not be interpreted as evidence of equivalent statistical validation in those markets.

## No guarantee of profitability

A market-state or volatility-risk signal can contain statistically useful information without being directly tradable after costs, latency, slippage, execution constraints, and risk management. The repository therefore distinguishes research utility from executable trading value.

## Model-selection risk

Repeated experimentation can create hidden overfitting even when individual tests appear rigorous. The project mitigates this with frozen hypotheses, sealed holdouts, pre-specified gates, cross-dataset checks, and retention of negative results, but cannot eliminate model-selection risk entirely.

A research result should therefore be interpreted together with its development history and validation protocol rather than as an isolated performance statistic.

## Market non-stationarity

Financial markets evolve. Relationships observed in one regime may weaken as liquidity, market structure, participants, regulation, or exchange microstructure change. Historical robustness cannot guarantee future stability.

## Data and implementation risk

Exchange feeds can differ in timestamping, liquidity, price construction, and missing-data behavior. Production-relevant research therefore requires explicit data-quality checks and, where relevant, independent implementation-parity audits.

## Proprietary implementation boundary

The public repository intentionally excludes production source code, formulas, calibrated parameters, private research infrastructure, raw private datasets, and execution-specific rules. As a result, the exact production indicator cannot be reconstructed solely from the public documentation.

The synthetic notebook demonstrates the **methodology**, not the private model.

## Educational purpose

This repository is an academic, research, and portfolio artifact. It is not investment advice, does not provide automated trading instructions, and does not guarantee future financial performance.

For the research process, see [`methodology.md`](methodology.md). For the validation and promotion rules, see [`validation_framework.md`](validation_framework.md).
