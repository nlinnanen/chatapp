from . import db
from sqlalchemy.sql import text


def create_conversation(categories: list):
    sql = text("INSERT INTO conversations DEFAULT VALUES RETURNING *")
    result = db.session.execute(sql)
    conversation = result.fetchone()
    for category_id in categories:
        sql = text(
            "INSERT INTO categories_conversation (conversation_id, category_id) VALUES (:conversation_id, :category_id)")
        db.session.execute(
            sql, {"conversation_id": conversation[0], "category_id": category_id})
    db.session.commit()
    return conversation


def get_conversations():
    result = db.session.execute(text("SELECT * FROM conversations"))
    return result.fetchall()


def get_conversation(id):
    result = db.session.execute(
        text("SELECT * FROM conversations WHERE id = :id"), {"id": id})
    return result.fetchone()


def get_conversations_for_category(category_id):
    result = db.session.execute(text('''
            SELECT c.id, c.created_at
            FROM categories_conversation cc JOIN conversations c ON cc.conversation_id = c.id
            WHERE category_id = :category_id
        '''), {"category_id": category_id})

    return result.fetchall()

def delete_conversation(id):
    result = db.session.execute(
        text("DELETE FROM conversations WHERE id = :id RETURNING *"), {"id": id})
    db.session.commit()
    return result.fetchone()
