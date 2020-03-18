
from ..service.admin_service import insert_admin, fetch_admin, update_admin, delete_admin, admin_login
from app.main.util.roles.roles import roles_required
from ..util.admin_dto import AdminDto
from app.main.service.constants import *
from flask_restplus import Resource
from flask import request


api = AdminDto.api

_insert_admin = AdminDto.AdminPost
_fetch_admin = AdminDto.AdminGet
_update_admin = AdminDto.AdminPut
_delete_admin = AdminDto.AdminDelete
_login_admin = AdminDto.AdminLogin


@api.route('/')
class Admin(Resource):
    @api.expect(_insert_admin, validate=True)
    #@api.doc(security='apikey')
    #@roles_required(Const.SITE_ADMIN, 'STUDENT')
    def post(self):
        """Create a new Admin"""
        data = request.json
        return insert_admin(data=data)

    @api.expect(_update_admin, validate=True)
    def put(self):
        """Update Admin"""
        data = request.json
        return update_admin(data=data)

    @api.marshal_list_with(_fetch_admin, envelope='data')
    def get(self):
        """List all Admin"""
        return fetch_admin()

    @api.expect(_delete_admin, validate=True)
    def delete(self):
        """Delete Admin"""
        data = request.json
        return delete_admin(data=data)


@api.route('/admin-login')
class LoginAdmin(Resource):
    @api.expect(_login_admin, validate=True)
    def post(self):
        """Login for a Admin"""
        data = request.json
        return admin_login(data=data)
