
from flask_restplus import reqparse
from flask_restplus import fields
from flask_jwt_extended import create_access_token
from app.main import bcrypt
import datetime
import random
import os


def gen_salt():
    salt = str(os.urandom(random.randint(14, 18))).lstrip('b')
    return salt


def hash_password(password_string, salt):
    hash_pwd = bcrypt.generate_password_hash(salt + password_string)
    return hash_pwd


def verify_password(provided, password_hash, salt):
    return bcrypt.check_password_hash(password_hash, salt + provided)


def generate_active_token(public_id, role):
    try:
        identity = {
            'publicId': public_id,
            'role': role
        }
        access_token = create_access_token(expires_delta=False, identity=identity)
        return access_token
    except Exception as e:
        return e


class Const():
    authorizations = {
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'X-API-KEY'
        }
    }

    parser = reqparse.RequestParser()
    parser.add_argument('page', type=int, required=False)
    parser.add_argument('per_page', type=int, required=False, choices=[5, 10, 20, 30, 40, 50])
    parser.add_argument('publicId', type=str, required=False)

    # Message Constants
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'
    SUCCESS_CODE = 201
    FAILURE_CODE = 400

    # User Types
    USER_INSERT_SUCCESS = 'User added successfully.'
    USER_UPDATE_SUCCESS = 'User updated successfully.'
    USER_DELETE_SUCCESS = 'User deleted  successfully.'


class TimeFormat(fields.DateTime):
    def format(self, value):
        newval = str(value).split(" ")
        newval1 = str(newval[0])
        dt = datetime.datetime.strptime(newval1, '%Y-%m-%d')
        dt_new = '{0}-{1}-{2}'.format('{:02d}'.format(dt.day), '{:02d}'.format(dt.month), dt.year)
        return dt_new


class DevelopmentConst(Const):
    APP_DEBUG = True
    BASE_URL = "http://127.0.0.1:5000"


class TestingConst(Const):
    APP_DEBUG = False
    BASE_URL = "http://ogapi.ho.opspl.com"


class ProductionConst(Const):
    APP_DEBUG = False
    BASE_URL = ""


const_by_name = dict(
    dev=DevelopmentConst,
    test=TestingConst,
    prod=ProductionConst
)


def init_configs(env, app):
    env = 'dev'
    envConst = const_by_name[env]()
    members = [attr for attr in dir(envConst) if not callable(getattr(envConst, attr)) and not attr.startswith("__")]
    for k in members:
        app.config[k] = envConst.__getattribute__(k)
    return const_by_name[env]()


