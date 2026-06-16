import streamlit as st

from utils.history_db import (
    get_interview_history
)

st.title(
    "📚 Interview History"
)
st.caption(
    "Review previous interview attempts and track long-term progress."
)



history = get_interview_history()

if len(history) == 0:

    st.warning(
        "No interview history found."
    )

    st.stop()

st.subheader(
    "📊 Previous Interviews"
)

st.dataframe(
    history,
    use_container_width=True
)

# ======================================
# SCORE TREND
# ======================================

if "overall_score" in history.columns:

    st.subheader(
        "📈 Score Trend"
    )

    chart_data = history[
        [
            "date",
            "overall_score"
        ]
    ]

    chart_data = chart_data.sort_values(
        "date"
    )

    st.line_chart(
        chart_data.set_index(
            "date"
        )
    )

# ======================================
# LATEST PERFORMANCE
# ======================================

latest = history.iloc[-1]

st.subheader(
    "🏆 Latest Interview"
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Role",
    latest["role"]
)

col2.metric(
    "Score",
    latest["overall_score"]
)

col3.metric(
    "Date",
    latest["date"]
)

