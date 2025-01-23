from flask import Flask, current_app, render_template, request, redirect, session, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from db import User, users, load_database, add_user, add_balance, remove_balance, set_balance, delete_account
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os
from dotenv import load_dotenv


# To-Do:
# DONE - Change and encrypt secret key


app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    load_database()
    if user_id not in users and user_id != "000000":
        return
    user = User()
    user.id = user_id
    if user_id == "000000":
        user.bal = 0.0
        user.name = "administrator"
        return user
    user.bal = users[user_id][2]
    user.name = users[user_id][0]
    return user

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('usern')
    t = 0
    for u in users:
        if username != users[u]:
            continue
        else:
            t = t + 1
    if username == "admin":
        user = User()
        user.id = "000000"
        return user
    if t == 0:
        return

    user = User()
    user.id = u
    return user


@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['usern']
        password = request.form['userp']
        passwordcon = request.form['userpc']
        load_database()
        for u in users:
            if username == users[u][0]:
                return 'Username already in use.'
            elif username == "admin":
                return 'Username already in use.'
        if password != passwordcon:
            return 'Passwords are not the same.'
        add_user(username, generate_password_hash(password, method='pbkdf2:sha1'))
        load_database()
        return redirect(url_for('login'))
    return render_template("signup.html")
        

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['usern']
        password = request.form['userp']
        load_database()
        load_dotenv()
        if username == "admin" and check_password_hash(os.getenv('AP'), password) == True:
                user = User()
                user.id = "000000"
                login_user(user)
                print(f"Administrator logged in at {request.environ['REMOTE_ADDR']}")
                return redirect(url_for('admin'))
        for u in users:
            if username == users[u][0] and check_password_hash(users[u][1], password) == True:
                user = User()
                user.id = u
                login_user(user)
                print(f"User with id {user.get_id()} logged in.")
                return redirect(url_for('protected'))
        return 'Bad login'
    return render_template("login.html")

@app.route('/config',methods=['GET','POST'])
def admin():
    try:
        if not current_user.id == "000000" and current_user.name == "admin":
            return current_app.login_manager.unauthorized()
        load_database()
        if request.method == 'POST':
            search = request.form['srch']
            lagre = {}
            if search in users:
                lagre[search] = users[search]
            elif search == "":
                return render_template("config.html", id=current_user.id, dictjava=users)
            else:
                for u in users:
                    if users[u][0] == search:
                        lagre[u] = users[u]
            return render_template("config.html", id=current_user.id, dictjava=lagre)
        return render_template("config.html", id=current_user.id, dictjava=users)
    except AttributeError:
        return current_app.login_manager.unauthorized()
    

@app.route('/protected', methods=['GET','POST'])
@login_required
def protected():
    if request.method == 'POST':
        toid = request.form['to']
        amnt = request.form['amt']
        load_database()
        if toid in users and float(users[current_user.id][2]) >= float(amnt) and float(amnt) > 0.0:
            add_balance(toid, amnt)
            remove_balance(current_user.id, amnt)
            print(f"Transferred {amnt} from id {current_user.id} to id {toid}")
            load_database()
            return redirect(url_for('protected'))
        return 'Operation impossible.'
    return render_template("protected.html", bal=current_user.bal, id=current_user.id, name=current_user.name)

@app.route('/edit', methods=['POST'])
def edit():
    try:
        if not current_user.id == "000000" and current_user.name == "admin":
            return current_app.login_manager.unauthorized()
        if request.method == 'POST':
            editing = request.form['key']
            session['editing'] = editing
            return redirect(url_for('editid'))
    except AttributeError:
        return current_app.login_manager.unauthorized()

@app.route('/editid', methods=['GET','POST'])
def editid():
    try:
        if not current_user.id == "000000" and current_user.name == "admin":
            return current_app.login_manager.unauthorized()
        if request.method == 'POST':
            load_database()
            if "delete" in request.form:
                print(f"Admin {request.environ['REMOTE_ADDR']} deleted user with id {users[session['editing']]} and balance {users[session['editing']][2]}")
                delete_account(session['editing'])
                return redirect(url_for('admin'))
            amnt = request.form['amt']
            if "set" in request.form:
                print(f"Admin {request.environ['REMOTE_ADDR']} set balance of id {session['editing']} to {amnt} from {users[session['editing']][2]}")
                set_balance(session['editing'],amnt)
            elif "add" in request.form:
                print(f"Admin {request.environ['REMOTE_ADDR']} added {amnt} to id {session['editing']}, (original bal: {users[session['editing']][2]})")
                add_balance(session['editing'],amnt)
            elif "remove" in request.form:
                print(f"Admin {request.environ['REMOTE_ADDR']} removed {amnt} from id {session['editing']}, (original bal: {users[session['editing']][2]})")
                remove_balance(session['editing'],amnt)
            return redirect(url_for('editid'))
        return render_template("edit.html", editid=session['editing'], bal=users[session['editing']][2])
    except AttributeError:
        return current_app.login_manager.unauthorized()

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


if __name__ == '__main__':
    app.run(debug=True)