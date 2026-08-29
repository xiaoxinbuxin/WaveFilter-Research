# Development Story

WaveFilter did not begin as a completely separate indicator. My first approach was to combine indicators I was already familiar with, especially **SKDJ, RSI, and Stochastic RSI**. The idea was straightforward: if several momentum indicators pointed in the same direction, the combined signal should be more reliable than any one indicator by itself.

That approach was useful as a starting point, but it did not work as well as I expected in practice. The biggest problem was **delay**. SKDJ, RSI, and Stochastic RSI each respond to price in slightly different ways, and waiting for several of them to agree often meant that part of the move had already happened. Adding more confirmation could reduce some noisy signals, but it also made the output slower and harder to interpret.

This was the point where I stopped asking, "Which indicators should I combine?" and started asking a different question: **what information was I actually trying to represent?**

I wanted an indicator that could show directional pressure and changes in market state without reacting to every small fluctuation. At the same time, I did not want to solve the noise problem simply by adding more smoothing, because that would recreate the same lag problem I had with the original indicator combination.

## Moving away from indicator voting

The next stage was to build the logic around the underlying state rather than around agreement between several finished indicators. Instead of treating RSI, SKDJ, or Stochastic RSI as separate votes, I began experimenting with a pressure representation and with rules for deciding when a move should count as a meaningful state change.

This changed the project substantially. The indicator was no longer just a collection of familiar oscillators. It became a separate system with its own internal state and transition logic.

One of the main design problems was the trade-off between **responsiveness and confirmation**. A line that reacts quickly is useful visually, but if every small movement changes the structural state, it becomes unstable. A very conservative line is more stable, but it can become too late to be useful.

To handle this, I gradually separated the **visible wave** from a more conservative **internal structural state**. The visible line could respond to changing pressure, while a formal structural reversal required stronger accumulated evidence. This made it possible to improve responsiveness without treating every visual pullback as a full reversal.

## Learning that smoother is not always better

A large part of the development process involved trying to improve the white wave line. Some modifications made the chart look cleaner or smoother at first, but they also introduced new problems. A smoother path could reduce one-bar jumps while increasing delay. A faster recovery rule could improve one section of the chart while creating larger catch-up moves later.

This became an important lesson for the project: **a visually better line is not automatically a better model**.

As the project developed, I started paying more attention to questions such as:

- Did a change reduce noise, or did it only delay the same movement?
- Did a faster response create more false reversals?
- Did an improvement still work on another asset or timeframe?
- Was a result still present after realistic confirmation delay?
- Did a new feature add information, or was it mostly duplicating something already in the core system?

Several ideas were removed for exactly these reasons. Some looked convincing on selected charts but did not remain useful when tested more broadly.

## From chart tuning to research testing

Early in the project, I relied much more on visual comparison. I would change the logic, compare charts, and decide whether the indicator looked more useful.

Over time, that became insufficient. It is easy to improve a chart after seeing the data, especially when many parameters or variations are available. I therefore started treating each proposed change as a separate experiment.

The stable version became the **Champion**, and new ideas became **Challengers**. Instead of immediately adding a promising feature to the main indicator, I tested it independently. Development data was used first, and important candidates were evaluated with time-ordered validation and holdout rules. I also began keeping negative results instead of repeatedly returning to ideas that had already failed.

This changed the way I thought about development. The goal was no longer to make every new version look more sophisticated. The goal was to determine whether a change actually added value without creating a larger problem somewhere else.

## Keeping different problems separate

Another lesson was that not every useful idea belongs inside the core wave line.

For example, volatility information is useful, but it answers a different question from directional state. A volatility warning can indicate that future movement may become larger without saying whether price should move up or down. Keeping these roles separate made the system easier to reason about and easier to test.

The same idea applies to main-chart structure tools and sub-chart state information. I prefer to keep them as separate modules rather than forcing every feature into one indicator.

## What changed most

Looking back, the biggest change in the project was not one particular formula. It was the way I approached indicator design.

At the beginning, the question was roughly:

> How can I combine SKDJ, RSI, and Stochastic RSI to get a cleaner signal?

Later, the question became:

> How can I build a market-state filter that responds early enough to be useful, remains stable around short-lived noise, and can be tested without relying only on how the chart looks?

That shift led to the current WaveFilter research framework.

The project is still intentionally conservative about what is kept. Some experiments improved individual examples but failed broader tests, so they were rejected. I now consider that part of the result rather than a failure of the development process.

The main lesson I took from the project is that **more indicators, more confirmation, and more complexity do not automatically create a better signal**. The difficult part is balancing responsiveness, stability, and causality—and being willing to remove an idea when the evidence does not support it.

This document describes the development process at a high level. The production formulas, exact parameterization, and private implementation remain outside the public repository.