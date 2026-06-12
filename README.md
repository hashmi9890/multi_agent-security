# multi_agent_security_project

Project scaffold for a multi-agent security application.

## Setup

1. In the terminal, ensure you’re in the project root:
   ```bash
   cd path/to/multi_agent_security_project
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate it:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
4. In VS Code, select this interpreter:
   - Open Command Palette: `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Type: `Python: Select Interpreter`
   - Choose the one that points to `.venv` inside your project.
5. Install dependencies in the same activated terminal:
   ```bash
   pip install -r requirements.txt
   ```
6. Configure environment variables
   - Copy `.env.example` → `.env`
   - Update values in `.env`.

   **Note:** The app reads `OPENAI_API_KEY` and optionally `OPENAI_MODEL` from environment variables (via `src/config.py`).

   Example `.env` contents:
   ```text
   OPENAI_API_KEY=sk-...your_real_key...
   OPENAI_MODEL=gpt-4.1-mini
   ```

`python-dotenv` in `src/config.py` will automatically load `.env` when the app runs.

## Structure

- `docs/` - project documentation
- `src/` - application source code
- `src/agents/` - agent implementations
- `src/workflows/` - workflow definitions

## ▶️ Run Application (see real output)

Run from the project root:

```bash
python -m src.main
```

You should see console output. If the OpenAI key is missing/invalid, you’ll get an API authentication error (401).

## What the workflow does

`src/workflows/basic_workflow.py` implements:
1. **InputSecurityAgent**: LLM-based classifier that returns SAFE/UNSAFE.
2. **HeadAgent**: routes to the correct worker.
3. **ResearchAgent**: produces the response.
4. **OutputSecurityAgent**: checks the worker output for secrets/harmful content.


