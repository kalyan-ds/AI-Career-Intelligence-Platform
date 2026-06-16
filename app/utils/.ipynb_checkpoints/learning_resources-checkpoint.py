import pandas as pd
import os


def get_learning_resources():

    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    csv_path = os.path.join(
        current_dir,
        "..",
        "..",
        "data",
        "learning_resources.csv"
    )

    df = pd.read_csv(
        csv_path
    )

    resources = {}

    for _, row in df.iterrows():

        resources[
            row["skill"]
        ] = {

            "documentation":
            row["documentation"],

            "youtube":
            row["youtube"],

            "project":
            row["project"]

        }

    return resources