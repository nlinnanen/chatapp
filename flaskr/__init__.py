from os import getenv
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

from . import routes

WHITELISTED_PATHS = ['/login', '/static']

@app.before_request
def check_user_logged_in():
    if "username" not in session and request.path not in WHITELISTED_PATHS:
        return redirect('/login')
