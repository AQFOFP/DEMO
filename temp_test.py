# coding=utf-8
import base64
import json
import time
import uuid

from Crypto.Cipher import DES
import requests

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
    ff = '11'
    print(ff.isdigit())


# 0e705186-2820-11eb-b5d8-28e34735abda
# 0e705186282011ebb5d828e34735abda