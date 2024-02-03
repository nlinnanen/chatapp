from . import db
from sqlalchemy.sql import text

def create_message(message, conversation_id, sender_id):
    sql = text("INSERT INTO messages (message, conversation_id, sender_id) VALUES (:message, :conversation_id, :sender_id) RETURNING *")
    result = db.session.execute(sql, {"message":message, "conversation_id":conversation_id, "sender_id":sender_id})
    db.session.commit()
    return result.fetchone()

def get_messages(conversation_id):
    result = db.session.execute(text("SELECT * FROM messages WHERE conversation_id = :conversation_id"), {"conversation_id":conversation_id})
    return result.fetchall()

def get_message(id):
    result = db.session.execute(text("SELECT * FROM messages WHERE id = :id"), {"id":id})
    return result.fetchone()

def update_message(id, message):
    sql = text("UPDATE messages SET message = :message WHERE id = :id RETURNING *")
    result = db.session.execute(sql, {"message":message, "id":id})
    db.session.commit()
    return result.fetchone()

def delete_message(id):
    result = db.session.execute(text("DELETE FROM messages WHERE id = :id RETURNING *"), {"id":id})
    db.session.commit()
    return result.fetchone()