def generate_coach_feedback(
    score
):

    strengths = []

    improvements = []

    if score >= 85:

        strengths.append(
            "Excellent conceptual understanding"
        )

        strengths.append(
            "Answer was clear and detailed"
        )

    elif score >= 70:

        strengths.append(
            "Good understanding of concepts"
        )

        improvements.append(
            "Add more technical depth"
        )

    elif score >= 50:

        strengths.append(
            "Basic understanding demonstrated"
        )

        improvements.append(
            "Provide more detailed explanations"
        )

        improvements.append(
            "Include practical examples"
        )

    else:

        improvements.append(
            "Review the topic fundamentals"
        )

        improvements.append(
            "Practice technical explanations"
        )

    return {

        "strengths":
        strengths,

        "improvements":
        improvements

    }