from flaskr import app
from ..db.conversations import create_conversation, get_conversation
from flask import render_template, request, redirect

@app.route("/conversations", methods=["POST"])
def create_conversation():
    name = request.form["name"]
    created_conversation = create_conversation(name)
    return redirect(f'/conversations/${created_conversation["id"]}')

@app.route("/conversations/<id>", methods=["GET"])
def get_conversation(id):
    conversation = get_conversation(id)
    return render_template("conversation.html", conversation=conversation)