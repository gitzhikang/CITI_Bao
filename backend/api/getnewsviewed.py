import time

from flask import Flask, render_template, jsonify, request
from myDb import myDB

DAY = 7
db = myDB()

def GetNewsViewed():
    cursor = db.getConn().cursor()
    e_history = [0, 0, 0, 0, 0, 0]
    s_history = [0, 0, 0, 0, 0, 0]
    g_history = [0, 0, 0, 0, 0, 0]
    result_e = []
    result_s = []
    result_g = []
    try:
        sql = "select * from news_viewed where e='1'"
        cursor.execute(sql)
        result_e = cursor.fetchall()
    except Exception as e:
        db.getConn().close()
        print(e.args)
        return jsonify({
            'state': "failed",
        })

    try:
        sql = "select * from news_viewed where s='1'"
        cursor.execute(sql)
        result_s = cursor.fetchall()
    except Exception as e:
        db.getConn().close()
        print(e.args)
        return jsonify({
            'state': "failed",
        })

    try:
        sql = "select * from news_viewed where g='1'"
        cursor.execute(sql)
        result_g = cursor.fetchall()
    except Exception as e:
        db.getConn().close()
        print(e.args)
        return jsonify({
            'state': "failed",
        })

    ruler = time.time()
    for re in result_e:
        gap = ruler - float(re[1])
        print("gap" ,gap)
        day = int(gap / (DAY * 24 * 60 * 60))
        print(day)
        e_history[day] += 1
    for re in result_s:
        gap = ruler - float(re[1])
        day = int(gap / (DAY * 24 * 60 * 60))
        s_history[day] += 1
    for re in result_g:
        gap = ruler - float(re[1])
        day = int(gap / (DAY * 24 * 60 * 60))
        g_history[day] += 1

    return jsonify({
            'state': "success",
            'e_history': e_history,
            's_history': s_history,
            'g_history': g_history
        })
