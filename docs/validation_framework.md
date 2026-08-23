# Validation Framework

## Why validation is central

Many indicator ideas improve historical charts while failing when evaluated on new data. This project therefore treats validation design as part of the model itself.

## Champion / Challenger protocol

The current production version is frozen as the **Champion**. Every proposed change is evaluated as a separate **Challenger**. A Challenger cannot replace the Champion based only on development-set performance.

## Development stage

Development data is used to answer whether an opportunity exists at all. Candidate features may be rejected before parameter search if they fail basic sample-size, stability, or causal requirements.

## Sealed holdout

The final holdout is kept inaccessible until:

- the candidate definition is frozen
- evaluation windows are frozen
- execution assumptions are frozen
- pass/fail gates are frozen

Once opened, the holdout is not reused for iterative tuning of the same hypothesis.

## Cross-dataset stability

A result is considered stronger when it persists across assets, timeframes, and periods rather than being driven by a single favorable segment.

## Platform parity

For production-relevant modules, TradingView/Pine events are compared bar-by-bar with an independent Python implementation. Timestamp shifts, field mismatches, or look-ahead violations must be resolved before performance evaluation.

## Dependence-aware uncertainty

Because cryptocurrency events are correlated through time and across assets, naive independent-sample statistics can overstate confidence. Block-based resampling and leave-one-dataset-out checks are used where appropriate.

## Execution realism

Trading applications are evaluated after confirmation delay, not from visually back-plotted pivot locations. Candidate rules are also stress-tested for transaction costs, slippage, and degradation of remaining opportunity after confirmation.

## Promotion rule

A feature is promoted only when it provides incremental, stable, out-of-sample value. Otherwise it is retained as a research result or rejected entirely.
