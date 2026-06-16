import pandas as pd
import os

def calculate_match_score(
    resume_skills,
    role_skills
):
    matched = []

    missing = []

    for skill in role_skills:

        if skill.lower() in [
            s.lower()
            for s in resume_skills
        ]:

            matched.append(skill)

        else:

            missing.append(skill)

    score = (
        len(matched)
        /
        max(
            1,
            len(role_skills)
        )
    ) * 100

    return {

        "score":
        round(score, 2),

        "matched":
        matched,

        "missing":
        missing

    }


def get_role_skills(
    role
):

    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    csv_path = os.path.join(
        current_dir,
        "..",
        "..",
        "data",
        "role_skills.csv"
    )

    df = pd.read_csv(
        csv_path
    )

    row = df[
        df["role"] == role
    ]

    if len(row) == 0:

        return []

    skills = row.iloc[0][
        "skills"
    ]

    return [
        s.strip()
        for s in skills.split(",")
    ]