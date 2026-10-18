from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)


llm = ChatOpenAI(
    base_url="http://localhost:8000/v1/",
    model="gemma-4-12B-it-4bit",
    seed=42
)

for chunk in llm.stream("Write a long eassy on generative ai"):
    print(chunk.content, end="", flush=True)
print("\n\n")