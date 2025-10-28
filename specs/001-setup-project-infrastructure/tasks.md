# Tasks: Project Infrastructure Setup

**Input**: Design documents from `/specs/001-setup-project-infrastructure/`  
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create backend directory structure: backend/src/, backend/tests/, backend/alembic/
- [x] T002 Create frontend directory structure: frontend/src/, frontend/tests/, frontend/public/
- [x] T003 [P] Create root configuration files: .gitignore, .dockerignore
- [x] T004 [P] Create README.md with project overview and setup instructions

---

## Phase 2: User Story 1 - Docker Development Environment (Priority: P1)

**Goal**: Developers can start all services (frontend, backend, database) with a single command and see changes hot-reload

**Independent Test**: Run `docker-compose up` → all services start → make code change → change reflects in <3 seconds

### Implementation for User Story 1

- [x] T005 [P] [US1] Create docker-compose.yml with frontend, backend, and network services at repository root
- [x] T006 [P] [US1] Create docker-compose.dev.yml with volume mounts for hot-reload at repository root
- [x] T007 [P] [US1] Create backend/Dockerfile with Python 3.11 base image and FastAPI dependencies
- [x] T008 [P] [US1] Create frontend/Dockerfile with Node.js 20 LTS base image and Vite build tools
- [x] T009 [US1] Configure docker-compose.yml services to expose ports 3000 (frontend) and 8000 (backend)
- [x] T010 [US1] Add volume mounts to docker-compose.dev.yml for ./backend/src and ./frontend/src
- [x] T011 [US1] Configure hot-reload for backend using uvicorn --reload in backend/src/main.py
- [x] T012 [US1] Configure hot-reload for frontend using Vite dev server in frontend/vite.config.ts

**Checkpoint**: Docker environment starts successfully, services accessible, hot-reload working

---

## Phase 3: User Story 2 - Project Structure and FastAPI Scaffold (Priority: P1)

**Goal**: FastAPI backend scaffold with working API structure, SQLAlchemy setup, Alembic migrations, and interactive documentation

**Independent Test**: Visit http://localhost:8000/docs → see FastAPI docs → add new endpoint → it appears in docs

### Implementation for User Story 2

- [x] T013 [P] [US2] Create backend/src/main.py with FastAPI app initialization
- [x] T014 [P] [US2] Create backend/src/config.py with environment configuration management
- [x] T015 [P] [US2] Create backend/src/db/database.py with SQLAlchemy engine and session setup
- [x] T016 [P] [US2] Create backend/src/db/models/__init__.py with empty models directory
- [x] T017 [P] [US2] Create backend/src/api/dependencies.py with shared API dependencies
- [x] T018 [P] [US2] Create backend/src/api/routes/__init__.py with empty routes directory
- [x] T019 [P] [US2] Create backend/src/services/__init__.py with empty services directory
- [x] T020 [P] [US2] Create backend/src/utils/logging.py with structured logging configuration
- [x] T021 [US2] Initialize Alembic with alembic init at backend/alembic/
- [x] T022 [US2] Configure backend/alembic/env.py with SQLAlchemy engine from src/db/database.py
- [x] T023 [US2] Create backend/requirements.txt with FastAPI, SQLAlchemy, Alembic, Uvicorn dependencies
- [x] T024 [US2] Create backend/.env.example with LOG_LEVEL, DATABASE_URL, API_HOST, API_PORT variables
- [x] T025 [US2] Add CORS middleware to backend/src/main.py for localhost:3000 frontend
- [x] T026 [US2] Register test health endpoint in backend/src/api/routes/health.py at /api/health
- [x] T027 [US2] Mount health route in backend/src/main.py to verify API structure

**Checkpoint**: FastAPI scaffold runs, /docs accessible, health endpoint returns 200 OK

---

## Phase 4: User Story 3 - Frontend React Scaffold (Priority: P1)

**Goal**: React + Vite frontend with TypeScript, routing, API integration, and component structure

**Independent Test**: Visit http://localhost:3000 → see React app → make UI change → change reflects in browser <3 seconds

### Implementation for User Story 3

- [x] T028 [P] [US3] Create frontend/src/main.tsx with React root initialization
- [x] T029 [P] [US3] Create frontend/src/App.tsx with root component and routing setup
- [x] T030 [P] [US3] Create frontend/src/components/common/Layout.tsx for page layout structure
- [x] T031 [P] [US3] Create frontend/src/pages/HomePage.tsx as basic page component
- [x] T032 [P] [US3] Create frontend/src/services/api.ts with API client configuration
- [x] T033 [P] [US3] Create frontend/src/hooks/useApi.ts for React Query API integration
- [x] T034 [P] [US3] Create frontend/src/utils/constants.ts for app constants
- [x] T035 [US3] Configure frontend/vite.config.ts with proxy to backend API at localhost:8000
- [x] T036 [US3] Create frontend/package.json with React, Vite, TypeScript, React Query dependencies
- [x] T037 [US3] Create frontend/tsconfig.json with TypeScript configuration
- [x] T038 [US3] Create frontend/.env.example with VITE_API_URL variable
- [x] T039 [US3] Add React Query provider to frontend/src/App.tsx
- [x] T040 [US3] Create frontend/src/components/layout/Header.tsx for navigation structure

**Checkpoint**: React scaffold runs, UI visible, API client configured, hot-reload working

---

## Phase 5: User Story 4 - Structured Logging Infrastructure (Priority: P2)

**Goal**: Structured logging with configurable levels, JSON output, and consistent patterns

**Independent Test**: Set LOG_LEVEL=DEBUG → make request → see structured log output with timestamp, level, message

### Implementation for User Story 4

- [x] T041 [US4] Configure backend/src/utils/logging.py with JSON formatter
- [x] T042 [US4] Add LogRecord schema to backend/src/utils/logging.py with timestamp, level, module, function, message, extra fields
- [x] T043 [US4] Create logging configuration in backend/src/config.py with LOG_LEVEL environment variable
- [x] T044 [US4] Initialize logging at startup in backend/src/main.py
- [x] T045 [US4] Add request logging middleware to backend/src/main.py to log all API requests
- [x] T046 [US4] Add context propagation to backend/src/utils/logging.py for request IDs
- [x] T047 [US4] Test logging at all levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) in backend/src/api/routes/health.py

**Checkpoint**: Structured logs appear in console with JSON format, levels configurable, context included

---

## Phase 6: User Story 5 - CI/CD Pipeline (Priority: P2)

**Goal**: Automated testing, linting, and Docker builds run on every push, blocking merge on failure

**Independent Test**: Push to GitHub → CI runs → all checks pass → merge allowed OR fail → merge blocked

### Implementation for User Story 5

- [x] T048 [P] [US5] Create .github/workflows/ci.yml with GitHub Actions workflow
- [x] T049 [US5] Configure backend test step in .github/workflows/ci.yml to run pytest
- [x] T050 [US5] Configure frontend test step in .github/workflows/ci.yml to run npm test
- [x] T051 [US5] Add linting step to .github/workflows/ci.yml to run Trunk check
- [x] T052 [US5] Add Docker build step to .github/workflows/ci.yml to build backend and frontend images
- [x] T053 [US5] Configure workflow triggers in .github/workflows/ci.yml for push and pull_request events
- [x] T054 [US5] Add step to block merge on CI failure in .github/workflows/ci.yml

**Checkpoint**: CI runs on push, all checks execute, failure blocks merge

---

## Phase 7: User Story 6 - Trunk Integration with Pre-commit Hooks (Priority: P2)

**Goal**: Automated code quality checks via Trunk run before commit, auto-fix where possible, block on violations

**Independent Test**: Commit code with formatting error → Trunk blocks commit → fix → commit succeeds

### Implementation for User Story 6

- [x] T055 [P] [US6] Create trunk.yaml at repository root with linter configuration
- [x] T056 [US6] Add Python linters to trunk.yaml: black, ruff, mypy
- [x] T057 [US6] Add TypeScript/JavaScript linters to trunk.yaml: eslint, prettier
- [x] T058 [US6] Configure pre-commit hooks in trunk.yaml to run on git commit
- [x] T059 [US6] Add auto-fix rules to trunk.yaml for safe formatting fixes
- [x] T060 [US6] Configure .gitignore to exclude .trunk/ and Trunk cache files
- [ ] T061 [US6] Test Trunk by committing code with intentional formatting violation

**Checkpoint**: Pre-commit hooks run, violations detected, auto-fix works, commit blocked on errors

---

## Phase 8: User Story 7 - tasks.json Configuration (Priority: P2)

**Goal**: Common development tasks configured for simple execution of frequent operations

**Independent Test**: Run ./tasks.json run start → all services start, run ./tasks.json run test → all tests run

### Implementation for User Story 7

- [x] T062 [P] [US7] Create tasks.json at repository root with version and task definitions
- [x] T063 [US7] Add "start" task to tasks.json to run docker-compose up -d
- [x] T064 [US7] Add "stop" task to tasks.json to run docker-compose down
- [x] T065 [US7] Add "test" task to tasks.json to run backend and frontend tests
- [x] T066 [US7] Add "lint" task to tasks.json to run trunk check
- [x] T067 [US7] Add "migrate" task to tasks.json to run alembic upgrade head
- [x] T068 [US7] Add "build" task to tasks.json to build Docker images
- [x] T069 [US7] Add "logs" task to tasks.json to run docker-compose logs -f
- [ ] T070 [US7] Test all tasks.json commands execute successfully

**Checkpoint**: tasks.json provides 7+ common tasks that execute successfully

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final infrastructure improvements and documentation

- [x] T071 [P] Update README.md with complete setup instructions and usage
- [x] T072 [P] Add error handling for port conflicts in docker-compose.yml
- [x] T073 [P] Add SQLite volume configuration to docker-compose.yml for data persistence
- [x] T074 Add GitHub Actions badge to README.md showing CI status
- [x] T075 Update .gitignore with comprehensive patterns for Python, Node.js, Docker
- [x] T076 [P] Create backend/tests/conftest.py with pytest fixtures for database
- [x] T077 [P] Create frontend/tests/setup.ts with test utilities and mocks
- [ ] T078 Run quickstart.md validation to ensure all steps work correctly

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **User Story 1 (Phase 2)**: Depends on Setup completion - BLOCKS all subsequent stories
- **User Stories 2-3 (Phases 3-4)**: Depend on User Story 1 (Docker environment)
- **User Stories 4-7 (Phases 5-8)**: Can proceed in parallel once Docker environment is running
- **Polish (Phase 9)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (Docker)**: Foundation for all other stories - COMPLETE FIRST
- **User Story 2 (FastAPI)**: Depends on User Story 1 - Needs Docker running
- **User Story 3 (React)**: Depends on User Story 1 - Needs Docker running, can parallel with US2
- **User Stories 4-7**: Can start once Docker is working - Can all run in parallel

### Within Each User Story

- Docker config before service implementation
- Models/directories before code
- Configuration before usage
- Core infrastructure before features

### Parallel Opportunities

- Setup tasks (T001-T004) can run in parallel
- Docker configuration tasks (T005-T008) can run in parallel
- Backend scaffold tasks (T013-T027) mostly parallel except dependencies
- Frontend scaffold tasks (T028-T040) mostly parallel except dependencies
- Infrastructure tasks (CI/CD, Trunk, tasks.json) fully independent and parallel
- All P1 stories should be complete before P2 stories

---

## Parallel Example: User Story 2 (FastAPI Scaffold)

```bash
# Launch all parallel structure tasks together:
Task: "Create backend/src/main.py"
Task: "Create backend/src/config.py"
Task: "Create backend/src/db/database.py"
Task: "Create backend/src/api/dependencies.py"
Task: "Create backend/src/utils/logging.py"

# Then sequential tasks:
Task: "Initialize Alembic" (depends on database.py)
Task: "Configure Alembic" (depends on database.py)
```

---

## Implementation Strategy

### MVP First (Critical Path Only)

1. **Setup (Phase 1)**: Create basic structure
2. **User Story 1 (Phase 2)**: Docker environment - MUST complete first
3. **User Story 2 (Phase 3)**: FastAPI scaffold - REQUIRED for backend
4. **User Story 3 (Phase 4)**: React scaffold - REQUIRED for frontend
5. **STOP and VALIDATE**: All services running, hot-reload working
6. Infrastructure ready for actual app feature development

### Incremental Delivery

1. Setup → Docker ready
2. Add Docker → Services run
3. Add FastAPI → Backend working
4. Add React → Frontend working
5. Add Logging → Observability improved
6. Add CI/CD → Quality gates active
7. Add Trunk → Pre-commit checks active
8. Add tasks.json → Developer experience improved

### Parallel Team Strategy

With multiple developers:

1. One developer: Docker setup (US1)
2. Once Docker works, two developers:
   - Developer A: Backend scaffold (US2)
   - Developer B: Frontend scaffold (US3)
3. Once scaffolds done:
   - Developer A: Logging (US4)
   - Developer B: CI/CD (US5)
   - Developer C: Trunk (US6), tasks.json (US7)

---

## Task Summary

- **Total Tasks**: 78
- **Setup Phase**: 4 tasks
- **User Story 1 (Docker)**: 8 tasks
- **User Story 2 (FastAPI)**: 15 tasks
- **User Story 3 (React)**: 13 tasks
- **User Story 4 (Logging)**: 7 tasks
- **User Story 5 (CI/CD)**: 7 tasks
- **User Story 6 (Trunk)**: 7 tasks
- **User Story 7 (tasks.json)**: 9 tasks
- **Polish Phase**: 8 tasks

**Suggested MVP Scope**: Phases 1-4 (Setup, Docker, FastAPI, React) provide working infrastructure for app development to begin.

**Estimated Timeline**: 
- Critical path (P1 stories): 6-8 hours
- Full implementation (all stories): 12-16 hours

---

## Notes

- Infrastructure only - no app features implemented
- All scaffolds must be working before app development begins
- Docker is the foundation - test it thoroughly before proceeding
- FastAPI and React scaffolds should be independently runnable
- Logging, CI/CD, Trunk, and tasks.json enhance developer experience but aren't blockers
- Each checkpoint should validate that infrastructure is working

