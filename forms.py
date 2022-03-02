from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Regexp

class LoginForm(FlaskForm):
    # basic in truly insecure method of validating email address for MVP using regex to validated email address
    email_address = StringField('Email Address', validators=[DataRequired(), Regexp('*rocketchips.com', 'Invalid Email Address')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class mpnForm(FlaskForm):
    mpn = StringField('MPN', validators=[DataRequired()])
    submit = SubmitField('Search')
