from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    # basic in truly insecure method of validating email address for MVP using regex to validated email address
    email_address = StringField('Email Address', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class mpnForm(FlaskForm):
    mpn = StringField('MPN', validators=[DataRequired()])
    submit = SubmitField('Search')
