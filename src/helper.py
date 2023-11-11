import psycopg2
from dotenv import load_dotenv
import os


def create_connection():
    """create a database connection to a SQLite database"""
    load_dotenv()

    DBNAME = os.getenv("DBNAME")
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")

    conn = psycopg2.connect(
        dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
    )
    return conn
