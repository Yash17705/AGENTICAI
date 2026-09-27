from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()


def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3.8-27b"),
        markdown=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=[
            "Use given tools whenever possible format your response using markdown and use tables to display data where possible.",
        ],
        add_datetime_to_context=True,
        tools=[YFinanceTools(all=True), DuckDuckGoTools()],
        debug_mode=True
    )


if __name__ == "__main__":
    agent = build_agent()
    agent.print_response(
        "Share the MSFT stock price in INR and analyst recommendation",
        markdown=True,
        show_tool_calls=True,
    )