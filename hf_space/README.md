---
title: Agentic AI Lab 4
emoji: 🛡️
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 6.19.0
app_file: app.py
pinned: false
---

# Agentic AI Lab 4 - Production & Safety

This Space packages a small production-oriented agent with:

- safe tool use through an allow-list;
- course search and safe arithmetic tools;
- input validation and prompt-injection filtering;
- output validation;
- traces, latency, LLM calls, token usage and estimated cost;
- an evaluation script.

## Secrets

Set these in Hugging Face Spaces settings:

- `LLM_PROVIDER`: `openai`, `anthropic`, `mistral`, `google` or `mock`
- provider key as a secret, for example `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`
- optional `LLM_MODEL`

Without secrets, set `LLM_PROVIDER=mock` or `FORCE_MOCK=1` for offline behavior.

## Local test

```bash
python agent_service.py
python eval_agent.py
python app.py
```
