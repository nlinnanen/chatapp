from . import db
from sqlalchemy.sql import text

def create_conversation(name):
    sql = text("INSERT INTO conversations (name) VALUES (:name) RETURNING *")
    result = db.session.execute(sql, {"name":name})
    db.session.commit()
    return result.fetchone()

def get_conversations():
    result = db.session.execute(text("SELECT * FROM conversations"))
    return result.fetchall()

def get_conversation(id):
    result = db.session.execute(text("SELECT * FROM conversations WHERE id = :id"), {"id":id})
    return result.fetchone()

def update_conversation(id, name):
    sql = text("UPDATE conversations SET name = :name WHERE id = :id RETURNING *")
    result = db.session.execute(sql, {"name":name, "id":id})
    db.session.commit()
    return result.fetchone()

def delete_conversation(id):  
    result = db.session.execute(text("DELETE FROM conversations WHERE id = :id RETURNING *"), {"id":id})
    db.session.commit()
    return result.fetchone()