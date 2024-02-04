from flaskr import app
from ..db.messages import create_message, update_message, delete_message
from flask import render_template, request

@app.route("/messages", methods=["POST"])
def create_message():
    message = request.form["message"]
    conversation_id = request.form["conversation_id"]
    sender_id = request.form["sender_id"]
    created_message = create_message(message, conversation_id, sender_id)
    return render_template("message.html", message=created_message)


@app.route("/messages/<id>", methods=["PUT"])
def update_message(id):
    message = request.form["message"]
    updated_message = update_message(id, message)
    return render_template("message.html", message=updated_message)

@app.route("/messages/<id>", methods=["DELETE"])
def delete_message(id):
    deleted_message = delete_message(id)
    return render_template("info.html", info="Successfully deleted message")
