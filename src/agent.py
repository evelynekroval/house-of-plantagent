from langchain.agents import create_agent  # import function to create agents
from langchain_openai import ChatOpenAI  # ChatOpenAI model wrapper
from langgraph.checkpoint.memory import InMemorySaver  # in-memory checkpointer for states
from langchain.agents.structured_output import ToolStrategy  # structured output strategy for agent responses
from dataclasses import dataclass  # dataclass decorator for simple data containers
import os  # access environment variables
from dotenv import load_dotenv  # helper to load .env files into environment

# Load environment variables
load_dotenv()

# Get the OpenAI API Key for the model
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Now LangSmith
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")  # read Langsmith API key from environment

# Define the model separately - allows better customisation
model = ChatOpenAI(  # instantiate the ChatOpenAI model with desired settings
    model="gpt-5",  # model name to use
    temperature=0.1,  # low temperature for more deterministic outputs
    timeout=30,  # request timeout in seconds
)

# Create the agent