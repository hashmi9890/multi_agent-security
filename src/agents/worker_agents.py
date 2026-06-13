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


class DataAnalysisAgent:
    """
    Senior-level data analysis agent.
    Given raw data or a dataset description, returns a structured,
    business-oriented analysis: statistics, insights, risks, and
    actionable recommendations -- written like a report a data analyst
    would hand to a business stakeholder.
    """

    def __init__(self):
        self.llm = get_llm()

    def run(self, task_description: str) -> str:
        prompt = f"""You are a senior data analyst producing a concise business report.

Data / Task:
{task_description}

Structure your response with these sections, using clear headers:

1. Key Metrics
   - Compute relevant statistics where possible (total, average, min, max,
     growth rate, variance). State any assumptions if data is incomplete.

2. Insights
   - 3-5 bullet points on patterns, trends, or anomalies in the data.

3. Business Implications
   - What do these numbers mean for the business? Frame in terms of
     opportunities, risks, or areas needing attention.

4. Recommendations
   - 2-3 concrete, actionable next steps a decision-maker could take.

Guidelines:
- Be precise, evidence-based, and avoid overstating confidence beyond
  what the data supports.
- Keep the entire response concise -- this is a summary report, not a
  full thesis. Avoid jargon where plain language works.
- Do not fabricate data points that were not provided or cannot be
  reasonably derived.
"""
        resp = self.llm.invoke(prompt)
        return resp.content.strip()