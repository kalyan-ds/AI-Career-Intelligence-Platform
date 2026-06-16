def generate_followup_question(
    question,
    score
):

    if score >= 80:

        return (
            "Can you explain this concept "
            "with a real-world example?"
        )

    elif score >= 60:

        return (
            "Can you provide more technical "
            "details about this topic?"
        )

    else:

        return (
            "Can you explain the basic "
            "concept again in simpler terms?"
        )