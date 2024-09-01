from flask import Flask, render_template, jsonify, request
from api.enterpriseindex import EnterpriseIndex
from api.esgnews import ESGnews
from api.news import News
from api.setnewsviewed import NewsViewed
from api.getnewsviewed import GetNewsViewed
from api.getheatednews import GetHeatedNews
from api.getmainnews import GetMainNews
from api.follow import setFollow
from api.iffollowed import getFollow
from api.email import getEmails, starEmail, throwEmails, sendEmail, getEmail, addDraft, readAll

app = Flask(__name__)


@app.route("/")
def root():
    """
    主页
    :return: Index.html
    """
    return render_template('Index.html')


@app.route("/api/esgquery", methods=['POST'])
def getESG():
    return EnterpriseIndex()


@app.route("/api/newsquery", methods=['GET'])
def getNews():
    return ESGnews()


@app.route("/api/newsdetailquery", methods=['POST'])
def getNewsDetail():
    return News()


@app.route("/api/newsviewed", methods=['POST'])
def setNewsViewed():
    return NewsViewed()


@app.route("/api/getnewsviewed", methods=['GET'])
def getNewsViewed():
    return GetNewsViewed()


@app.route("/api/getheatednews", methods=['GET'])
def getHeatedNews():
    return GetHeatedNews()


@app.route("/api/getmainnews", methods=['GET'])
def getMainNews():
    return GetMainNews()


@app.route("/api/follow", methods=['POST'])
def Follow():
    return setFollow()


@app.route("/api/getfollow", methods=['POST'])
def getMyFollow():
    return getFollow()


@app.route("/api/getemails", methods=['POST'])
def getEmails_():
    return getEmails()


@app.route("/api/staremail", methods=['POST'])
def starEmail_():
    return starEmail()


@app.route("/api/throwemail", methods=['POST'])
def throwEmail_():
    return throwEmails()


@app.route("/api/sendemail", methods=['POST'])
def sendEmail_():
    return sendEmail()


@app.route("/api/getemail", methods=['POST'])
def getEmail_():
    return getEmail()


@app.route("/api/adddraft", methods=['POST'])
def addDraft_():
    return addDraft()


@app.route("/api/readall", methods=['POST'])
def readAll_():
    return readAll()


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
