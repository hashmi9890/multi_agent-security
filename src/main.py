from src.workflows.basic_workflow import run_research_workflow


def main():
    user_query = "Research 3 competitors for an AI writing tool and summarize them."
    result = run_research_workflow(user_query)
    print("=== WORKFLOW RESULT ===")
    print(result)


if __name__ == "__main__":
    main()

