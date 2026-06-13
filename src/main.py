from src.workflows.basic_workflow import run_research_workflow


def main():
    user_query = "Analyze this data: sales were 100, 150, 200, 175, 220 over 5 months. What's the average and trend?"
    result = run_research_workflow(user_query)
    print("=== WORKFLOW RESULT ===")
    print(result)


if __name__ == "__main__":
    main()

