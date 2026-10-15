# Public Notebooks

This directory contains reproducible, non-proprietary demonstrations of the research workflow.

## Included notebook

Open the [executed results snapshot](../results/public_demo_results.md) for a readable table, uncertainty interval, boundary audit, and chart. The notebook itself contains saved outputs. The exact software versions used for that snapshot are recorded in [public_demo_run.json](../results/public_demo_run.json).

[`public_demo.ipynb`](public_demo.ipynb) demonstrates, using **synthetic data only**:

- causal event construction without look-ahead
- complete six-bar future labels and purged chronological development / holdout splitting
- non-directional volatility-risk evaluation
- block-bootstrap uncertainty analysis
- separation between research evidence and trading claims

The notebook is intentionally illustrative. Its thresholds, synthetic data generator, and event logic are **not** the production indicator and are not calibrated from the private research system.

Its results also do not reproduce the [previously reported private-study statistics](../results/private_study_context.md). The original public-demo event settings and seeds are unchanged; negative or uncertain outcomes are retained.

## Run locally

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter notebook notebooks/public_demo.ipynb
```

To regenerate and save the notebook outputs and public snapshot from the repository root:

```bash
jupyter nbconvert \
  --to notebook \
  --execute notebooks/public_demo.ipynb \
  --inplace \
  --ExecutePreprocessor.timeout=180
```

The final cell refreshes `results/public_demo_results.md`, three aggregate CSV tables, `results/public_demo_run.json`, and `figures/public_demo_synthetic.png`. It reads no private files. These outputs contain only synthetic-demo results and public-demo settings. Library versions are recorded on each run; the requirements specify supported ranges rather than a complete environment lock.

Run the boundary regression checks with:

```bash
python -m unittest discover -s tests -v
```

The tests execute the notebook's actual labeling and split cells. They check missing-history labels, incomplete future windows, development labels crossing into holdout, target alignment, and split validity. GitHub Actions runs these tests, executes the entire notebook, and checks the regenerated aggregate tables against the saved snapshot through [`.github/workflows/public-demo.yml`](../.github/workflows/public-demo.yml).

## Interpretation

The event becomes observable at the current bar close. The evaluation target uses the next six bars; it is not an input. Development rows whose labels reach holdout are purged, while holdout features may use already observed history. This is a demonstration of a holdout protocol on previously public synthetic data, not a newly sealed study.

The baseline includes all eligible bars within the same split. The block-bootstrap interval is illustrative and conditional on this sample and fixed procedure; its positive-resample fraction is not a p-value or a posterior probability. The snapshot reports the outcome without selecting parameters to improve holdout performance.

## Not included

- production indicator formulas
- exact parameterization
- Pine Script source
- private AutoLab implementation
- raw private datasets
- proprietary execution logic

The purpose is to make the **research methodology reproducible** without exposing the private implementation.
