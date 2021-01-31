from flask import Flask

from qh_app.web import app
from qh_app.web.view_user import user
app.register_blueprint(blueprint=user)  # 注册蓝图

if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True, debug=True)
