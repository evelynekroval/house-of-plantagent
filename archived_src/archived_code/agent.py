from langchain.agents import create_agent, AgentState  # import function to create agents
from langchain_openai import ChatOpenAI  # ChatOpenAI model wrapper
from langgraph.checkpoint.memory import InMemorySaver  # in-memory checkpointer for states
from pydantic import BaseModel
import os  # access environment variables
from dotenv import load_dotenv  # helper to load .env files into environment
from tools import scrying_the_skies # Import the vegan search tool I've defined.
from middleware import handle_tool_errors
from typing import Optional
from system_prompt import SYSTEM_PROMPT


# Load environment variables
load_dotenv()

# Get the OpenAI API Key for the model
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Context class
class Context(BaseModel):
    """Pydantic context schema — safe for libraries that may call Context() internally."""
    user_id: Optional[str] = None
    
# Memory checkpointer.

checkpointer = InMemorySaver()  # create an in-memory checkpointer for conversation state

# # `thread_id` is a unique identifier for a given conversation.
config = {"configurable": {"thread_id": "1"}}

class CustomState(AgentState):
    pass
    
model = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature = 0.3,
    timeout = 60
    )

# Create the agent
agent = create_agent(
    model=model,
    system_prompt = SYSTEM_PROMPT,
    tools=[scrying_the_skies],
    middleware=[handle_tool_errors],
    context_schema=Context,
    checkpointer=checkpointer,
    state_schema=CustomState
)

