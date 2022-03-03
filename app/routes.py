from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, mpnForm
from app.models import User


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home')

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email_address=form.email_address.data).first()
        if user is None:
            flash('Invalid email address')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)

        return redirect('/search')
    return render_template('login.html', title = 'Sign In', form=form)

@app.route("/search", methods=['GET','POST'])
def search():
    form = mpnForm()
    user = {'username': 'TJ'}
    # I am going to need to do the logic to search for MPNs here
    return render_template('search.html', title='Search', form=form, user=user)