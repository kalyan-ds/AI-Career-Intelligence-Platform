
import streamlit as st

from utils.interview_engine import (
    load_questions
)

#from utils.voice_interview import (
#    record_answer
#)

# ======================================
# PAGE TITLE
# ======================================

st.title(
    "🎤 Interview"
)

# ======================================
# SESSION STATE
# ======================================

if "answers" not in st.session_state:

    st.session_state.answers = []

if "questions" not in st.session_state:

    st.session_state.questions = []

if "current_question" not in st.session_state:

    st.session_state.current_question = 0

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
# START INTERVIEW
# ======================================

if st.button(
    "🚀 Start Interview"
):

    if (

        "personalized_questions"
        in st.session_state

        and

        len(
            st.session_state.personalized_questions
        ) > 0

    ):

        questions = []

        for question in (

            st.session_state.personalized_questions

        ):

            questions.append(

                {

                    "question":
                    question,

                    "ideal_answer":
                    "Sample ideal answer",

                    "difficulty":
                    difficulty

                }

            )

    else:

        questions = load_questions(

            selected_role,

            difficulty

        )

    st.session_state.questions = questions

    st.session_state.current_question = 0

    st.session_state.answers = []

    st.success(
        f"{len(questions)} Questions Loaded"
    )

# ======================================
# QUESTION DISPLAY
# ======================================

if (

    len(st.session_state.questions) > 0

    and

    st.session_state.current_question

    <

    len(st.session_state.questions)

):

    current_index = (

        st.session_state.current_question

    )

    question = (

        st.session_state.questions[
            current_index
        ]

    )

    st.subheader(

        f"Question {current_index + 1} / "

        f"{len(st.session_state.questions)}"

    )

    st.write(
        question["question"]
    )

    # ======================================
    # VOICE STORAGE
    # ======================================

    if (

        f"voice_answer_{current_index}"

        not in st.session_state

    ):

        st.session_state[
            f"voice_answer_{current_index}"
        ] = ""

    # ======================================
    # VOICE BUTTON
    # ======================================

    st.info(
        "🎤 Voice recording is available only in local execution."
    )
    audio_file = st.file_uploader(
        "Upload your answer (.wav)",
        type=["wav"],
        key=f"audio_{current_index}"
    )
    if audio_file is not None:
        st.success(
            "Audio uploaded successfully"
    )

    # ======================================
    # ANSWER BOX
    # ======================================

    answer = st.text_area(

        "Your Answer",

        value=st.session_state[
            f"voice_answer_{current_index}"
        ],

        key=f"answer_{current_index}",

        height=200

    )

    # ======================================
    # NEXT QUESTION
    # ======================================

    if st.button(
        "Next Question"
    ):

        st.session_state.answers.append(

            {

                "question":
                question["question"],

                "answer":
                answer,

                "ideal_answer":
                question["ideal_answer"],

                "difficulty":
                question["difficulty"]

            }

        )

        st.session_state.current_question += 1

        st.rerun()

# ======================================
# INTERVIEW COMPLETE
# ======================================

if (

    len(st.session_state.questions) > 0

    and

    st.session_state.current_question

    >=

    len(st.session_state.questions)

):

    st.success(
        "🎉 Interview Completed!"
    )

    st.write(
        f"Answers Saved: "
        f"{len(st.session_state.answers)}"
    )

    st.subheader(
        "📝 Interview Answers"
    )

    st.write(
        st.session_state.answers
    )

