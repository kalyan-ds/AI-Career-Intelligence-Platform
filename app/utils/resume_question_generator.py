
def generate_questions(
    skills,
    role=None,
    difficulty="Medium"
):

    generated_questions = []

    # ======================================
    # SKILL BASED QUESTIONS
    # ======================================

    advanced_questions = {

        "Python": [

            "Explain Python decorators and their real-world applications.",

            "How does Python manage memory internally?",

            "What are generators and when would you use them?",

            "Describe a Python project where you optimized performance."

        ],

        "Machine Learning": [

            "Explain the complete lifecycle of a Machine Learning project.",

            "How do you handle overfitting in Machine Learning models?",

            "Describe a Machine Learning project you have built.",

            "Which evaluation metrics do you use and why?"

        ],

        "Deep Learning": [

            "How do neural networks learn from data?",

            "Explain backpropagation in simple terms.",

            "What techniques do you use to prevent overfitting?",

            "Describe a Deep Learning project you worked on."

        ],

        "TensorFlow": [

            "Explain TensorFlow architecture.",

            "How does TensorFlow handle model training?",

            "Describe a TensorFlow project you have built.",

            "What are the advantages of TensorFlow?"

        ],

        "NLP": [

            "Explain the workflow of an NLP pipeline.",

            "What preprocessing techniques do you use in NLP?",

            "How do transformer models work?",

            "Describe an NLP project you have developed."

        ],

        "SQL": [

            "Explain different types of SQL joins.",

            "How do you optimize slow SQL queries?",

            "Describe database indexing.",

            "How would you design a database for a large application?"

        ],

        "Streamlit": [

            "Why did you choose Streamlit for your project?",

            "How would you deploy a Streamlit application?",

            "How can Streamlit session state be used effectively?",

            "Describe challenges you faced while building a Streamlit project."

        ],

        "Data Science": [

            "Describe an end-to-end Data Science project.",

            "How do you clean and preprocess data?",

            "What visualization techniques do you prefer?",

            "How do you deal with missing values?"

        ],

        "Computer Vision": [

            "Explain a Computer Vision project you have built.",

            "How do Convolutional Neural Networks work?",

            "What image preprocessing techniques do you use?",

            "How would you improve image classification accuracy?"

        ]

    }

    # ======================================
    # ROLE BASED QUESTIONS
    # ======================================

    role_questions = {

        "Data Scientist": [

            "Explain the bias-variance tradeoff.",

            "How would you handle missing values?",

            "Describe an end-to-end machine learning pipeline.",

            "How would you evaluate a recommendation system?"

        ],

        "AI Engineer": [

            "Explain transformer architecture.",

            "How would you deploy a large language model?",

            "How do you optimize inference latency?",

            "Describe model quantization."

        ],

        "Machine Learning Engineer": [

            "How would you deploy an ML model to production?",

            "Explain feature engineering techniques.",

            "How do you monitor model drift?",

            "Describe a scalable ML architecture."

        ],

        "Data Analyst": [

            "Explain SQL joins.",

            "How do you clean raw data?",

            "Which visualization tools do you prefer?",

            "Describe a dashboard you have built."

        ]

    }

    # ======================================
    # SKILL QUESTIONS
    # ======================================

    for skill in skills:

        if skill in advanced_questions:

            generated_questions.extend(
                advanced_questions[skill]
            )

    # ======================================
    # ROLE QUESTIONS
    # ======================================

    if role in role_questions:

        generated_questions.extend(
            role_questions[role]
        )

    # ======================================
    # DIFFICULTY QUESTIONS
    # ======================================

    if difficulty == "Hard":

        generated_questions.extend([

            "Explain a complex technical challenge you solved.",

            "How would you design a scalable AI system?",

            "What tradeoffs do you consider in production deployments?"

        ])

    elif difficulty == "Easy":

        generated_questions.extend([

            "Tell me about yourself.",

            "Why are you interested in this role?",

            "Describe a project you enjoyed working on."

        ])

    # ======================================
    # FALLBACK QUESTIONS
    # ======================================

    if len(generated_questions) < 10:

        generated_questions.extend([

            "Tell me about a challenging technical project you worked on.",

            "How do you approach debugging complex issues?",

            "Describe a situation where you learned a new technology quickly.",

            "What are your strengths as a developer?",

            "Explain a project you are most proud of."

        ])

    # ======================================
    # RETURN TOP 10 QUESTIONS
    # ======================================

    return generated_questions[:10]

