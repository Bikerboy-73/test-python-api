
from ..service.users_service import insert_users, fetch_users, update_users, delete_users
from app.main.util.roles.roles import roles_required
from ..util.users_dto import UsersDto
from app.main.service.constants import *
from flask_restplus import Resource
from flask import request


api = UsersDto.api

_insert_users = UsersDto.UsersPost
_fetch_users = UsersDto.UsersGet
_update_users = UsersDto.UsersPut
_delete_users = UsersDto.UsersDelete


@api.route('/')
class Users(Resource):
    @api.expect(_insert_users, validate=True)
    #@api.doc(security='apikey')
    #@roles_required(Const.SITE_ADMIN, 'STUDENT')
    def post(self):
        """Create a new User"""
        data = request.json
        return insert_users(data=data)

    @api.expect(_update_users, validate=True)
    def put(self):
        """Update User"""
        data = request.json
        return update_users(data=data)

    @api.marshal_list_with(_fetch_users, envelope='data')
    def get(self):
        """List all Users"""
        return fetch_users()

    @api.expect(_delete_users, validate=True)
    def delete(self):
        """Delete User"""
        data = request.json
        return delete_users(data=data)
