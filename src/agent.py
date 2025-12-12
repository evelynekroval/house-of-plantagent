from langchain.agents import create_agent  # import function to create agents
from langchain_openai import ChatOpenAI  # ChatOpenAI model wrapper
from langgraph.checkpoint.memory import InMemorySaver  # in-memory checkpointer for states
from langchain.agents.structured_output import ToolStrategy  # structured output strategy for agent responses
from dataclasses import dataclass  # dataclass decorator for simple data containers
import os  # access environment variables
from dotenv import load_dotenv  # helper to load .env files into environment
from tools import vegan_search # Import the vegan search tool I've defined.
from middleware import dynamic_model_selection, handle_tool_errors, basic_model, advanced_model, COMMON_MODEL_KWARGS


# Load environment variables
load_dotenv()

# Get the OpenAI API Key for the model
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Now LangSmith
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")  # read Langsmith API key from environment

# Now Tavily
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Define the model separately - allows better customisation
# model = ChatOpenAI(  # instantiate the ChatOpenAI model with desired settings
#     model="gpt-5",  # model name to use
#     temperature=0.1,  # low temperature for more deterministic outputs
#     timeout=60,  # request timeout in seconds
# )

# SYSTEM_PROMPT: multi-line system instruction for the agent. 
# Could this be part of what's causing the error?
SYSTEM_PROMPT = """You are an expert vegan/plant-based nutritionist and meal generator.
Your name is House of PlantAgent.

You have access to one tool, which you MUST use before generating each new recipe-generated response:

- tavily_search_tool: use this to search for a vegan recipe based on the user's stated preferences.

Rules:
- Think step-by-step.
- Based on your tool results, provide the ingredients, quantities, and cooking instructions in return to the user query.
- If the user asks non-recipe related questions, state that your purpose is only to generate user recipes.


"""

@dataclass
class Context:
    """Custom runtime context schema."""
    user_id: str

# # I always wonder if I should write more for this? Or call a parent class? Idk

checkpointer = InMemorySaver()  # create an in-memory checkpointer for conversation state

# # `thread_id` is a unique identifier for a given conversation.
config = {"configurable": {"thread_id": "1"}}

# @dataclass  # response schema for structured agent outputs
# class ResponseFormat:
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
#     # The ingredients required to make the recipe.
#     recipe_ingredients: str
#     # Cooking instructions for the recipe
#     recipe_instructions: str


# Create the agent
agent = create_agent(
    model=basic_model,
    system_prompt = SYSTEM_PROMPT,
    tools=[vegan_search],
    middleware=[dynamic_model_selection, handle_tool_errors],
    context_schema=Context,
    checkpointer=checkpointer,
    # response_format=ToolStrategy(ResponseFormat),
)

question = "What's an easy tofu and noodle recipe?"

for step in agent.stream(
    {"messages": {"role": "user", "content": question}},
    stream_mode="values",
    config=config,
    context=Context(user_id="1")
):
    step["messages"][-1].pretty_print()

