
from app.main.model.users import Users
import uuid
from app.main.service.constants import *


def insert_users(data):
    try:
        if data['password'] != data['confirmPassword']:
            response_object = {
                'status': Const.FAIL,
                'message': 'Mismatch password.'
            }
            return response_object, Const.FAILURE_CODE
        del data['confirmPassword']
        data['publicId'] = uuid.uuid4()
        salt = gen_salt()
        data['password'] = hash_password(data['password'], salt)
        data['passwordSalt'] = salt
        Users(**data).save()
        response_object = {
            'status': Const.SUCCESS,
            'message': Const.USER_INSERT_SUCCESS
        }
        return response_object, Const.SUCCESS_CODE
    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE


def update_users(data):
    try:
        Users.objects(publicId=data['publicId']).update(**data)
        response_object = {
            'status': Const.SUCCESS,
            'message': Const.USER_UPDATE_SUCCESS
        }
        return response_object, Const.SUCCESS_CODE

    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE


def fetch_users():
    data_set = Users.objects.aggregate(*[
        {"$project":
            {
                'publicId': 1,
                'name': 1,
                'email': 1,
                'status': 1,
                'gender': 1,
                'age': 1,
                'website': 1,
                'introduction': 1
            }
        }
    ])
    details = list(data_set)
    return details


def delete_users(data):
    try:
        Users.objects(publicId=data['publicId']).delete()
        response_object = {
            'status': Const.SUCCESS,
            'message': Const.USER_DELETE_SUCCESS
        }
        return response_object, Const.SUCCESS_CODE
    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE
