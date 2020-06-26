
from flask import Flask, request, jsonify

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
    print(request.stream.read().decode().strip())
    print(request.stream.read().decode().strip())

    params = {
        "name": 'zhangsan',
        'age': 33
    }

    # 返回json
    return jsonify(params)


if __name__ == '__main__':
    app.run(host="127.0.0.1", threaded=True)