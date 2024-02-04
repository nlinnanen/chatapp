from flaskr import app
from ..db.categories import create_category, get_category
from flask import render_template, request

@app.route("/api/categories", methods=["POST"])
def create_category():
    name = request.form["name"]
    created_category = create_category(name)
    return render_template("category.html", category=created_category)


@app.route("/api/categories/<id>", methods=["GET"])
def get_category(id):
    category = get_category(id)
    return render_template("category.html", category=category)

