from langchain_tavily import TavilySearch  # Tavily search tool (external integration)
import os  # access environment variables
from dotenv import load_dotenv  # helper to load .env files into environment
from langchain.tools import tool
load_dotenv()




TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")  # read Tavily API key from environment


@tool
def scrying_the_skies(user_query:str) -> dict:
    """Main web-search tool for vegan recipes.
    
    Args:
        user_query: obtained from user conversation

    Return: 
        customised_search_results: a dictionary containing:
            title: recipe's title
            url: recipe's url
            content: full recipe content, including instructions and ingredients.

    """

    search_tool = TavilySearch(  # create a TavilySearch instance with basic settings
            max_results=1,  # only keep the top result
            topic="general",  # general topic search
            search_depth = "advanced",  # depth parameter for the search
        )
    print(f"\nSearching for '{user_query}'")
    full_search_results = search_tool.invoke(user_query)
    
    customised_search_results = {
        "title":full_search_results["results"][0]["title"],
        "url": full_search_results["results"][0]["url"],
        "content":full_search_results["results"][0]["content"]
    }

    return customised_search_results
