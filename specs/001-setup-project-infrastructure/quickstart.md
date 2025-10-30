# Quick Start Guide: Development Infrastructure

**Date**: 2025-01-27  
**Feature**: 001-setup-project-infrastructure

## Prerequisites

- Docker Desktop installed and running
- Git installed
- Code editor (VS Code recommended)

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd PersonalActivityLogger
```

### 2. Copy Environment Files

```bash
# Backend
cp backend/.env.example backend/.env

# Frontend
cp frontend/.env.example frontend/.env

# Root
cp .env.example .env
```

### 3. Start Development Environment

```bash
# Option 1: Using tasks.json
./tasks.json run start

# Option 2: Using Docker Compose directly
docker-compose up -d
```

### 4. Verify Services

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Backend API with alternative docs: http://localhost:8000/redoc

### 5. View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
```

## Development Workflow

### Make Code Changes

1. Edit files in `backend/src/` or `frontend/src/`
2. Save file
3. Changes automatically reload (hot-reload < 3 seconds)
4. Check browser/API for updated output

### Run Tests

```bash
# All tests
./tasks.json run test

# Backend only
docker-compose exec backend pytest

# Frontend only
docker-compose exec frontend npm test

# With coverage
docker-compose exec backend pytest --cov=src tests/
```

### Run Linters

```bash
# All linters via Trunk
./tasks.json run lint

# Or via Trunk CLI
trunk check
```

### Database Migrations

```bash
# Run pending migrations
./tasks.json run migrate

# Or via Alembic directly
docker-compose exec backend alembic upgrade head

# Create new migration (when adding models)
docker-compose exec backend alembic revision --autogenerate -m "description"
```

### Stop Services

```bash
# Stop (preserves containers)
docker-compose stop

# Stop and remove containers (keeps volumes)
docker-compose down

# Stop and remove everything including volumes
docker-compose down -v
```

## Common Tasks Reference

| Task | Command | Description |
|------|---------|-------------|
| Start | `./tasks.json run start` | Start all Docker services |
| Test | `./tasks.json run test` | Run all tests |
| Lint | `./tasks.json run lint` | Run all linters |
| Migrate | `./tasks.json run migrate` | Run database migrations |
| Logs | `docker-compose logs -f` | View all logs |
| Restart | `docker-compose restart` | Restart all services |

## Debugging

### Container Not Starting

```bash
# Check container logs
docker-compose logs backend
docker-compose logs frontend

# Check container status
docker-compose ps

# Rebuild containers
docker-compose up --build -d
```

### Port Conflicts

If ports 3000 or 8000 are in use:

1. Find process using port:
   ```bash
   # Windows
   netstat -ano | findstr :3000
   
   # macOS/Linux
   lsof -i :3000
   ```

2. Stop the process or change ports in `docker-compose.yml`

### Database Issues

```bash
# View database file
docker-compose exec backend ls -la /app/data/

# Reset database (⚠️ deletes all data)
docker-compose exec backend rm /app/data/app.db
./tasks.json run migrate
```

### Hot-Reload Not Working

1. Check file permissions
2. Verify volume mounts in `docker-compose.yml`
3. Restart containers: `docker-compose restart`

## Environment Variables

### Backend (.env)

```bash
# Logging
LOG_LEVEL=DEBUG  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# API Server
API_HOST=0.0.0.0
API_PORT=8000

# Database
DATABASE_URL=sqlite:///./data/app.db

# CORS
CORS_ORIGINS=http://localhost:3000
```

### Frontend (.env)

```bash
# Backend API URL
VITE_API_URL=http://localhost:8000

# App Configuration
VITE_APP_NAME=Personal Activity Logger
VITE_APP_ENV=development
```

## Architecture Overview

```
┌─────────────────────────────────────────┐
│         Developer Machine                │
│                                          │
│  ┌──────────────┐      ┌──────────────┐ │
│  │  Frontend   │      │   Backend    │ │
│  │  React+Vite │──────▶│   FastAPI    │ │
│  │  localhost  │      │   localhost  │ │
│  │  :3000      │      │   :8000      │ │
│  └──────────────┘      └──────┬───────┘ │
│                                 │        │
│                          ┌──────▼───────┐ │
│                          │   SQLite    │ │
│                          │  /data/     │ │
│                          └────────────┘ │
│                                          │
└──────────────────────────────────────────┘

All services run in Docker containers on localhost
```

## Next Steps After Setup

Once infrastructure is running:

1. Verify all services are accessible
2. Check API documentation at http://localhost:8000/docs
3. Run tests to confirm everything works
4. Begin implementing actual application features

## Troubleshooting

### "Cannot connect to Docker daemon"

- Ensure Docker Desktop is running
- Try: `docker ps` to verify Docker is accessible

### "Port already in use"

- Stop conflicting services or change ports in `docker-compose.yml`

### "Module not found" errors

- Run `docker-compose exec backend pip install -r requirements.txt`
- Run `docker-compose exec frontend npm install`

### Trunk pre-commit hooks not running

- Install Trunk: https://docs.trunk.io/install
- Initialize in repo: `trunk init`

## Support

- Check README.md in repository root for full documentation
- Review logs for specific error messages
- Consult `.specify/memory/constitution.md` for development principles

