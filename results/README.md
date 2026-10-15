# Public Results

This directory separates reproducible synthetic-demo output from author-reported private-research decisions.

## Executed public demo

Start with [the readable results snapshot](public_demo_results.md). Its tables and chart are generated from the public notebook's synthetic data only.

- [Aggregate metrics](public_demo_summary.csv)
- [Bootstrap summary](public_demo_bootstrap.csv)
- [Boundary audit](public_demo_split_audit.csv)
- [Software versions and public-demo settings](public_demo_run.json)
- [Executed notebook](../notebooks/public_demo.ipynb) and [run instructions](../notebooks/README.md)

These artifacts do not reproduce or validate the private WaveFilter model.

## `validation_summary.csv`

The table records previously reported research directions and decisions from private studies. It is a decision record, not an independently reproducible empirical dataset. See [Private-study context](private_study_context.md) for the provenance and missing context of the previously published numerical claims.

| Column | Meaning |
|---|---|
| `module` | High-level research component or hypothesis family |
| `status` | Public decision such as `Retained`, `Rejected`, or `Not validated` |
| `public_result` | Non-proprietary summary of the observed result |
| `notes` | Interpretation boundary or implementation-disclosure note |

## Decision language

### Retained

The author reports that the component survived the relevant research gates and was retained. This status does not mean that those private studies have been independently reproduced here, nor does it imply guaranteed profitability or universal generalization.

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
