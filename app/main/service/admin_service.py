
from app.main.model.admin import Admin
import uuid
from app.main.service.constants import *


def insert_admin(data):
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
        Admin(**data).save()
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


def update_admin(data):
    try:
        Admin.objects(publicId=data['publicId']).update(**data)
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


def fetch_admin():
    data_set = Admin.objects.aggregate(*[
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


def delete_admin(data):
    try:
        Admin.objects(publicId=data['publicId']).delete()
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


def admin_login(data):
    for item in Admin.objects(email=data['email']):
        verify = verify_password(data['password'], item['password'].encode('utf-8'),  item['passwordSalt'])
        print(verify)
        if not verify:
            response_object = {
                'status': Const.FAIL,
                'message': 'Incorrect username or password.'
            }
            return response_object, Const.FAILURE_CODE
        token = generate_active_token(str(item['publicId']), item['role'])
        response_object = {
            'status': Const.SUCCESS,
            'token': token,
            'publicId': str(item['publicId']),
            'role': item['role'],
            'message': 'Successfully logged in.'
        }
        return response_object, Const.SUCCESS_CODE
    response_object = {
        'status': Const.FAIL,
        'message': 'Incorrect username or password.'
    }
    return response_object, Const.FAILURE_CODE





