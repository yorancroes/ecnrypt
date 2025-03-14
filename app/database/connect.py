import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5433")
        )
        print("Database connection established!")
        return connection

    except Exception as e:
        print(f"Error: {e}")
        return None


