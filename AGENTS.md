---
title: "rungard-demo-service — brief for agents"
status: approved
owner: Product
author: Georgian Dinca
created: 2026-11-14
classification: public
last-reviewed: 2026-11-14
ai-trust: authoritative
---

# AGENTS.md — rungard-demo-service

A small, synthetic Python service that Rungard's agents work on in demonstrations. It holds no real data and serves nobody. Its code has known bugs on purpose: each is a task an agent can be given.

## Rules for an agent working here

- Change only what the task asks for. Keep each change small and readable.
- Every behaviour you fix gets a test in a `test_*.py` file next to the code, using `unittest` from the standard library. No third-party packages.
- Code runs on Python 3.12.
- The gates must pass before a change is proposed:
  - `sh scripts/gates/tests.sh` runs the test suite.
  - `sh scripts/gates/lint.sh` checks that every file compiles and the change has no whitespace errors.
- A change reaches `main` only through a pull request, reviewed by a person.
- Never add secrets, credentials or personal data.
