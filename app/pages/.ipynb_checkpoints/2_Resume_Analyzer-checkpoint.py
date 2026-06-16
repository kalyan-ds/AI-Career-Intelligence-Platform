import streamlit as st
import pandas as pd

from utils.resume_parser import extract_text
from utils.resume_analyzer import extract_skills
from utils.resume_question_generator import generate_questions
from utils.resume_summary import ( generate_resume_summary )

from utils.resume_matcher import (
    get_role_skills,
    calculate_match_score
)

from utils.roadmap_generator import (
    generate_roadmap
)

from utils.learning_resources import (
    get_learning_resources
)

from utils.career_advisor import (
    generate_career_advice
)

# ======================================
# PAGE TITLE
# ======================================

st.title(
    "📄 Resume Analyzer"
)

# ======================================
# ROLE & DIFFICULTY
# ======================================

roles = [

    "Data Scientist",

    "AI Engineer",

    "Machine Learning Engineer",

    "Data Analyst"

]

selected_role = st.selectbox(
    "Select Role",
    roles
)

difficulty = st.selectbox(
    "Select Difficulty",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)

# ======================================
# RESUME UPLOAD
# ======================================

st.subheader(
    "📄 Resume Upload"
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx", "txt"]
)

# ======================================
# RESUME ANALYSIS
# ======================================

if uploaded_file:

    resume_text = extract_text(
        uploaded_file
    )

    skills = extract_skills(
        resume_text
    )

    personalized_questions = (
        generate_questions(
            skills,
            selected_role,
            difficulty
        )
    )

    st.session_state.personalized_questions = (
        personalized_questions
    )

    st.success(
        "Resume Uploaded Successfully"
    )

    st.text_area(
        "Resume Content",
        resume_text[:3000],
        height=200
    )

    # ======================================
    # SKILLS
    # ======================================

    st.subheader(
        "🛠 Extracted Skills"
    )

    if skills:

        for skill in skills:

            st.markdown(
                f"✅ **{skill}**"
            )

    else:

        st.warning(
            "No skills detected."
        )

    # ======================================
    # QUESTIONS
    # ======================================

    st.subheader(
        "🎯 Personalized Interview Questions"
    )

    if personalized_questions:

        for i, question in enumerate(
            personalized_questions,
            start=1
        ):

            st.write(
                f"{i}. {question}"
            )

    else:

        st.info(
            "No personalized questions generated."
        )

    # ======================================
    # ROLE MATCHING
    # ======================================

    role_skills = get_role_skills(
        selected_role
    )

    match_result = (
        calculate_match_score(
            skills,
            role_skills
        )
    )
    resume_summary = (
        generate_resume_summary(

        skills,

        match_result["score"],

        selected_role
        )
    )



    st.session_state.match_result = (
        match_result
    )

    # ======================================
    # CAREER ADVISOR
    # ======================================

    career_advice = (
        generate_career_advice(
            match_result["score"],
            match_result["matched"],
            match_result["missing"]
        )
    )

    st.session_state.career_advice = (
        career_advice
    )

    roadmap = generate_roadmap(
        match_result["missing"]
    )

    st.session_state.roadmap = (
        roadmap
    )

    # ======================================
    # MATCH SCORE
    # ======================================

    st.subheader(
        "🎯 Resume Match Score"
    )

    st.metric(
        "Match Score",
        f"{match_result['score']}%"
    )
    st.subheader(
        "🤖 AI Resume Summary"
    )
    st.success(
        f"Experience Level: {resume_summary['level']}"
    )
    st.info(
        f"Resume Strength: {resume_summary['strength']}"
    )
    st.write(
        "🔥 Top Skills"
    )
    for skill in resume_summary[
        "top_skills"
        ]:
        st.success(skill)
    st.write(
        "🎯 Career Recommendation"
    )
    st.info(
        resume_summary[
            "recommendation"
            ]
    )



    # ======================================
    # SKILL GAP CHART
    # ======================================

    matched_count = len(
        match_result["matched"]
    )

    missing_count = len(
        match_result["missing"]
    )

    st.subheader(
        "📊 Skill Gap Analysis"
    )

    skill_chart = pd.DataFrame({

        "Category": [

            "Matched Skills",

            "Missing Skills"

        ],

        "Count": [

            matched_count,

            missing_count

        ]

    })

    st.bar_chart(
        skill_chart.set_index(
            "Category"
        )
    )

    # ======================================
    # CAREER RECOMMENDATION
    # ======================================

    st.subheader(
        "🎯 Career Recommendations"
    )

    if match_result["score"] >= 80:

        st.success(
            "Your resume is strongly aligned with this role."
        )

    elif match_result["score"] >= 60:

        st.warning(
            "Your resume is moderately aligned. Consider learning missing skills."
        )

    else:

        st.error(
            "Significant skill gaps detected. Focus on the missing skills below."
        )

    # ======================================
    # MATCHED SKILLS
    # ======================================

    st.write(
        "✅ Matched Skills"
    )

    for skill in match_result["matched"]:

        st.success(skill)

    # ======================================
    # MISSING SKILLS
    # ======================================

    st.write(
        "❌ Missing Skills"
    )

    for skill in match_result["missing"]:

        st.warning(skill)

    # ======================================
    # ROADMAP
    # ======================================

    st.subheader(
        "🎯 Career Roadmap"
    )

    if len(roadmap) == 0:

        st.success(
            "You already have all required skills."
        )

    else:

        for item in roadmap:

            st.info(
                f"Month {item['month']}: Learn {item['skill']}"
            )

        st.success(
            f"Estimated Job Readiness: {len(roadmap)} Month(s)"
        )

    # ======================================
    # LEARNING RESOURCES
    # ======================================

    resources = get_learning_resources()

    st.subheader(
        "📚 Learning Resources"
    )

    for skill in match_result["missing"]:

        if skill in resources:

            with st.expander(skill):

                st.write(
                    "📖 Documentation"
                )

                st.write(
                    resources[skill][
                        "documentation"
                    ]
                )

                st.write(
                    "🎥 YouTube Course"
                )

                st.write(
                    resources[skill][
                        "youtube"
                    ]
                )

                st.write(
                    "💻 Project Idea"
                )

                st.write(
                    resources[skill][
                        "project"
                    ]
                )

    # ======================================
    # AI CAREER ADVISOR
    # ======================================

    st.subheader(
        "🧠 AI Career Advisor"
    )

    st.success(
        f"Current Level: {career_advice['level']}"
    )

    st.write(
        "💪 Strengths"
    )

    for skill in career_advice[
        "strengths"
    ]:

        st.success(skill)

    st.write(
        "📌 Skill Gaps"
    )

    for skill in career_advice[
        "skill_gaps"
    ]:

        st.warning(skill)

    st.info(
        f"Estimated Job Readiness: "
        f"{career_advice['job_readiness']} Month(s)"
    )

