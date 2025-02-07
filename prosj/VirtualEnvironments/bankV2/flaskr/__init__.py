from flask import Flask, current_app, render_template, request, redirect, session, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from db import User, users, load_database, add_user, add_balance, remove_balance, set_balance, delete_account
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os
import logging
from time import gmtime, strftime
from dotenv import load_dotenv


time = strftime("%d-%m-%Y_%H-%M-%S", gmtime())
filenam =  fr"{os.getcwd()}\logs\{time}.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s»  %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')

file_handler = logging.FileHandler(filename=filenam,encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # You can set the desired log level for console output
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# To-Do:
# DONE - Change and encrypt secret key


app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

log = logging.getLogger('werkzeug')
log.disabled = True

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
    try:
        if not current_user.id == "000000" and current_user.name == "admin":
            return current_app.login_manager.unauthorized()
        if request.method == 'POST':
            username = request.form['usern']
            password = request.form['userp']
            passwordcon = request.form['userpc']
            load_database()
            for u in users:
                if username == users[u][0]:
                    return 'Brukernavn allerede i bruk.'
                elif username == "admin":
                    return 'Brukernavn allerede i bruk.'
            if password != passwordcon:
                return 'Passordene er ikke like.'
            info = add_user(username, generate_password_hash(password, method='pbkdf2:sha1'))
            logger.info(info)
            load_database()
            return redirect(url_for('login'))
        return render_template("signup.html")
    except AttributeError:
        return current_app.login_manager.unauthorized()

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
                logger.info(f'Administrator logget inn ved {request.environ['REMOTE_ADDR']}')
                return redirect(url_for('admin'))
        for u in users:
            if username == users[u][0] and check_password_hash(users[u][1], password) == True:
                user = User()
                user.id = u
                login_user(user)
                logger.info(f'Bruker med id {user.get_id()} logget inn.')
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
            logger.info(f"Overførte {amnt} fra id {current_user.id} til id {toid}")
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
                logger.info(f"Admin {request.environ['REMOTE_ADDR']} slettet bruker med id {session['editing']}, med pengesum {users[session['editing']][2]}")
                delete_account(session['editing'])
                return redirect(url_for('admin'))
            amnt = request.form['amt']
            if "set" in request.form:
                logger.info(f"Admin {request.environ['REMOTE_ADDR']} endret pengesum av bruker {session['editing']} til {amnt} PEC fra {users[session['editing']][2]} PEC")
                set_balance(session['editing'],amnt)
            elif "add" in request.form:
                logger.info(f"Admin {request.environ['REMOTE_ADDR']} la {amnt} PEC til konto med id {session['editing']}, (original pengesum: {users[session['editing']][2]} PEC)")
                add_balance(session['editing'],amnt)
            elif "remove" in request.form:
                logger.info(f"Admin {request.environ['REMOTE_ADDR']} fjernet {amnt} PEC fra konto med id {session['editing']}, (original pengesum: {users[session['editing']][2]} PEC)")
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
    app.run()