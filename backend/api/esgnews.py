from flask import Flask, render_template, jsonify, request
from myDb import myDB

db = myDB()

def ESGnews():
  cursor = db.getConn().cursor()
  sql = "select * from esgnews"
  try:
    cursor.execute(sql)
    result = cursor.fetchall()
    e_news = []
    s_news = []
    g_news = []
    for re in result:
      if re[1] == "E":
        e_news.append(re)
      elif re[1] == "S":
        s_news.append(re)
      elif re[1] == "G":
        g_news.append(re)
    print(len(e_news))
    db.getConn().close()
    return jsonify({
      'state': "success",
      "e_news" : e_news,
      "s_news" : s_news,
      "g_news" : g_news,
    })
  except Exception as e:
    db.getConn().close()
    print(e.args)
    return jsonify({
      'state': "failed",
    })

