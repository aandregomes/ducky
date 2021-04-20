from main import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    long_url = db.Column(db.String(2048), unique=True)
    short_url = db.Column(db.String(7), unique=True)