# Data Chord

Data harmonization workflow application. Upload tabular data, review AI-suggested column mappings, run harmonization, and approve results before export.

For a comprehensive overview of what Data Chord does and why, see [app.md](app.md).

## First-Time Setup

### 1. Install uv (Python package manager)

Data Chord uses [uv](https://docs.astral.sh/uv/) to manage Python and dependencies. You don't need to install Python separately — uv handles that automatically. See the [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/) for other install methods or troubleshooting.

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installing, **close and reopen your terminal** so the `uv` command is available.

Verify it works:
```bash
uv --version
```

### 2. Clone the repository

```bash
git clone https://github.com/netrias/data_chord.git
cd data_chord
```

### 3. Install dependencies

```bash
uv sync
```

This automatically downloads the correct Python version (3.13+) and installs all project dependencies into an isolated virtual environment. Nothing is installed globally on your system.

### 4. Configure environment variables

```bash
cp .env.example .env
```

Open `.env` in a text editor and replace `your_api_key_here` with your Netrias API key (contact Netrias for access).

### 5. Run the application

```bash
uv run uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000 in your browser. You should see the Data Chord upload screen.

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `NETRIAS_API_KEY` | Yes | API key for Netrias harmonization, CDE discovery, and Data Model Store |

## Docker

```bash
# Build
docker build -t data-chord .

# Run
docker run -p 8000:8000 --env-file .env data-chord
```

## Development

If you have [just](https://github.com/casey/just) installed, run `just --list` for available shortcuts:

```bash
just sync        # Install with dev dependencies
just app-reload  # Run with auto-reload
just test        # Run tests
just lint        # Lint
just typecheck   # Type check
```

Or use the underlying commands directly:

```bash
uv sync --extra dev
uv run pytest
uv run ruff check src backend tests
uv run basedpyright
```

## Workflow Stages

1. **Upload** - Upload CSV file and analyze columns
2. **Review Columns** - Review/override AI-suggested column-to-model mappings
3. **Harmonize** - Execute harmonization pipeline
4. **Review Results** - Inspect and approve harmonized values
5. **Review Summary** - Review change statistics and download harmonized dataset

## CDE Endpoint Configuration

Data Chord uses [netrias-client](https://github.com/netrias/netrias_client) for CDE discovery and harmonization. See [ADR 005](adr/ADR_005_cde_lambda_migration.md) for migration details and rollback procedure.
