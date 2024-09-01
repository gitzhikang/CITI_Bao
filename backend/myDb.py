import pymysql


class myDB(object):

    def __init__(self):
        self.host = 'rm-bp1sb38sv3ud760177o.mysql.rds.aliyuncs.com'
        self.user = 'share'
        self.password = 'Share12345'
        self.db = 'esg-web'
        self.port = 3306
        self.charset = 'utf8'
        self.conn = None

    def getConn(self):
        self.conn = pymysql.connect(host='rm-bp1sb38sv3ud760177o.mysql.rds.aliyuncs.com', user='share',
                               password='Share12345',
                               db='esg', port=3306, charset='utf8', autocommit=True)
        print('连接数据库成功！')
        cursor = self.conn.cursor()
        return self.conn

    def closeDB(self):
        if (self.conn != None):
            self.conn.close()


