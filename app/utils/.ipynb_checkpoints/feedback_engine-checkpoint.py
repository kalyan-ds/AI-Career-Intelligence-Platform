def generate_feedback(score):

    feedback = {

        "strengths": [],

        "improvements": [],

        "suggested_answer": ""

    }

    if score >= 80:

        feedback["strengths"] = [

            "Excellent understanding of the topic.",

            "Answer is technically accurate.",

            "Good level of detail and clarity."

        ]

        feedback["improvements"] = [

            "Add more real-world examples.",

            "Discuss production use cases."

        ]

        feedback["suggested_answer"] = (

            "Expand the answer by including "

            "industry applications and practical examples."

        )

    elif score >= 60:

        feedback["strengths"] = [

            "Basic concepts are explained correctly.",

            "Shows reasonable understanding."

        ]

        feedback["improvements"] = [

            "Add more technical depth.",

            "Include implementation details.",

            "Discuss challenges and solutions."

        ]

        feedback["suggested_answer"] = (

            "Explain the concept step-by-step "

            "and include practical examples."

        )

    else:

        feedback["strengths"] = [

            "Attempted to answer the question."

        ]

        feedback["improvements"] = [

            "Answer lacks technical depth.",

            "Important concepts are missing.",

            "Provide more structured explanations."

        ]

        feedback["suggested_answer"] = (

            "Study the topic fundamentals and "

            "practice explaining concepts clearly."

        )

    return feedback

