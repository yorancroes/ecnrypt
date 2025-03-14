import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



def connect_db():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("Database connection established!")
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None


