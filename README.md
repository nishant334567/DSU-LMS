# LENA

LENA (Learning Experience & Nurturing Agent) is a planned AI-powered learning
assistant. Its Learning, Quiz, and Recommendation agents will eventually be
coordinated with LangGraph.

This initial scaffold contains a minimal FastAPI backend. The Next.js frontend,
agents, MongoDB connection, and LLM integration have not been implemented.

## Structure

- `frontend/`: reserved for the Next.js frontend.
- `backend/app/`: FastAPI entry point and directories for future API, agents,
  orchestration, tools, database, schemas, and core code.
- `backend/requirements.txt`: initial Python dependencies.
- `data/` and `docs/`: reserved for project data and documentation.
- `.env.example`: configuration placeholders, not loaded by the application yet.

Empty directories exist locally but are not tracked by Git until files are added.

## Run the backend

From the project root, using Python 3.12:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r backend/requirements.txt
cd backend
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/health`.
