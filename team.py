from agno.agent import Agent
from agno.models.groq import Groq
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()

eng_agent = Agent(name="English Agent",role=" Answer in english ")
chi_agent = Agent(name="Chinese Agent",role=" Answer in chinese ")
germ_agent = Agent(name="German Agent",role=" Answer in German ")

team_leader= Team(
    name="Answer and translation team",
    members=[eng_agent,chi_agent,germ_agent],
    model=Groq(id="openai/gpt-oss-20b"),
    markdown=True,
    show_members_responses=True,
    instructions=""" All member agents must respond to answer the query in their specific language. 
                        Do not route to just one agent.
                        Output the response of all agents.
                """
)

team_leader.print_response("What is the capital of india ? ")