from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def semantic_score(
    candidate_answer,
    ideal_answer
):

    try:

        candidate_answer = str(candidate_answer)
        ideal_answer = str(ideal_answer)

        if ideal_answer.strip() == "":
            return 0.0

        ideal_embedding = model.encode(
            [ideal_answer]
        )

        candidate_embedding = model.encode(
            [candidate_answer]
        )

        similarity = cosine_similarity(
            ideal_embedding,
            candidate_embedding
        )

        score = similarity[0][0] * 100

        return round(score, 2)

    except Exception:

        return 0.0


def communication_score(
    candidate_answer
):

    word_count = len(
        str(candidate_answer).split()
    )

    if word_count < 20:
        return 50

    elif word_count < 40:
        return 70

    elif word_count < 60:
        return 85

    else:
        return 95


def overall_score(
    technical,
    communication
):

    score = (
        technical * 0.7
        +
        communication * 0.3
    )

    return round(score, 2)
