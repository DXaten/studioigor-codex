---
name: studioigor-codex
description: "Build or continue a browser game with Codex through short, playable iterations: concept, visual direction, web stack, mechanic gyms, vertical slice, content, polish, and release. Use for requests to make or finish a web game; not for a single isolated asset or routine bug fix."
---

# studioigor for Codex — browser game studio

Adapted from [studioigor/studioigor-skill](https://github.com/studioigor/studioigor-skill) for OpenAI Codex. The original author is studioigor. This edition focuses on browser games and uses Codex project guidance, tools, and approval boundaries.

## Start or resume

1. Read the user's brief and the existing repository before choosing a stack or changing files. If `.studioigor/state.json` exists, run `python3 <skill>/scripts/studio.py status` and read the relevant `.studioigor/` records. Do not ask again about recorded decisions.
2. For a new game, initialize its chosen project folder with `python3 <skill>/scripts/studio.py init <folder> --name "<working title>"`. This creates project-local records, `AGENTS.md`, and git if absent. Respect existing files. If the user named a folder, use it; otherwise prefer the current empty workspace.
3. Work through the phases below at the pace of the user's request. A clear, detailed brief may let you make several decisions without an interview. A request for a prototype need not wait for a full release plan.
4. Record meaningful choices with `studio.py decide "..." --by user|agent --why "..."`, progress with `studio.py note "done" "next"`, and completed phases with `studio.py phase N --evidence "..."`. The phase number must be current. Keep the records brief and useful to a new Codex session.
5. If playtesting changes an earlier decision, run `studio.py reopen N` and revise that phase. Previous notes stay available in the journal.

`<skill>` is the directory containing this file. Project state is in `<game>/.studioigor/`.

## How to work with the user

- The user directs taste, scope, and release destination. Infer ordinary implementation choices from the brief and evidence. Ask concise questions only when a decision materially affects the game; offer a recommended answer. Use the available user-input tool when helpful, or ask in conversation if none exists. Do not depend on Claude Code's `AskUserQuestion` or its option preview format.
- Show a playable build or a capture at the first useful opportunity. A working engine scaffold alone is not a playtest. Ask what feels fun, frustrating, slow, confusing, or visually wrong, then tune the actual game.
- If the user explicitly delegates creative choices, choose and record them. Review the result with the user later. Do not interpret ordinary silence as delegation.
- Codex may use available browser, image, code, and research tools. Inspect the current tool list; do not assume a particular MCP server or plugin exists. Use official current documentation for changing engine, browser, store, and deployment facts.
- Preserve existing project conventions. If the user asks to continue a game, inspect code and artifacts before adding project records. Avoid replacing the game's build system merely to fit this skill.

## The production loop

| Phase | Deliverable and evidence |
| --- | --- |
| 0. Start | Project folder, git, recorded brief and next step. |
| 1. Idea | A compact pitch, player fantasy, 30-second action loop, win/loss, scope, and 2–4 distinctive mechanic ideas in `CONCEPT.md` and `DESIGN.md`. User decides among ideas that change the brief. |
| 2. Style | 2–4 visual directions with actual references, then `ART_BIBLE.md`: palette, shapes, lighting, interface, and visual rules. Use `board.py`/`refs.py` when a local board helps. Credit sources and note reuse rights in `ASSETS.md`. |
| 3. Web stack | Compare a small number of suitable approaches for this game (for example Canvas, DOM/CSS, Phaser, PixiJS, Three.js, or Godot web export). Choose based on required mechanics, target devices, performance, and the existing code. Record the version and run/build commands in `TECH.md`. |
| 4. Playable prototype | Make the core action playable in a browser as soon as possible. Include input, feedback, a goal, a failure state, and restart. Run it and inspect a real frame. |
| 5. Mechanics | Build one mechanic at a time in an isolated gym or debug route with adjustable parameters. Capture it, play it, tune it, and only then integrate it. Keep each mechanic's acceptance criteria in `DESIGN.md` and feedback in `PLAYTESTS.md`. |
| 6. Vertical slice | Connect menu → game → result → replay, with a meaningful first minute, sound, coherent visuals, and a complete short loop. Let the user play. |
| 7. Content | Add levels, enemies, tracks, dialogue, or progression as data where useful. Make adjacent units meaningfully different. Play from start to end. |
| 8. Polish | Improve the largest observed problem per pass: responsiveness, readability, sound, accessibility, mobile controls, loading, or performance. Test the worst scene on target devices. |
| 9. Release | Produce a reproducible build, credits and licenses, and deployment instructions. Publish only when the user requests it. |

Read [game design](references/game-design.md) for concept, mechanics, playtests, and scope. Read [web production](references/web-production.md) when choosing the stack, implementing, capturing, or preparing release. Read [visual references](references/visual-references.md) for style boards and asset rights.

## Codex-specific operating rules

- A new game's `AGENTS.md` is durable project guidance; keep taste and progress in `.studioigor/`. Do not create `.claude/agents`, call `claude mcp`, or rely on `CronCreate`. Use Codex tools and capabilities actually available in the current session.
- This skill does not require subagents. If the user or current instructions explicitly call for delegation, give agents independent file ownership and review their work before integration.
- Do not turn “make the game yourself” into an unattended schedule by default. Work in the current task. If the user specifically requests recurring or later work, use the Codex automation capability available in the app, with a concrete goal and stopping condition.
- Commit coherent milestones when git is available and the working tree is suitable. Do not overwrite unrelated changes. Pushing code, deploying, paying for services, or publishing the game follows the user's actual authorization.
- Prioritize gameplay over extra process. Add tests for failure modes that are costly or hard to spot manually, such as saves, scoring, and core rules. Verify the experience by running the game and inspecting output.

## Optional helpers

- `scripts/board.py` and `scripts/refs.py` are adapted from the original project for local reference boards. Run each with `--help` before use. Network sources and image reuse terms vary.
- `scripts/templates/capture.mjs` is the upstream Playwright capture helper. Copy it into the game project when repeatable browser captures are useful; it requires local Playwright and Chromium. See its header for CLI options.
- `scripts/studio.py` is this Codex edition's small, standard-library-only project journal. It is not an autopilot runner.
