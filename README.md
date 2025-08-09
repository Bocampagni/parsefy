# FastAPI Template

A simple FastAPI template using [uv](https://docs.astral.sh/uv/) for fast Python package management.

## Features

- 🚀 FastAPI web framework
- ⚡ uv for fast dependency management
- 🐳 Docker support
- 🎯 Python 3.12
- 🛠️ Makefile for common tasks
- 🧹 Code formatting and linting with ruff

## Quick Start

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed
- Python 3.12 (managed by uv)
- Make (for using Makefile commands)

### Development

1. Clone the repository:
```bash
git clone git@github.com:Bocampagni/fastapi-template.git
cd fastapi-template
```

2. Install dependencies:
```bash
make install
```

3. Run the development server:
```bash
make dev
```

The API will be available at:
- App: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Makefile Commands

The project includes a Makefile with common development tasks:

```bash
make help          # Show available commands
make install       # Install dependencies with uv
make dev          # Run FastAPI development server
make lint         # Run ruff linter
make format       # Format code with ruff
make docker-build # Build Docker image
make docker-run   # Run Docker container
make docker-stop  # Stop running Docker container
make clean        # Clean up Docker images and containers
```

### Docker

Build and run with Docker using Makefile:

```bash
make docker-build
make docker-run
```

Or manually:

```bash
docker build -t fastapi-template .
docker run -p 80:80 fastapi-template
```

## Code Quality

Format and lint your code:

```bash
# Format code and fix linting issues
make format

# Check code quality
make lint
```

## API Endpoints

- `GET /` - Hello World
- `GET /items/{item_id}` - Get item by ID with optional query parameter

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   └── main.py          # FastAPI application
├── dockerfile           # Docker configuration
├── pyproject.toml       # Project dependencies
├── uv.lock             # Dependency lock file
├── Makefile            # Common development tasks
└── README.md
```

## Adding Dependencies

```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Sync dependencies
make install
```