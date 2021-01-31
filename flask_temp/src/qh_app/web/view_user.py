from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/home', methods=['GET', 'POST', 'OPTIONS'])
def home():
    return 'HOME'