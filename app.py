import streamlit as st

from src.workflows.basic_workflow import run_research_workflow
from src.agents.head_agent import HeadAgent

st.set_page_config(
    page_title="Multi-Agent Security System",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Multi-Agent Security System")
st.caption(
    "A multi-agent AI system with input/output security checks, "
    "dynamic task routing, and specialized worker agents."
)

with st.expander("ℹ️ How it works", expanded=False):
    st.markdown(
        """
This system processes your query through several stages:

1. **Input Security Check** — Your input is screened for prompt
   injection attempts or unsafe requests.
2. **Task Routing** — The Head Agent analyzes your query and routes
   it to the most appropriate specialist agent.
3. **Worker Execution** — One of the following agents handles the task:
   - 🔬 **Research Agent** — general knowledge and research queries
   - 💻 **Code Agent** — code generation, explanation, and debugging
   - 📊 **Data Analysis Agent** — statistics, insights, and business reports
4. **Output Security Check** — The response is screened before being
   shown to you.
        """
    )

st.divider()

user_input = st.text_area(
    "Enter your query",
    placeholder="e.g. 'Write a Python function to check if a number is prime' "
    "or 'Analyze this data: sales were 100, 150, 200, 175, 220 over 5 months'",
    height=120,
)

col1, col2 = st.columns([1, 4])
with col1:
    submit = st.button("Run", type="primary", use_container_width=True)

if submit:
    if not user_input.strip():
        st.warning("Please enter a query before running.")
    else:
        # Show which agent will likely handle this (preview routing)
        head = HeadAgent(name="HeadAgent")
        route_info = head.route_task(user_input)
        worker_type = route_info.get("worker_type", "research")

        agent_labels = {
            "research": "🔬 Research Agent",
            "code": "💻 Code Agent",
            "data_analysis": "📊 Data Analysis Agent",
        }
        agent_label = agent_labels.get(worker_type, worker_type)

        with st.spinner(f"Routing to {agent_label}..."):
            result = run_research_workflow(user_input)

        st.divider()

        if result.startswith("REQUEST BLOCKED") or result.startswith("OUTPUT BLOCKED"):
            st.error(result)
        else:
            st.success(f"Handled by: {agent_label}")
            st.markdown("### Result")
            st.markdown(result)

st.divider()
st.caption("Built with LangChain, Groq, and Streamlit. Security checks run on every request.")
