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

## Run locally

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter notebook notebooks/public_demo.ipynb
```

For a non-interactive reproducibility check:

```bash
jupyter nbconvert \
  --to notebook \
  --execute notebooks/public_demo.ipynb \
  --output public_demo.executed.ipynb \
  --output-dir /tmp
```

GitHub Actions runs the same public notebook automatically through [`.github/workflows/public-demo.yml`](../.github/workflows/public-demo.yml).

## Not included

- production indicator formulas
- exact parameterization
- Pine Script source
- private AutoLab implementation
- raw private datasets
- proprietary execution logic

The purpose is to make the **research methodology reproducible** without exposing the private implementation.
