def analyze_difficulty_scores(
    answers,
    semantic_scores
):

    difficulty_data = {

        "Easy": [],
        "Medium": [],
        "Hard": []

    }

    for answer, score in zip(
        answers,
        semantic_scores
    ):

        difficulty = answer[
            "difficulty"
        ]

        difficulty_data[
            difficulty
        ].append(score)

    results = {}

    for difficulty in difficulty_data:

        scores = difficulty_data[
            difficulty
        ]

        if len(scores) > 0:

            results[difficulty] = round(
                sum(scores)
                /
                len(scores),
                2
            )

        else:

            results[difficulty] = 0

    return results