import re

SKILLS = [

    "Python",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "TensorFlow",
    "PyTorch",
    "Scikit-Learn",
    "SQL",
    "Pandas",
    "NumPy",
    "Power BI",
    "Tableau",
    "Streamlit",
    "Flask",
    "Django",
    "OpenAI",
    "LangChain",
    "Transformers",
    "Computer Vision",
    "Data Analysis"

]

def extract_skills(resume_text):

    found_skills = []

    text = resume_text.lower()

    for skill in SKILLS:

        if skill.lower() in text:

            found_skills.append(skill)

    return list(set(found_skills))