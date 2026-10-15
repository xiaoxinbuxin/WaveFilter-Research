# Context for Previously Reported Private-Study Numbers

This page records the limits of claims already present in the public repository. It adds no new private results, formulas, parameters, or datasets. These are **author-reported private-study summaries, not results independently reproducible from this repository**.

## What was already reported

| Previously published statement | Public source | What the source establishes |
|---|---|---|
| High-volatility frequency of 31.2% at baseline and 65.4% after a standard volatility warning, described as a sealed-holdout study | [Earlier README](https://github.com/xiaoxinbuxin/WaveFilter-Research/blob/b44be85e2d4499edc1a7f29963944e9765be7b3b/README.md#selected-results) and [decision summary](validation_summary.csv) | The figures and their reported non-directional interpretation were published; underlying calculations are not available here. |
| Positive lift across all nine evaluated folds | [Earlier README](https://github.com/xiaoxinbuxin/WaveFilter-Research/blob/b44be85e2d4499edc1a7f29963944e9765be7b3b/README.md#selected-results) | A fold-level consistency claim was reported; per-fold counts, values, and dependence are not documented publicly. |

These frequencies are not trade win rates, returns, or profitability estimates. The published summaries do not establish that nine folds are nine independent experiments.

## What cannot be checked from the public record

The existing public summaries do not provide the study-specific sample and event counts, observation dates, exact asset/feed/timeframe coverage, high-volatility target definition, evaluation horizon, baseline sampling rule, fold boundaries, or uncertainty intervals. The general validation documents describe a protocol but do not supply those missing study records.

Consequently, a reader cannot reconstruct the reported frequencies, assess event coverage, calculate sampling uncertainty, or independently verify the sealed-holdout and fold-stability claims. Missing details are left unspecified rather than inferred from chart screenshots or supplied from private research.

## Relationship to the public demo

The [executed synthetic demo](public_demo_results.md) provides inspectable code, sample counts, a defined evaluation target, split checks, and uncertainty output for a separate, generated dataset. Its six-bar target, event settings, and sample size belong only to that demonstration. They must not be used to fill gaps in the private-study description or to validate the reported 31.2% / 65.4% figures.

The README therefore emphasizes research decisions and links here for the previously reported numbers. Any future expansion of the private-study evidence would need an explicitly approved public summary; none is inferred or added by this update.
