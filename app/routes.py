from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {'username':'asela'}

    posts = [
        {
            'author':{'username':'bobby'},
            'body': 'lunar elipse'
        },

        {
            'author':{'username':'don'},
            'body': 'frimi is cool'
        }
    ]

    return render_template('index.html',title='Good Morning!', user=user, posts=posts)

@app.route("/login", methods = ['GET','POST'])
# login view function
def login(): 
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me ={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign-in' , form=form)