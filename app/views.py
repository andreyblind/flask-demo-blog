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
def start():
    return "string"
@app.route('/test')
def test_route():
    return 'test string'
