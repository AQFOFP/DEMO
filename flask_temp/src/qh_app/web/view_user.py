from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')
# url_prefix url前缀:http://127.0.0.1:5000/user/home
# 蓝图的作用：
# 1:路由分发（目录结构划分）
# 2：为某一类路由添加前缀
# 3：为某一类路由添加中间件


@user.before_request
def bf():
    print('before_request')


@user.route('/home', methods=['GET', 'POST', 'OPTIONS'])
def home():
    return 'HOME'