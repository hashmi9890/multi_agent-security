from src.config import get_llm


class ResearchAgent:
    """
    Simple research agent.
    Given a task description, returns a short research summary.
    """

    def __init__(self):
        self.llm = get_llm()

    def run(self, task_description: str) -> str:
        prompt = f"""
You are a research agent.

Task:
{task_description}

Provide:
- 3–5 bullet points with key information.
- A short summary paragraph at the end.

Be concise and factual.
"""
        resp = self.llm.invoke(prompt)
        return resp.content.strip()