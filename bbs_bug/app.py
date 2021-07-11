from database import comment, init_db
from flask import Flask
from flask_cors import *
from controller import identification, personal, message, comment, index, search
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config.from_pyfile('config.py')
CORS(app)

@app.errorhandler(404)
def deal_404(error):
    app.logger.error(error)
    return 'not exist'

@app.errorhandler(405)
def deal_405(error):
    app.logger.error(error)
    return 'methods forbidden'

@app.errorhandler(503)
def deal_503(error):
    app.logger.error(error)
    return 'service unavailable'


if __name__ == '__main__':
    init_db(app)
    logging.basicConfig(level=logging.DEBUG)
    #创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限
    file_log_handler = RotatingFileHandler('flask.log',maxBytes=1024*1024,backupCount=10)
    formatter=logging.Formatter('%(levelname)s %(filename)s %(lineno)d %(message)s')
    
    #将日志记录器指定日志的格式
    file_log_handler.setFormatter(formatter)
    #为全局的日志工具对象添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
    app.register_blueprint(identification)
    app.register_blueprint(personal)
    app.register_blueprint(message)
    app.register_blueprint(comment)
    app.register_blueprint(index)
    app.register_blueprint(search)
    app.run(debug=True)