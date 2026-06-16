import streamlit as st

from utils.scoring import semantic_score
from utils.feedback_engine import generate_feedback
from utils.followup_engine import generate_followup_question
from utils.certificate_generator import (generate_certificate)



# ======================================
# PAGE TITLE
# ======================================

st.title(
    "📊 Interview Reports"
)

# ======================================
# CHECK INTERVIEW DATA
# ======================================

if "answers" not in st.session_state:

    st.warning(
        "No interview data found."
    )

    st.stop()

if len(st.session_state.answers) == 0:

    st.warning(
        "Complete an interview first."
    )

    st.stop()

# ======================================
# CALCULATE SCORES
# ======================================

semantic_scores = []

for item in st.session_state.answers:

    score = semantic_score(

        item["answer"],

        item["ideal_answer"]

    )

    semantic_scores.append(
        score
    )

technical_score = round(

    sum(semantic_scores)

    /

    max(
        1,
        len(semantic_scores)
    ),

    2

)

# ======================================
# COMMUNICATION SCORE
# ======================================

total_words = 0

for item in st.session_state.answers:

    total_words += len(
        item["answer"].split()
    )

average_words = (

    total_words

    /

    max(
        1,
        len(st.session_state.answers)
    )

)

if average_words < 20:

    communication_score = 50

elif average_words < 40:

    communication_score = 70

elif average_words < 60:

    communication_score = 85

else:

    communication_score = 95

# ======================================
# OVERALL SCORE
# ======================================

overall_score = (

    technical_score * 0.7

    +

    communication_score * 0.3

)

# ======================================
# METRICS
# ======================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Technical Score",
    f"{technical_score:.1f}"
)

col2.metric(
    "Communication Score",
    f"{communication_score:.1f}"
)

col3.metric(
    "Overall Score",
    f"{overall_score:.1f}"
)

# ======================================
# CANDIDATE RATING
# ======================================

if overall_score >= 80:

    rating = "⭐ Strong Candidate"

elif overall_score >= 60:

    rating = "🟡 Average Candidate"

else:

    rating = "🔴 Needs Improvement"

st.subheader(
    f"Candidate Rating: {rating}"
)

# ======================================
# AI SUMMARY
# ======================================

if overall_score >= 80:

    summary = (
        "Excellent performance. Candidate demonstrates strong technical understanding and communication skills."
    )

elif overall_score >= 60:

    summary = (
        "Good performance. Candidate shows reasonable technical knowledge but can improve answer depth."
    )

else:

    summary = (
        "Candidate requires additional preparation and deeper understanding of core concepts."
    )

st.subheader(
    "🤖 AI Interview Summary"
)

st.info(
    summary
)

# ======================================
# INTERVIEW SUMMARY
# ======================================

st.info(
    f"""
Technical Score: {technical_score:.1f}

Communication Score: {communication_score:.1f}

Overall Score: {overall_score:.1f}

Rating: {rating}
"""
)

# ======================================
# HIRING PROBABILITY
# ======================================

hiring_probability = min(

    100,

    round(
        overall_score + 5,
        0
    )

)

st.subheader(
    f"📈 Hiring Probability: {hiring_probability}%"
)

# ======================================
# QUESTION WISE FEEDBACK
# ======================================

st.divider()

st.header(
    "📝 Question Wise Feedback"
)

for i, item in enumerate(

    st.session_state.answers,

    start=1

):

    score = semantic_score(

        item["answer"],

        item["ideal_answer"]

    )

    feedback = generate_feedback(
        score
    )

    followup_question = (

        generate_followup_question(

            item["question"],

            score

        )

    )

    with st.expander(

        f"Question {i}"

    ):

        st.write(
            "Question:"
        )

        st.write(
            item["question"]
        )

        st.write(
            "Your Answer:"
        )

        st.write(
            item["answer"]
        )

        st.write(
            f"Score: {score:.1f}%"
        )

        st.subheader(
            "💪 Strengths"
        )

        for strength in feedback[
            "strengths"
        ]:

            st.success(
                strength
            )

        st.subheader(
            "📌 Areas for Improvement"
        )

        for improvement in feedback[
            "improvements"
        ]:

            st.warning(
                improvement
            )

        st.subheader(
            "💡 Suggested Improvement"
        )

        st.info(
            feedback[
                "suggested_answer"
            ]
        )

        st.subheader(
            "🤖 AI Follow-Up Question"
        )

        st.info(
            followup_question
        )

# ======================================
# FINAL RECOMMENDATION
# ======================================

st.divider()

st.subheader(
    "🎯 Final Recommendation"
)

if overall_score >= 80:

    st.success(
        "You are interview-ready for most entry-level and intermediate positions."
    )

elif overall_score >= 60:

    st.warning(
        "You are progressing well. Focus on improving technical depth and communication."
    )

else:

    st.error(
        "Spend more time strengthening fundamentals and practicing mock interviews."
    )

st.divider()

st.subheader(
    "🏆 Interview Certificate"
)

certificate_file = (
    generate_certificate(
        overall_score,
        rating
    )
)

with open(
    certificate_file,
    "rb"
) as file:

    st.download_button(

        label=
        "📄 Download Certificate",

        data=file,

        file_name=
        "Interview_Certificate.pdf",

        mime=
        "application/pdf"

    )



