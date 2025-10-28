# API Contracts

## Current Status

**No API contracts exist yet.**

This feature (`001-setup-project-infrastructure`) creates the infrastructure scaffolds only. No application endpoints are implemented.

## Future API Contracts

When implementing actual application features, API contracts will be documented here in OpenAPI/Swagger format.

### Expected Structure

```
contracts/
├── README.md                    # This file
├── backend-openapi.yaml         # FastAPI automatic OpenAPI schema (generated)
└── endpoint-contracts.md        # Manual contract specifications
```

### Contract Types

- **Backend FastAPI**: Automatically generated from FastAPI route handlers
- **Frontend**: TypeScript interfaces matching backend responses
- **Integration**: Request/response examples for manual testing

## Standards

- All endpoints use JSON for request/response bodies
- UTC timestamps stored internally
- Consistent error format across all endpoints
- OpenAPI documentation accessible at `/docs` endpoint

## Next Steps

API contracts will be created when implementing:
- Feature `002-*` (Core activity logging features)
- Feature `003-*` (Dashboard and visualization features)

