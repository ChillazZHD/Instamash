from . import db

class Girldata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    elo = db.Column(db.Float)
    image_source = db.Column(db.String(200))
    ph = db.Column(db.String(100))
    insta = db.Column(db.String(200))
    twitter = db.Column(db.String(100))

