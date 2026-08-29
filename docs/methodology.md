# Methodology

## Research question

The project studies whether a market-state filter can remain responsive to meaningful regime changes while reducing short-lived reversals, implementation artifacts, and hindsight bias.

## Experimental workflow

Each research direction is treated as a separate hypothesis rather than an invitation to keep adding features to the production system.

1. Define a single research hypothesis and its intended role.
2. Freeze the current production Champion.
3. Specify causal inputs, evaluation windows, and implementation boundaries.
4. Run development-only opportunity diagnostics before broad parameter search.
5. Implement the candidate as a separate Challenger.
6. Evaluate across multiple assets, timeframes, and market periods.
7. Inspect failure modes, stability, implementation consistency, and dependence on extreme observations.
8. Freeze candidate rules and pass/fail gates before opening a sealed holdout.
9. Open the holdout once for the frozen hypothesis.
10. Promote, restrict, or reject the candidate according to the pre-specified decision rule.

## Causal observability

Event timestamps are treated causally: a signal is evaluated from the time it becomes observable, not from a historical pivot to which it may later be visually anchored. Features used to construct an event must be available at or before that event time.

Future information may be used only as an **evaluation target after the event is fixed**. It is never allowed to alter the event definition retrospectively.

## Time-ordered data discipline

The research process favors chronological development / holdout splits over random shuffling. When event labels require future bars, embargoes or equivalent boundaries are used where appropriate so that future-label windows do not leak across evaluation segments.

Cross-asset and cross-timeframe results are inspected separately before aggregation. This reduces the risk that one favorable dataset masks instability elsewhere.

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
- dependence on a small number of extreme observations

The exact metrics depend on the research question. For example, a non-directional volatility warning is evaluated as risk information rather than forced into a directional-return objective.

## Implementation consistency

For production-relevant modules, an independent Python implementation is used to audit TradingView/Pine behavior. Event timestamps and state transitions are compared bar-by-bar where practical. A performance result is not considered trustworthy if implementation parity is unresolved.

## Negative results

Rejected experiments are preserved as part of the research record. A visually attractive feature is not considered useful unless it provides incremental information after controlling for related market states and survives the relevant out-of-sample requirements.

Negative results serve two purposes:

- they constrain what the project is allowed to claim;
- they reduce the temptation to repeat previously failed parameter or feature families under slightly different names.

## Reproducibility boundary

The public repository makes the **research workflow** reproducible through documentation, a synthetic notebook, and compact public result summaries. It intentionally omits production source code, exact formulas, proprietary parameterization, private AutoLab infrastructure, raw private datasets, and execution-specific rules.

For the formal promotion rules, continue with [`validation_framework.md`](validation_framework.md). Selected outcomes are summarized in [`experiment_history.md`](experiment_history.md).
