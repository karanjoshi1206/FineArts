# from app import db

class Artists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    batch = db.Column(db.String(8), nullable=False)
    pic = db.Column(db.String(10000), nullable=True)

    def __repr__(self):
        return '<Name %r>' % self.id

    