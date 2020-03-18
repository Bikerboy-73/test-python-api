from flask_restplus import Namespace, fields

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


class UsersDto:
    api = Namespace('users', authorizations=authorizations, description='Users related operations')

    UsersPost = api.model('UsersPost', {
        'name': fields.String(),
        'email': fields.String(),
        'password': fields.String(),
        'confirmPassword': fields.String(),
        # 'gender': fields.String(),
        # 'age': fields.Integer(),
        # 'website': fields.String(),
        # 'introduction': fields.String()
    })

    UsersGet = api.model('UsersGet', {
        'publicId': fields.String(),
        'name': fields.String(),
        'email': fields.String(),
        'status': fields.String(),
        'age': fields.Integer(),
        'website': fields.String(),
        'introduction': fields.String()
    })

    UsersPut = api.model('UsersPut', {
        'publicId': fields.String(),
        'role': fields.String()
    })

    UsersDelete = api.model('UsersDelete', {
        'publicId': fields.String()
    })

    UserLogin = api.model('UserLogin', {
        'email': fields.String(),
        'password': fields.String()
    })
