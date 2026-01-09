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
