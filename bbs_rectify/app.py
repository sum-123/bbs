from database import comment, init_db
from flask import Flask, make_response
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
def deal_404(error):
    app.logger.error(error)
    return 'methods forbidden'

@app.errorhandler(503)
def deal_404(error):
    app.logger.error(error)
    return 'service unavailable'

if __name__ == '__main__':
    init_db(app)
    #设置日志记录等级
    logging.basicConfig(level = logging.DEBUG)
    #创建日志记录器，给出记录地址，每个日志的大小，保存日志上限
    file_log_handler = RotatingFileHandler('bbs.log', maxBytes=1024 * 1024,backupCount=10)
    #设置记录日志的格式
    formatter = logging.Formatter('%(levelname)s %(filename)s %(lineno)d %(message)s')
    #为全局的日志工具对象添加日志记录器并开始工作
    file_log_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_handler)
    app.register_blueprint(identification)
    app.register_blueprint(personal)
    app.register_blueprint(message)
    app.register_blueprint(comment)
    app.register_blueprint(index)
    app.register_blueprint(search)
    app.run(debug=True)