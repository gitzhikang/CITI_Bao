from flask import Flask, render_template, jsonify, request
from myDb import myDB

db = myDB()

def EnterpriseIndex():
  enter_name = request.get_json()["name"]
  print(enter_name)
  cursor = db.getConn().cursor()
  sql = "select * from enterprises where corpname='" + enter_name + "';"
  sql2 = "select * from dataset_e where id='芒果超媒';"
  sql3 = "select * from dataset_s where id='芒果超媒';"
  sql4 = "select * from dataset_g where id='芒果超媒';"
  try:
    # 执行SQL语句
    try:
      cursor.execute(sql)
      result = cursor.fetchone()

    except Exception as e:
      print("fetch meg error" + e.args)
      db.getConn().close()
      return jsonify({
        'state': "failed",
      })
    try:

      cursor.execute(sql2)
      des = cursor.description
      result_e = cursor.fetchone()

      header_e = [item[0] for item in des]
      cursor.execute(sql3)
      des = cursor.description
      result_s = cursor.fetchone()
      header_s = [item[0] for item in des]
      cursor.execute(sql4)
      result_g = cursor.fetchone()
      des = cursor.description
      header_g = [item[0] for item in des]

      e = []
      s = []
      g = []

      for i in range(1, len(header_e) - 1):
        e.append({
          "pro": header_e[i],
          "value": result_e[i],
          "tag": "E"
        })

      for i in range(1, len(header_s) - 1):
        s.append({
          "pro": header_s[i],
          "value": result_s[i],
          "tag": "S"
        })
      for i in range(1, len(header_g) - 1):
        g.append({
          "pro": header_g[i],
          "value": result_g[i],
          "tag": "G"
        })

    except Exception as e:
      db.getConn().close()
      print("fetch esg error" + e.args)
      return jsonify({
        'state': "failed",
      })
    E_point = 0
    S_point = 0
    G_point = 0
    for i in range(len(result[8])):
      if result[8][i] == "C":
        E_point = E_point + 1
      elif result[8][i] == "B":
        E_point = E_point + 2
      elif result[8][i] == "A":
        E_point = E_point + 3
    for i in range(len(result[9])):
      if result[9][i] == "C":
        S_point = S_point + 1
      elif result[9][i] == "B":
        S_point = S_point + 2
      elif result[9][i] == "A":
        S_point = S_point + 3
    for i in range(len(result[10])):
      if result[10][i] == "C":
        G_point = G_point + 1
      elif result[10][i] == "B":
        G_point = G_point + 2
      elif result[10][i] == "A":
        G_point = G_point + 3
    try:
      sql_news = "select * from "
    except Exception as e:
      db.getConn().close()
      print(e.args)
    db.getConn().close()
    return jsonify({
      'state': "success",
      'name': result[0],
      'legalreprentative': result[1],
      'cc': result[2],
      'tel': result[3],
      'net': result[4],
      'email': result[5],
      'addr': result[6],
      'brief': result[7],
      'E': E_point,
      'S': S_point,
      'G': G_point,
      'msg1': result[11],
      'msg1href': result[12],
      'msg2': result[13],
      'msg2href': result[14],
      'msg3': result[15],
      'msg3href': result[16],
      'msg4': result[17],
      'msg4href': result[18],
      'msg5': result[19],
      'msg5href': result[20],
      "table_e": e,
      "table_s": s,
      "table_g": g,
    })
  except Exception as e:
    db.getConn().close()
    print(e.args)
    return jsonify({
      'state': "failed",
    })
