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
        book_banner = ListField(default=[])

    link_list = [{
        'origin': 'http://www.baidu.com',
        'thumbnail': 'http://www.qq.com',
        }
    ]
    Book(head='http://www.baidu.com', book_banner=link_list).save()
    # reg = {'book_banner': {'$regex': '^(http://www.qq.com)'}}
    # books = Book.objects(__raw__=reg).all()
    # # print(books)
    # for b in books:
    #     print(isinstance(b['book_banner'], list))
    #     b['book_banner'] = eval(str(b['book_banner']).replace('http://www.qq.com', 'http://www.888.com', ))
    #     b.save()


if __name__ == '__main__':
    # savexl()
    # mongoorm()
    link_list = [{
        'origin': 'http://www.baidu.com',
        'thumbnail': 'http://www.qq.com',
        }
    ]
    print(eval(str(link_list).replace('http://www.qq.com', 'http://www.888.com')))






    # dd = '2018-1-7'
    # doj = datetime.datetime.strptime(dd, '%Y-%m-%d')





