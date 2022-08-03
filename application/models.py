
from application import db


class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    positive_count = db.Column(db.Integer)
    positive_reviews = db.Column(db.String)
    negative_reviews = db.Column(db.String)
    data = db.Column(db.JSON)
    

    