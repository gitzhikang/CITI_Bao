#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, jsonify, request
from myDb import myDB

db = myDB()

def setFollow():
  cursor = db.getConn().cursor()
  label = request.get_json()["label"]
  e = '0'
  s = '0'
  g = '0'
  e_op = '0'
  s_op = '0'
  g_op = '0'
  total = '0'
  total_op = '0'
  for l in label:
      if (l == 'E数据满意'):
          e = '1'
      elif (l == 'S数据满意'):
          s = '1'
      elif (l == 'G数据满意'):
          g = '1'
      elif (l == 'E潜力数据满意'):
          e_op = '1'
      elif (l == 'S潜力数据满意'):
          s_op = '1'
      elif (l == 'G潜力数据满意'):
          g_op = '1'
      elif (l == 'ESG整体数据满意'):
          total = '1'
      elif (l == 'ESG整体潜力数据满意'):
          total_op = '1'
  sql = "insert into follow values('zx', '万达电影', " + e + ", " + s + ", " + g + ", " + total + ", " + e_op + ", "\
            + s_op + ", " + g_op + ", " + total_op + ");"
  print(sql)
  try:
    cursor.execute(sql)
    db.getConn().close()
    return jsonify({
      'state': "success",
    })
  except Exception as e:
    db.getConn().close()
    print(e.args[0])
    return jsonify({
        'state': "failed",
        'errorcode': e.args[0]
    })

