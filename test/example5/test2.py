# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/2/28 22:31
# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/2/28 22:04
import pymysql
from pymysql.cursors import DictCursor
conn = None
try:
    #建立连接，获取一个connections实例
    conn = pymysql.connect('120.25.160.52','root','111111','test')
    # print(conn.ping(False))
    #获取一个cursor游标实例，用游标操作数据库
    cursor = conn.cursor(cursor=DictCursor)
    #操作数据库
    sql = "select * from student where id = %s"
    id = '5 or 1 =1'
    line = cursor.execute(sql,(id,))
    print(line)
    # print(cursor.fetchone())
    # print(cursor.fetchone())
    # print(cursor.fetchmany(5))
    # print(cursor.fetchmany(5))
    # cursor.rownumber=0
    print(cursor.fetchall())
    print(cursor.rowcount)
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