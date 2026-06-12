"""Head agent orchestration logic."""


class HeadAgent:
    def __init__(self, name: str) -> None:
        self.name = name

    def coordinate(self) -> None:
        print(f"{self.name} coordinating workers...")

    def create_plan(self, user_input: str) -> dict:
        """Create a simple plan for handling the user's request."""
        return {
            "original_input": user_input,
            "steps": ["analyze_request", "route_to_worker", "execute", "return_result"],
        }

    def route_task(self, user_input: str) -> dict:
        """Decide which worker should handle this task."""
        return {
            "worker_type": "research",
            "task_description": user_input,
        }