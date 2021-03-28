# coding=utf-8
import base64
import datetime
import json
import os
import time
import uuid
from collections import OrderedDict

from Crypto.Cipher import DES
import requests
from bson import ObjectId

mdes = DES.new(b'*nd3()12', 1)


def decode_base64(text):
    if not text: return text
    data = text.encode("utf-8")
    ret = mdes.decrypt(base64.decodebytes(data))
    padding_len = ret[-1]
    dec_text = ret[:-padding_len].decode("utf-8")
    return dec_text


def encrypt_base64(text):
    pad_len = 8 - len(text) % 8
    padding = chr(pad_len) * pad_len
    text += padding

    data = text.encode("utf-8")
    data = base64.encodebytes(mdes.encrypt(data))
    return data.decode("utf-8").replace('\n', '')

def get_short_link_bitly(full_link):
    index=full_link.find('bitly')
    if full_link and index==-1:
        try:
            requer_url = "https://api-ssl.bitly.com/v4/shorten"
            data = dict(domain='bit.ly', long_url=full_link)
            data = json.dumps(data)
            access_token = '5fee85372bb926597aa1a354c6897f54e37b8909'

            headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(access_token)}
            respone = requests.post(requer_url, data, headers=headers)
            response_dict = respone.json()
            short_link = response_dict.get('link', '')
            print("full_link={}---->>>>short_link={}".format(full_link,short_link))
            return short_link
        except Exception as e:
            print("Exception----full_link={} e={}".format(full_link,e))
            return full_link
    else:
        return full_link


def get_register_str(actor_id):
    if actor_id:
        register_day = actor_id.generation_time.replace(tzinfo=None)
        print(time.mktime(register_day.timetuple()))
        # print(register_day)
    else:
        register_day_str = 0







if __name__ == '__main__':
    # print(decode_base64('MfpnQcJusUUp/9X9h1fqUhHcPx5RHeZE+qUBwbMUDsMvwAwhjBz5ACAq4ujFFTpIunypK5OPfm8='))
    # url = 'https://cdn3.qmovies.tv/youstar/quran_recitation__competition.png'
    # print(get_short_link_bitly(url))
    # res = requests.get(url='https://bit.ly/2CuODx8')
    # print(res.url)
    # uid = str(uuid.uuid1()).replace('-', '')
    # suid = ''.join(uid.split('-'))
    # print(type(uid))
    # print(suid)
    # get_register_str(ObjectId('600c39a532a61091e2d5fc07'))
    # print(30 * 12 * 60 * 60)
    from threading import Thread
    from threading import local
    import threading
    import time
    from threading import get_ident

    # 特殊的对象
    xianglong = local()


    def task(arg):
        # 对象.val = 1/2/3/4/5
        # print(threading.get_ident())
        ss = getattr(xianglong, 'value', None)
        if ss:
            ss.value = arg
            time.sleep(2)  # 亲亲翔龙
            print(99999)
            print(ss.value)
        else:
            xianglong.value = arg
            print(xianglong.__str__())
            time.sleep(2)  # 亲亲翔龙
            print(xianglong.value)


    for i in range(10):
        t = Thread(target=task, args=(i,))
        t.start()