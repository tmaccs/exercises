# coding=utf-8
from pymysql import *
try:
    name = input("请输入家用电器名：")
    conn = connect(host='localhost',port=3306,user='root',passwd='root',database='classify',charset='utf8')
    curor1 = conn.cursor()

    # 字符串必须用"",''不行
    # sql = 'insert into classify values(13,"手机",2)'
    sql = 'insert into classify values(15,%s,2)'
    curor1.execute(sql,[name])
    conn.commit()

    curor1.close()
    conn.close()

except Exception as e:
    print(e.message)
