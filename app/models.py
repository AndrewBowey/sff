from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    contribution = db.Column(db.Integer, nullable=False)
    employer_contribution = db.Column(db.Integer, nullable=False)
    retirement_age = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.String, nullable=False)
    coins = db.Column(db.Integer, nullable=False)