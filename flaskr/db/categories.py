from . import db
from sqlalchemy.sql import text


def create_category(name):
    sql = text("INSERT INTO categories (name) VALUES (:name) RETURNING *")
    result = db.session.execute(sql, {"name": name})
    db.session.commit()
    return result.fetchone()


def get_categories():
    result = db.session.execute(text("SELECT * FROM categories"))
    return result.fetchall()


def get_category(id):
    result = db.session.execute(
        text("SELECT * FROM categories WHERE id = :id"), {"id": id})
    return result.fetchone()


def get_conversation_categories(conversation_id):
    result = db.session.execute(text(
        "SELECT c.id, c.name FROM categories_conversation cc JOIN categories c ON cc.category_id = c.id WHERE conversation_id = :conversation_id"), {"conversation_id": conversation_id})
    return result.fetchall()


def update_category(id, name):
    sql = text("UPDATE categories SET name = :name WHERE id = :id RETURNING *")
    result = db.session.execute(sql, {"name": name, "id": id})
    db.session.commit()
    return result.fetchone()


def delete_category(id):
    result = db.session.execute(
        text("DELETE FROM categories WHERE id = :id RETURNING *"), {"id": id})
    db.session.commit()
    return result.fetchone()
