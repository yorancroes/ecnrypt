from flask import Flask
from app.database.init_db import init_db

init_db()
app = Flask(__name__)

@app.route("/")
def hello():
    return "hoi"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
