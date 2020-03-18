from flask_restplus import Api
from flask import Blueprint
from .main.controller.users_controller import api as users_ns
from .main.controller.admin_controller import api as admin_ns


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(blueprint,
          title='TestApi',
          version='1.0',
          description='API web service'
          )


api.add_namespace(admin_ns)
api.add_namespace(users_ns)
