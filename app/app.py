from flask import Flask
from app.database.init_db import init_db

app = Flask(__name__)

@app.before_first_request
def initialize():
    init_db()

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
