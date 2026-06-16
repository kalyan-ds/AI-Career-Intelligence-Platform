def generate_resume_summary(
    skills,
    match_score,
    selected_role
):

    if match_score >= 80:

        strength = "Strong"

        level = "Advanced"

    elif match_score >= 60:

        strength = "Moderate"

        level = "Intermediate"

    else:

        strength = "Needs Improvement"

        level = "Beginner"

    top_skills = skills[:5]

    recommendation = (

        f"You are well suited for {selected_role} roles. "

        f"Continue improving your missing skills "

        f"to increase your employability."

    )

    return {

        "level": level,

        "strength": strength,

        "top_skills": top_skills,

        "recommendation": recommendation

    }

