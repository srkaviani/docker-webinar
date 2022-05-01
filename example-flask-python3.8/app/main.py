from flask import Flask
from datetime import datetime

app = Flask(__name__)
date = datetime.now()


@app.route("/")
def hello():
    return f"<h4> <center> Hello World from Flask in a uWSGI Nginx Docker container {date} </h4> "


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
