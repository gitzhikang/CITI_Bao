from flask import Flask, render_template, jsonify, request
from myDb import myDB

db = myDB()


def GetHeatedNews():
    cursor = db.getConn().cursor()

    try:
        sql = "select * from heated_news"
        cursor.execute(sql)
        result = cursor.fetchall()
        return jsonify({
            'state': "success",
            'result': result
        })
    except Exception as e:
        db.getConn().close()
        print(e.args)
        return jsonify({
            'state': "failed",
        })




