import datetime
import pickle
import time

import redis
from openpyxl import Workbook

sub_rds = redis.StrictRedis(db=0)



# # redis的发布订阅模式
def run():
    ps = sub_rds.pubsub()  # redis的发布订阅模式
    ps.subscribe("message:send_gift")

    # sync_gift_devote_to_redis()
    # sync_month_gift_devote_to_redis()

    while True:
        try:
            ps_message = ps.get_message(ignore_subscribe_messages=True)
            time.sleep(1)
            print(ps_message, type(
                ps_message))  # {'type': 'message', 'pattern': None, 'channel': b'message:send_gift', 'data': b'zhangsan'} <class 'dict'>
            if not ps_message:
                time.sleep(0.04)
                continue

            _message_data = ps_message.get('data', b'') or b''
            if not _message_data:
                continue
            # _message = pickle.loads(_message_data)
            # do_task(_message)
            print(_message_data, type(_message_data))

        except Exception as e:
            # log.exception(e)
            print(e)
            time.sleep(1)


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




# openpyxl操作
def savexl():
    connect('mydb', host='localhost', port=27017)

    class Users(Document):
        name = StringField(required=True, max_length=200)
        age = IntField(required=True)

    users = Users.objects.all()  # 返回所有的文档对象列表



    wb = Workbook()
    _save_sheet = wb.active

    rowNum = 1
    _save_sheet.cell(row=rowNum, column=1).value = 'name'
    _save_sheet.cell(row=rowNum, column=2).value = 'age'

    for index, item in enumerate(users):
        e_pos = index + 1
        _save_sheet.cell(row=rowNum + e_pos, column=1).value = item.name
        _save_sheet.cell(row=rowNum + e_pos, column=2).value = item.age

    path = 'list_credit_charge_bill.xlsx'
    # 把文件保存到linux本地，
    wb.save(path)



if __name__ == '__main__':
    # savexl()
    mongoorm()
    # dd = '2018-1-7'
    # doj = datetime.datetime.strptime(dd, '%Y-%m-%d')
    #
    # n = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
    # d = ((1, 21), (2, 19), (3, 20), (4, 20), (5, 20), (6, 20), (7, 22), (8, 22), (9, 22), (10, 22), (11, 22), (12, 22))
    # print(n[len(list(filter(lambda y: y <= (doj.month, doj.day), d))) % 12])



    # dd_str = '2020-07-31 23:59:59'
    # ww = time.strptime(dd_str, "%Y-%m-%d %X")
    # atime = (time.mktime(ww) + 5*60*60)*1000
    # print(int(atime))

    print(int(time.time()))

