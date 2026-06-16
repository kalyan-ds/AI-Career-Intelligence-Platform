def get_badges(

    overall_score,

    match_score

):

    badges = []

    if overall_score >= 90:

        badges.append(
            "👑 Expert Candidate"
        )

    elif overall_score >= 80:

        badges.append(
            "🥇 Advanced Candidate"
        )

    elif overall_score >= 60:

        badges.append(
            "🥈 Intermediate Candidate"
        )

    else:

        badges.append(
            "🥉 Beginner Candidate"
        )

    if match_score >= 80:

        badges.append(
            "🎯 Resume Expert"
        )

    if overall_score >= 85:

        badges.append(
            "🧠 Interview Master"
        )

    if overall_score >= 95:

        badges.append(
            "🔥 High Performer"
        )

    return badges