from flaskr import app
from flaskr.db import users
from flask import session, redirect, render_template, request
from werkzeug.security import check_password_hash


@app.route("/login", methods=["POST", "GET"])
def login():
    if(session.get('username')):
        return redirect('/')

    if request.method == "GET":
        return render_template("login.html")
    
    username = request.form["username"]
    password = request.form["password"]

    user = users.get_user_by_username(username)

    if not user:
        return redirect('/register')

    if not check_password_hash(user.password, password):
        return redirect('/login')


    session['username'] = username
    session['user_id'] = user[0]

    return redirect('/')


@app.route("/logout", methods=["GET"])
def logout():
    del session['username']

    return redirect('/login')

@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_post():
    username = request.form["username"]
    password = request.form["password-1"]
    password_2 = request.form["password-2"]

    if password != password_2:
        return redirect('/register')
    
    user = users.get_user_by_username(username)

    if user:
        return redirect('/register')

    users.create_user(username, password)

    return redirect('/login')