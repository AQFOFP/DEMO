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

    class LuckyJulyDevote(Document):
        ruid = StringField(default='')
        point = IntField(default=0)
        giftcount = IntField(default=0)
        round_number = IntField(default=0)
        type = IntField(default=0)  # 0:代表sender 1:代表revicer 2:代表room

    per_list = ['sen_data', 'rece_data', 'room_data']
    data = {}
    data_list = []
    for rs in range(1, 5):
        for no, item in enumerate(per_list):
            tempdict = {}
            uid = 'r:'+'11111' if no == 2 else '11111'

            lkobj = LuckyJulyDevote.objects(ruid=uid, round_number=rs, type=no).first()
            if no == 2:
                print(lkobj)
            tempdict['count'] = lkobj.giftcount if lkobj else 0
            tempdict['point'] = lkobj.point if lkobj else 0
            data[item] = tempdict
        data['rounds'] = rs
        data_list.append(data.copy())

    print(data_list)



    # user = Users()
    # user.name = 'zhangsan'
    # user.age = 18
    # #
    # user.save()
    # users = Users.objects(name='zhangsan').all()  # 返回所有的文档对象列表
    #
    # print(users, type(users))
    # print(len(users))
    #
    # for rn, alr in enumerate(users):
    #     print(rn, type(rn))  # 0 <class 'int'>
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