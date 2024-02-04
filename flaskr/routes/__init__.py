from flaskr import app
from flaskr.db.conversations import get_conversations
from flask import render_template

@app.route("/")
def index():
    conversations = get_conversations()
    return render_template("index.jinja2", conversations=conversations)

from . import login, categories, messages, users, conversations 