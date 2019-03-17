# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/2/28 22:04
import pymysql
conn = None
try:
    #建立连接，获取一个connections实例
    conn = pymysql.connect('120.25.160.52','root','111111','test')
    print(conn.ping(False))
    #获取一个cursor游标实例，用游标操作数据库
    cursor = conn.cursor()
    #操作数据库
    for i in range(10):
        sql = "insert into student(name,age) values('dean',30)"
        line = cursor.execute(sql)
        print(line)
    #关闭游标,或者在finally中进行关闭操作
    # cursor.close()
    #提交事务
    conn.commit()
except:
    conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()