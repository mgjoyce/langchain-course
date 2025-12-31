from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from langchain_tavily import TavilySearch

# from langchain_openai import ChatOpenAI
# llm =ChatOpenAI()

from langchain_ollama import ChatOllama
llm = ChatOllama(model="gpt-oss:20b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    print("Hello from Te Awamutu!")
    result = agent.invoke({ "messages": HumanMessage(content="search for 3 job postings in seek nz for senior it roles in the Auckland area")})
    print(result)

if __name__ == "__main__":
    main()
