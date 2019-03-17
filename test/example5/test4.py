# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/2/28 23:42
#数据库连接池实现
import pymysql
from queue import Queue
import threading
class ConnPool:
    def __init__(self,size,*args,**kwargs):
        self._size = size
        self._pool = Queue(size) #用队列的方式实现一个连接池
        self.local = threading.local()
        for i in range(size):
            # conn = pymysql.connect('120.25.160.52','root','111111','test')
            conn = pymysql.connect(*args,**kwargs)
            self._pool.put(conn)
    def get_conn(self):
        return self._pool.get() #从池中获取一个连接，池中连接全部被取走后就会blocking
    def return_conn(self,conn:pymysql.connections.Connection): #用完连接后将连接重新放回到池中
        if isinstance(conn,pymysql.connections.Connection):
            self._pool.put(conn)
    @property
    def size(self):
        return self._pool.qsize()

    def __enter__(self):
        return self.get_conn()
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

pool = ConnPool(5,'120.25.160.52','root','111111','test')

conn = pool.get_conn()
print(type(conn))
with conn as cursor:
    with cursor:
        cursor.execute('select * from user;')

pool.return_conn(conn)
