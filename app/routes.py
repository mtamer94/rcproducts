from pickle import FALSE, TRUE
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, mpnForm
from app.models import User
import pandas as pd
from os.path import join, dirname, realpath


data_path = join(dirname(realpath(__file__)), 'data/catalogue.csv')



@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home')

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('search'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email_address=form.email_address.data).first()
        if user is None:
            flash('Invalid email address')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
    return render_template('login.html', title = 'Sign In', form=form)


# the problems start here
@app.route("/search", methods=['GET','POST'])
def search():
    form = mpnForm()
    # I am going to need to do the logic to search for MPNs here
    if form.validate_on_submit():
        part = form.mpn.data
        included = None
        catalogue = pd.read_csv(data_path)
        if part in catalogue['MPNs'].values:
            # if the part is in the catalog, return the result on a new page
            included = TRUE
            return redirect(url_for('results', pt=part, inc=included))
        elif part not in catalogue['MPNs'].values:
            included = FALSE
            return redirect(url_for('results', pt=part, inc=included))
    else:
        return render_template('search.html', title='Search', form=form)


@app.route("/results<pt><inc>", methods=['GET','POST'])
def results(pt,inc):
    return render_template('results.html',title='Results',pt=pt, inc=inc)
