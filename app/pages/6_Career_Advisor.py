import streamlit as st

st.title(
    "🧠 Career Advisor"
)
st.info(
    """
    Personalized career guidance based on your
    resume, skills, and interview performance.
    """
)


# ======================================
# CHECK DATA EXISTS
# ======================================

if (
    "career_advice"
    not in st.session_state
):

    st.warning(
        "Please analyze a resume first in the Resume Analyzer page."
    )

    st.stop()

career_advice = (
    st.session_state.career_advice
)

roadmap = (
    st.session_state.roadmap
)

# ======================================
# CURRENT LEVEL
# ======================================

st.success(
    f"Current Level: {career_advice['level']}"
)

# ======================================
# STRENGTHS
# ======================================

st.subheader(
    "💪 Strengths"
)

for skill in career_advice[
    "strengths"
]:

    st.success(skill)

# ======================================
# SKILL GAPS
# ======================================

st.subheader(
    "📌 Skill Gaps"
)

for skill in career_advice[
    "skill_gaps"
]:

    st.warning(skill)

# ======================================
# ROADMAP
# ======================================

st.subheader(
    "🗺 Career Roadmap"
)

if len(roadmap) == 0:

    st.success(
        "You already possess all required skills."
    )

else:

    for item in roadmap:

        st.info(
            f"Month {item['month']}: Learn {item['skill']}"
        )

# ======================================
# JOB READINESS
# ======================================

st.success(
    f"Estimated Job Readiness: "
    f"{career_advice['job_readiness']} Month(s)"
)

