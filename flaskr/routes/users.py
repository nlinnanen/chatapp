from flaskr import app
from flask import render_template, request, redirect

from flaskr.db import users

@app.route("/users", methods=["POST"])
def create_user():
    username = request.form["username"]
    password = request.form["password"]
    users.create_user(username, password)

    messages = get_messages()

    return redirect("/")

@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = users.get_user(id)
    return render_template("user.html", user=user)

@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    username = request.form["username"]
    password = request.form["password"]
    updated_user = users.update_user(id, username, password)
    return render_template("user.html", user=updated_user)