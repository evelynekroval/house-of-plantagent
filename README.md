# House of PlantAgent

The project is a vegan / plant-based nutrition and cuisine LLM agent that:

- Does not generate recipes from model memory.
- Retrieves real recipes from predetermined online sources.
- Applies retrieval, filtering, and scoring based on user preferences (ingredients, cuisines, dislikes).
- Integrates nutritional analysis using open data sources, scraping, or offline ingestion pipelines.
- Keeps track of user's minimum nutritional needs for a "well-planned vegan diet".
- Demonstrates the user's grasp of RAG, grounding, and agentic orchestration patterns.

## Quick Start

### Prerequisites
- Python 3.10 or higher
- `pip` (comes with Python)

### Installation

1. **Clone the repository and navigate to the root:**
   ```bash
   cd house-of-plantagent
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the project with dev dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Copy the environment template and configure:**
   ```bash
   cp .env.example .env
   # Edit .env with your recipe source URL, model endpoint, etc.
   ```

5. **Run tests to verify setup:**
   ```bash
   pytest
   ```

You're ready to start developing!

## Architecture Overview

[To be updated as project grows—see `.github/copilot-instructions.md` for AI agent guidance.]

## Project Structure

```
house-of-plantagent/
├── .venv/                      # Virtual environment (auto-generated)
├── src/                        # Main agent code
│   ├── __init__.py
│   ├── retrieval/              # Recipe retrieval & filtering
│   ├── grounding/              # Nutritional grounding & validation
│   └── orchestration/          # Agentic loop & decision logic
├── tests/                      # Unit & integration tests
│   ├── __init__.py
│   └── test_*.py
├── notebooks/                  # Exploratory notebooks (not part of package)
├── data/                       # Local data files (recipes, nutrition DB)
├── pyproject.toml              # Project metadata & dependencies
├── .env.example                # Config template (don't commit .env)
└── README.md                   # This file
```

## Development Workflow

```bash
# Activate environment
source .venv/bin/activate

# Run tests
pytest

# Format code
black src/

# Lint
ruff check src/

# Type check
mypy src/
```

## Next Steps

- [ ] Decide on orchestration framework (LangChain, LlamaIndex, or custom loop).
- [ ] Identify recipe data sources (APIs or scraping targets).
- [ ] Build the retrieval pipeline.
- [ ] Integrate nutritional grounding.
- [ ] Implement the agentic orchestration loop.

See `.github/copilot-instructions.md` for AI agent guidance.