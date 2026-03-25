# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the projects

**Python Tic Tac Toe:**
```bash
python tictactoe.py
```

**Browser Tic Tac Toe:**
Open `tictactoe.html` directly in any web browser — no build step or server needed.

## Repository structure

This is a small, multi-language learning/practice project. There is no build system, package manager, or test suite.

- `tictactoe.py` — terminal two-player game; pure Python stdlib, no dependencies
- `tictactoe.html` — single-file browser game; vanilla HTML/CSS/JS, no frameworks or bundlers
- `hello.md` — scratch notes file

## Git workflow

- Remote: `https://github.com/1234marshall-stack/git-practice`
- Branch: `main`
- **After every change: stage, commit, and push immediately** — this keeps GitHub in sync and ensures no work is lost
- Commit messages should be concise and descriptive (imperative mood, present tense)
- Do **not** embed credentials in the remote URL — use the credential manager or a separate auth mechanism
- `.claude/` is gitignored and should never be committed

## Architecture notes

Both Tic Tac Toe implementations share the same game logic structure:

- A flat 9-element array represents the board (indices 0–8)
- Win detection checks 8 hard-coded winning combinations
- The Python version is terminal-based with a game loop; the HTML version is event-driven (click handlers update DOM state directly)
- Score tracking persists across rounds in both versions (in-memory only)
