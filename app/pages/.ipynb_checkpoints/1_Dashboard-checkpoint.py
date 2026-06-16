import streamlit as st
from utils.history_db import (get_interview_history)
from utils.progress_dashboard import (calculate_progress_stats)

st.title(
    "📊 Dashboard"
)
st.info(
    """
    Welcome to the AI Career Intelligence Platform.

    Analyze your resume,
    practice interviews,
    track progress,
    and improve your career readiness.
    """
)



st.markdown(
    """
    Welcome to the AI Career Intelligence Platform.

    Use the sidebar to access:

    - Resume Analyzer
    - Interview
    - Reports
    - Analytics
    - Career Advisor
    - History
    """
)
history = get_interview_history()
progress_stats = (
    calculate_progress_stats(
        history
    )
)
st.header(
    "📊 Progress Dashboard"
)
col1, col2, col3, col4 = st.columns(4)
col1.metric(
    "Total Interviews",
    progress_stats[
        "total_interviews"
        ]
)
col2.metric(
    "Average Score",
    progress_stats[
        "average_score"
            ]
)
col3.metric(
    "Highest Score",
    progress_stats[
        "highest_score"
        ]
)
col4.metric(
    "Top Role",
    progress_stats[
        "most_selected_role"
        ]
)
if len(history)>0:
    st.subheader(
        "📈 Score Improvement Trend"
    )
    trend_data = history[
        [
            "date",
            "overall_score"
        ]
        ]
    trend_data = trend_data.sort_values(
        "date"
    )
    st.line_chart(
        trend_data.set_index(
            "date"
        )
    )
    st.header(
        "📚 Interview History"
    )
    
    if len(history) > 0:
        st.dataframe(
            history
        )