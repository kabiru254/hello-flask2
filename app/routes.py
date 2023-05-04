from app import app
from flask import render_template, flash, redirect, url_for
from app.form import LoginForm

@app.route('/')
@app.route('/home')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/about-me')
def about_me():
    """About Me URL"""
    return render_template('about_me.html', title= 'About Me Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Log In URL"""
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'You are requesting to log in {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title= 'Log In Page', form=form)