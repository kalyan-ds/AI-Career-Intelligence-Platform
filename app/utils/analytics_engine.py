def analyze_interview(
    scores
):
    average_score = round(
        sum(scores) /
        max(1, len(scores)),
        2
    )
    strongest_score = max(scores)
    weakest_score = min(scores)
    strongest_question = (
        scores.index(
            strongest_score
        ) + 1
    )
    weakest_question = (
        scores.index(
            weakest_score
        ) + 1
    )
    return {
        "average_score":
        average_score,
        
        "strongest_question":
        strongest_question,
        
        "weakest_question":
        weakest_question,
        
        "strongest_score":
        strongest_score,
        
        "weakest_score":
        weakest_score
    
    }

