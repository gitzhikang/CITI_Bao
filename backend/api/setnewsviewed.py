import time

from flask import Flask, render_template, jsonify, request
from myDb import myDB

db = myDB()

def NewsViewed():
    label = request.get_json()["label"]
    cursor = db.getConn().cursor()
    sql = ""
    if label == "E":
        sql = "insert into news_viewed(viewtime, e, s, g) values('" + str(time.time()) + "', '1', '0', '0')"
    elif label == "S":
        sql = "insert into news_viewed(viewtime, e, s, g) values('" + str(time.time()) + "', '0', '1', '0')"
    elif label == "G":
        sql = "insert into news_viewed(viewtime, e, s, g) values('" + str(time.time()) + "', '0', '0', '1')"
    print(sql)
    try:
        cursor.execute(sql)
        db.getConn().commit()
        db.getConn().close()
        return jsonify({
            'state': "success",
        })

    except Exception as e:
        db.getConn().close()
        print(e.args)
        return jsonify({
            'state': "failed",
        })

