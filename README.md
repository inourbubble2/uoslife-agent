# UOSLIFE Agent

RAG-based AI Agent for UOSLIFE.

## Tech Stack

- **Language**: Python 3.14
- **Framework**: FastAPI
- **Agent**: LangGraph 1.0.5, LangChain 1.2.0
- **Manager**: uv
- **DB**: PostgreSQL (SQLAlchemy + asyncpg)

## Setup

### 1. Install Dependencies
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies
uv sync --all-extras
```

### 2. Configure Environment
Copy `.env.example` to `.env`.
```bash
cp .env.example .env
```

### 3. Setup Pre-commit
```bash
uv run pre-commit install
```

### 4. Run Local Server
```bash
uv run uvicorn app.main:app --reload
```

### 5. Database Migration (Alembic)
> **Note:** Migrations are applied **ONLY** to the **Agent Database**. The Source Database is read-only and managed separately.

To manage database schema changes, use the following commands:

```bash
# Generate a new migration file (after modifying models)
uv run alembic revision --autogenerate -m "description_of_changes"

# Apply migrations to the database
uv run alembic upgrade head
```

#### Docker Behavior
When running via Docker (e.g., `docker run` or `docker compose`), the container is configured to **automatically apply pending migrations** (`alembic upgrade head`) before starting the application server. This ensures the database schema is always in sync with the application code.

## Docker

### Local Development (Recommended)
```bash
docker compose up --build
```

### Manual Build
```bash
docker build -t uoslife-agent .
docker run -p 8000:8000 --env-file .env uoslife-agent
```
