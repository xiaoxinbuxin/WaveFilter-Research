# Development Timeline

This timeline summarizes how WaveFilter changed as I learned more about the weaknesses of each earlier version. It is intentionally high level: the public repository documents the reasoning and validation process, while production formulas, exact parameters, and private research code remain private.

## 1. Starting from familiar oscillators

My first approach combined **SKDJ, RSI, and Stochastic RSI**. I expected agreement between several momentum indicators to reduce false signals and make turning points easier to identify.

The result was cleaner in some places, but the main weakness was **confirmation delay**. By the time several indicators agreed, part of the move had often already happened. Adding more conditions reduced signal frequency, but it did not solve the timing problem.

**What I learned:** more confirmation can reduce noise while still making the signal less useful.

## 2. Adding trend context

I then compared the oscillator behavior with **EMA 21, 55, 100, and 200** to give the signal broader trend context.

This helped explain some countertrend moves, but simply stacking EMA conditions on top of the original oscillators created another version of the same problem: more filtering, fewer signals, and additional lag.

**What I learned:** trend context was useful, but it needed to shape the state representation rather than act as another independent vote.

## 3. SMI / local-range stage

An important intermediate version used a more **SMI / local-range style** representation. It described where price sat inside a recent swing and made short-term movement easy to visualize.

The limitation became clearer during sustained trends. The line could reach extreme zones too easily and did not retain enough memory of persistent directional pressure.

**What I learned:** local position inside a recent range is not the same thing as accumulated directional pressure.

## 4. Moving to a pressure-based wave

I redesigned the core around an **RSI-style directional-pressure representation with accumulated pressure memory**. EMA structure became contextual information rather than another binary confirmation layer.

This was the stage where the project stopped being a combination of standard oscillators and became a separate market-state framework.

The white wave also became the main visual object. I preferred a simple normalized line that summarized pressure rather than several overlapping indicators.

**What I learned:** one coherent state representation was easier to reason about and test than a collection of partially redundant signals.

## 5. Extreme zones and structural reversals

Once the pressure-based wave was working, the overbought and oversold regions became their own research problem.

I did not want an extreme reading to mean an automatic reversal. Strong trends can remain extreme for a long time, so I tested different release, recovery, persistence, and re-entry ideas.

Some versions solved one visual problem but created another. This eventually led to a simpler interpretation: **extreme zones represent strong pressure; they do not by themselves define a structural reversal.**

## 6. Separating the visible wave from the structural state

A major design change was separating the **responsive visible wave** from a more conservative **internal structural state**.

This allowed the visible line to react to changing pressure without forcing every small pullback to become a formal direction change. Structural reversals required stronger accumulated evidence.

This separation also made it possible to study confirmation delay, recovery behavior, and resynchronization without forcing one line to perform two conflicting jobs.

**What I learned:** responsiveness and confirmation are different objectives and should not always be represented by the same state variable.

## 7. Evidence accumulation, recovery, and resynchronization

The next stage focused on what should happen near the center of the oscillator and when the visible line fell behind the pressure it was meant to represent.

A simple zero crossing was too sensitive in choppy periods, so I explored evidence accumulation before formal state changes. I also tested different recovery and resynchronization mechanisms.

Some changes made the chart smoother but increased delay. Others reacted faster but created larger catch-up moves later.

This produced one of the most important lessons in the project:

> **A visually smoother line is not automatically a better model.**

## 8. Testing additional modules

As the core stabilized, I explored additional ideas such as:

- divergence-based interpretation,
- non-directional volatility warnings,
- multi-timeframe context,
- adaptive thresholds,
- faster response and acceleration mechanisms,
- volume-related confirmation.

Several ideas looked promising on selected charts but did not provide stable incremental value when tested more broadly. Some were retained only for a narrower role, while others were rejected.

This was when the project became less about adding features and more about determining which features deserved to remain.

## 9. From chart tuning to a research workflow

Early versions were judged mostly through visual comparison. Over time, I realized that this was not enough because a historical chart is easy to improve after seeing the data.

I therefore moved toward a more formal **Champion / Challenger** process:

1. freeze a stable Champion;
2. test one Challenger idea separately;
3. evaluate it causally from the point where the signal becomes observable;
4. compare behavior across assets and timeframes;
5. freeze important rules before a final holdout;
6. retain failed experiments instead of tuning them until they look successful.

This changed the project from indicator tuning into a repeatable model-development process.

## Current public milestone

The current public research milestone is based on the **v21.8.24** WaveFilter line developed in September 2026.

At that stage, the core wave-state framework remained the retained baseline after additional audit, causal replay, and locked validation. A simplified **single non-directional volatility-warning layer** was retained for its specific role, while several alternative predictive, multi-timeframe, divergence, and faster-response ideas were not promoted when they failed to show sufficiently stable incremental value.

The exact production logic, formulas, thresholds, parameterization, private replay outputs, and Pine Script remain outside this repository.

## What the timeline shows

The development path was not a straight progression toward more complexity. In several cases, the better decision was to remove an idea, simplify a module, or keep two research problems separate.

The main progression was:

```text
indicator combination
        ↓
trend context
        ↓
local-range / SMI representation
        ↓
directional-pressure wave
        ↓
visible wave + structural state
        ↓
evidence / recovery research
        ↓
independent challenger modules
        ↓
Champion / Challenger validation
```

For the narrative version of this process, see [`development_story.md`](development_story.md). For retained and rejected research directions, see [`experiment_history.md`](experiment_history.md).
