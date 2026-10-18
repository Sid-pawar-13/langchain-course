
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

#from langchain_ollama import ChatOllama

load_dotenv()

@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet.
    Args:
        query: The query to search for
    Returns:
        The search return
    """
    print(f"Searching for {query}")
    return "Tokyo has sunny weather"



llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0
    )
#llm = ChatOllama(model="gemma4:12b-mlx", temperature=0)

tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")

    result = agent.invoke({"messages":[HumanMessage(content="What is the weather in Tokyo?")]})

    print(result)

if __name__ == "__main__":
    main()