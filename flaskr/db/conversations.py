from . import db
from sqlalchemy.sql import text

def create_conversation():
    sql = text("INSERT INTO conversations DEFAULT VALUES RETURNING *")
    result = db.session.execute(sql)
    db.session.commit()
    return result.fetchone()

def get_conversations():
    result = db.session.execute(text("SELECT * FROM conversations"))
    return result.fetchall()

def get_conversation(id):
    result = db.session.execute(text("SELECT * FROM conversations WHERE id = :id"), {"id":id})
    return result.fetchone()

def delete_conversation(id):  
    result = db.session.execute(text("DELETE FROM conversations WHERE id = :id RETURNING *"), {"id":id})
    db.session.commit()
    return result.fetchone()