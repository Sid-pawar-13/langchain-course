from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv(override=True)


tools = [TavilySearch()]

llm = ChatOpenAI(
    base_url="http://localhost:8000/v1/",
    model="mlx-community/gemma-4-12B-it-4bit",
    seed=42
)

search_agents = create_agent(
    model=llm,
    tools=tools
)

response = search_agents.invoke({"messages":HumanMessage(content="tell about ollama in 10 words")})

print(response["messages"][-1].content)
print("Usage_metadata",response["messages"][-1].usage_metadata)