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
    conn = pymysql.connect('120.25.160.52','root','111111','test')
    with conn as cursor:  #with conn 返回一个connections对象，这个对象的__enter__方法返回一个cursor，__exit__方法在退出时会自动回滚或者提交，但是不会关闭cursor，也不会关闭连接，因此需要自己控制关闭cursor和连接
        with cursor: # 或者写成with cursor as cursor
            #使用with cursor时，由cursor类的__enter__方法可知道返回的是一个cursor自己，__exit__函数可知道退出时会自动关闭cursor
            #操作数据库
            sql = "select * from student where id = %s"
            id = 5
            line = cursor.execute(sql,(id,))
            print(line)
            print(cursor.fetchall())
finally:
    if conn:
        conn.close()