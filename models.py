from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.email_address)