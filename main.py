from dotenv import load_dotenv
load_dotenv()

from typing import List
from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_ollama.chat_models import ChatOllama
from langchain.tools import tool
from tavily import TavilyClient
# from langchain_tavily import TavilySearch



class Source(BaseModel):
    """schema for source in the repsonse"""
    url:str = Field(description="URL of the source")

class AgentResponse(BaseModel): 
    """schema for the anent response with answers and sources"""
    answer:str = Field(description="model answer for the user query")
    sources:List[Source] = Field(default_factory=list, description="list of all sources")



tavily = TavilyClient()


@tool
def tavily_search(query: str) -> str:
    """
    Tool that searches over internet.
    arg:
        query:- The search term given by user.
    returns:
        The serch result.
    """
    return tavily.search(query=query)


llmmodel = ChatOllama(model='llama3.2:latest', temperature=0.2)
customtools = [tavily_search]
# customtools = [TavilySearch()]

agent = create_agent(model=llmmodel, tools=customtools, response_format=AgentResponse)
response = agent.invoke({'messages':HumanMessage('what is current weather in punawale, pune?')} )
print(response)