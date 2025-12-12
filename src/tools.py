from langchain_tavily import TavilySearch  # Tavily search tool (external integration)
import os  # access environment variables
from dotenv import load_dotenv  # helper to load .env files into environment
from langchain.tools import tool, ToolRuntime  # tool decorator and runtime typing
load_dotenv()

TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")  # read Tavily API key from environment

tavily_search_tool = TavilySearch(  # create a TavilySearch instance with basic settings
        max_results=1,  # only keep the top result
        topic="general",  # general topic search
        search_depth = "advanced",  # depth parameter for the search
    )

test_results = tavily_search_tool.invoke("tofu and noodle soup")

url=test_results["results"][0]["url"]