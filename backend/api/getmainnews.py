from flask import Flask, render_template, jsonify, request
from myDb import myDB

db = myDB()


def GetMainNews():
    cursor = db.getConn().cursor()

    try:
        sql = "select * from main_news"
        cursor.execute(sql)
        result = cursor.fetchone()
        return jsonify({
            'state': "success",
            'title': result[0],
            'vicetitle': result[1],
            'content': result[2]
        })
    except Exception as e:
        db.getConn().close()
        print(e.args)
        return jsonify({
            'state': "failed",
        })




