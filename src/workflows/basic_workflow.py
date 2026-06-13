from src.agents.head_agent import HeadAgent
from src.agents.worker_agents import ResearchAgent, CodeAgent
from src.agents.security_agents import InputSecurityAgent, OutputSecurityAgent


def run_research_workflow(user_input: str) -> str:
    """
    Basic end-to-end workflow for testing:
    1. Input security check
    2. Head agent planning + routing
    3. Worker execution (research or code)
    4. Output security check
    """

    # 1) Input security
    input_guard = InputSecurityAgent()
    is_safe_input, input_msg = input_guard.check(user_input)
    if not is_safe_input:
        return f"REQUEST BLOCKED BY INPUT SECURITY: {input_msg}"

    # 2) Head agent
    head = HeadAgent(name="HeadAgent")
    plan = head.create_plan(user_input)
    route_info = head.route_task(user_input)

    worker_type = route_info.get("worker_type")
    task_description = route_info.get("task_description", user_input)

    if worker_type == "research":
        worker = ResearchAgent()
        worker_output = worker.run(task_description)
    elif worker_type == "code":
        worker = CodeAgent()
        worker_output = worker.run(task_description)
    else:
        return f"Unknown worker type: {worker_type}"

    # 3) (Optional) plan ka use baad me karein, abhi ignore kar rahe hain

    # 4) Output security
    output_guard = OutputSecurityAgent()
    is_safe_output, output_msg = output_guard.check(worker_output)
    if not is_safe_output:
        return f"OUTPUT BLOCKED BY SECURITY: {output_msg}"

    return worker_output