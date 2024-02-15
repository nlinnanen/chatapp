from os import getenv
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

from . import routes

WHITELISTED_PATHS = ['login', 'register', 'static']

@app.before_request
def check_user_logged_in():
    first_part_of_path = request.path.split('/')[1] 
    if "username" not in session and first_part_of_path not in WHITELISTED_PATHS:
        return redirect('/login')
