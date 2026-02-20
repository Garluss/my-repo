from flask import Flask, redirect, session, url_for, request, render_template
import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS norai (id INTEGER, word TEXT, translation TEXT, type TEXT)")
connection.commit()
connection.close()

app = Flask(__name__)

app.secret_key = 'simba12'



norai = {}
def load_database():
    norai.clear()
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM norai")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    for row in rows:
        id, nor, ai, type = row
        norai[id] = [nor, ai, type]

def finn_id(ord):
    filterres = []
    print(norai)
    if ord != "":
        for x in norai:
            if ord in norai[x][0]:
                filterres.append(x)
    return filterres

ordtyper = ["verb","adjektiv","substantiv","adverb","pronomen","determinativ","konjunksjon","subjunksjon","preposisjon","interjeksjon"]
def legg_til_norai(ordnor,ordai,type):
    t = len(norai)+1
    print(t)
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    if type not in ordtyper:
        return False
    if len(norai) > 0:
        for i in norai:
            inst = 0
            if norai[i][0] == ordnor and norai[i][1] == ordai:
                inst += 1
            if inst == 0:
                cursor.execute("INSERT INTO norai VALUES (?, ?, ?, ?)", (t, ordnor,ordai,type))
                connection.commit()
    else:
        cursor.execute("INSERT INTO norai VALUES (?, ?, ?, ?)", (t, ordnor,ordai,type))
        connection.commit()
    cursor.close()
    connection.close()

def slett_ord_norai(id):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    if int(id) in norai:
        cursor.execute("DELETE FROM norai WHERE id = ?", (int(id),))
        print(f"Deleted {norai[int(id)]} from table")
        connection.commit()
        if len(norai) > int(id):
            for i in range(len(norai)-int(id)):
                newId = int(id) + i
                oldId = newId + 1
                cursor.execute('''UPDATE norai SET id = ? WHERE id = ?''', (newId, oldId))
                connection.commit()
    cursor.close()
    connection.close()

def soek_norai(ord):
    ord = ord.lower()
    if ord in norai:
        print(f"Ord: {ord} =  {norai[ord][0]} ({norai[ord][1]})")
    else:
        print(f"Fant ikke ordet {ord} i Norsk-Ai-Fel-ordbok")

@app.route("/")
def home():
    return render_template("test.html")

@app.route("/list", methods=['POST','GET'])
def list():
    if "logged_in" in session and request.method == 'POST':
        try:
            ordn = request.form["on"].lower()
            orda = request.form["oa"].lower()
            ordk = request.form["ok"].lower()
            load_database()
            legg_til_norai(ordn,orda,ordk)
            load_database()
            return render_template("list.html", dictjava={})
        except KeyError:
            try:
                slettord = request.form["sletto"]
                load_database()
                slett_ord_norai(slettord)
                load_database()
                return render_template("list.html", dictjava={})
            except KeyError:
                filterord = request.form["filtero"]
                liste = []
                load_database()
                liste = finn_id(filterord)
                load_database()
                if len(liste) > 0:
                    lagre = {}
                    for tall in liste:
                        lagre[tall] = norai[tall]
                    return render_template("list.html", dictjava=lagre)
                else:
                    return render_template("list.html", dictjava={})
    elif "logged_in" in session:
        load_database()
        return render_template("list.html", dictjava={})
    else:
        return "Invalid credentials."

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        password = request.form['nm']
        if password == "admin":
            session['logged_in'] = True
            return redirect(url_for('list'))
        else:
            return redirect(url_for('home'))
    else:
        password = request.args.get('nm')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)