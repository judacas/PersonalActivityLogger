# Data Model: Project Infrastructure Setup

**Date**: 2025-01-27  
**Feature**: 001-setup-project-infrastructure

## Overview

This document defines the data structures for the project infrastructure setup. Since this feature creates scaffolds and configuration (not application features), the "data model" primarily concerns logging configuration, environment variables, and project structure metadata.

## Logging Configuration Schema

### LogRecord (Python logging)

**Purpose**: Structured log entry format for backend API logging

**Attributes**:
- `timestamp` (datetime) - When the log was created
- `level` (str) - Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `module` (str) - Python module where log originated
- `function` (str) - Function name where log originated
- `message` (str) - Human-readable log message
- `extra` (dict, optional) - Additional context (request ID, user ID, etc.)

**Format**: JSON for easy parsing and extensibility

**Example**:
```json
{
  "timestamp": "2025-01-27T10:30:00.123Z",
  "level": "INFO",
  "module": "src.api.routes.logs",
  "function": "create_log",
  "message": "Creating new activity log",
  "extra": {
    "category": "work",
    "user_id": null
  }
}
```

## Environment Configuration Schema

### Backend Environment (.env)

**Purpose**: Configuration for FastAPI backend service

**Variables**:
- `DEBUG` (bool) - Enable debug mode (default: false)
- `LOG_LEVEL` (str) - Minimum log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `DATABASE_URL` (str) - SQLite database file path
- `API_HOST` (str) - API host binding (default: 0.0.0.0)
- `API_PORT` (int) - API port number (default: 8000)
- `CORS_ORIGINS` (str, comma-separated) - Allowed CORS origins

**Validation Rules**:
- `LOG_LEVEL` must be one of valid levels
- `API_PORT` must be valid port number (1-65535)
- `DEBUG` set to false in production (handled by env-specific files)

### Frontend Environment (.env)

**Purpose**: Configuration for React + Vite frontend

**Variables**:
- `VITE_API_URL` (str) - Backend API base URL
- `VITE_APP_NAME` (str) - Application name
- `VITE_APP_ENV` (str) - Environment (development, production)

**Validation Rules**:
- `VITE_API_URL` must be valid URL
- Required by Vite convention (prefixed with VITE_)

## Docker Configuration Schema

### Docker Compose Services

**Service: backend**
- Image: Python 3.11-slim base
- Build context: `./backend`
- Ports: `8000:8000`
- Volumes: `./backend:/app` (dev), SQLite data volume
- Environment: From `backend/.env`

**Service: frontend**
- Image: Node.js 20 LTS base
- Build context: `./frontend`
- Ports: `3000:3000`
- Volumes: `./frontend:/app` (dev), `node_modules` anonymous volume
- Environment: From `frontend/.env`

**Service: sqlite** (future)
- Volume: SQLite database file storage
- Used for data persistence across container restarts

### Docker Network

- Name: `activity-logger-network`
- Driver: bridge
- All services communicate via service names (backend, frontend)

## Trunk Configuration Schema

### trunk.yaml

**Structure**:
```yaml
version: 0.1
cli:
  version: 1.17.1
lint:
  enabled:
    - black@latest
    - ruff@latest
    - mypy@latest
    - eslint@latest
    - prettier@latest
  ignore:
    - alembic/versions/
```

**Purpose**: Define linters, formatters, and pre-commit hook behavior for code quality enforcement

## tasks.json Schema

### Task Definition

**Structure**:
```json
{
  "version": "1.0.0",
  "tasks": {
    "start": {
      "description": "Start all Docker services",
      "command": "docker-compose up -d"
    }
  }
}
```

**Purpose**: Provide simple CLI for common development operations

## Project Structure Metadata

### Directory Conventions

**Naming Rules**:
- `backend/` - Python backend code
- `frontend/` - React frontend code
- `backend/src/` - Source code
- `backend/tests/` - Test code (mirrors src structure)
- `backend/alembic/` - Database migrations
- `frontend/src/` - Source code
- `frontend/tests/` - Test code (mirrors src structure)

**File Conventions**:
- Python: `lowercase_with_underscores.py` for modules, `UppercaseCase` for classes
- TypeScript: `camelCase.ts` for utilities, `PascalCase.tsx` for components
- Configuration: `.yaml` for YAML, `.json` for JSON, `.env` for environment

## Relationships

- Logging configuration → Environment variables (LOG_LEVEL controls behavior)
- Docker services → Environment configs (via .env files)
- Trunk config → Pre-commit hooks → Git hooks
- tasks.json → Docker Compose → Services

## State Transitions

### Development Environment States

1. **Initial**: No containers running
   - Transition: `docker-compose up`
   - End state: All services running

2. **Running**: All containers active
   - Transition: Code change
   - End state: Hot-reload triggered, changes reflected

3. **Stopped**: Containers stopped but not removed
   - Transition: `docker-compose restart`
   - End state: Containers restarted with persisted data

4. **Removed**: Containers removed
   - Transition: `docker-compose up`
   - End state: Fresh containers with persisted volumes

### Log Levels Hierarchy

```
DEBUG < INFO < WARNING < ERROR < CRITICAL
```

- Setting LOG_LEVEL to INFO suppresses DEBUG logs
- Setting LOG_LEVEL to ERROR only shows ERROR and CRITICAL

## Constraints

- SQLite database must be in a Docker volume for persistence
- Environment variables must not contain secrets (use separate secrets management post-MVP)
- Port conflicts must be detected and reported
- All logging must be asynchronous to avoid blocking request processing
- Hot-reload must preserve application state where possible

## Future Extensibility

**Post-MVP Enhancements**:
- Add user authentication (separate user table, scoped logs)
- PostgreSQL migration (same models, different database URL)
- External observability integration (structured logs → Datadog/Sentry)
- Multi-user support (add user_id to log records)
- Cloud deployment configuration (Kubernetes manifests, Helm charts)

