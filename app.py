from flask import Flask, render_template, url_for
from forms import LoginForm, mpnForm

app = Flask(__name__)

# to prevent cross-site request forgery
app.config['SECRET_KEY'] = 'rocketchips1'

@app.route("/")
@app.route("/home")
def hello():
    form = mpnForm()
    user = {'username': 'TJ'}
    return render_template('index.html', title='Home', user=user, form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In', form=form)

@app.route("/results")
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run()