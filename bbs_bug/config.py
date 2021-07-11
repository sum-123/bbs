import os

SECRET_KEY = os.urandom(24)

# SQLAlchemy configuration
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:xxxxxx@localhost/our_bbs"
SQLALCHEMY_TRACK_MODIFICATIONS = True
