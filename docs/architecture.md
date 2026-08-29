# Architecture

## Scope

WaveFilter is organized as a market-state research system rather than a single buy/sell rule. The public architecture documents responsibilities and interfaces while intentionally omitting proprietary formulas and calibrated parameter values.

![WaveFilter public research architecture](../figures/research_architecture.svg)

## Design principles

The architecture follows four public design principles:

1. **Separate state estimation from trading claims.** A market-state representation can be useful even when it is not an executable strategy.
2. **Separate visible responsiveness from structural confirmation.** The visual state can react without automatically forcing a formal structural reversal.
3. **Keep challengers modular.** Experimental modules are evaluated independently so failed ideas can be removed without destabilizing the core.
4. **Preserve causal observability.** Events are evaluated from the time they become knowable, not from historical locations to which they may later be plotted.

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

WaveFilter itself is a **sub-chart state indicator**. It expresses normalized market pressure, state transitions, extreme conditions, and volatility-risk context.

Price-coordinate tools belong to separate main-chart modules. Examples include moving averages, price channels, support and resistance, price-structure overlays, and execution levels.

The research system may combine information logically across modules, but the visualization and coordinate systems remain separated. This prevents a normalized state oscillator from being visually or conceptually mixed with price-coordinate overlays.

## Modular challenger design

A challenger may consume the core state as contextual information, but it is evaluated independently:

```text
Core state representation
        ↓
Independent challenger
        ↓
Separate validation decision
```

rather than:

```text
Core + every new feature
        ↓
Monolithic indicator
```

This makes it possible to reject a divergence, acceleration, or multi-timeframe extension without rewriting the validated core.

## Production governance

A stable production version acts as the **Champion**. New ideas are implemented as **Challengers** and must pass the same validation protocol before they are allowed to replace or modify the Champion.

The evaluation pipeline includes development-only diagnostics, time-ordered validation, sealed holdouts, implementation-parity checks, dependence-aware stability analysis, and cost/delay stress tests where relevant.

## Public disclosure boundary

This architecture communicates **responsibilities and research interfaces rather than implementation details**. The public repository does not contain the production Pine source, calibrated parameter values, private AutoLab code, or execution-specific rules.

For the experimental process, continue with [`methodology.md`](methodology.md). For promotion and rejection rules, see [`validation_framework.md`](validation_framework.md).
