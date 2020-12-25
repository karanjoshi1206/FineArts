from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from pic_db import database as Database
# from user import Artists as Artists

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///artist.db"

# db = SQLAlchemy(app)

@app.route("/")
def home():
    # artists = Artists.query.order_by(Artists.id)
    return render_template("base.html",artists=Database)

@app.route("/<username>")
def display(username):
    return render_template("display.html", user=Database[username])


@app.route("/admin/", methods=["POST","GET"])
def admin():
    # if request.method == "POST":
        # artist_name = request.form['name']
        # new_artist = Artists(name=artist_name)

        # try:
        #     db.session.add(new_artist)
        #     db.session.commit()
        #     return redirect(url_for('home'))
        # except:
        #     return "Error adding the Artist"
    return render_template("admin.html")
#driver code
if(__name__=="__main__"):
    app.run(debug=True)