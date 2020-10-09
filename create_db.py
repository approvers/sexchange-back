import sqlite3


dbpath = './sexchange.sqlite'


connection = sqlite3.connect(dbpath)
cursor = connection.cursor()
 

try:
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, twitter_id, TEXT, password TEXT, seiheki TEXT)"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS exchange (id INTEGER PRIMARY KEY, twitter_id_1 TEXT, twitter_id_2 TEXT)"
    )

except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])
 
# 保存を実行（忘れると保存されないので注意）
connection.commit()
 
# 接続を閉じる
connection.close()