from database.comment import Comment
from flask import request, Blueprint
from flask_cors import *
from database import Comment, Message, User

comment = Blueprint('comment', __name__)

@comment.route('/createComment',methods = ["POST"])
def createComment():
    msg_id = request.get_json().get('messageId')
    username = request.get_json().get('username')
    comment = request.get_json().get('comment')

    res = User.through_username(username)
    user_id = res[0].user_id

    Comment.insert_comment(user_id,msg_id,comment)
    Message.increase_reply_count(msg_id)
    return 'success'