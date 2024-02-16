from flaskr import app
from flask import render_template, request

from flaskr.db import categories, conversations

@app.route("/categories", methods=["POST"])
def create_category():
    name = request.form["name"]
    created_category = categories.create_category(name)
    return render_template("category_button.html", category=created_category, selected_category=None)


@app.route("/categories/<id>", methods=["GET"])
def get_category(id):
    if id == "all":
        conversation_list = conversations.get_conversations()
    else:
        conversation_list = conversations.get_conversations_for_category(id)
        
    categories_list = categories.get_categories()
    app.logger.info(categories_list)
    return render_template("conversation_list.html", conversations=conversation_list, categories=categories_list, selected_category=id)

