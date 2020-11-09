# creating Flask instance variable app

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("pages/index.html")


@app.route('/elements.html')
def elements():
    return render_template('pages/elements.html')


@app.route('/generic.html')
def generic():
    return render_template('pages/generic.html')


@app.route("/index.html")
def index():
    return render_template("pages/index.html")
