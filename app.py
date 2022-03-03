from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, mpnForm
from flask_login import (
    LoginManager, UserMixin, login_user, current_user,login_required, logout_user)
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# to prevent cross-site request forgery
app.config['SECRET_KEY'] = 'rocketchips1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app.db' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#login instance
login = LoginManager(app)

authorized_users = {1:'mtamer@rocketchips.com',2:'jpierce@rocketchips.com',3:'tjwhitney@rocketchips.com',4:'awong@fusionww.com'}

@login.user_loader
def load_user(id):
    return authorized_users[int(id)]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home')

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.email_address.data in authorized_users.values()
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

if __name__ == '__main__':
    app.run()