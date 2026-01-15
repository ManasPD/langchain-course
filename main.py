from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
#from tavily import TavilyClient
from langchain_tavily import TavilySearch

#tavily = TavilyClient()
#@tool
#def search(query: str) -> str:
  # Tool that searches over internet
  #  Args:
  #      query: The query to search for
  #  Returns:
  #      The search results
  #  """
  #  print(f"Searching for {query}")
  #  return tavily.search(query=query)

llm = ChatOllama(model="gpt-oss:20b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)
def main():
    #print(os.getenv("OPENAI_API_KEY"))
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo?")})
    print(result)

if __name__ == "__main__":
    main()
