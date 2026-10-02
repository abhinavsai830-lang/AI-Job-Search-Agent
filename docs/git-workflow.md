# Git Workflow

## Branches

`main` is always kept in a known working state.

For each milestone, create a short-lived feature branch from `main`:

```text
main
  |
  +-- feature/phase-01-job-ingestion
  |
  +-- feature/phase-02-job-intelligence
  |
  +-- feature/phase-03-deduplication
```

Merge only after tests and manual verification pass.

## Commit format

Use small, focused commits:

```text
feat: add greenhouse job collector
fix: handle missing location field
refactor: separate source client from parser
test: add normalization edge cases
chore: pin dependency versions
docs: explain ingestion flow
```

## Fallback strategy

Before a large change:

```bash
git status
git log --oneline --decorate -10
```

After a milestone passes:

```bash
git tag -a v0.2.0 -m "Phase 1 job ingestion"
```

Never use `git push --force` on `main` for this project.
