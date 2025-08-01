# mkdir froshims_flask_app
# cd froshims_flask_app
# cp ../my_flask_app/requirements.txt .
# . ../../bin/activate (. _Git/_test/bin/activate)
# pip install -r requirements.txt
# touch app.py
# mkdir templates
# touch layout.html index.html
# flask run

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

DB = "shows.db"

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    #if request.method == "POST":
    #if request.form.get("q"):
        #query = request.form.get("q") # pro POST
        query = request.args.get("q")
        if query:
            con = sqlite3.connect(DB)
            #con.row_factory = sqlite3.Row
            con.row_factory = dict_factory
            cur = con.execute(f"SELECT * from shows where title LIKE '%{query}%'")
            shows = cur.fetchall()
            con.close
        #print(query)
        else:
            shows = [{'title':'tady bude vysledek'}]
        #return render_template("search.html", shows=shows)
        return jsonify(shows)
