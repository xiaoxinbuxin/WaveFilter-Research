# Architecture

## Scope

WaveFilter is organized as a market-state research system rather than a single buy/sell rule. The public architecture documents responsibilities and interfaces while intentionally omitting proprietary formulas and calibrated parameter values.

## Conceptual pipeline

```text
Market data
   ↓
Momentum / structural inputs
   ↓
Robust normalization
   ↓
Evidence accumulation
   ↓
Internal structural state
   ↓
Visible wave-state representation
   ↓
Independent research modules
```

## Separation of responsibilities

### Core wave-state layer

The core layer represents directional market pressure and structural transition state. Its design separates the visible output from a more conservative internal state so that visual responsiveness does not automatically force structural reversals.

### Volatility-risk layer

Volatility warnings are explicitly non-directional. They answer whether the market has entered a higher-volatility regime, not whether price should move up or down.

### Experimental modules

Divergence, multi-timeframe context, acceleration, adaptive thresholds, and other extensions are evaluated as independent challengers. They are not promoted into production merely because they improve selected historical examples.

## Main-chart vs. sub-chart separation

The WaveFilter itself is a sub-chart state indicator. Price-coordinate tools such as moving averages, price channels, support/resistance, or price-structure overlays belong to separate main-chart modules. The research process allows logical interaction between modules while keeping their visualization and coordinate systems separate.

## Production governance

A stable production version acts as the **Champion**. New ideas are implemented as **Challengers** and must pass the same validation protocol before they are allowed to replace or modify the Champion.
