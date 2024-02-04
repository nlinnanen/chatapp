from . import db
from sqlalchemy.sql import text


def create_user(username: str, password: str) -> dict: 
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password) RETURNING *")
    result = db.session.execute(sql, {"username":username, "password":password})
    db.session.commit()
    return result.fetchone()

def get_users() -> list:
    result = db.session.execute(text("SELECT * FROM users"))
    return result.fetchall()

def get_user(id: str) -> dict:
    result = db.session.execute(text("SELECT * FROM users WHERE id = :id"), {"id":id})
    return result.fetchone()

def get_user_by_username(username: str) -> dict:
    result = db.session.execute(text("SELECT * FROM users WHERE username = :username"), {"username":username})
    return result.fetchone()

def update_user(id: str, username: str, password: str) -> dict:
    sql = text("UPDATE users SET username = :username, password = :password WHERE id = :id RETURNING *")
    result = db.session.execute(sql, {"username":username, "password":password, "id":id})
    db.session.commit()
    return result.fetchone()

def delete_user(id: str) -> dict:
    result = db.session.execute(text("DELETE FROM users WHERE id = :id RETURNING *"), {"id":id})
    db.session.commit()
    return result.fetchone()