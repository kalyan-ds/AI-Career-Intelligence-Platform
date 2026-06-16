def calculate_progress_stats(
    history_df
):

    if len(history_df) == 0:

        return {

            "total_interviews": 0,

            "average_score": 0,

            "highest_score": 0,

            "most_selected_role": "N/A"

        }

    return {

        "total_interviews":
        len(history_df),

        "average_score":
        round(
            history_df[
                "overall_score"
            ].mean(),
            2
        ),

        "highest_score":
        round(
            history_df[
                "overall_score"
            ].max(),
            2
        ),

        "most_selected_role":
        history_df[
            "role"
        ].mode()[0]

    }