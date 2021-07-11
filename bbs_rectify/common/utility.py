from datetime import *
from jwt import *
import jwt
from flask import request
from functools import wraps

key = "fzsshizhu"

def generate_access_token(username, exp: float = 2):

    now = datetime.utcnow()
    exp_datetime = now + timedelta(hours=exp)
    access_payload = {
        'exp': exp_datetime,
        'flag': 0,   #标识是否为一次性token，0是，1不是
        'iat': now,   # 开始时间
        'iss': 'leon',   # 签名
        'username': username   #用户名(自定义部分)
    }
    access_token = jwt.encode(access_payload, key, algorithm='HS256')
    return access_token

def decode_auth_token(token):
    try:
        payload = jwt.decode(token, key=key, algorithms='HS256')
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, jwt.InvalidSignatureError):
        return ""
    else:
        return payload


def identify(auth_header):
    """
    用户鉴权
    """

    if auth_header:
        payload = decode_auth_token(auth_header)
        if not payload:
            return False
        if "username" in payload and "flag" in payload:
            if payload["flag"] == 0:
                return payload["username"]
            else:
                return False
    return False

def login_required(f):
    """
    登录保护，验证用户是否登录
    :param f:
    :return:
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization", default=None)
        if not token:
            print('not login')
            return 'not Login','403 Permission Denied'
        username = identify(token)
        if not username:
            return 'not Login','403 Permission Denied'      # return 响应体, 状态码, 响应头
        return f(*args, **kwargs)
    return wrapper