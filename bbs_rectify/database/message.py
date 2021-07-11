from flask import session
from sqlalchemy.sql.elements import False_
from database import User
from sqlalchemy import *
from .database_f import Base,db
from sqlalchemy.dialects.mysql import *

class Message(Base):
    message_id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.ForeignKey('user.user_id'),index = True)
    type = db.Column(db.String(50),nullable = False)
    head = db.Column(db.String(100),nullable = False) 
    content = db.Column(db.TEXT)
    read_count = db.Column(db.Integer,nullable = False,server_default = db.text("'0"))
    reply_count = db.Column(db.Integer, nullable=False, server_default=db.text("'0'"))
    update_time = db.Column(DateTime,server_default = text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    user = db.relationship('User')

    #筛选显示给用户看的留言，只有作者本人才可以看到存为草稿的留言
    @staticmethod
    def find_by_id(msg_id, self_id):
        res = db.session.query(Message, User.username, User.user_id).join(User, User.user_id == Message.user_id).filter(or_(Message.drafted == 0, User.user_id == self_id),Message.message_id == msg_id).all()
        return res

    #用用户ID检索留言
    @staticmethod
    def find_by_user(user_id):
        res = Message.query.filter_by(user_id=user_id).all()
        return res

    #用message_id查找留言
    @staticmethod
    def find_by_message_id(msg_id):
        res = Message.query.filter_by(message_id=msg_id).first()
        return res

    #插入一条新留言
    @staticmethod
    def insert_message(username, msg_type, head, content):
        res = User.query.filter_by(username = username).first()
        id = res.user_id
        msg = Message(user_id=id, type=msg_type, head=head,
                      content=content)
        db.session.add(msg)
        db.session.commit()
        return msg.message_id

    #增加阅读数量
    @staticmethod
    def increase_read_count(msg_id):
        """increase message's read count by 1"""
        msg = db.session.query(Message).filter_by(message_id=msg_id).first()
        if msg is None:
            return -1
        else:
            msg.read_count += 1
            db.session.commit()
            return msg.read_count
    
    #增加回复数量
    @staticmethod
    def increase_reply_count(msg_id):
        msg = db.session.query(Message).filter_by(message_id=msg_id).first()
        if msg is None:
            return -1
        else:
            msg.reply_count += 1
            db.session.commit()
            return msg.reply_count

    #查询固定类型的留言并显示指定条数
    @staticmethod
    def find_limit_of_type(msg_type):
        result = db.session.query(Message) \
            .join(User, User.user_id == Message.user_id) \
            .filter(Message.type == msg_type) \
            .order_by(Message.message_id.desc()).all()
        return result

    #计算固定类型留言的条数
    @staticmethod
    def count_msg_of_type(msg_type):
        """return number of messages of certain type"""
        result = Message.query \
            .filter(Message.type == msg_type) \
            .count()
        return result

    #通过user_id统计总留言数
    @staticmethod
    def count_msg(user_id):
       # user_id = int(user_id)
        return Message.query.filter_by(user_id=user_id).count()


    #模糊搜索
    @staticmethod
    def fuzzy_search(f_keyword):
        result = db.session.query(Message, User).join(User, User.user_id == Message.user_id).filter(or_(Message.head.like('%'+f_keyword+'%'), Message.content.like('%'+f_keyword+'%'))).all()
        return result