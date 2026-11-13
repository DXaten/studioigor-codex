# Game design and playtests

## Concept

Turn the brief into a small playable promise: who the player is, what they do repeatedly, what resists them, and why another attempt is attractive. Capture the core loop at roughly 30 seconds, a session loop, and longer progression only if the game needs it. State scope in countable terms: stages, enemy types, modes, and target session length.

Offer 2–4 signature ideas that add a memorable interaction without changing the genre. Show the cost and effect of each. Record accepted ideas in `DESIGN.md`; leave rejected ones out of the build. An idea should be demonstrated in play before being treated as a pillar.

## Mechanic gym

For each core mechanic, write a short hypothesis, controls, tunable values, and observable acceptance conditions. Make a small test route or scene with restart, visible debug information, and controls for changing feel when practical. Examples: a track with three turns for drifting; a target room for combat; a short sequence of gaps for jumping. Include input latency and frame-rate behavior where they matter.

Play or automate the gym, inspect a capture, and invite user play. Record the date, build or commit, what happened, and one actionable next change in `PLAYTESTS.md`. If the mechanic works but feels dull, change the mechanic before building content around it. Mark it integrated only after the core interaction is satisfying enough for the intended scope.

## Vertical slice and content

The slice should show the game's actual visual and audio quality, including a clear beginning, meaningful challenge, feedback, result, and replay path. A polished menu hiding an empty prototype is not a slice.

Add content in batches small enough to play through. Compare neighboring levels on at least two useful dimensions such as challenge, timing, layout, enemy mix, story beat, or reward. Use data files when repeating content would otherwise duplicate code.

## Scope decisions

When time is constrained, keep the 30-second action loop, goal, fail state, restart, and a consistent visual style. Reduce the number of levels and secondary systems first. Record a cut explicitly so a later session does not silently restore it.
