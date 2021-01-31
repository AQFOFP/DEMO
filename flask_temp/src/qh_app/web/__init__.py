# coding=utf-8
from flask import Flask, request, make_response

app = Flask(__name__)


@app.before_request
def bef_req():
    if request.method == 'OPTIONS':
        # print(list(request.headers.keys()))
        #
        respon = make_response()
        respon.headers['Access-Control-Allow-Origin'] = '*'
        respon.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,PATCH,OPTIONS'
        # respon.headers['Access-Control-Allow-Headers'] = 'User-Agent,Origin,Referer,X-Requested-With, Content-Type, content-type,Accept, token, Authorization',
        respon.headers['Access-Control-Allow-Headers'] = '*'
        respon.status_code = 204
        return respon


@app.after_request
def f(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = '*'

    return resp
