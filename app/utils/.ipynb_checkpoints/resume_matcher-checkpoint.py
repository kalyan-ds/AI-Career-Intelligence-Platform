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