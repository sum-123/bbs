from pymysql.cursors import Cursor
from common.utility import *
from flask import request, Blueprint
from flask_cors import *
from database import User
import pymysql

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
    flag = request.headers.get('flag')
    flag1 = request.headers.get('flag1')
    print(flag)
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Zjm123..',
        database='our_bbs',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # sql = """INSERT INTO our_bbs.header(flag) VALUES ('{}');""".format(flag)
    # sql = "select updatexml(1,concat(0x7e,(SELECT password from user where username='fzs'),0x7e),1);"
    # flag = updatexml(1,concat(0x7e,(SELECT password
    # flag1 = fzs'),0x7e),1);#
    sql = "select {} from user where username='{}'".format(flag,flag1)
    # INSERT INTO `user` VALUES (320, 'fzs', '123', 'monster.jpg', '2021-07-07 09:59:01');
    res = cursor.execute(sql)
    # conn.commit()
    print(res)
    username = request.get_json().get('username')
    password = request.get_json().get('password')
    res = User.through_username(username)
    if len(res) != 1:
        return 'invalid'
    if password == res[0].password:
        token = generate_access_token(username)
        dic = {
            '0':'success',
            '1': res[0].avatar,
            '2': token
        }
        return dic
    else:
        return 'fail'