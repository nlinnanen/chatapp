from flaskr import app
from .db import db
from flask import render_template, request
from sqlalchemy.sql import text

@app.route("/")
def index():
    print(type(db))
    result = db.session.execute(text("SELECT message, username FROM messages INNER JOIN users ON messages.sender_id = users.id ORDER BY messages.created_at"))
    messages = result.fetchall()
    return render_template("index.html", messages=messages) 

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/messages", methods=["POST"])
def create_message():
    message = request.form["message"]
    user = db.session.execute(text("SELECT id, username FROM users WHERE username = :username"), {"username":"user"}).fetchone()
    sql = text("INSERT INTO messages (message, sender_id) VALUES (:message, :sender_id) RETURNING *")
    created_message = db.session.execute(sql, {"message":message, "sender_id":user.id}).fetchone()
    db.session.commit()
    return render_template("message.html", message={"message": created_message.message, "username":user.username})
    