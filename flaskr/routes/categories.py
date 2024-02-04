from flaskr import app
from flask import render_template, request

from flaskr.db import categories

@app.route("/api/categories", methods=["POST"])
def create_category():
    name = request.form["name"]
    created_category = categories.create_category(name)
    return render_template("category.html", category=created_category)


@app.route("/api/categories/<id>", methods=["GET"])
def get_category(id):
    category = categories.get_category(id)
    return render_template("category.html", category=category)

