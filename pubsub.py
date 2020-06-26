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

    # user = Users()
    # user.name = 'zhangsan'
    # user.age = 18
    #
    # user.save()
    users = Users.objects(name='zhangsan').all()  # 返回所有的文档对象列表

    print(users, type(users))
    print(len(users))

    for rn, alr in enumerate(users):
        print(rn, type(rn))  # 0 <class 'int'>
        print(alr, type(alr))  # Users object <class '__main__.mongoorm.<locals>.Users'>

    for u in users:
        print("id", u.id, "name:", u.name, ",age:", u.age, type(u.age))  # name: zhangsan ,age: 18

    data = dict()
    creditcount = dict()
    creditdiamond = dict()
    data_list = []
    Total = Paid1 = Paid2 = Unpaid1 = Unpaid2 = 0
    for credit in users:
        temp = dict()
        temp['id'] = str(credit.id)
        temp['name'] = credit.name
        temp['age'] = credit.age
        data_list.append(temp.copy())

        if credit.age == 18:
            Paid1 += 1
            Paid2 += credit.age

        if credit.age == 1 or credit.age == 0:
            Unpaid1 += 1
            Unpaid2 += credit.age

        Total += credit.age

    data["data_list"] = data_list

    creditcount['Times'] = len(users)
    creditcount['Paid'] = Paid1
    creditcount['Unpaid'] = Unpaid1
    creditcount['Credibility1'] = str(round(Paid1 / len(users) * 100, 2)) + '%' if len(users) else '0%'
    data["creditcount"] = creditcount

    creditdiamond['Total'] = Total
    creditdiamond['Unpaid'] = Unpaid2
    creditdiamond['Credibility2'] = str(round(Paid2 / Total * 100, 2)) + '%' if Total else '0%'
    data["creditdiamond"] = creditdiamond

    print(data)




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
    # mongoorm()
    print(all([1, 1, ""]))