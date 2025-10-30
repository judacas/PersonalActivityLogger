# Research: Project Infrastructure Setup

**Date**: 2025-01-27  
**Feature**: 001-setup-project-infrastructure

## Overview

This research document captures the technical decisions made for setting up the project infrastructure. Since this is infrastructure setup (not application features), most decisions follow established best practices and the project constitution.

## Decisions & Rationale

### 1. Docker Compose Configuration

**Decision**: Use `docker-compose.yml` for production-like services and `docker-compose.dev.yml` for development overrides with hot-reload.

**Rationale**:
- Aligns with 12-Factor App Principle V (Build, Release, Run)
- Ensures consistent environments across all developers (Windows, macOS, Linux)
- Simplifies onboarding (single `docker-compose up` command)
- Enables parallel service management (frontend, backend, SQLite)

**Alternatives Considered**:
- Individual docker run commands: More verbose, harder to manage service dependencies
- Kubernetes: Overkill for local MVP development, adds unnecessary complexity

### 2. FastAPI Backend Structure

**Decision**: Use FastAPI with SQLAlchemy 2.0+ and Alembic migrations, structured as:
- `src/main.py` - FastAPI app entry point
- `src/db/database.py` - Database connection and session management
- `src/db/models/` - SQLAlchemy models
- `src/api/routes/` - API route handlers
- `src/services/` - Business logic layer
- `src/utils/logging.py` - Structured logging setup

**Rationale**:
- FastAPI provides automatic OpenAPI documentation, type hints, and async support
- SQLAlchemy 2.0+ offers modern async ORM capabilities and migration path to PostgreSQL
- Separation of concerns (models → services → routes) follows KISS and DRY principles
- Alembic ensures schema migrations work identically on SQLite and PostgreSQL

**Alternatives Considered**:
- Django: More opinionated, heavier framework, SQLAlchemy more flexible for our needs
- Flask: Missing automatic docs and async support, less modern ecosystem

### 3. React + Vite Frontend Structure

**Decision**: Use React 18+ with Vite, TypeScript, React Query for API state management:
- `src/components/` - Reusable UI components
- `src/pages/` - Route-level page components
- `src/services/api.ts` - Centralized API client
- `src/hooks/` - Custom React hooks

**Rationale**:
- Vite provides instant hot module replacement (<3 second feedback)
- TypeScript catches errors at compile time, improves DX
- React Query simplifies server state management with caching and refetching
- Component-based architecture scales well as features grow

**Alternatives Considered**:
- Create React App: Slower build times, more configuration needed
- Next.js: SSR adds complexity not needed for MVP, static build simpler for local-first app

### 4. Structured Logging with Python's `logging` Module

**Decision**: Use Python's built-in `logging` module with:
- Standard levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- JSON-formatted output for easy parsing (future observability tools)
- Contextual information (timestamps, module names, trace IDs)
- Console output for local development, extensible to external services post-MVP

**Rationale**:
- Built-in to Python, no external dependencies
- Well-documented, familiar to all developers
- Easy to extend with handlers (FileHandler, SysLogHandler, etc.)
- JSON output allows structured log aggregation tools (ELK, Datadog, Sentry) post-MVP

**Alternatives Considered**:
- Structlog: Adds unnecessary dependency for MVP, built-in logging sufficient
- External services (Sentry, LogRocket): Post-MVP feature, local logging first

### 5. GitHub Actions for CI/CD

**Decision**: Use GitHub Actions with workflow that:
- Runs on every push to PR branches
- Tests both frontend and backend
- Lints with Trunk configuration
- Builds Docker images
- Blocks merge on failure

**Rationale**:
- GitHub Actions is free for public repos, tightly integrated with repo
- Can reuse Trunk configuration for linting consistency
- Docker image building ensures containers work in all environments
- Fails fast to catch issues before merge

**Alternatives Considered**:
- Jenkins: Requires server setup, more complex for MVP
- GitLab CI: Would require migration from GitHub, not beneficial

### 6. Trunk for Code Quality

**Decision**: Use Trunk.io for:
- Pre-commit hooks (linting, formatting)
- Python linters: black, ruff, mypy
- TypeScript/JavaScript linters: ESLint, Prettier
- Auto-fixing violations where safe

**Rationale**:
- Single tool for all languages (Python + TypeScript)
- Pre-commit hooks catch issues before CI runs
- Auto-fix reduces developer friction
- Unified configuration in `trunk.yaml`

**Alternatives Considered**:
- Individual tools (black, eslint separately): More complex setup, harder to maintain
- pre-commit framework: More manual configuration, Trunk provides better DX

### 7. tasks.json for Common Operations

**Decision**: Use `tasks.json` (JSON-based task runner) for:
- `start` - Start all Docker services
- `test` - Run all tests (backend + frontend)
- `lint` - Run all linters
- `migrate` - Run database migrations
- `build` - Build Docker images

**Rationale**:
- Simple JSON format, easy to read and modify
- Provides shortcuts for frequent operations
- Makes project more accessible to new developers
- Reduces cognitive load (no need to remember Docker compose commands)

**Alternatives Considered**:
- Makefile: Platform-specific, harder to maintain
- npm scripts: Only covers frontend, not unified
- Custom shell scripts: Less portable across platforms

## Unresolved Decisions

None. All technical decisions are resolved and ready for implementation.

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Trunk Documentation](https://trunk.io/)
- [Python Logging HowTo](https://docs.python.org/3/howto/logging.html)

