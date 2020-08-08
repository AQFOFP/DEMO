import datetime
import os
import pickle
import shutil
import time

import redis
from openpyxl import Workbook




from mongoengine import *

# mongo的orm操作
def mongoorm():
    connect('mydb', host='localhost', port=27017)
    import datetime
    class Users(Document):
        name = StringField(required=True, max_length=200)
        age = IntField(required=True)
        type = IntField(required=True)
        hoppy = ListField(default=[])
        time_sp = IntField(default=0)

    user = Users(name = 'ddad', age = 18,type = 65, hoppy = ['eere', 'erw',], time_sp = 1577808001956).save()
    # user.name = 'l6'
    # user.age = 18
    # user.type = 666
    # user.hoppy = ['lanqi', 'youyong',]
    # user.time_sp = 1577808001956
    # user.save()


    # users = Users.objects(hoppy__in=['youyong', 'running', 'll'], time_sp__gte=1577808001956).all()  # 返回所有的文档对象列表
    #
    print(user.name, type(user))
    # print(len(users))
    #
    # for rn, alr in enumerate(users):
    #     # print(rn, type(rn))  # 0 <class 'int'>
    #     print(alr.hoppy, type(alr.hoppy))  # 0 <class 'int'>
    #     if 'youyong' in alr.hoppy:
    #         print('6666')
    #     print(alr, type(alr))  # Users object <class '__main__.mongoorm.<locals>.Users'>
    #
    # for u in users:
    #     print("id", u.id, "name:", u.name, ",age:", u.age, type(u.age))  # name: zhangsan ,age: 18

    # user = Users.objects(name='zhangsan').first()
    # print(user.id.generation_time.replace(tzinfo=None))
    # print(str(user.id))


if __name__ == '__main__':
    # savexl()
    # mongoorm()
    # dd = '2018-1-7'
    # doj = datetime.datetime.strptime(dd, '%Y-%m-%d')

    print(os.path.abspath(__file__))
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    n_path = os.path.join(BASE_DIR, 'thumb.png')

    print(n_path)
    # dd_str = '2020-07-31 23:59:59'
    # ww = time.strptime(dd_str, "%Y-%m-%d %X")
    # atime = (time.mktime(ww) + 5*60*60)*1000
    # print(int(atime))

    print(int(time.time()))

