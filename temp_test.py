# coding=utf-8
import base64
import datetime
import json
import os
import random
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


def gen_func():
    try:
        yield "http://projectsedu.com"
    except BaseException:
        pass
    yield 2
    yield 3
    return "bobby"


def init_prize_pool(atype, statictime):
    """
    # A  == > Family
    # B  == > Health
    # C  == > Love
    # D  == > Happiness
    # E  == > Peace
    :param atype: 1：免费抽  2：付费抽
    :return:
    """
    temp_str = ''

    # 指定默认数据
    if atype == 1:
        prize_key = 'celebrate_daily_key'
        prize_pool_dict = {
            'A': 50,
            'B': 30,
            'D': 10,
            'C': 9,
            'E': 1,
        }
    else:
        prize_key = 'celebrate_pay_key'
        prize_pool_dict = {
            'A': 50,
            'B': 30,
            'D': 10,
            'C': 9,
            'E': 1,
        }



    if atype == 1 and statictime >= 20210503 and statictime <= 20210505:
        prize_key = 'celebrate_daily_key'
        prize_pool_dict = {
            'A': 50,
            'B': 30,
            'D': 10,
            'C': 9,
            'E': 1,
        }

    elif atype == 1 and statictime >= 20210506 and statictime <= 20210509:
        prize_key = 'celebrate_daily_key'
        prize_pool_dict = {
            'A': 50,
            'B': 20,
            'D': 15,
            'C': 10,
            'E': 5,
        }

    elif atype == 1 and statictime > 20210509:
        prize_key = 'celebrate_daily_key'
        prize_pool_dict = {
            'A': 50,
            'B': 20,
            'D': 10,
            'C': 10,
            'E': 10,
        }

    # 付费
    elif atype == 2 and statictime >= 20210503 and statictime <= 20210505:
        prize_key = 'celebrate_pay_key'
        prize_pool_dict = {
            'A': 30,
            'B': 20,
            'D': 20,
            'C': 20,
            'E': 10,
        }

    elif atype == 2 and statictime >= 20210506:
        prize_key = 'celebrate_pay_key'
        prize_pool_dict = {
            'A': 20,
            'B': 20,
            'D': 20,
            'C': 20,
            'E': 20
        }

    print(prize_pool_dict)
    print(prize_key)



if __name__ == '__main__':
    # init_prize_pool(atype=1, statictime=20210509)
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
    for i in range(10):
        if i == 3:
            print(i)
        print(1)

