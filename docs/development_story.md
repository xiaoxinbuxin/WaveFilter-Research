# Development Story

WaveFilter did not begin as a completely separate indicator. My first approach was to combine indicators I was already familiar with, especially **SKDJ, RSI, and Stochastic RSI**. At that stage, I was mainly trying to improve short-term momentum and turning-point signals. The idea was simple: if several indicators agreed, the combined signal should be more reliable than any one indicator by itself.

That approach was useful as a starting point, but it did not work as well as I expected in practice. The biggest problem was **delay**. SKDJ, RSI, and Stochastic RSI respond to price differently, and waiting for several of them to confirm the same move often meant that part of the move had already happened. Adding more confirmation could reduce some noisy signals, but it also made the output slower and harder to interpret.

I also started comparing those oscillators with trend context from **EMA 21, 55, 100, and 200**. The EMAs were useful for understanding the larger trend, but simply stacking trend filters on top of momentum indicators did not solve the basic problem. More conditions usually meant fewer signals, but not necessarily earlier or better ones.

This was the point where I stopped asking, "Which indicators should I combine?" and started asking a different question: **what information was I actually trying to represent?**

I wanted an indicator that could show directional pressure and changes in market state without reacting to every small fluctuation. At the same time, I did not want to solve the noise problem by adding more and more smoothing, because that would recreate the same lag problem I had with the original indicator combination.

## Moving away from indicator voting

The next stage was to build the logic around the underlying state rather than around agreement between several finished indicators. Instead of treating RSI, SKDJ, or Stochastic RSI as separate votes, I began experimenting with a single wave-style representation that could summarize pressure more directly.

One of the important intermediate versions used a more **SMI / local-range style** idea. It was good at showing where price sat inside a recent swing, but the comparison exposed a deeper problem: during strong trends, the line could reach the extreme zones too easily and did not retain enough memory of sustained directional pressure. A stronger reference behavior showed fewer extreme events and better trend persistence, which made the limitation much clearer.

That mismatch became a turning point. Rather than continuing to tune the local-range oscillator, I moved the core toward an **RSI-based directional-pressure representation with accumulated pressure memory**. The goal was no longer to describe only the current position inside a recent swing. I wanted the line to reflect whether upward or downward pressure had been building over time.

EMA structure was still useful, but I began using it as context for the pressure signal rather than as another independent confirmation layer. This was a major change in the project: the goal was no longer to make several indicators agree, but to build one state representation that already understood both momentum and market context.

## Using trend context without simply adding more lag

Once the pressure-based core was working, I experimented with how much trend information should affect it. I did not want the EMA structure to shift the whole oscillator mechanically or block every countertrend move. That would have made the signal look cleaner while hiding real reversals.

Instead, I gradually treated trend context more like a **gate or weighting condition**. Movement that agreed with the broader structure could be expressed more clearly, ordinary countertrend noise could be reduced, and unusually strong opposing pressure could still pass through.

This was also when the white line became more important to me as the main visual object. I preferred a simple single-line representation rather than several overlapping oscillators. I gradually moved toward a stepped or wave-like line because it made state changes easier to read and kept the chart less crowded.

## Extreme zones became their own design problem

As the white line improved, the overbought and oversold regions became another challenge. I did not want an extreme reading to mean "automatic reversal," because strong trends can remain extreme for a long time.

During development, I saw both failure modes: sometimes the line left an extreme region too quickly, and sometimes it remained there too long. I tried different ideas involving extreme-state tracking, aging, release conditions, recovery behavior, and re-entry control.

Some of those versions became too complicated. They solved one chart problem but introduced another. That eventually pushed me toward a simpler interpretation: an extreme region should represent **strong pressure**, while the decision that a real structural reversal has happened should be handled separately.

That separation became one of the most important ideas in the later design.

## Separating responsiveness from confirmation

One of the hardest trade-offs was **responsiveness versus confirmation**. A line that reacts quickly is useful visually, but if every small movement changes the structural state, it becomes unstable. A very conservative line is more stable, but it can become too late to be useful.

To handle this, I gradually separated the **visible wave** from a more conservative **internal structural state**. The visible white line could release, recover, or react to changing pressure before the underlying structural direction formally changed. A formal reversal required stronger accumulated evidence.

This meant that I no longer had to force one line to do two conflicting jobs at the same time.

The visible line could answer:

> What is happening to pressure right now?

while the internal state could answer:

> Has enough evidence accumulated to call this a real structural change?

This was much more useful than simply making the original oscillator slower or smoother.

## Evidence accumulation and the zero area

Another recurring problem was what should happen near the center of the oscillator. A simple zero crossing can be too sensitive if the line moves back and forth during a choppy period.

I therefore experimented with evidence accumulation before allowing a formal directional change. This helped separate a temporary release in pressure from a stronger reversal. The center of the oscillator became less of a simple on/off boundary and more of a place where the system had to decide whether the opposing move had enough evidence behind it.

This also made the relationship between the visible line and the structural state clearer. The white line could move first, but the internal state did not have to follow immediately.

## Recovery, resynchronization, and the white line

Once the visible and structural states were separated, a new problem appeared: the white line could sometimes fall too far behind the pressure it was supposed to represent. I tested different recovery and resynchronization ideas to reduce that lag.

Some changes helped in one situation but caused large catch-up moves later. Others made the line smoother but delayed important transitions. This became one of the longest-running parts of the project because it was easy to make the line look better without actually making its behavior better.

This led to another lesson that became central to the project:

> **A smoother line is not automatically a better model.**

A modification had to be judged not only by how clean the chart looked, but also by what it did to delay, reversals, extreme behavior, and structural consistency.

## Adding features, then learning to remove them

As the core became more stable, I explored a number of additional ideas. These included divergence-style interpretation, warning logic, volume-related confirmation, multi-timeframe context, adaptive thresholds, and faster response mechanisms.

Some of these ideas looked useful on selected charts. That made them tempting to keep. But broader testing often showed that the apparent improvement was conditional, duplicated information already present in the core, or disappeared when timing and execution assumptions were treated more realistically.

This was when I started to become much more comfortable **removing** features.

Earlier in the project, I often assumed that a more advanced version should contain more logic. Later, I realized that the better version could actually be the simpler one if the extra logic did not add independent value.

## From chart tuning to research testing

At the beginning, I relied heavily on visual comparison. I would change the logic, compare charts, and decide whether the indicator looked more useful.

Over time, that became insufficient. It is very easy to improve a historical chart after seeing the data, especially when many settings and variations are available.

I therefore started treating proposed changes as separate experiments. The stable version became the **Champion**, and new ideas became **Challengers**. Instead of immediately adding a promising feature to the main indicator, I tested it independently.

My evaluation process gradually became more structured:

- use time-ordered data rather than random shuffling,
- evaluate an event from the bar where it actually becomes observable,
- compare behavior across several assets and timeframes,
- check whether an improvement comes from useful information or simply more delay,
- freeze important rules before using a final holdout,
- keep failed experiments in the research record instead of repeatedly tuning them until they look successful.

This changed the way I thought about indicator development. The goal was no longer to make every version look more sophisticated. The goal was to determine whether a change actually added value without creating a larger problem somewhere else.

## Keeping different problems separate

Another lesson was that not every useful idea belongs inside the core wave line.

For example, volatility information is useful, but it answers a different question from directional state. A volatility warning can indicate that future movement may become larger without saying whether price should rise or fall. Keeping those roles separate made the system easier to reason about and easier to test.

I came to the same conclusion with main-chart structure tools. Price structure and execution levels live in price coordinates, while WaveFilter is a normalized sub-chart state representation. I prefer to keep those modules separate rather than forcing everything into one indicator.

## What changed most

Looking back, the biggest change in the project was not one formula or one version. It was the way I approached the problem.

At the beginning, the question was roughly:

> How can I combine SKDJ, RSI, and Stochastic RSI to get a cleaner signal?

Then it became:

> How can I represent directional pressure without relying on several delayed confirmations?

Later, it became:

> How can I let the visible wave stay responsive while requiring stronger evidence for a real structural reversal?

And eventually:

> How can I test whether a change is genuinely better instead of only looking better on the chart?

That progression is what turned the project from an indicator-combination experiment into the current WaveFilter research framework.

The main lesson I took from the project is that **more indicators, more confirmation, more smoothing, and more complexity do not automatically create a better signal**. The difficult part is balancing responsiveness, stability, trend context, and causality—and being willing to reject an idea when the evidence does not support it.

This document describes the development process at a high level. The production formulas, exact parameterization, private implementation, and private research data remain outside the public repository.