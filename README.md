# Personal Activity Logger

A private, low-friction system to log daily activities and visualize time use, starting local-only and growing into a small multi-user web app.

## Project Overview

This is a full-stack web application for tracking personal activities and time usage.

### Tech Stack

- **Backend**: Python 3.11, FastAPI, SQLAlchemy, Alembic, SQLite
- **Frontend**: React 18, Vite, TypeScript, React Query
- **Development**: Docker, Docker Compose
- **Quality**: Trunk (linting, formatting), pytest, React Testing Library
- **CI/CD**: GitHub Actions

### Project Structure

```
backend/          - FastAPI backend application
frontend/         - React + Vite frontend application
specs/            - Feature specifications and planning
docs/             - Product and technical specifications
.github/           - GitHub Actions CI/CD workflows
```

## Getting Started

### Prerequisites

- Docker Desktop installed and running
- Git installed

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd PersonalActivityLogger
   ```

2. **Start the development environment**:
   ```bash
   docker-compose up -d
   ```
   
   Or use the tasks.json runner:
   ```bash
   # After configuring tasks.json
   ./tasks.json run start
   ```

3. **Access the services**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

4. **View logs**:
   ```bash
   docker-compose logs -f
   ```

5. **Stop the services**:
   ```bash
   docker-compose down
   ```

## Development

### Available Commands

The project uses `tasks.json` for common operations (coming soon).

### Project Status

This project is currently in **infrastructure setup** phase. The development environment, API scaffold, and frontend scaffold are being created.

## Architecture

### Local-Only MVP

For the MVP, all infrastructure runs locally via Docker:
- No cloud hosting
- No authentication
- SQLite database
- Single-user only

### Post-MVP

Future features will include:
- Cloud hosting deployment
- Authentication and multi-user support
- PostgreSQL migration
- External observability tools
- iPhone Shortcuts integration
- AI trend analysis

## Contributing

This is a personal project for learning and experimentation.

## License

MIT

