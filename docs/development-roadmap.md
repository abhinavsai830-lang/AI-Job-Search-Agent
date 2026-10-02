# Development Roadmap

## How we build

Every milestone follows the same loop:

1. Understand the problem.
2. Design the component.
3. Implement the smallest working version.
4. Test it.
5. Review the code and failure cases.
6. Commit the completed slice.
7. Only then move forward.

## Phase 0 — Foundation

Goal: establish a reliable application skeleton.

```text
Browser -> FastAPI -> SQLAlchemy -> PostgreSQL
```

## Phase 1 — Job ingestion

Goal: pull permitted/public job listings from real sources and store them.

```text
Job Source -> Collector -> Normalizer -> Database
```

## Phase 2 — Job intelligence

Goal: turn unstructured job descriptions into validated structured requirements.

```text
Raw JD -> LLM -> Structured JobRequirements -> Database
```

## Phase 3 — Deduplication

Goal: prevent the same job from being processed repeatedly.

```text
Exact rules + semantic similarity -> canonical job
```

## Phase 4 — Resume intelligence

Goal: convert a resume into a verified candidate profile.

```text
Resume -> Parser -> Profile + Evidence
```

## Phase 5 — RAG

Goal: retrieve only relevant candidate evidence when evaluating a job.

```text
Candidate documents -> chunks -> embeddings -> pgvector
Job requirement -> retrieval -> evidence
```

## Phase 6 — Matching

Goal: combine semantic matching with deterministic business rules.

```text
Candidate + Job + Evidence -> score + confidence + explanation
```

## Phase 7 — LangGraph

Goal: orchestrate the complete job-intelligence workflow.

```text
collect -> normalize -> dedupe -> analyze -> retrieve -> evaluate -> recommend
```

## Phase 8 — Notifications

Goal: send useful job alerts without blocking the API request.

```text
Recommendation -> queue -> worker -> email provider -> candidate
```

## Phase 9 — Feedback and memory

Goal: learn from candidate actions and explicit preferences.

## Phase 10 — Evaluation

Goal: measure extraction quality, retrieval quality, recommendation quality, and hallucination rate.

## Phase 11 — Observability

Goal: trace agent runs, retrieval, LLM calls, latency, errors, and token usage.

## Phase 12 — Production

Goal: secure, containerize, test, deploy, and document the system.
