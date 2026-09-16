import pathlib
from dotenv import load_dotenv, find_dotenv

from google.adk import Agent
from google.adk.skills import load_skill_from_dir 
from google.adk.tools.skill_toolset import SkillToolset
from google.adk.models.lite_llm import LiteLlm
from google.adk.code_executors.unsafe_local_code_executor import UnsafeLocalCodeExecutor

load_dotenv(find_dotenv())

weather_skill = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "weather-skill"
)

agent_skils = SkillToolset(
    skills=[weather_skill],
    code_executor=UnsafeLocalCodeExecutor()
)

groq_model = LiteLlm(model="groq/openai/gpt-oss-120b")

root_agent = Agent(
    name="skill_user_agent",
    model=groq_model,
    description="an agent that can use specilized skills",
    tools=[agent_skils]
)
