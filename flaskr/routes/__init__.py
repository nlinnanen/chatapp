from flaskr import app
from flaskr.db.conversations import get_conversations
from flaskr.db.categories import get_categories
from flask import render_template

@app.route("/")
def index():
    conversations = get_conversations()
    categories = get_categories()
    return render_template("index.html", conversations=conversations, categories=categories, selected_category="all")

from . import login, categories, messages, users, conversations 