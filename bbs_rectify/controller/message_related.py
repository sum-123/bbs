from database.comment import Comment
from flask import request, Blueprint
from flask_cors import *
from sqlalchemy.sql.expression import null, update
from database import Message, User

message = Blueprint('message', __name__)

@message.route('/createMessage',methods = ["POST"])
def createMessage():
    head = request.get_json().get('headline')
    content = request.get_json().get('content')
    type = request.get_json().get('type')
    username = request.get_json().get('username')

    message_id = Message.insert_message(username, type, head, content)
    res = Message.find_by_message_id(message_id)
    dic = {
        0: 'success',
        1: res.create_time,
        2: res.read_count,
        3: res.reply_count
    }
    return dic

@message.route('/myMessage2',methods = ['POST'])
def myMessage2():
    username = request.get_json().get('username')
    res = User.through_username(username)
    ID = res[0].user_id
    mes = Message.find_by_user(ID)

    dic1 = {}
    temp = 0
    for item in mes:
        dic = {
            0: item.message_id,
            1: item.head,
            2: item.create_time,
            3: item.read_count,
            4: item.reply_count,
            5: item.content,
            6: item.type
        }
        a = {temp: dic}
        dic1.update(a)
        temp += 1
    return dic1

@message.route('/messageDetail', methods = ['POST'])
def messageDetail():
    msg_id = request.get_json().get('messageId')
    Message.increase_read_count(msg_id)
    comment = Comment.find_original_comment(msg_id)
    res = Message.find_by_message_id(msg_id)
    user = User.through_id(res.user_id)
    username = user[0].username
    dic1 = {}
    dic1[0] = res.head
    dic1[1] = res.content
    dic1[2] = res.create_time
    dic1[3] = username
    dic1[4] = res.read_count
    dic1[5] = res.reply_count
    dic1[6] = res.type
    temp = 7
    if comment is not null:
        for item in comment:
            userid = item.user_id
            user = User.through_id(userid)
            dic = {
                0: item.content,
                1: item.create_time,
                2: user[0].username,
                3: user[0].avatar
            }
            a = {temp: dic}
            dic1.update(a)
            temp += 1
    print(dic1)
    return dic1

@message.route('/myMessage1/1', methods = ['GET'])
def msg_study():
    res = Message.find_limit_of_type('学习交流')
    dic1 = {}
    temp = 0
    for item in res:
        user_id = item.user_id
        user = User.through_id(user_id)
        username = user[0].username
        avatar = user[0].avatar
        dic = {
            0: item.message_id,
            1: item.head,
            2: item.create_time,
            3: item.read_count,
            4: item.reply_count,
            5: item.content,
            6: username,
            7: avatar
        }
        a = {temp: dic}
        dic1.update(a)
        temp += 1
    return dic1

@message.route('/myMessage1/2', methods = ['GET'])
def msg_movie():
    res = Message.find_limit_of_type('影视文学')
    dic1 = {}
    temp = 0
    for item in res:
        user_id = item.user_id
        user = User.through_id(user_id)
        username = user[0].username
        avatar = user[0].avatar
        dic = {
            0: item.message_id,
            1: item.head,
            2: item.create_time,
            3: item.read_count,
            4: item.reply_count,
            5: item.content,
            6: username,
            7: avatar
        }
        a = {temp: dic}
        dic1.update(a)
        temp += 1
    return dic1

@message.route('/myMessage1/3', methods = ['GET'])
def msg_fun():
    res = Message.find_limit_of_type('吃喝玩乐')
    dic1 = {}
    temp = 0
    for item in res:
        user_id = item.user_id
        user = User.through_id(user_id)
        username = user[0].username
        avatar = user[0].avatar
        dic = {
            0: item.message_id,
            1: item.head,
            2: item.create_time,
            3: item.read_count,
            4: item.reply_count,
            5: item.content,
            6: username,
            7: avatar
        }
        a = {temp: dic}
        dic1.update(a)
        temp += 1
    return dic1

@message.route('/myMessage1/4', methods = ['GET'])
def msg_emotion():
    res = Message.find_limit_of_type('情感树洞')
    dic1 = {}
    temp = 0
    for item in res:
        user_id = item.user_id
        user = User.through_id(user_id)
        username = user[0].username
        avatar = user[0].avatar
        dic = {
            0: item.message_id,
            1: item.head,
            2: item.create_time,
            3: item.read_count,
            4: item.reply_count,
            5: item.content,
            6: username,
            7: avatar
        }
        a = {temp: dic}
        dic1.update(a)
        temp += 1
    return dic1