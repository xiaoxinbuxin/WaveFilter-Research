# Experiment History

This file summarizes selected research directions at a non-proprietary level. It intentionally excludes production formulas, exact parameter values, private event-level diagnostics, and execution-specific rules.

| Research direction | Outcome | Interpretation |
|---|---|---|
| Core wave-state filtering | Retained | Stable production Champion after iterative validation |
| Evidence acceleration | Rejected | Faster response increased short-lived reversals or reduced stability |
| Near-threshold acceleration | Rejected | No safe cross-dataset candidate |
| Same-side micro-pullback suppression | Rejected | Many apparent visual pullbacks carried genuine state information |
| Adaptive zero-axis thresholding | Rejected | Conditional lowering/raising did not produce robust incremental value |
| Single-timeframe decay warning | Rejected | Implementation parity was verified, but predictive utility did not pass production gates |
| Multi-timeframe automatic filtering | Rejected | Some development-set separation existed, but executable or cost-adjusted holdout value was insufficient |
| Divergence as a trading signal | Not validated | Selected development results did not survive sealed-holdout robustness requirements |
| Non-directional volatility warning | Retained | Demonstrated reproducible information about future volatility risk |

## How to interpret the table

**Retained** means the component survived the relevant validation requirements for its stated role. It does not imply universal market validity or guaranteed profitability.

**Rejected** means the hypothesis failed one or more required research gates and was not added to the validated production logic.

**Not validated** means the idea may still be useful for visual interpretation or further research, but the evidence did not justify promoting it to independent trading logic.

## Why negative results are preserved

A failed experiment is not removed from the research record. Negative results help:

- prevent repeated testing of already weak hypothesis families;
- document why the production system remains simpler than the full set of ideas explored;
- distinguish research discipline from feature accumulation;
- make the public portfolio more representative of the actual model-selection process.

The compact machine-readable public summary is available in [`../results/validation_summary.csv`](../results/validation_summary.csv). The decision framework is documented in [`validation_framework.md`](validation_framework.md).
