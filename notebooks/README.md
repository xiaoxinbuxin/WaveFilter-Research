# Public Notebooks

This directory contains reproducible, non-proprietary demonstrations of the research workflow.

## Included notebook

[`public_demo.ipynb`](public_demo.ipynb) demonstrates, using **synthetic data only**:

- causal event construction without look-ahead
- time-ordered development / holdout splitting
- non-directional volatility-risk evaluation
- block-bootstrap uncertainty analysis
- separation between research evidence and trading claims

The notebook is intentionally illustrative. Its thresholds, synthetic data generator, and event logic are **not** the production indicator and are not calibrated from the private research system.

## Not included

- production indicator formulas
- exact parameterization
- Pine Script source
- private AutoLab implementation
- raw private datasets
- proprietary execution logic

The purpose is to make the **research methodology reproducible** without exposing the private implementation.
