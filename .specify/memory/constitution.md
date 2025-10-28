# Personal Activity Logger Constitution

<!--
  Sync Impact Report:
  - Version change: 1.0.0 → 1.1.0 (MINOR: new principles and sections added)
  - Modified principles: None (principles expanded)
  - Added sections: 
    - VI. Code Quality Principles (DRY, KISS, Separation of Concerns, Small Functions, Return Don't Mutate, Error Handling, Avoid Premature Optimization)
    - VII. 12-Factor App Principles (all 12 factors expanded)
    - VIII. Infrastructure & Tooling (Docker, Trunk, tasks.json, Folder Structure, Documentation)
    - IX. Continuous Integration (CI/CD, Pre-commit Hooks)
  - Removed sections: None
  - Templates requiring updates: 
    - ✅ plan-template.md: Constitution Check already aligned
    - ⚠️ spec-template.md: May need updates for 12-Factor principles
    - ⚠️ tasks-template.md: Should include tasks.json setup, Docker setup, Trunk setup
  - Follow-up TODOs: Consider adding Trunk and Docker setup tasks to tasks-template.md
-->

## Core Principles

### I. MVP-First Development (NON-NEGOTIABLE)

Every feature MUST deliver the simplest implementation that satisfies core requirements. Local-only functionality before multi-user. No authentication before public hosting. SQLite before PostgreSQL. YAGNI (You Aren't Gonna Need It) strictly enforced. Features marked "Post-MVP" in the product spec MUST NOT be implemented in MVP unless explicitly approved.

### II. Testing Discipline

Unit tests required for time arithmetic, overlap prevention, rounding logic, and data transformations. Integration tests mandatory for all API endpoints (Start/Stop/Quick/Export). Smoke tests for UI flows (Start→Stop→Review). Tests MUST be written before or alongside implementation. No merging feature code without corresponding test coverage.

### III. Migration-Ready Architecture

Use SQLAlchemy ORM and Alembic migrations from day one, even on SQLite. Database schema MUST be defined via Alembic migrations only. Direct SQL or manual schema changes prohibited. This ensures smooth migration to PostgreSQL for post-MVP multi-user deployment.

### IV. Local-First MVP

MVP runs exclusively on local machine. No authentication, no external services, no internet dependencies. Frontend served by Vite dev server in development, static build for deployment. Backend uses SQLite file database. All external integrations (iPhone Shortcuts, hosted deployments) marked for post-MVP only.

### V. REST API Design

API endpoints MUST follow RESTful conventions. JSON in/out only. UTC timestamps stored internally, local time conversion in UI. Exactly one active running log at a time; new start automatically stops previous. All endpoints return consistent error format with descriptive messages.

### VI. Code Quality Principles

**DRY (Don't Repeat Yourself)**: Eliminate duplication. Extract shared logic into reusable functions/modules. If similar code appears in 3+ places, refactor into shared utilities.

**KISS (Keep It Simple, Stupid)**: Simpler solutions preferred over complex ones. Clarity beats cleverness. Choose straightforward implementations over intricate abstractions.

**Separation of Concerns**: Models handle data. Services handle business logic. Controllers/endpoints handle HTTP requests. Components handle UI. Clear boundaries with single responsibility per module.

**Small Functions**: Functions MUST do one thing well. Limit function length to ~20-30 lines. Extract complex logic into helper functions with descriptive names. One purpose per function.

**Return Don't Mutate**: Prefer returning new data over mutating existing objects. Use immutable patterns where possible. Exception: ORM models may mutate state.

**Error Handling & Logging**: ALL errors MUST be logged with context (structured logging). Never suppress errors silently. Return meaningful error messages to API consumers. Use proper logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).

**Avoid Premature Optimization**: Write clear, correct code first. Profile before optimizing. Optimize only when measured bottlenecks exist. No micro-optimizations without data.

### VII. 12-Factor App Principles

**I. Codebase**: One codebase per app (monorepo). Many deploys (dev/staging/prod).

**II. Dependencies**: Explicitly declare and isolate dependencies. Use `requirements.txt` (Python), `package.json` (frontend). Docker for consistent environments.

**III. Config**: Store config in environment variables. Never commit secrets. Use `.env` files for local dev, CI/CD vars for production. No hardcoded config values.

**IV. Backing Services**: Treat databases, caches, APIs as attached resources. Swap providers without code changes via config. SQLite → PostgreSQL migration path.

**V. Build, Release, Run**: Strict separation of build (compile/bundle), release (apply config), run (execute). Docker images for consistent builds.

**VI. Processes**: Execute as stateless processes. No shared memory. HTTP sessions stored in backing service (DB/cache).

**VII. Port Binding**: Export services via port binding. Frontend dev server on one port, backend API on another. Exposed via environment variables.

**VIII. Concurrency**: Scale via process model (horizontal scaling). Stateless design enables parallelism.

**IX. Disposability**: Minimize startup time, graceful shutdown. Handle SIGTERM. No data loss on shutdown.

**X. Dev/Prod Parity**: Keep dev, staging, and prod environments as similar as possible. Use same database type, same OS family via Docker.

**XI. Logs**: Treat logs as event streams. Write to stdout/stderr. Capture via log aggregation (ELK, CloudWatch, etc. for post-MVP).

**XII. Admin Processes**: Run migrations, one-off scripts via same codebase/deploy. No ad-hoc manual DB changes. Use Alembic CLI.

### VIII. Infrastructure & Tooling

**Docker**: All development MUST use Docker for consistent environments. Dev containers for local development. Production deployments use Docker images.

**Trunk**: Use Trunk for linters, formatters, and pre-commit hooks. Configure trunk.yaml with appropriate linters for Python and TypeScript/JavaScript.

**Tasks.json**: Implement `tasks.json` configuration for common development tasks:
- Build Docker containers
- Run linters and checkers
- Run migrations
- Start dev servers
- Run tests

**Folder Structure**: Follow clear project structure conventions. Frontend in `frontend/`, backend in `backend/`. Tests mirror source structure.

**Documentation**: Keep README updated with setup instructions, development workflow, and architecture decisions. Document breaking changes and new patterns.

### IX. Continuous Integration

**CI/CD Pipeline** (pre-MVP): Automated testing, linting, and Docker builds on every push. All tests must pass before merge. Automated deployment to staging and production environments. Failure blocks merge.

**Pre-commit Hooks**: Run Trunk linters and formatters before commits. Enforce code quality at commit time, not in CI.

## Technology Stack

### Required Dependencies

- **Frontend**: React + Vite
- **Backend**: Python FastAPI
- **Database**: SQLite (MVP) → PostgreSQL (post-MVP)
- **Testing**: pytest (backend), React Testing Library (frontend)
- **Charts**: Recharts
- **State Management**: React Query for API caching
- **Containerization**: Docker (dev and production)
- **Code Quality**: Trunk for linters, formatters, and pre-commit hooks
- **Task Runner**: tasks.json configuration for common development tasks

### Architecture Constraints

- Frontend: Single-page React app with React Query for server state
- Backend: FastAPI REST API, served by Uvicorn in dev
- Database: SQLite via SQLAlchemy/Alembic (migration path to Postgres)
- Build: Docker containers for consistent dev/prod environments
- Deployment: CI/CD pipeline (post-MVP) with automated testing and Docker builds

## Development Workflow

### Feature Implementation

1. Read product spec (`docs/productAndTechSpec.md`) to understand scope
2. Validate feature against MVP scope (Section 2: Non-goals)
3. Write tests first (Red-Green-Refactor)
4. Implement simplest solution that passes tests
5. Validate against acceptance criteria (Section 16)
6. No scope creep into post-MVP features without explicit approval

### Database Changes

ALL database schema changes MUST go through Alembic migrations. No direct SQL execution allowed unless explicitly stated. Migrations must be tested in isolation before integration. Review migration file for accuracy before applying.

### API Endpoints

New endpoints MUST follow existing patterns in `docs/productAndTechSpec.md` Section 8. Maintain consistent error handling and response formats. Update API documentation when adding endpoints.

## Governance

This constitution supersedes all other development practices. All PRs, reviews, and implementations MUST verify compliance. Any violation requires explicit justification in the Complexity Tracking section.

Amendments to this constitution require:
1. Clear rationale for the change
2. Impact analysis on existing code and workflows
3. Update to all dependent templates
4. Version bump following semantic versioning

Complexity beyond MVP MUST be justified. When in doubt, choose the simpler implementation.

**Version**: 1.1.0 | **Ratified**: 2025-01-27 | **Last Amended**: 2025-01-27
