from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") 
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute(text("SELECT message FROM messages"))
    messages = result.fetchall()
    return render_template("index.html", count=len(messages), messages=messages) 

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    message = request.form["message"]
    sql = text("INSERT INTO messages (message, conversation_id) VALUES (:message, '679219f4-df70-463e-b686-6d1652861447')")
    db.session.execute(sql, {"message":message})
    db.session.commit()
    return redirect("/")