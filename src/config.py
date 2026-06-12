import os
from dotenv import load_dotenv

# Prefer Groq, fall back to OpenAI if configured.
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm():
    """Return an LLM client configured for Groq only.

    Required env:
      - GROQ_API_KEY

    Optional:
      - GROQ_MODEL (default: llama-3.1-70b-versatile)
    """

    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise RuntimeError("GROQ_API_KEY is not set. Add it to your .env")

    groq_model = os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile")
    return ChatGroq(groq_api_key=groq_api_key, model=groq_model)

