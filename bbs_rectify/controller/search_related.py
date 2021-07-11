from flask import request, Blueprint
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.type_api import NULLTYPE
from database import Message, User
from flask_cors import *

search = Blueprint('search', __name__)

@search.route('/search', methods = ['POST'])
def search_fuzzy():
    flag = request.get_json().get('select')
    target = request.get_json().get('input')

    if target == "":
        return 'invalid'

    if flag == '1':
        dic1 = {}
        temp = 0
        res = Message.fuzzy_search(target)
        for item in res:
            dic = {
                0: item[0].message_id,
                1: item[0].head,
                2: item[0].create_time,
                3: item[0].read_count,
                4: item[0].reply_count,
                5: item[0].content,
                6: item[1].avatar,
                7: item[1].username
            }
            a = {temp: dic}
            dic1.update(a)
            temp += 1
        return dic1

    if flag == '2':
        dic1 = {}
        temp = 0
        res = User.through_username(target)
        print(res)
        msg = Message.find_by_user(res[0].user_id)
        print(msg)
        for item in msg:
            dic = {
                0: item.message_id,
                1: item.head,
                2: item.create_time,
                3: item.read_count,
                4: item.reply_count,
                5: item.content,
                6: res[0].avatar,
                7: res[0].username
            }
            a = {temp: dic}
            dic1.update(a)
            temp += 1
        return dic1
    return null