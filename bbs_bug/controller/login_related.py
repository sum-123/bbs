from flask import request, Blueprint
from flask_cors import *
from database import User


identification = Blueprint('identification', __name__)

@identification.route('/register', methods = ["GET", "POST"])
def register():
    username = request.get_json().get('username')
    password = request.get_json().get('password')
    avatar = request.get_json().get('avatar')
    if len(User.through_username(username)) > 0:
        return 'repetition'
    User.register(username, password, avatar)
    return 'success'

@identification.route('/login', methods = ['GET', 'POST'])
def login():
    username = request.get_json().get('username')
    password = request.get_json().get('password')
    # res = User.through_username(username)
    res = User.authentication(username,password)
    print(password)
    # if len(res) != 1:
    #     return 'invalid'
    print(res)
    if res == 'success':
        return 'success'
    else:
        return 'fail'