from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///artist.db"

db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("base.html")
#driver code
if(__name__=="__main__"):
    app.run(debug=True)