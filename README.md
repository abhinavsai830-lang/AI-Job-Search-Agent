# AI Job Intelligence Agent

An agentic AI platform that discovers relevant job opportunities, understands job requirements, matches them against a candidate's verified profile, learns from feedback, and sends personalized job alerts through email.

## Current milestone

**Phase 0 — Foundation**

- FastAPI backend
- PostgreSQL + pgvector via Docker
- SQLAlchemy ORM
- Environment-based configuration
- Basic health endpoint
- Initial jobs API scaffold
- Vanilla HTML/CSS/JavaScript frontend structure

## Planned milestones

1. Foundation
2. Job ingestion
3. Job normalization + validation
4. Deduplication
5. JD intelligence with structured LLM output
6. Resume intelligence
7. Candidate RAG with embeddings + pgvector
8. Hybrid matching and ranking
9. LangGraph workflow
10. Redis background processing
11. Personalized email notifications
12. Feedback + memory
13. Evaluation
14. Observability
15. Production deployment

## Development principles

- Keep `main` stable.
- Build each milestone on a feature branch.
- Make small, meaningful commits.
- Test before moving to the next milestone.
- Prefer deterministic code for deterministic work.
- Use LLMs only where semantic reasoning is genuinely useful.
- Never invent candidate qualifications; important claims must be grounded in evidence.

## Local setup

### Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .[dev]
uvicorn app.main:app --reload
```

### Database

Start Docker Desktop first, then from the repository root:

```powershell
docker compose up -d postgres
```

The backend expects PostgreSQL at `localhost:5432`.

> Note: the sandbox used to prepare this repository does not have Docker or network access, so PostgreSQL connectivity is intentionally verified on your development machine.

API docs:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/health

## Git workflow

See `docs/git-workflow.md` for the branch and commit policy.


```text
main
  └── feature/phase-00-foundation
       └── feature/phase-01-job-ingestion
       └── feature/phase-02-job-intelligence
       ...
```

Commit style:

```text
feat: add job ingestion service
fix: handle duplicate job URLs
refactor: separate job repository from service
chore: update docker configuration
test: add job normalization tests
docs: explain candidate retrieval flow
```
