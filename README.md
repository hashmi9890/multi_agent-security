# Multi-Agent Security Project

A multi-agent AI system built with LangChain and Groq, featuring input/output security checks, task planning, and specialized worker agents for research tasks.

## Architecture

    User Input
        |
        v
    InputSecurityAgent       -> Validates and sanitizes input
        |  (if safe)
        v
    HeadAgent                -> create_plan() + route_task()
        |
        v
    ResearchAgent            -> Executes the task via Groq LLM
    (or other workers)
        |
        v
    OutputSecurityAgent      -> Validates output before returning
        |  (if safe)
        v
    Final Result

## Project Structure

    multi_agent_security_project/
        src/
            agents/
                head_agent.py        - Orchestration: planning + routing
                worker_agents.py     - Task-executing agents (e.g. ResearchAgent)
                security_agents.py   - Input/output security checks
            workflows/
                basic_workflow.py    - End-to-end workflow orchestration
            config.py                - Environment and API key configuration
            main.py                  - Entry point
        .env                          - API keys (not committed)
        .env.example                  - Template for environment variables
        .gitignore
        README.md

## Setup

1. Clone the repository

       git clone https://github.com/hashmi9890/multi_agent-security.git
       cd multi_agent-security

2. Create and activate a virtual environment

       python -m venv .venv
       source .venv/Scripts/activate

3. Install dependencies

       pip install -r requirements.txt

4. Configure environment variables
   Copy .env.example to .env and add your GROQ_API_KEY (get one at https://console.groq.com/keys)

## Usage

Run the workflow

    python -m src.main

## Security Features

- Input validation: all user input is checked by InputSecurityAgent before processing
- Output validation: all agent output is checked by OutputSecurityAgent before being returned to the user
- Environment isolation: API keys are stored in .env, excluded from version control via .gitignore

## Branching Strategy

- main: stable, production-ready code
- dev: active development branch
- feature/*: individual feature branches, merged into dev when complete

## Tech Stack

- Python 3.14
- LangChain (langchain_openai / Groq integration)
- Groq API for LLM inference
- Git and GitHub for version control