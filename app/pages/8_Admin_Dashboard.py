import streamlit as st
import pandas as pd

st.title(
    "📊 Admin Dashboard"
)

st.caption(
    "Platform Performance Overview"
)

# ======================================
# INTERVIEW DATA
# ======================================

if "answers" not in st.session_state:

    st.warning(
        "No interview data available."
    )

    st.stop()

answers = st.session_state.answers

total_interviews = 1

total_questions = len(
    answers
)

# ======================================
# SCORE CALCULATION
# ======================================

scores = []

for item in answers:

    score = item.get(
        "score",
        0
    )

    if score != 0:

        scores.append(score)

if len(scores) == 0:

    average_score = 0

    highest_score = 0

else:

    average_score = round(
        sum(scores) / len(scores),
        2
    )

    highest_score = round(
        max(scores),
        2
    )

# ======================================
# METRICS
# ======================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Interviews",
    total_interviews
)

col2.metric(
    "Average Score",
    average_score
)

col3.metric(
    "Highest Score",
    highest_score
)

# ======================================
# ROLE INFO
# ======================================

if "match_result" in st.session_state:

    st.subheader(
        "🎯 Current Resume Match"
    )

    st.metric(
        "Match Score",
        st.session_state.match_result[
            "score"
        ]
    )

# ======================================
# TOP SKILLS
# ======================================

if "career_advice" in st.session_state:

    st.subheader(
        "🔥 Top Skills"
    )

    for skill in st.session_state.career_advice[
        "strengths"
    ]:

        st.success(skill)

# ======================================
# QUESTION TREND
# ======================================

if total_questions > 0:

    st.subheader(
        "📈 Interview Activity"
    )

    chart_data = pd.DataFrame({

        "Question":

        list(
            range(
                1,
                total_questions + 1
            )
        ),

        "Completed":

        [1] * total_questions

    })

    st.line_chart(
        chart_data.set_index(
            "Question"
        )
    )

