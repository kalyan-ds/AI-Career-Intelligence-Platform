import sqlite3
import pandas as pd

def create_database():

    conn = sqlite3.connect(
        "interview_history.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS interviews (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            date TEXT,

            role TEXT,

            semantic_score REAL,

            communication_score REAL,

            overall_score REAL,

            hiring_probability REAL

        )
        """
    )

    conn.commit()

    conn.close()
def save_interview(

    date,

    role,

    semantic_score,

    communication_score,

    overall_score,

    hiring_probability

):

    conn = sqlite3.connect(
        "interview_history.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        INSERT INTO interviews (

            date,

            role,

            semantic_score,

            communication_score,

            overall_score,

            hiring_probability

        )

        VALUES (?, ?, ?, ?, ?, ?)
        """,

        (

            date,

            role,

            semantic_score,

            communication_score,

            overall_score,

            hiring_probability

        )

    )

    conn.commit()

    conn.close()

def get_interview_history():

    conn = sqlite3.connect(
        "interview_history.db"
    )

    df = pd.read_sql_query(

        """
        SELECT *
        FROM interviews
        ORDER BY id DESC
        """,

        conn

    )

    conn.close()

    return df