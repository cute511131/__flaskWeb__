from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hellow_world")
def hello_world():
    return"<h1>Hello! world.</h1>"