from datetime import datetime
from app import db, login
from flask_login import UserMixin

# add UserMixin to make the model compatible with Flask-Login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.email_address)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))