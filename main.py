from dotenv import load_dotenv
load_dotenv()


from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_ollama.chat_models import ChatOllama
# from langchain.tools import tool
# from tavily import TavilyClient
from langchain_tavily import TavilySearch


# tavily = TavilyClient()


# @tool
# def tavily_search(query: str) -> str:
#     """
#     Tool that searches over internet.
#     arg:
#         query:- The search term given by user.
#     returns:
#         The serch result.
#     """
#     return tavily.search(query=query)


llmmodel = ChatOllama(model='llama3.2:latest', temperature=0.2)
# customtools = [tavily_search]
customtools = [TavilySearch()]

agent = create_agent(model=llmmodel, tools=customtools)
response = agent.invoke({'messages':HumanMessage('what is current weather in punawale, pune?')} )
print(response)