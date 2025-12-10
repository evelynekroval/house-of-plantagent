# Import required packages
import os
import json
from dataclasses import dataclass
from langchain_core.tools import tool
from langgraph.runtime import get_runtime
from langchain.agents import create_agent

# For web-searching tool
from langchain.tools import tool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

# Access APIs from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

# System prompt for agent

SYSTEM_PROMPT = """You are an expert vegan/plant-based nutritionist and meal generator.
Your name is House of PlantAgent.

Rules:
- Think step-by-step.
- Provide a list of ingredients, quantities, and cooking instructions in return to the user query for recipe.
- If the user asks non-recipe related questions, state that your purpose is only to generate user recipes.

You have access to one tool, which you MUST use before generating each new recipe-generated response:

- search_plantbased_recipe: use this to search vegan recipe websites based on the user's stated preferences.
"""

# Creating runtime context
@dataclass
class RuntimeContext:
    """Custom runtime context schema."""
    pass


# Defining the tool
@tool
def search_plantbased_recipe(query:str) -> str:
    """
    Safe wrapper that always returns a string.
    Use this as the tool passed to the agent.

    Argument 'query': The search query string"""
    runtime = get_runtime(RuntimeContext)
    try:
        wrapper = DuckDuckGoSearchAPIWrapper()
        try:
            # prefer .run()
            result = wrapper.run(query)
        except Exception:
            # fallback if the wrapper method differs
            result = wrapper.run(query)

        # If result is already a string, return it.
        if isinstance(result, str):
            return result
        # If it's a dict/list/obj, try to serialise to json as safe fallback
        try:
            return json.dumps(result, default=str, ensure_ascii=False)
        except Exception:
            return str(result)
    except Exception as e:
        # Always return a string without raising so the agent gets a tool response
        return f"ERROR in search_plantbased_recipe: {type(e).__name__}: {e}"