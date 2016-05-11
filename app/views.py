from flask import render_template, flash, redirect
from app import app
from app.custom_forms import LoginForm

# функция представления index опущена для краткости

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template('login.html',
#         title = 'Sign In',
#         form = form)

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # выдуманный пользователь
    return render_template("index.html",
        title = 'Home',
        user = user)
