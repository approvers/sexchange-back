from flask import *
import sqlite3


app = Flask(__name__)


dbpath = './sexchange.sqlite'

@app.route('/register', methods=['POST'])
def register():
    name = request.form["name"]
    twitter_id = request.form["twitter_id"]
    password = request.form["password"]
    seiheki = request.form["seiheki"]

    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()

    cursor.execute(
        "select * from users where twitter_id={};".format(twitter_id)
    )

    res = cursor.fetchone()
    if res == None:
        cursor.execute(
            "insert into users values (?, {}, {}, {}, {});".format(name, twitter_id, password, seiheki)
        )
        connection.commit()
        connection.close()
        return jsonify({"status": 1})
    else:
        connection.commit()
        connection.close()
        return jsonify({"status": 0})


@app.route('/login', methods=['POST'])
def login():
    twitter_id = request.form("twitter_id")
    password = request.form("password")
    
    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()

    cursor.execute(
        "select * from users where twitter_id={} and password={};".format(twitter_id, password)
    )

    res = cursor.fetchone()
    if res == None:
        connection.commit()
        connection.close()
        return jsonify({"status": 0})    
    else:
        connection.commit()
        connection.close()
        return jsonify({"status": 1})



if __name__ == '__main__':
    app.run(debug = True)