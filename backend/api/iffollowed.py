#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, jsonify, request
from myDb import myDB

db = myDB()

def getFollow():
  cursor = db.getConn().cursor()
  follower = request.get_json()["follower"]
  followed = request.get_json()["followed"]
  sql = "select * from follow where follower = '" + follower + "' and followed = '" + followed + "'"

  try:
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    db.getConn().close()
    return jsonify({
      'state': "success",
        'len': len(result)
    })
  except Exception as e:
    db.getConn().close()
    print(e.args[0])
    return jsonify({
        'state': "failed",
    })

