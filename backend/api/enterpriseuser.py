#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, jsonify, request
from myDb import myDB
import uuid

db = myDB()


def createUser():
    cursor = db.getConn().cursor()
    userid = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'enterprise_user'))
    username = request.get_json()["user"]
    email = request.get_json()["email"]
    phone = request.get_json()["phone"]
    sql = "insert into enterprise_user values('" + userid + "', '" \
          + username + "', '" + email + "', '" + phone + "');"
    sql_email_box = '''
        CREATE TABLE {}(
            emailid char(255) NOT NULL,
            origin char(255) NOT NULL,
            title char(255) NOT NULL,
            content char(255) DEFAULT NULL,
            readed int(1) DEFAULT NULL,
            starred int(1) DEFAULT NULL,
            discarded int(1) DEFAULT NULL,
            drafted int(1) DEFAULT NULL,
            sent int(1) DEFAULT NULL,
            time char(255) DEFAULT NULL,
            PRIMARY KEY (`emailid`)
	    );
    '''.format(userid + "_emailbox")
    while True:
        try:
            cursor.execute(sql)
            try:
                cursor.execute(sql_email_box)
                db.getConn().close()
                return jsonify({
                    'state': "success",
                })
            except Exception as e:
                db.getConn().close()
                print(e.args[0])
                return jsonify({
                    'state': "failed",
                })
        except Exception as e:
            if e.args[0] == 1062:
                continue
            else:
                return jsonify({
                    'state': "failed",
                })

