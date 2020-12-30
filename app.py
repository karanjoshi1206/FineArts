from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(50), nullable=False)
    instagram = db.Column(db.String(120), nullable=False)
    branch = db.Column(db.String(6), nullable=False)
    image = db.Column(db.String(400), nullable=False, default='https://res.cloudinary.com/humbleartist/image/upload/v1609164246/Profile/IMG-20201220-WA0244_-_Vidushi_Agarwal_mwjlev.jpg')
    votes = db.Column(db.Integer, nullable=False, default=0)
    post = db.relationship('Post', backref='artist', lazy=True)

    def __repr__(self):
        return f"User('{self.artist_name}','{self.branch}','{self.instagram}','{self.image}','{self.votes}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    art = db.Column(db.String(), nullable=False, default='')
    likes = db.Column(db.Integer, nullable=False, default=0)
    artist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.art}','{self.likes}')"

@app.route("/")
def home():
    return render_template("base.html", artists=User.query.all())

@app.route("/team/")
def team():
    return render_template("team.html")

@app.route("/nicetrybutIdontkeeptheadminurlasadminurlcauseIain'tStupid/")
def admin():
    return render_template("admin.html")

@app.route("/artsteam/")
def artsteam():
    return render_template("artsteam.html")

@app.route("/<username>")
def display(username):
    user=User.query.filter_by(artist_name=username).first()
    print(user)
    work = user.post
    return render_template("display.html",user=user, work=work)



#driver code
if(__name__=="__main__"):
    app.run(debug=True)