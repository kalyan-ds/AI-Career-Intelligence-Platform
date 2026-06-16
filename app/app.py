import streamlit as st

st.set_page_config(
    page_title="AI Career Intelligence Platform",
    page_icon="🧠",
    layout="wide"
)
st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    div[data-testid="metric-container"] {

        border: 1px solid #444;

        padding: 15px;

        border-radius: 12px;

        background-color: #1e1e1e;
    }

    div[data-testid="stExpander"] {

        border-radius: 10px;

    }

    </style>
    """,
    unsafe_allow_html=True
)
st.title(
    "🧠 AI Career Intelligence Platform"
)
st.sidebar.success(
    "🧠 AI Career Intelligence Platform"
)

st.sidebar.markdown(
    "AI Powered Interview Preparation"
)



st.markdown(
    """
    Welcome to the AI Career Intelligence Platform.

    Use the sidebar to access:

    - 📄 Resume Analyzer
    - 🎤 Interview
    - 📊 Reports
    - 📈 Analytics
    - 🧠 Career Advisor
    - 📚 History
    """
)

st.success(
    "Select a page from the sidebar to begin."
)