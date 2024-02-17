from flaskr import app
from flaskr.db import users
from flask import session, redirect, render_template, request,make_response 
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
        return render_template("notification.html", error="Invalid username or password")

    if not check_password_hash(user.password, password):
        return render_template("notification.html", error="Invalid username or password")


    session['username'] = username
    session['user_id'] = user[0]

    response = make_response('', 200)
    response.headers['HX-Redirect'] = '/'
    return response


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
        return render_template("notification.html", error="Passwords do not match")
    
    if len(password) < 8:
        return render_template("notification.html", error="Password must be at least 8 characters long")
    
    if len(username) < 3:
        return render_template("notification.html", error="Username must be at least 3 characters long")
    

    user = users.get_user_by_username(username)

    if user:
        return render_template("notification.html", error="User already exists")

    users.create_user(username, password)

    response = make_response('', 201)
    response.headers['HX-Redirect'] = '/login'
    return response