import requests
import os
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from typing import Any

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

async def serpapi_search(query:str) -> dict[str,Any]:
    """
    Perform a gogle search using serpAPI. 
    
    Args: 
        api_key (str) : your serp api key
        query (str) : search query string 
        
    Returns:
        dict : JSON response from api 
        
    """
    
    api_key = os.getenv("SERP_API_KEY")
    url = os.getenv("SERP_API_URL")
    
    params = {
        "engine":"google",
        "q":query,
        "api_key":api_key
    }
    
    response = requests.get(url,params=params)
    
    response.raise_for_status()
    return response.json()


def reverse_str(s:str) -> str:
    return s[::-1]


# tools 

serpi_tool = FunctionTool(func=serpapi_search)
reverse_string_tool = FunctionTool(func=reverse_str)


root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="agent with multiple tools",
    instruction="Your a helpful agent who can search on internet and reverse string based on user query",
    tools=[serpi_tool,reverse_string_tool]
)