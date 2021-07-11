from common.utility import decode_auth_token, identify, login_required
from controller.login_related import register
from database.message import Message
from flask import request, Blueprint
from flask_cors import *
from database import User, Message, Comment

personal = Blueprint('personal', __name__)

@personal.route('/personal', methods = ['POST'])
@login_required
def personal_profile():
    username = request.get_json().get('username')
    res = User.through_username(username)
    user_id = res[0].user_id
    register_time = res[0].create_time
    msg_count = len(Message.find_by_user(user_id))
    comment_count = Comment.count_self_comment(user_id)

    dic = {
        0: register_time,
        1: msg_count,
        2: comment_count
    }
    return dic

@personal.route('/changeAvatar',methods = ['POST'])
def changeAvatar():
    username = request.get_json().get('username')
    img = request.get_json().get('img')
    print(username)
    print(img)
    User.alt_avatar(username,img)
    return 'success'

@personal.route('/changePass',methods = ['POST'])
def changePass():
    username = request.get_json().get('username')
    new_pass = request.get_json().get('password')
    print(username)
    print(type(new_pass))
    User.alt_password(username,new_pass)
    return 'success'