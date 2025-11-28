<!--
This file guides AI coding agents working in this repository.
Observations: when this file was created the workspace contained no source files
or typical manifest files (`README.md`, `package.json`, `pyproject.toml`, etc.).
Update this doc after adding real project files so the examples below can be
replaced with concrete references.
-->

# Copilot / AI Agent Instructions — house-of-plantagent

Keep changes minimal, well-scoped, and test-backed. If the repository is empty
or missing expected manifests, ask the human before making large structural
changes.

- **Current snapshot:** No top-level source or manifest files were detected.
  If this is incorrect, trigger a workspace refresh or point the agent to the
  code root that contains `package.json`, `pyproject.toml`, `go.mod`, etc.

- **Primary objective:** Make atomic, reviewable edits that are easy for a
  human reviewer to validate. Prefer small PRs with one logical change and a
  short description of why the change was made.

- **How to discover the architecture (checklist):**
  - Look for `package.json`, `tsconfig.json`, `pyproject.toml`, `requirements.txt`, `go.mod`, `Cargo.toml`, or `pom.xml` to infer language and build tools.
  - Look for `README.md`, `docs/`, or `design/` for high-level architecture notes.
  - Search for `Dockerfile`, `docker-compose.yml`, `k8s/`, or `helm/` for deployment patterns.
  - If present, inspect `src/`, `cmd/`, `app/`, or `server/` directories for entrypoints.

- **Commands to run (detect & run safely):**
  - Node.js: if `package.json` exists run `npm ci` then `npm test`.
  - Python: if `pyproject.toml` or `requirements.txt` exists create venv, install, then `pytest`.
  - Go: if `go.mod` exists run `go test ./...`.
  - Rust: if `Cargo.toml` exists run `cargo test`.
  - Docker: run `docker build -t local/test .` only after asking if local builds are allowed.
  Always run tests before proposing changes.

- **Project-specific patterns & conventions (discoverable):**
  - If linting/formatting configs exist (`.eslintrc`, `pyproject.toml` with `black`, `.prettierrc`), follow those tools; run `npm run lint` / `pre-commit run --all-files` when present.
  - Look for files like `.env.example` or `config/*.yaml` for runtime configuration patterns.

- **Integration & secrets:**
  - If you find `aws/`, `gcp/`, `terraform/`, or CI workflows (`.github/workflows/`), assume external cloud infra integration — do not attempt to apply infra changes without human approval.
  - Never create or commit credentials. If secrets are needed, ask the user and prefer `.env.example` updates or documented secret names.

- **What a PR from the agent should contain:**
  - A short title and 2–4 line description explaining the change and why.
  - The exact commands used to test locally (e.g., `npm ci && npm test`).
  - Any files added/modified and why, plus suggested manual verification steps.

- **When to stop and ask:**
  - The repository is missing build/test manifests and you plan to add one (ask first).
  - You need secrets, access, or cloud-side privileges to validate changes.
  - A change affects CI, deployment, or infra (always ask before modifying `.github/workflows`, `Dockerfile`, or `terraform` files).

- **Example guidance (replace with real examples after repo discovery):**
  - "If you add a new endpoint, add an integration test under `tests/` and run `pytest`." — update paths to match actual test layout when discovered.

If anything here is unclear or you want the file tailored to the project's stack (Node/Python/Go/Rust), tell me which language or point me to the main source files and I'll update this file with concrete examples and commands.
