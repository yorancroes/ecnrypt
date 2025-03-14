from .connect import  connect_db

def init_db():
    connection = connect_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        username VARCHAR(255),
                        password VARCHAR(255),
                        email VARCHAR(255),
                        date_created TIMESTAMP default CURRENT_TIMESTAMP
                    );
                """)
                #Todo: add tables
                connection.commit()
            print("Database initialized successfully.")
        except Exception as e:
            print(f"An error occurred while initializing the database: {e}")
        finally:
            connection.close()
    else:
        print("Failed to connect to the database.")

if __name__ == '__main__':
    init_db()
