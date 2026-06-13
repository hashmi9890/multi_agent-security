from src.config import get_llm


class ResearchAgent:
    """
    Simple research agent.
    Given a task description, returns a short research summary.
    """

    def __init__(self):
        self.llm = get_llm()

    def run(self, task_description: str) -> str:
        prompt = f"""You are a research agent.

Task:
{task_description}

Provide:
- 3-5 bullet points with key information.
- A short summary paragraph at the end.

Be concise and factual.
"""
        resp = self.llm.invoke(prompt)
        return resp.content.strip()


class CodeAgent:
    """
    Simple code agent.
    Given a task description (code snippet, error, or coding question),
    returns an explanation, fix, or generated code.
    """

    def __init__(self):
        self.llm = get_llm()

    def run(self, task_description: str) -> str:
        prompt = f"""You are a code assistant agent.

Task:
{task_description}

Instructions:
- If the task includes code with a bug or error, explain the issue and provide a corrected version.
- If the task asks for an explanation of code, explain it clearly and concisely.
- If the task asks to generate code, provide clean, working code with brief comments.
- Always wrap code in fenced code blocks with the correct language tag.

Be precise and avoid unnecessary explanation.
"""
        resp = self.llm.invoke(prompt)
        return resp.content.strip()