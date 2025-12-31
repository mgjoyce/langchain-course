from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from langchain_tavily import TavilySearch

from langchain_openai import ChatOpenAI
llm =ChatOpenAI()

class Source(BaseModel):
    """Scheme for a source used by the agent"""
    url: str = Field(..., description="URL of the source")

class AgentResponse(BaseModel):
    """Scheme for the response from the agent"""
    answer: str = Field(..., description="Answer from agent")
    sources: List[Source] = Field(default_factory=list, description="Sources used by the agent")

from langchain_ollama import ChatOllama
#llm = ChatOllama(model="gpt-oss:20b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    print("Hello from Te Awamutu!")
    result = agent.invoke({ "messages": HumanMessage(content="search for 3 job postings in seek nz for senior it roles in the Auckland area")})
    print(result)

if __name__ == "__main__":
    main()
