# Limitations

## Scope

The documented experiments focus on cryptocurrency market data and a limited set of assets, timeframes, and exchange feeds. Results should not be assumed to generalize automatically to equities, futures, foreign exchange, other exchanges, or non-standard chart types.

## No guarantee of profitability

A market-state or volatility-risk signal can contain statistically useful information without being directly tradable after costs, latency, slippage, and risk constraints. The repository therefore distinguishes research utility from executable trading value.

## Model-selection risk

Repeated experimentation can create hidden overfitting even when individual tests appear rigorous. The project mitigates this with sealed holdouts, pre-specified gates, and retention of negative results, but cannot eliminate model-selection risk entirely.

## Market non-stationarity

Cryptocurrency markets evolve. Relationships observed in one regime may weaken as liquidity, market structure, participants, or exchange microstructure change.

## Proprietary implementation boundary

The public repository intentionally excludes production source code, formulas, calibrated parameters, and private research infrastructure. As a result, the exact production indicator cannot be reconstructed solely from the public documentation.

## Educational purpose

This repository is an academic and research portfolio. It is not investment advice and does not provide automated trading instructions.
