import time

import pymysql

if __name__ == '__main__':
    try:
        # 连接数据库
        conn = pymysql.connect(host='rm-bp1sb38sv3ud760177o.mysql.rds.aliyuncs.com', user='share',
                               password='Share12345',
                               db='esg', port=3306, charset='utf8')
        print('连接数据库成功！')
        cursor = conn.cursor()
        cursor.execute("insert into news_viewed(viewtime, e, s, g) values('1644582500.8819463', '0', '1', '0')")
        conn.commit()
        conn.close()
        print(time.ctime(time.time()))
    except Exception as e:
        print(e)

