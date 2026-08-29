# Validation Framework

## Why validation is central

Many indicator ideas improve historical charts while failing when evaluated on new data. This project therefore treats validation design as part of the model-development process rather than as a final reporting step.

## Champion / Challenger protocol

The current production version is frozen as the **Champion**. Every proposed change is evaluated as a separate **Challenger**. A Challenger cannot replace the Champion based only on selected screenshots or development-set performance.

A useful Challenger should improve a clearly defined objective without materially degrading protected properties such as causal timing, structural stability, or implementation consistency.

## Development stage

Development data is used to answer whether an opportunity exists at all. A candidate may be rejected before broad parameter search if it fails basic requirements such as:

- causal validity
- minimum event count
- cross-dataset consistency
- acceptable timing or regret behavior
- implementation invariants
- robustness to a small number of extreme observations

This stopping rule is intended to reduce parameter fishing.

## Frozen candidate stage

If development evidence is strong enough to continue, the candidate definition is frozen before final validation. The frozen specification includes, where relevant:

- feature and event definitions
- parameter values
- evaluation horizons
- execution assumptions
- embargo or label-completion rules
- pass/fail thresholds

The specification is not loosened after seeing holdout results.

## Sealed holdout

The final holdout is kept inaccessible until the candidate and evaluation protocol are frozen. Once opened, the holdout is not reused for iterative tuning of the same hypothesis.

A near miss is still a miss when the threshold was frozen in advance. Post-hoc threshold changes would turn the holdout into development data.

## Cross-dataset stability

A result is considered stronger when it persists across assets, timeframes, and periods rather than being driven by one favorable segment. Aggregate metrics are therefore interpreted together with fold-level behavior.

Where appropriate, leave-one-dataset-out or related sensitivity checks are used to identify whether the conclusion depends excessively on a single market.

## Platform parity

For production-relevant modules, TradingView/Pine events are compared bar-by-bar with an independent Python implementation. Timestamp shifts, field mismatches, or look-ahead violations must be resolved before performance conclusions are trusted.

Implementation parity is a correctness requirement, not a performance metric.

## Dependence-aware uncertainty

Financial events are correlated through time and often across assets. Naive independent-sample statistics can therefore overstate confidence. Block-based resampling and other dependence-aware checks are used where appropriate.

## Execution realism

Trading applications are evaluated after confirmation delay, not from visually back-plotted pivot locations. Candidate rules may also be stress-tested for transaction costs, slippage, and degradation of remaining opportunity after confirmation.

Non-directional risk modules are not forced into directional trading metrics. Their evaluation target should match their stated role.

## Decision outcomes

A research module can end in one of three public states:

- **Retained** — the component survived the relevant validation requirements for its stated role.
- **Rejected** — the hypothesis failed one or more required gates and is not promoted.
- **Not validated** — the idea may remain useful for visualization or interpretation, but the evidence does not justify independent trading logic.

The public summary of these outcomes is documented in [`../results/validation_summary.csv`](../results/validation_summary.csv).

## Promotion rule

A feature is promoted only when it provides incremental, stable, out-of-sample value for its stated purpose. Otherwise it is restricted to research interpretation or rejected entirely.

For examples of how this rule affected actual research directions, see [`experiment_history.md`](experiment_history.md).
