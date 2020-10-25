import json
import time

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login(*args, **kwargs):
    """
    采用post请求， 账号和密码采用加密传输
    :return:  account, pwd, android_id
    """
    # params = handle_params(
    #     "account", "pwd", "android_id"
    # )

    # 获取POST方式传递过来的参数
    # print(type(request.stream.read().decode().strip()))
    # print(request.form)  # 获取表单格式数据
    print(json.loads(request.get_data()))   # 获取前端json格式数据
    # print(type(json.loads(request.get_data())))
    rank_list = json.loads(request.get_data()).get('rank')
    for item in rank_list:
        print(item, type(item))

    params = {
        "name": 'zhangsan',
        'age': 336
    }

    # 返回json
    return jsonify(params)

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('thumb')
        filename = "op_sys_{}_".format(int(time.time()))+secure_filename(f.filename)
        f.save(filename)
        test_file()
        return 'ok'


def test_file():
    print('666666')
    f = request.files.get('thumb')
    if f:
        filename = '666' + secure_filename(f.filename)
        f.save(filename)


if __name__ == '__main__':
    app.run(host="127.0.0.1", threaded=True, debug=True)
    # print(__name__)