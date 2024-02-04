from flaskr import app
from ..db import db
from flask import render_template, request
from sqlalchemy.sql import text

@app.route("/")
def index():
    print(type(db))
    result = db.session.execute(text("SELECT message, username FROM messages INNER JOIN users ON messages.sender_id = users.id ORDER BY messages.created_at"))
    messages = result.fetchall()
    return render_template("index.html", messages=messages) 

from . import categories, messages, users, conversations 