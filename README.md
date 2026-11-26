# LENA

LENA (Learning Experience & Nurturing Agent) is a planned AI-powered learning
assistant. Its Learning, Quiz, and Recommendation agents will eventually be
coordinated with LangGraph.

The prototype includes a student dashboard and a FastAPI backend. Agents,
MongoDB connection, and LLM integration have not been implemented.

## Structure

- `frontend/`: Next.js student dashboard.
- `backend/app/`: FastAPI entry point and directories for future API, agents,
  orchestration, tools, database, schemas, and core code.
- `backend/requirements.txt`: initial Python dependencies.
- `data/seed/`: fictional JSON seed data; `docs/` is reserved for documentation.
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

The dashboard API reads the synthetic JSON files from `data/seed/`.

## Run the dashboard

With the backend running, from `frontend/`:

```sh
npm install
npm run dev
```

Open `http://localhost:3000` and enter a student ID from the seed data.
Requests are proxied to `http://127.0.0.1:8000`; set `BACKEND_URL` before
starting Next.js if the backend runs elsewhere. Performance combines published
marks by total marks; topic-level insights are unavailable from the current API.
This prototype has no authentication and is intended for fictional data only.

## Seed document schemas

`backend/app/schemas/` contains Pydantic models for the ten seed collections.
They validate seed document shapes and values; they are not yet API request or
response models and do not connect to MongoDB. Existing `_id` strings map to the
Python attribute `id`; serialize with `model_dump(by_alias=True)` to use `_id`.
Assessment results use `result_id` instead and do not invent an `_id` field.

Dates and timestamps are parsed into Python `date` and `datetime` objects. For
JSON-compatible seed documents, use `model_dump(mode="json", by_alias=True,
exclude_unset=True)`. MongoDB integration must explicitly choose a storage
representation for date-only values and handle MongoDB-generated IDs for
assessment results; neither is configured here.

To validate the schemas against the seed files:

```sh
cd backend
python -m unittest discover -s tests
```
