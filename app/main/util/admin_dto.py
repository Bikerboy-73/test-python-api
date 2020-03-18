from flask_restplus import Namespace, fields

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


class AdminDto:
    api = Namespace('admin', authorizations=authorizations, description='Users related operations')

    AdminPost = api.model('AdminPost', {
        'name': fields.String(),
        'email': fields.String(),
        'password': fields.String(),
        'confirmPassword': fields.String(),
        # 'gender': fields.String(),
        # 'age': fields.Integer(),
        # 'website': fields.String(),
        # 'introduction': fields.String()
    })

    AdminGet = api.model('AdminGet', {
        'publicId': fields.String(),
        'name': fields.String(),
        'email': fields.String(),
        'status': fields.String(),
        'age': fields.Integer(),
        'website': fields.String(),
        'introduction': fields.String()
    })

    AdminPut = api.model('AdminPut', {
        'publicId': fields.String(),
        'role': fields.String()
    })

    AdminDelete = api.model('AdminDelete', {
        'publicId': fields.String()
    })

    AdminLogin = api.model('AdminLogin', {
        'email': fields.String(),
        'password': fields.String()
    })
