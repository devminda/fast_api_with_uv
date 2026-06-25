# TODO: Project Name

[![CI](https://github.com/TODO-org/TODO-repo/actions/workflows/ci.yml/badge.svg)](https://github.com/TODO-org/TODO-repo/actions/workflows/ci.yml)
[![Docs](https://github.com/TODO-org/TODO-repo/actions/workflows/docs.yml/badge.svg)](https://TODO-org.github.io/TODO-repo/)

TODO: project description.

📖 **[Full documentation →](https://TODO-org.github.io/TODO-repo/)**

---

## Setup

```bash
git clone https://github.com/TODO-org/TODO-repo.git
cd TODO-repo
cp .env.example .env       # fill in your values
pip install uv
uv sync --extra dev --extra docs
uv run pre-commit install
```

## Run locally

```bash
uv run uvicorn app.main:app --reload
```

- API: `http://localhost:8000`
- Interactive docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Run with Docker

```bash
docker build -t app .
docker run -p 8000:8000 app
```

## Tests

```bash
uv run pytest
```

## Project structure

```
.
├── src/app/
│   ├── api/v1/endpoints/   # route handlers
│   ├── core/               # config, shared utilities
│   ├── db/                 # database connection & schemas
│   ├── models/             # ORM models (if needed)
│   ├── schemas/            # Pydantic request/response models
│   ├── services/           # business logic
│   └── main.py             # app entrypoint
├── tests/
│   ├── unit/
│   └── integration/
├── docs/                   # MkDocs pages
├── Dockerfile
├── .env.example
└── pyproject.toml          # all tool config lives here
```

## TODO checklist after cloning this template

- [ ] Replace all `TODO` placeholders in `pyproject.toml`, `mkdocs.yml`, `README.md`
- [ ] Fill in `.env` from `.env.example`
- [ ] Enable GitHub Pages: Settings → Pages → GitHub Actions
- [ ] Set up branch protection: Settings → Rules → New ruleset
- [ ] Delete the example `items` endpoint and write your own
