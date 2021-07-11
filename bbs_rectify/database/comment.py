from database import User
from sqlalchemy.dialects.mysql import *
from .database_f import Base,db

class Comment(Base):
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.user_id'), index=True)
    message_id = db.Column(db.ForeignKey('message.message_id'), index=True)
    content = db.Column(db.Text)
    

    message = db.relationship('Message')
    foreigh_u = db.relationship('User', foreign_keys=[user_id])



    #插入一条新评论
    @staticmethod
    def insert_comment(user_id, msg_id, content):
        com = Comment(user_id = user_id, message_id = msg_id, content = content)
        db.session.add(com)
        db.session.commit()
        return com.comment_id

    #通过评论ID查找评论
    @staticmethod
    def find_by_id(comment_id):
        result = Comment.query.filter_by(comment_id = comment_id).all()
        return result


    #查找针对选定留言的所有评论
    @staticmethod
    def find_original_comment(msg_id):
        result = db.session.query(Comment).join(User, User.user_id == Comment.user_id).filter(Comment.message_id == msg_id).order_by(Comment.comment_id.desc()).all()
        return result


    #计算针对选定留言的评论总数
    @staticmethod
    def count_comment(msg_id):
        return Comment.query.filter(Comment.message_id == msg_id, Comment.reply_to == 0).count()



    @staticmethod
    def find_reply_by_comment(reply_to):
        """find replies to a certain comment"""
        # reply_to can also constraint the message that the reply belongs to
        result = db.session.query(Comment, User).join(User, User.user_id == Comment.user_id) \
            .filter(Comment.reply_to == reply_to, Comment.hidden == 0).all()
        return result

    @staticmethod
    def find_reply_to(user_id, offset, length):
        """query replies to user_id, return records from offset to offset + length"""
        result = db.session.query(Comment, User.nickname, User.avatar) \
            .join(User, User.user_id == Comment.user_id) \
            .filter(Comment.reply_to_id == user_id, Comment.hidden == 0, Comment.user_id != user_id) \
            .order_by(Comment.comment_id.desc()).limit(length).offset(offset).all()
        return result

    @staticmethod
    def count_reply_to(user_id):
        """return the number of comments that replied to user_id"""
        return Comment.query\
            .filter(Comment.reply_to_id == user_id, Comment.hidden == 0, Comment.user_id != user_id)\
            .count()

    @staticmethod
    def find_self_comment(self_id, offset, length):
        """query author's(self_id) own comments, return records from offset to offset + length"""
        result = db.session.query(Comment, User.nickname, User.avatar) \
            .join(User, User.user_id == Comment.reply_to_id) \
            .filter(Comment.user_id == self_id) \
            .order_by(Comment.comment_id.desc()).limit(length).offset(offset).all()
        return result

    # 通过user_id统计总评论数
    @staticmethod
    def count_self_comment(self_id):
        return Comment.query.filter(Comment.user_id == self_id).count()