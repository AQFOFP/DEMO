# coding=utf-8
import base64
from Crypto.Cipher import DES

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

if __name__ == '__main__':
    print(decode_base64('MfpnQcJusUUp/9X9h1fqUhHcPx5RHeZE+qUBwbMUDsMvwAwhjBz5ACAq4ujFFTpIunypK5OPfm8='))