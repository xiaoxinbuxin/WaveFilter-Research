# Methodology

## Research question

The project studies whether a market-state filter can remain responsive to meaningful regime changes while reducing short-lived reversals, implementation artifacts, and hindsight bias.

## Experimental workflow

1. Define a single research hypothesis.
2. Freeze the current production Champion.
3. Implement the candidate as a separate Challenger.
4. Run development-only opportunity diagnostics before parameter search.
5. Evaluate across multiple assets, timeframes, and market periods.
6. Inspect failure modes, stability, and implementation consistency.
7. Freeze rules and evaluation gates before opening a sealed holdout.
8. Reject the candidate if improvements do not survive out-of-sample validation.

## Data discipline

The research process favors time-ordered evaluation over random shuffling. Event timestamps are treated causally: a signal is evaluated from the time it becomes observable, not from a historical pivot to which it may later be visually anchored.

## Event evaluation

Candidate modules are assessed using combinations of:

- directional return at fixed horizons
- maximum favorable excursion (MFE)
- maximum adverse excursion (MAE)
- event hit rate
- reversal or regret rate
- confirmation delay
- remaining executable opportunity after confirmation
- cross-dataset stability
- sensitivity to transaction costs and slippage

## Negative results

Rejected experiments are preserved as part of the research record. A visually attractive feature is not considered useful unless it provides incremental information after controlling for related market states and survives out-of-sample testing.

## Reproducibility boundary

The public repository documents the methodology but omits production source code, exact formulas, and proprietary parameterization. This allows the research process to be reviewed without disclosing the implementation itself.
