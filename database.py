
import mysql.connector
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"), override=True)

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=3306
    )

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Database Connected Successfully!")
        conn.close()
    except mysql.connector.Error as e:
        print("Database Error:", e)
