from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-20b"),
        instructions=" You are an expert and helpful travel agent",
        add_datetime_to_context=True,
        tools=[DuckDuckGoTools()],
    )
agent = build_agent()

agent.print_response("Is it safe to travel to UAE today")


