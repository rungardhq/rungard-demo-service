---
title: "rungard-demo-service"
status: approved
owner: Product
author: Georgian Dinca
created: 2026-11-14
classification: public
last-reviewed: 2026-11-14
ai-trust: working
---

# rungard-demo-service

A small, synthetic Python service for demonstrating [Rungard](https://app.rungard.ai), an operations control plane for engineering agents. Its code has known bugs on purpose, for an agent to fix under Rungard's control.

- `pagination.py` splits a list into numbered pages.
- `projects.py` answers `GET /projects/<id>`.

Run the gates the way the agent does:

    sh scripts/gates/tests.sh
    sh scripts/gates/lint.sh

See [AGENTS.md](./AGENTS.md) for the rules an agent follows here.
