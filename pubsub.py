import datetime
import os
import pickle
import shutil
import time

import redis
from openpyxl import Workbook




from mongoengine import *
from mongoengine import FileField


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
    flag = 1
    filter_m = dict()
    # print(filter_m)
    # if flag == 1:
    #     filter_m.update({'head': {'$in': ['http://www.baidu.com']}})
    # elif flag == 2:
    #     filter_m.update({'head': 'http://www.baidu.com'})
    # else:
    #     pass

    books = Book.objects().first()
    filter_m = books.to_mongo()
    filter_m['head'] = 111
    print(filter_m['head'])
    # for item in books:
    #     print(item.head)
    # dd = set()
    # dd.update(books)
    # pipeline = [
    #     # {'$match': {'_id': {'$in': login_list}, 'fb_gender': 2}},
    #     {'$group': {'_id': '$head', "ip_user_list": {"$push": {'$toString': '$_id'}}}},
    # ]
    # zone_act_list = Book._get_collection().aggregate(pipeline)

    # for b in zone_act_list:
    #     print(b['_id'], b['ip_user_list'])
    #     print(b.book_banner)
    #     print(isinstance(b['book_banner'], list))
    #     b['book_banner'] = eval(str(b['book_banner']).replace('http://www.qq.com', 'http://www.888.com', ))
    #     b.save()


def get_current_day_begin_timestamp():
    time_string = datetime.datetime.fromtimestamp(
        time.time()).strftime('%Y-%m-%d 00:00')
    timestamp = time.mktime(datetime.datetime.strptime(
        time_string, "%Y-%m-%d 00:00").timetuple())
    return float(timestamp) - 8 * 60 * 60


if __name__ == '__main__':
    # savexl()
    # mongoorm()


    # ddd =
    # print(ddd.timestamp())

    # today = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
    # time_string = today.strftime('%Y-%m-%d 00:00')
    # print(today.timetuple())
    # print(time.mktime(datetime.datetime.strptime(time_string, "%Y-%m-%d 00:00").timetuple()) + 5*60*60)


    now_stamp = int(time.time())
    now = now_stamp - 9000  # 印度时间转换为沙特时间统计  gmt +5.5 --> gmt +3
    timeArray = time.localtime(now)

    static_time = time.strftime('%Y-%m-%d', timeArray)
    s_stamp = int(datetime.datetime.strptime(static_time, '%Y-%m-%d').timestamp()) + 9000
    e_stamp = s_stamp + 24*60*60
    print(static_time)
    print(s_stamp, e_stamp)
