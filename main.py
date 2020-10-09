from flask import *
import sqlite3


app = Flask(__name__)


dbpath = './sexchange.sqlite'
connection = sqlite3.connect(dbpath)
cursor = connection.cursor()

@app.route('/register', methods=['POST'])
def register():
    name = request.form["name"]
    twitter_id = request.form["twitter_id"]
    password = request.form["password"]
    seiheki = request.form["seiheki"]

    cursor.execute(
        "select * from users where twitter_id={};".format(twitter_id)
    )

    res = cursor.fetchone()
    if res == None:
        cursor.execute(
            "insert into users values (?, {}, {}, {}, {});".format(name, twitter_id, password, seiheki)
        ) 
        return jsonify({"status": 1})
    else:
        return jsonify({"status": 0})


if __name__ == '__main__':
    app.run(debug = True)