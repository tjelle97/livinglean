# creating Flask instance variable app

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("pages/index.html")


@app.route('/elements.html', methods=['GET', 'POST'])
def elements():
    return render_template('pages/elements.html')


@app.route('/generic.html', methods=['GET', 'POST'])
def generic():
    return render_template('pages/generic.html')


@app.route("/index.html", methods=['GET', 'POST'])
def index():
    return render_template("pages/index.html")
