from src.workflows.basic_workflow import run_research_workflow


def main():
    user_query = "Write a Python function to check if a number is prime"
    result = run_research_workflow(user_query)
    print("=== WORKFLOW RESULT ===")
    print(result)


if __name__ == "__main__":
    main()

