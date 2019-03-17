# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/2 13:49
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Date,ForeignKey
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from enum import Enum


Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    age = Column(Integer)
    def __repr__(self):
        return "User(name='%s',age='%d')>" % (self.name,self.age)


engine = create_engine('mysql+pymysql://root:111111@120.25.160.52:3306/test',echo=True)
# engine = create_engine('mysql+pymysql://root:111111@120.25.160.52:3306/test',echo=False)
Base.metadata.create_all(engine)
# Session =sessionmaker(bind=engine)
# session = Session()
# 或者下面的session绑定方法
Session = sessionmaker()
session = Session(bind=engine)

# try:
#     lst = []
#     for i in range(10):
#         ed_user= User()
#         ed_user.name='ed1+{}'.format(i)
#         # session.add(ed_user)
#         lst.append(ed_user)
#
#     session.add_all(lst)
#     session.commit()
# except Exception as e:
#     print(e)
#     session.rollback()
# finally:
#     session.close()

# for instance in session.query(User):
#     print(instance)
    # print(instance.id,instance.name)



# for name,age in session.query(User.name,User.age).filter(User.age == 15):
#     print(name,age)

# querobj = session.query(User).filter(User.age == 15)
# for x in querobj:
#     print(x)
#
# for row in session.query(User).order_by(User.age):
#     print(row)

#update
# user = session.query(User).get(3)
# user.age = 55
# session.add(user)
# session.commit()

#delete
try:
    # user = session.query(User).get(2)
    # session.delete(user)
    # session.query(User).filter(User.age == 13).delete()
    session.query(User).filter(User.id > 3).delete()
    session.commit()
except Exception as e:
    print(e)
    session.rollback()
finally:
    session.close()



def show(emps):
    for x in emps:
        print(x)
        print('=' * 10)

# emps = session.query(User)
# # print(emps.count())
# print(emps.first())

'''
CREATE TABLE `employee` (
`emp_no`  int(11) NOT NULL ,
`birth_date`  date NOT NULL ,
`first_name`  varchar(14) NOT NULL ,
`last_name`  varchar(16) NOT NULL ,
`gender`  enum('M','F') NOT NULL ,
`hire_date`  date NOT NULL ,
PRIMARY KEY (`emp_no`)
)engine=InnoDB DEFAULT CHARSET=utf8mb4;
'''
# class MyEnum(Enum):
#     M = 'M'
#     F = 'F'
# class Employee(Base):
#     __tablename__='employee'
#     emp_no = Column(Integer,primary_key=True)
#     birth_date= Column(Date,nullable=False)
#     first_name=Column(String(14),nullable=False)
#     last_name=Column(String(17),nullable=False)
#     gender=Column(MyEnum,nullable=False)
#     hire_date=Column(Date,nullable=False)
#
#     def __repr__(self):
#         return "<{} emp_no:{} name:{} >".format(self.__class__.__name__,self.emp_no,"{}.{}").format(self.first_name,self.last_name)
#
#     __str__ = __repr__

# emps = session.query(Employee).filter(Employee.emp_no > 10015)
# show(emps)

from sqlalchemy import or_,not_,and_
from sqlalchemy import func

