# I-Only Debate System — Codex

Prototype service stack:

- **Backend:** Python + FastAPI
- **Agents:** LLM-driven (OpenAI / local model)
- **DB:** SQLite (upgrade later)
- **Scheduler:** Async loop
- **Frontend:** Read-only (later)

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Structure

- `app/main.py`: FastAPI app + lifespan hooks
- `app/scheduler.py`: async scheduler loop
- `app/db.py`: SQLite initialization
- `app/agents.py`: LLM agent placeholders + personal agent profile
- `app/api.py`: API routes
