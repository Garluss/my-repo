import random
import sqlite3

from flask_login import UserMixin

connection = sqlite3.connect("users.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS userdata (id TEXT, username TEXT, password TEXT, balance FLOAT)")
connection.commit()
connection.close()

users = {}
def load_database():
    users.clear()
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM userdata")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    for row in rows:
        id, name, password, bal = row
        users[id] = [name, password, bal]

class User(UserMixin):
    bal = 0.0
    name = ""

def set_balance(id, balance):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('''UPDATE userdata SET balance = ? WHERE id = ?''', (balance, id))
    connection.commit()
    cursor.close()
    connection.close()

def add_balance(id, add: float):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    load_database()
    oldBal = float(users[id][2])
    newBal = oldBal + float(add)
    cursor.execute('''UPDATE userdata SET balance = ? WHERE id = ?''', (newBal, id))
    connection.commit()
    cursor.close()
    connection.close()

def remove_balance(id, remove: float):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    load_database()
    oldBal = float(users[id][2])
    newBal = oldBal - float(remove)
    cursor.execute('''UPDATE userdata SET balance = ? WHERE id = ?''', (newBal, id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_account(id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    load_database()
    cursor.execute('''DELETE FROM userdata WHERE id = ?''', (id,))
    connection.commit()
    cursor.close()
    connection.close()


def add_user(name, passw):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    while True:
        id = ""
        for i in range(6):
            id = id + str(random.randint(1,9))
        if id in users:
            continue
        elif id == "000000":
            continue
        else:
            break
    bal = 0
    string = f"Skapte bruker med id {id} og navn {name}"
    cursor.execute("INSERT INTO userdata VALUES (?, ?, ?, ?)", (id,name,passw,bal))
    connection.commit()
    cursor.close()
    connection.close()
    return string