#创建User表，同时定义了之后会用到的方法
from sqlalchemy.sql.functions import user
from .database_f import Base,db

class User(Base):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.CHAR(32))
    avatar = db.Column(db.String(50), nullable=False, server_default=db.text("'default.png'"))
    
    @staticmethod
    def through_username(username):
        res = User.query.filter_by(username = username).all()
        return res

    @staticmethod
    def through_id(user_id):
        res = User.query.filter_by(user_id = user_id).all()
        return res

    @staticmethod
    def register(username,password,avatar):
        u = User(username = username,password = password,avatar = avatar)
        db.session.add(u)
        db.session.commit()
        return u
    
    @staticmethod
    def alt_avatar(username, up_avatar):
        res = User.query.filter_by(username = username).first()
        if res is not None:
            res.avatar = up_avatar
            db.session.commit()

    @staticmethod
    def alt_password(username,new_pass):
        res = User.query.filter_by(username = username).first()
        if res is not None:
            res.password = new_pass
            db.session.commit()

    @staticmethod
    def find_limit_of_user():
        result = db.session.query(User.username) \
            .order_by(User.user_id.desc()).all()
        return result