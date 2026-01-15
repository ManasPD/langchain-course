from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print(os.getenv("OPENAI_API_KEY"))
    print("Hello from langchain-course!")
    


if __name__ == "__main__":
    main()
