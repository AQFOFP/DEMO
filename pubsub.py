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

    class Book(Document):
        head = StringField(default='')
        title = StringField(default='')
        icon = ListField(default=[])
        book_banner = ListField(default=[])

    # link_list = [{
    #     'origin': 'http://www.baidu.com',
    #     'thumbnail': 'http://www.qq.com',
    #     }
    # ]
    # Book(head='3333', title='rrteee', icon=['678', '5644', '5w54242'],  book_banner=[]).save()
    # reg = {'book_banner': {'$regex': '^(http://www.qq.com)'}}
    # books = Book.objects().all()
    # dd = set()
    # dd.update(books)
    pipeline = [
        # {'$match': {'_id': {'$in': login_list}, 'fb_gender': 2}},
        {'$group': {'_id': '$head', "ip_user_list": {"$push": {'$toString': '$_id'}}}},
    ]
    zone_act_list = Book._get_collection().aggregate(pipeline)

    for b in zone_act_list:
        print(b['_id'])
        print(b['ip_user_list'])
    #     print(b.book_banner)
    #     print(isinstance(b['book_banner'], list))
    #     b['book_banner'] = eval(str(b['book_banner']).replace('http://www.qq.com', 'http://www.888.com', ))
    #     b.save()


if __name__ == '__main__':
    # savexl()
    mongoorm()
    # dd = '2018-1-7'
    # doj = datetime.datetime.strptime(dd, '%Y-%m-%d')




