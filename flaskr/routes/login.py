from flaskr import app
from flaskr.db import users
from flask import session, redirect, render_template, request



@app.route("/login", methods=["POST", "GET"])
def login():
    if(session.get('username')):
        return redirect('/')

    if request.method == "GET":
        return render_template("login.jinja2")
    
    username = request.form["username"]
    password = request.form["password"]
    
    user = users.get_user_by_username(username)

    if not user:
        user = users.create_user(username, password)

    session['username'] = username
    session['user_id'] = user[0]

    return redirect('/')

@app.route("/logout", methods=["GET"])
def logout():
    del session['username']

    return redirect('/login')