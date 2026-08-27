from dotenv import load_dotenv, find_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm  # Import the LiteLLM backend

# Load environment keys
load_dotenv(find_dotenv())
            
# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

groq_model = LiteLlm(model="groq/openai/gpt-oss-120b")

root_agent = Agent(
    model=groq_model,
    name="time_agent",
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)
