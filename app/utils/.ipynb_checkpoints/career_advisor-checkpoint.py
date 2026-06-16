def generate_career_advice(

    match_score,

    matched_skills,

    missing_skills

):

    if match_score >= 80:

        level = "Advanced"

    elif match_score >= 60:

        level = "Intermediate"

    else:

        level = "Beginner"

    return {

        "level": level,

        "strengths": matched_skills,

        "skill_gaps": missing_skills,

        "job_readiness":
        len(missing_skills)

    }