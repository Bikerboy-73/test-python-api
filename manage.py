import os
import unittest
from app import blueprint
from flask_cors import CORS
from app.main import create_app
from flask_script import Manager
from flask_jwt_extended import JWTManager

app = create_app(os.getenv('ENV') or 'DEV')
app.register_blueprint(blueprint)
app.app_context().push()
jwt = JWTManager(app)
manager = Manager(app)
CORS(app)
# app.run()


def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    app.run(debug=True)
    app.config['SOAP'] = True
