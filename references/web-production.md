# Web game production

## Choose an implementation

Inspect the existing repository first. For a new game, choose the simplest web technology that supports the intended play: DOM/CSS for interface-heavy or turn-based play, Canvas/Phaser/PixiJS for 2D real-time play, Three.js/WebGL for 3D, or a web export from an existing engine project. Compare current browser support, mobile input, asset size, and deployment limits using up-to-date official docs before committing to a new dependency.

Record exact development, build, test, and capture commands in `.studioigor/TECH.md`. Keep game state separate from drawing and UI where this makes deterministic replay and tuning easier. Use a fixed simulation step for timing-sensitive play. Expose important tuning values in data or a debug panel. Save formats need a version if player progress persists across releases.

## Verify what the player sees

Run the game locally. Inspect actual browser output at desktop and the intended mobile size. Try keyboard, pointer, touch, and gamepad only where the design promises them. Check start, pause, loss, win, restart, audio unlock, focus loss, and a full playthrough. A successful build command does not establish that gameplay works.

For repeatable capture, copy `scripts/templates/capture.mjs` into the game repository and install Playwright locally. It can serve a static build or capture a running URL, run scripted inputs, save frames, a contact sheet, and metrics. Use `node capture.mjs --dir dist --out .studioigor/captures/slice` for a static build. View at least one resulting image; inspect console errors and metrics. The script is optional when an existing browser tool provides equivalent evidence.

Use targeted automated tests for saves, scoring, progression, and hard-to-see regressions. Keep ordinary visual and feel checks in playtests and captures.

## Ship

Build from a clean state with recorded commands. Check loading time, asset size, audio behavior, credits, third-party licenses, keyboard and touch usability, and error behavior when storage or network fails. Use current documentation for the target host or portal. Keep credentials outside the repository. Publication requires the user's requested destination and authorization; produce a ready build and release notes before that step.
