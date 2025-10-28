# Personal Time Logger — Product & Tech Spec (v0.2)

## 1) One-liner

A private, low-friction system to log daily activities and visualize time use, starting local-only and growing into a small multi-user web app.

## 2) Problem & Goals

**Problem.** Manual tracking is tedious and scattered (notes, memory, spreadsheets).
**Goals.**

* Make logging **fast** and **simple** so it actually happens.
* Provide **clear visualizations** that inform habit and planning.
* Start **local-only** (single user), then evolve to **secure multi-user** with hosted access.

**Non-goals (for MVP).**

* Authentication and multi-user.
* iPhone Shortcuts / Focus-mode automations.
* Backups, rate limits, or complex ops.

## 3) Use Cases

1. **Quick Start/Stop** a running activity in the browser.
2. **Quick Duration Add** (e.g., “Reading — 20 min” after the fact).
3. **Review** today/week/last 30 days with category breakdowns.
4. **Export** CSV for deeper analysis (Sheets/Jupyter).

*Post-MVP additions:*

* Secure API endpoints callable from iPhone Shortcuts/Focus automations.
* AI trend analysis on historical data (identify changes, anomalies, streaks, goals).

## 4) Scope

### MVP (single user, local-only)

* React + Vite frontend (served locally for dev; static build).
* FastAPI backend.
* SQLite database.
* No authentication.
* Features: Start/Stop logs; quick duration logs; categories/tags/notes; basic charts (day/week/30-day); CSV export.
* Deployment: local dev only. (Public hosting **after** MVP.)

### Post-MVP (public hosting & small multi-user)

* **Hosting:**

  * Frontend: GitHub Pages (static).
  * Backend+DB: Hosting **TBD** (design for CI/CD to auto-deploy on push).
* **Security & Auth:** add authentication; user-scoped data separation.
* **DB:** migrate to PostgreSQL for multi-user scale and concurrency.
* **Automations:** iPhone Focus-mode → Shortcuts → authenticated API calls.
* **AI Insights:** analyze charts/data to produce trend summaries and suggestions.

## 5) Functional Requirements

* Create a log with `start_ts`, `end_ts` (or duration), `category`, optional `tags[]`, `note`, `source` (ui/import).
* Exactly one active running log at a time; starting a new one auto-stops the previous.
* Edit/merge/split logs.
* List/filter by time range, category, tag.
* Export CSV for any filter.

## 6) Non-Functional Requirements

* **MVP:** Simple, local, dependable. No auth, no rate limits, no backup.
* **Post-MVP:** Add auth, HTTPS, CI/CD, and consider backups & observability.

## 7) Data Model (MVP: SQLite → Post-MVP: PostgreSQL)

**tables**

* `log`

  * `id` (pk)
  * `start_ts` (utc iso)
  * `end_ts` (utc iso, nullable if running)
  * `category_id` (fk)
  * `note` (text)
  * `source` (enum: ui, import)
  * `created_at`, `updated_at`
* `category`

  * `id` (pk), `name` (unique), `color_hex` (optional), `is_active` (bool)
* `tag`

  * `id` (pk), `name` (unique)
* `log_tag`

  * `log_id` (fk), `tag_id` (fk), composite pk

**Post-MVP (multi-user):**

* Add `user` table.
* Add `user_id` to `log`, `category`, `tag` (scoping).
* Unique constraints become `(user_id, name)` where applicable.

## 8) API (MVP)

*All endpoints unauthenticated (local-only). JSON in/out.*

* `POST /api/logs/start` → `{ category, tags?, note? }`
  Starts a new running log; auto-stops any existing running log.
* `POST /api/logs/stop` → stops current running log.
* `POST /api/logs/quick` → `{ category, duration_min, tags?, note? }`
* `GET /api/logs?from=&to=&category=&tag=` → list/filter logs.
* `PATCH /api/logs/{id}` → edit fields (incl. `end_ts`).
* `POST /api/export/csv?from=&to=` → streamed CSV.

**Post-MVP (automations & auth):**

* Add token-based auth (e.g., OAuth2 password flow / JWT or session).
* Rate limits and CSRF as appropriate for public endpoints.
* Maintain simple URLs for iPhone Shortcuts (manual setup on device).

## 9) UX Notes

* **Home:** prominent Start/Stop button with active timer and current category.
* **Quick Add:** category chips; optional tags and note field; commonly used presets.
* **Review:** Today / Week / 30-day tabs with bar/pie charts; top tags and totals.
* **Edit:** timeline view with drag handles for adjusting start/end; merge/split.

## 10) Architecture

* **Frontend:** React + Vite → static assets (for prod: GitHub Pages).
* **Backend:** FastAPI (REST), served by Uvicorn/Gunicorn (prod).
* **DB:** SQLite (MVP) → PostgreSQL (post-MVP).
* **Build/Deploy:**

  * MVP: local dev scripts.
  * Post-MVP: CI/CD pipeline (build frontend, run tests, deploy backend+DB to chosen host).

## 11) Security & Privacy

* **MVP:** Local-only; no auth; not exposed to the internet.
* **Post-MVP:** Public hosting with HTTPS, authentication, user data isolation, and least-privilege DB access.

## 12) Risks & Mitigations

* **Scope creep:** Keep MVP minimal (no auth, no automations).
* **Migration risk (SQLite → Postgres):** Use SQLAlchemy + migrations (Alembic) from the start to smooth upgrade.
* **Unauthenticated endpoints:** Only acceptable in local-only MVP; block external exposure until auth is ready.

## 13) Testing

* **Unit:** time arithmetic (overlap prevention, rounding, merges).
* **Integration:** API contract tests for Start/Stop/Quick/Export.
* **UI:** smoke tests for main flows (Start→Stop→Review).
* **Post-MVP:** auth tests, user scoping, and external endpoint hardening.

## 14) Prioritization (MoSCoW, no numbers)

* **Must (MVP):** Start/Stop, quick duration, list/filter, basic charts, CSV export, SQLite, local-only.
* **Should (post-MVP):** Auth + user scoping, Postgres migration, hosted backend, CI/CD.
* **Could:** iPhone Shortcuts/Focus-mode automations (once auth exists).
* **Later:** AI trend analysis and suggestions.

## 15) Milestones

* **M1 — Skeletons:**

  * Repo setup, React+Vite app scaffold, FastAPI scaffold, SQLite via SQLAlchemy/Alembic.
* **M2 — Core Logging:**

  * `/api/logs/start|stop|quick`, overlap rules, basic list/filter, seed categories.
* **M3 — Dashboards & Export:**

  * Today/Week/30-day charts; CSV export; edit/merge/split.
* **M4 — Hardening for Public (post-MVP):**

  * Choose hosting for backend+DB; add auth and user scoping; CI/CD; migrate to Postgres.
* **M5 — Automations & AI (post-MVP):**

  * Shortcut-friendly endpoints with auth, AI trend insights.

## 16) Acceptance Criteria (MVP)

* Start a running log and auto-stop the previous one with a new start.
* Add a duration-based log in a single form.
* View accurate totals for Today/Week/30-day that match CSV export for the same range.
* Edit/merge/split produces consistent, non-overlapping data.
* App runs locally with no external dependencies beyond the browser.

## 17) Future: AI Insights (high-level)

* Summarize weekly trends (time per category, deltas vs. previous period).
* Detect anomalies (unusual spikes/drops) and highlight potential causes (tags/notes).
* Surface streaks and adherence to self-defined targets.
* Natural-language insights card on the dashboard.

---

### Developer Notes & Decisions

* **State Mgmt (FE):** Start with React Query for API caching; minimal global state.
* **Charts:** Recharts or Chart.js (whichever you prefer) with a light theme.
* **Dates/Times:** Store UTC in DB; convert to local in UI.
* **Migrations:** Use Alembic from day one even on SQLite to simplify Postgres migration.
* **Auth (post-MVP):** Likely session cookies or OAuth2 password flow; keep Shortcut calls token-based.

### Immediate Next Steps

1. Initialize React+Vite and FastAPI scaffolds.
2. Define SQLAlchemy models + Alembic baseline.
3. Implement `start/stop/quick` endpoints and overlap enforcement.
4. Build Home (Start/Stop) and Review (basic charts) pages.
5. CSV export and simple edit/merge/split UI.