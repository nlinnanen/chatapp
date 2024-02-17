from flaskr import app
from flask import render_template, request

from flaskr.db import categories, conversations

@app.route("/categories", methods=["POST"])
def create_category():
    name = request.form["name"]

    if not name:
        return render_template("notification.html", error="Category name cannot be empty")
    
    if len(name) > 10:
        return render_template("notification.html", error="Category name cannot be longer than 10 characters")
    
    if len(name) < 3:
        return render_template("notification.html", error="Category name must be at least 3 characters long")

    try:
        created_category = categories.create_category(name)
    except Exception as e:
        return render_template("notification.html", error=e.args[0])

    category_button = render_template("category_button.html", category=created_category, selected_category=None)
    notification = render_template("notification.html", info="Successfully created category")
    return category_button + notification


@app.route("/categories/<id>", methods=["GET"])
def get_category(id):
    if id == "all":
        conversation_list = conversations.get_conversations()
    else:
        conversation_list = conversations.get_conversations_for_category(id)
        
    categories_list = categories.get_categories()
    app.logger.info(categories_list)
    return render_template("conversation_list.html", conversations=conversation_list, categories=categories_list, selected_category=id)

