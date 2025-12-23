from langchain.agents import create_agent, AgentState  # import function to create agents
from langchain_openai import ChatOpenAI  # ChatOpenAI model wrapper
from langgraph.checkpoint.memory import InMemorySaver  # in-memory checkpointer for states
from langchain.agents.structured_output import ToolStrategy, ProviderStrategy  # structured output strategy for agent responses
from dataclasses import dataclass  # dataclass decorator for simple data containers
from pydantic import BaseModel
import os  # access environment variables
from dotenv import load_dotenv  # helper to load .env files into environment
from tools import scrying_the_skies # Import the vegan search tool I've defined.
from middleware import (
    dynamic_model_selection, 
    handle_tool_errors, 
    basic_model, 
    advanced_model, 
    COMMON_MODEL_KWARGS)
from typing import (
    Any,
    Optional
    )



# Load environment variables
load_dotenv()

# Get the OpenAI API Key for the model
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Now LangSmith
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")  # read Langsmith API key from environment

# Now Tavily
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# SYSTEM_PROMPT: multi-line system instruction for the agent. 
SYSTEM_PROMPT = """You are an expert vegan/plant-based nutritionist and meal generator.
You are also Eleanor of Aquitane of the House of PlantAgent. You imbue the personality of your historical reference in all of your responses.

First and firemost, respond with the attitude befitting of Eleanor of Aquitane, and only then output the necessary recipe information.

You have access to one main tool, which you MUST use before generating each new recipe-generated response. 
Call it only ONCE per query:

- `scrying_the_skies`: use this to search for a vegan recipe based on the user's stated preferences.

Your other tools are:
- `handle_tool_errors`: use this where the search term is not appropriate to your role and you need the user to reconsider their query.

Rules:
- Think step-by-step.
- Based on your tool results, provide the ingredients, quantities, and cooking instructions in return to the user query.
- If the user asks non-recipe related questions, state that your purpose is only to generate user recipes.

From `scrying_the_skies`'s output, {customised_search_results}, output in this format:
'Alas, I hath found {title} from this realm: {url}. Behold:

{content}

'
Chat history: {chat_history}
"""

class Context(BaseModel):
    """Pydantic context schema — safe for libraries that may call Context() internally."""
    user_id: Optional[str] = None

# # I always wonder if I should write more for this? Or call a parent class? Idk

checkpointer = InMemorySaver()  # create an in-memory checkpointer for conversation state

# # `thread_id` is a unique identifier for a given conversation.
config = {"configurable": {"thread_id": "1"}}

# # Creating response format.
# class ResponseFormat(BaseModel):
#     """Response schema for the agent.
#     All are compulsory.
#     """
#     # Title of the recipe received in the search results
#     recipe_title: str 
#     # The URL of te recipe received in search results
#     recipe_url: str
#     # Prep time - if available from search results
#     recipe_prep_time: str
#     # Cooking time - if available from search results
#     recipe_cook_time: str
#     # Rest of response - this forms the longest part of the generation and contains:
#     # 1: The ingredients required to make the recipe.
#     # 2: Cooking instructions for the recipe
#     rest_of_response: str

class CustomState(AgentState):
    pass
    


# Create the agent
agent = create_agent(
    model=basic_model,
    system_prompt = SYSTEM_PROMPT,
    tools=[scrying_the_skies],
    middleware=[dynamic_model_selection, handle_tool_errors],
    context_schema=Context,
    # checkpointer=checkpointer,
    state_schema=CustomState
    # response_format=ProviderStrategy(ResponseFormat),
)

question = "What's an easy tofu and noodle recipe?"

for chunk in agent.stream({
    "messages": [{"role": "user", "content": question}],
    # "user_preferences": [{"style": "culinary", "verbosity": "minimal"}]
}, context=Context(user_id="1"),
    stream_mode="values",
    config=config,
    ):
    # Each chunk contains the full state at that point
    latest_message = chunk["messages"][-1]
    if latest_message.content:
        print(f"Agent: {latest_message.content}")
    elif latest_message.tool_calls:
        print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")


