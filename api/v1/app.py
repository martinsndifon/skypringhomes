#!/usr/bin/python3
"""flask app"""

from models import storage
from api.v1.views import app_views
from flask import Flask, make_response, jsonify, render_template
from flask import request, Response
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from functools import wraps
from os import getenv


def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.register_blueprint(app_views)

    # cross origin permission
    cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['SWAGGER'] = {
            'title': 'skyspringhomes Restful API',
            'uiversion': 3
    }

    Swagger(app)

    
    @app.teardown_appcontext
    def close_db_api(error):
        """close the db storage"""
        storage.close()


    @app.errorhandler(404)
    def not_found_api(error):
        """handle 404 error"""
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

def check_auth(username, password):
    """Verifies api authentication"""
    admin_name = getenv('ADMIN_USERNAME')
    admin_password = getenv('ADMIN_PASSWORD')
    return username == admin_name and password == admin_password

def authenticate():
    return Response(
        'Permission denied',
        403,
    )



if __name__ == "__main__":
    """main entry"""
    app = create_app()
    app.run(host='0.0.0.0', port='5000', threaded=True)
