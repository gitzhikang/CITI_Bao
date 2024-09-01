#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, jsonify, request
from myDb import myDB
import uuid
import time

db = myDB()


def getEmails():
    cursor = db.getConn().cursor()
    user = request.get_json()["user"]
    sql = "select * from " + user + "_emailbox"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        unreaded = []
        readed = []
        starred = []
        trashed = []
        drafted = []
        sent = []
        for re in result:
            if re[5] == 0 and re[7] == 0 and re[8] == 0 and re[9] == 0:
                unreaded.append(re)
            if re[5] == 1 and re[6] == 0:
                readed.append(re)
            if re[5] == 1 and re[6] == 1:
                starred.append(re)
            if re[7] == 1:
                trashed.append(re)
            if re[8] == 1:
                drafted.append(re)
            if re[9] == 1:
                sent.append(re)
        db.getConn().close()
        return jsonify({
            'state': "success",
            'unreaded': unreaded,
            'readed': readed,
            'starred': starred,
            'trashed': trashed,
            'drafted': drafted,
            'sent': sent,
        })
    except Exception as e:
        db.getConn().close()
        return jsonify({
            'state': "failed",
        })


def throwEmails():
    cursor = db.getConn().cursor()
    emails = request.get_json()["emails"]
    for email in emails:
        try:
            sql = "update test_emailbox set readed=0, starred=0, discarded=1, drafted=0, sent=0 where emailid='" + \
                  email['index'] + "';"
            cursor.execute(sql)
            db.getConn().close()

        except Exception as e:
            db.getConn().close()
            return jsonify({
                'state': "failed",
            })
    return jsonify({
        'state': "success",
    })


def starEmail():
    cursor = db.getConn().cursor()
    email = request.get_json()["email"]
    sql_pre = "select * from test_emailbox where emailid='" + email['index'] + "';"
    try:
        cursor.execute(sql_pre)
        result = cursor.fetchone()
        if (result[6] == 1):
            sql = "update test_emailbox set readed=1, starred=0, discarded=0, drafted=0, sent=0 where emailid='" + \
                  email['index'] \
                  + "';"
            try:
                cursor.execute(sql)
                db.getConn().close()
                return jsonify({
                    'state': "success",
                    'op': 0
                })
            except Exception as e:
                print(e.args)
                db.getConn().close()
                return jsonify({
                    'state': "failed",
                })
        else:
            sql = "update test_emailbox set readed=1, starred=1, discarded=0, drafted=0, sent=0 where emailid='" + \
                  email['index'] \
                  + "';"
            try:
                cursor.execute(sql)
                db.getConn().close()
                return jsonify({
                    'state': "success",
                    'op': 1
                })
            except Exception as e:
                print(e.args)
                db.getConn().close()
                return jsonify({
                    'state': "failed",
                })
    except Exception as e:
        print(e.args)
        db.getConn().close()
        return jsonify({
            'state': "failed",
        })


def sendEmail():
    cursor = db.getConn().cursor()
    email = request.get_json()["email"]
    id = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'email_' + 'zx_' + str(time.time())))
    sql = "insert into test_emailbox values('" + id + "', '" + email['origin'] + "', '" + email['target'] + "', '"\
            + email['title'] + "', '" + email['content'] + "', 0, 0, 0, 0, 1, '" + time.ctime(time.time()) + "')"
    try:
        cursor.execute(sql)
        return jsonify({
            'state': "success",
        })
    except Exception as e:
        print(e.args)
        db.getConn().close()
        return jsonify({
            'state': "failed",
        })


def getEmail():
    cursor = db.getConn().cursor()
    index = request.get_json()["index"]
    sql = "select * from test_emailbox where emailid='" + index + "';"
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        return jsonify({
            'state': "success",
            "email": result
        })
    except Exception as e:
        print(e.args)
        db.getConn().close()
        return jsonify({
            'state': "failed",
        })


def addDraft():
    cursor = db.getConn().cursor()
    email = request.get_json()["email"]
    id = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'email_' + 'zx_' + str(time.time())))
    sql = "insert into test_emailbox values('" + id + "', '" + email['origin'] + "', '" + email['target'] + "', '" \
          + email['title'] + "', '" + email['content'] + "', 0, 0, 0, 1, 0, '" + time.ctime(time.time()) + "')"
    try:
        cursor.execute(sql)
        return jsonify({
            'state': "success",
        })
    except Exception as e:
        print(e.args)
        db.getConn().close()
        return jsonify({
            'state': "failed",
        })


def readAll():
    cursor = db.getConn().cursor()
    emails = request.get_json()["emails"]
    for email in emails:
        try:
            sql = "update test_emailbox set readed=1 where emailid='" + \
                  email['index'] + "';"
            cursor.execute(sql)
            db.getConn().close()

        except Exception as e:
            db.getConn().close()
            return jsonify({
                'state': "failed",
            })
    return jsonify({
        'state': "success",
    })



