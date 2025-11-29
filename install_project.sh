#!/usr/bin/env bash


uv sync


# Detect platform and activate accordingly
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    # Windows (Git Bash/MSYS/WSL)
    source .venv/Scripts/activate
else
    # macOS and Linux
    source .venv/bin/activate
fi


