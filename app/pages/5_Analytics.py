import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils.analytics_engine import (analyze_interview)

from utils.analytics_difficulty import (analyze_difficulty_scores)

st.title(
    "📈 Analytics Dashboard"
)
st.caption(
    "Track your performance and monitor interview improvement trends."
)


if "answers" not in st.session_state:

    st.warning(
        "No interview data available."
    )

    st.stop()

if len(st.session_state.answers) == 0:

    st.warning(
        "Complete an interview first."
    )

    st.stop()

semantic_scores = []

for item in st.session_state.answers:

    score = item.get(
        "score",
        0
    )

    if score == 0:

        from utils.scoring import (
            semantic_score
        )

        score = semantic_score(

            item["answer"],

            item["ideal_answer"]

        )

    semantic_scores.append(
        score
    )

analytics = analyze_interview(
    semantic_scores
)

difficulty_scores = (

    analyze_difficulty_scores(

        st.session_state.answers,

        semantic_scores

    )

)

st.header(
    "📊 Interview Analytics"
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Average Score",
        analytics[
            "average_score"
        ]
    )

    st.metric(
        "Strongest Question",
        analytics[
            "strongest_question"
        ]
    )

with col2:

    st.metric(
        "Weakest Question",
        analytics[
            "weakest_question"
        ]
    )

    st.metric(
        "Best Score",
        analytics[
            "strongest_score"
        ]
    )

st.divider()

st.subheader(
    "📈 Performance Trend"
)

chart_data = pd.DataFrame({

    "Question":

    list(

        range(

            1,

            len(
                semantic_scores
            ) + 1

        )

    ),

    "Score":
    semantic_scores

})

st.line_chart(

    chart_data.set_index(
        "Question"
    )

)

st.divider()

st.header(
    "📈 Difficulty Analytics"
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Easy",
    difficulty_scores[
        "Easy"
    ]
)

col2.metric(
    "Medium",
    difficulty_scores[
        "Medium"
    ]
)

col3.metric(
    "Hard",
    difficulty_scores[
        "Hard"
    ]
)

difficulty_chart = pd.DataFrame({

    "Difficulty": [

        "Easy",

        "Medium",

        "Hard"

    ],

    "Score": [

        difficulty_scores[
            "Easy"
        ],

        difficulty_scores[
            "Medium"
        ],

        difficulty_scores[
            "Hard"
        ]

    ]

})

st.bar_chart(

    difficulty_chart.set_index(
        "Difficulty"
    )

)
st.divider()

st.subheader(
    "🎯 Skill Radar Chart"
)

categories = [

    "Technical",

    "Communication",

    "Problem Solving",

    "Resume Match",

    "Interview",

    "Career Readiness"

]

values = [

    80,

    75,

    70,

    85,

    78,

    82

]

values += values[:1]

angles = np.linspace(

    0,

    2 * np.pi,

    len(categories),

    endpoint=False

).tolist()

angles += angles[:1]

fig, ax = plt.subplots(

    figsize=(6, 6),

    subplot_kw=dict(
        polar=True
    )

)

ax.plot(
    angles,
    values
)

ax.fill(
    angles,
    values,
    alpha=0.25
)

ax.set_xticks(
    angles[:-1]
)

ax.set_xticklabels(
    categories
)

st.pyplot(
    fig
)

