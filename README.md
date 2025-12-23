# House of PlantAgent

The project is a vegan / plant-based nutrition and cuisine LLM agent that:

- Does not generate recipes from model memory.
- Retrieves real recipes from the Internet.

## Quick Start

### Prerequisites
- Python 3.10 or higher (preferably 3.13)
- `uv` (instead of `pip`)

### Installation

1. **Clone the repository and navigate to the root:**
   ```bash
   cd house-of-plantagent
   ```

2. **Create and activate a virtual environment:**
   ```bash
   uv venv .venv
   source .venv/bin/activate
   ```

3. **Install the project with dev dependencies:**
   ```bash
   uv sync
   ```

4. **Copy the environment template and configure:**
   ```bash
   cp .env.example .env
   # Edit .env with your recipe source URL, model endpoint, etc.
   ```

## Architecture Overview

https://drive.google.com/file/d/1mVlCivBxm1Sefn0bzI8IMZ5maSdmqDSU/view?usp=sharing

## Project Structure

[To be updated as project nears completion. However, note the `src/` folder containing the various scripts, as well as the `PROGRESS_DIARY.md` in the root folder.]

See `.github/copilot-instructions.md` for AI agent guidance.