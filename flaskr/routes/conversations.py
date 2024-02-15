from flaskr import app
from ..db import conversations, messages, categories
from flask import render_template, request, redirect

@app.route("/conversations", methods=["POST"])
def post_conversation():
    categories = request.form.getlist('categories')
    created_conversation = conversations.create_conversation(categories)
    return redirect(f'/conversations/{created_conversation[0]}')

@app.route("/conversations/<id>", methods=["GET"])
def get_conversation_id(id):
    conversation = conversations.get_conversation(id)
    message_list = messages.get_messages(id)
    category_list = categories.get_conversation_categories(id)
    return render_template("conversation.html", conversation=conversation, messages=message_list, categories=category_list)

@app.route("/conversations/<id>", methods=["DELETE"])
def delete_conversation(id):
    conversations.delete_conversation(id)
    return ""
    # return render_template("info.html", info="Successfully deleted conversation")