# Public Results

This directory contains compact, non-proprietary research summaries intended for portfolio review and reproducibility checks.

## `validation_summary.csv`

The table records selected research directions and their public disposition.

| Column | Meaning |
|---|---|
| `module` | High-level research component or hypothesis family |
| `status` | Public decision such as `Retained`, `Rejected`, or `Not validated` |
| `public_result` | Non-proprietary summary of the observed result |
| `notes` | Interpretation boundary or implementation-disclosure note |

## Decision language

### Retained

The component survived the relevant research gates and remains part of the validated research framework. `Retained` does not imply guaranteed profitability or universal generalization.

### Rejected

The hypothesis failed one or more pre-specified requirements such as stability, causal validity, execution realism, or out-of-sample robustness. Rejected results are preserved to reduce repeated overfitting and cherry-picking.

### Not validated

The idea may remain useful for visualization or research interpretation, but the available evidence did not justify promoting it to independent trading logic.

## Disclosure boundary

The public results deliberately omit:

- exact production formulas
- calibrated parameter values
- private event-level diagnostics
- raw private datasets
- private AutoLab implementation
- execution-specific trading rules

For research design, see [`../docs/methodology.md`](../docs/methodology.md). For the validation protocol, see [`../docs/validation_framework.md`](../docs/validation_framework.md).
