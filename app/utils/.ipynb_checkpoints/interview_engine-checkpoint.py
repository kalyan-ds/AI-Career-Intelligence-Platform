import pandas as pd
import os
def load_questions(role, difficulty):
    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )
    csv_path = os.path.join(
        current_dir,
        "..",
        "..",
        "data",
        "interview_questions_v3.csv"
    )
    df = pd.read_csv(csv_path)
    filtered_df = df[
        (df["role"] == role)
        &
        (df["difficulty"] == difficulty)
        ]
    questions = filtered_df.sample(
        n=min(10, len(filtered_df))
    )
    return questions.to_dict("records")