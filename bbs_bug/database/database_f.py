from sqlalchemy import DateTime,  text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#创建一个Base类用作所有的数据库表格模型
class Base(db.Model):
    __abstract__ = True
    create_time = db.Column(DateTime,server_default = text("CURRENT_TIMESTAMP"))
    
