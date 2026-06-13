import os
from dotenv import load_dotenv

# Prefer Groq, fall back to OpenAI if configured.
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm():
    """Return an LLM client configured for Groq only.

    Required (set in .env locally, or in Streamlit Secrets when deployed):
      - GROQ_API_KEY

    Optional:
      - GROQ_MODEL (default: llama-3.1-70b-versatile)
    """

    groq_api_key = os.getenv("GROQ_API_KEY")

    # Fallback: if running on Streamlit Cloud, secrets may not yet be
    # mirrored to os.environ in some edge cases -- check st.secrets too.
    if not groq_api_key:
        try:
            import streamlit as st
            groq_api_key = st.secrets.get("GROQ_API_KEY")
        except Exception:
            pass

    if not groq_api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Add it to your .env (local) "
            "or to Streamlit Secrets (when deployed)."
        )

    groq_model = os.getenv("GROQ_MODEL") or "llama-3.1-70b-versatile"
    return ChatGroq(groq_api_key=groq_api_key, model=groq_model)