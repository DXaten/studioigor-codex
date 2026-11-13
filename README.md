# studioigor for Codex

A browser-game development skill adapted for **OpenAI Codex** from [studioigor/studioigor-skill](https://github.com/studioigor/studioigor-skill) by **studioigor**.

The original skill introduced the guided game-studio workflow: idea interview, visual references, mechanic test scenes, a playable vertical slice, content, polish, and release. This repository rewrites that workflow for Codex and concentrates on web games. It uses `SKILL.md`, Codex-readable `AGENTS.md`, a project-local journal, browser captures, and Codex's available tools instead of Claude Code commands and `CronCreate`.

## Install

Clone this repository and copy the **whole folder** into a Codex skill directory. For a personal installation, use `~/.agents/skills/studioigor-codex/`; for one project, use `<project>/.agents/skills/studioigor-codex/`. Restart the Codex task or open a new task so the skill is discovered.

```bash
git clone https://github.com/DXaten/studioigor-codex.git
mkdir -p ~/.agents/skills/studioigor-codex
cp -R studioigor-codex/. ~/.agents/skills/studioigor-codex/
```

Then ask Codex: **“Use $studioigor-codex to make a browser game about …”** or **“Use $studioigor-codex to continue this web game.”** The skill can also be selected automatically for a browser-game development request.

## What changed for Codex

- Replaced Claude-specific project instructions and agent files with a compact `AGENTS.md` template.
- Replaced `AskUserQuestion` and Claude MCP assumptions with Codex's available user-input, browser, research, image, and code tools.
- Replaced the Claude autopilot runner with a small project-local progress journal. Scheduled work is optional and uses Codex automations only when requested.
- Focused the pipeline on browser games, from first playable prototype to web release.
- Kept and adapted the upstream reference-board scripts, and included its Playwright capture helper.

## Requirements

Python 3.9+ and git for the journal and reference-board helpers. The capture helper needs Node.js, Playwright, and Chromium in the game project. A browser game may need additional dependencies based on its chosen stack.

## Credit and license

Original work: [studioigor/studioigor-skill](https://github.com/studioigor/studioigor-skill), copyright © 2026 studioigor, MIT License. This Codex adaptation is based on upstream commit `14d9d09b9a36371a9f038cfe02d882ff8b11dc19` (2026-09-28). The retained MIT [LICENSE](LICENSE) notice applies to the upstream portions. Adaptation by the maintainers of this repository.

This is a community adaptation and is not an official OpenAI or studioigor release.
