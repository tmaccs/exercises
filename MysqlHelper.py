from pymysql import *

class MysqlHelper:
    def __init__(self,host,port,user,passwd,database,charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
    def open(self):
        self.conn = connect(host=self.host,port=self.port,user = self.user,passwd = self.passwd,database = self.database,charset = self.charset)
        self.cursors1 = self.conn.cursor()

    def close(self):
        self.cursors1.close()
        self.conn.close()

    def cud(self,sql,params):
        try:
            self.open()
            self.cursors1.execute(sql, params)
            self.conn.commit()
            self.close()
            print('Ok')
        except Exception as e:
            print(e.message)
# params=()给参数设置默认值
    def read(self,sql,params=()):
        try:
            self.open()
            self.cursors1.execute(sql, params)
            result = self.cursors1.fetchall()

            self.close()
            return result
            # print('查询完毕')

        except Exception as e:
            print(e.message)
