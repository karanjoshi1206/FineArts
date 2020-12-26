from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from pic_db import database as Database

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html",artists=Database)

@app.route("/team/")
def team():
    return render_template("team.html")

@app.route("/<username>")
def display(username):
    return render_template("display.html", user=Database[username], username=username)



#driver code
if(__name__=="__main__"):
    app.run(debug=True)