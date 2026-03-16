from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my first server!"

app.run(port=5000)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my first server!"

app.run(port=5000)
