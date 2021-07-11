from sqlalchemy.sql.functions import user
from database.comment import Comment
from flask import request, Blueprint
from flask_cors import *
from sqlalchemy.sql.expression import update
from database import Message, User

index = Blueprint('index', __name__)

@index.route('/index', methods = ['GET'])
def myIndex():
    res1 = Message.find_limit_of_type('学习交流')[:3]
    res2 = Message.find_limit_of_type('影视文学')[:3]
    res3 = Message.find_limit_of_type('吃喝玩乐')[:3]
    res4 = Message.find_limit_of_type('情感树洞')[:3]
    count_res1 = Message.count_msg_of_type('学习交流')
    count_res2 = Message.count_msg_of_type('影视文学')
    count_res3 = Message.count_msg_of_type('吃喝玩乐')
    count_res4 = Message.count_msg_of_type('情感树洞')
    res_user = User.find_limit_of_user()[:4]
    res = res1 + res2 + res3 + res4
    temp = 0
    dic1 = {}
    dic1.update({temp: count_res1})
    dic1.update({temp + 1: count_res2})
    dic1.update({temp + 2: count_res3})
    dic1.update({temp + 3: count_res4})
    temp = temp + 4
    for i in res_user:
        b = {temp: i.username}
        dic1.update(b)
        temp += 1
    for item in res:
        username = User.through_id(item.user_id)[0].username
        avatar = User.through_id(item.user_id)[0].avatar
        dic = {
            0: item.head,
            1: item.content,
            2: item.read_count,
            3: item.reply_count,
            4: item.create_time,
            5: item.type,
            6: username,
            7: item.message_id,
            8: avatar
        }
        a = {temp: dic}
        dic1.update(a)
        temp += 1
    return dic1