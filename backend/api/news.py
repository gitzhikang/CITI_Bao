from flask import Flask, render_template, jsonify, request
from myDb import myDB

db = myDB()

def News():
  title = request.get_json()["title"]
  cursor = db.getConn().cursor()
  sql = "select * from esgnews where title = '" + title + "';"
  try:
    cursor.execute(sql)
    result = cursor.fetchone()
    db.getConn().close()
    return jsonify({
      'state': "success",
      'content' : result[4],
      'url' : result[3],
      'label' : result[1],
      'origin' : result[5],
      'data': result
    })

  except Exception as e:
    db.getConn().close()
    print(e.args)
    return jsonify({
      'state': "failed",
    })

