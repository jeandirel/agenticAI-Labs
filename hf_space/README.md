---
title: Agentic AI Lab 4
emoji: 🛡️
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
---

# Agentic AI Lab 4 - FastAPI Production Agent

This Space exposes a production-oriented **FastAPI endpoint** around an agent
handler function.

The project includes:

- `agent_service.py`: handler function, tools, guardrails and monitoring;
- `app_fastapi.py`: FastAPI API;
- `eval_agent.py`: evaluation harness;
- `llm_helpers.py`: provider-agnostic LLM helper layer;
- `Dockerfile`: Hugging Face Spaces Docker deployment.

## API

Health check:

```http
GET /health
```

Agent endpoint:

```http
POST /agent
Content-Type: application/json

{"query": "Explique le risque de prompt injection en production"}
```

Interactive API docs:

```text
/docs
```

## Secrets / Variables

Set these in Hugging Face Spaces settings:

- `LLM_PROVIDER`: `anthropic`
- `LLM_MODEL`: `claude-sonnet-4-6`
- `ANTHROPIC_API_KEY`: secret

Without secrets, set `LLM_PROVIDER=mock` or `FORCE_MOCK=1` for offline behavior.

## Local test

```bash
python agent_service.py
python eval_agent.py
uvicorn app_fastapi:app --host 0.0.0.0 --port 7860
```
