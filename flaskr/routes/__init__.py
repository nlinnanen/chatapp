from flaskr import app
from ..db import db
from flask import render_template, session, redirect
from sqlalchemy.sql import text

@app.route("/")
def index():
    return render_template("index.html")

from . import login, categories, messages, users, conversations 