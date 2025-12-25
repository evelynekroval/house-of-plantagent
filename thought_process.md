
It seems that that only relevant code is in app.py

Check dependencies? Only streamlit and openai stated, clear the packages in pyproject.toml
manually add streamlit and openai  (this makes it simpler)

eg go from

```

dependencies = [
    "requests>=2.31.0",      # HTTP library for web scraping recipes
    "python-dotenv>=1.0.0",  # Loads environment variables from .env files
    "pytest>=7.4.0",         # Testing framework
    "pytest-cov>=4.1.0",     # Code coverage measurement plugin for pytest
    "ipykernel>=7.1.0",
    "ruff>=0.14.7",
    "torchvision>=0.24.1",
    "jupyterlab>=4.5.0",
    "notebook>=7.5.0",
    "tiktoken>=0.12.0",
    "openai>=2.8.1",
    "langchain>=1.1.0",
    "langchain-openai>=1.1.0",
    "langchain-anthropic>=1.2.0",
    "transformers>=4.57.3",
    "ipywidgets>=8.1.8",
    "cheerio>=1.4",
    "axios>=0.4.0",
    "duckduckgo-search>=8.1.1",
    "langchain-community>=0.4.1",
    "ddgs>=9.9.2",
    "langchain-ollama>=1.0.0",
    "ollama>=0.6.1",
    "langchain-tavily>=0.2.13",
    "debugpy>=1.8.18",
    "streamlit>=1.52.1",
    "langgraph-cli[inmem]>=0.4.9",
    "streamlit-js-eval>=0.1.7",
]
```

```
dependencies = [

]
```

Manually uv add streamlit openai

```
uv add streamlit openai
```

(still a lot of dependencies, though!)

Add a shellcheck to check and apply automatic format fixes, and change lint setup in pyproject.toml
