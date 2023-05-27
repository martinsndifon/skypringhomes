#!/usr/bin/python3
"""flask app"""

from models import storage
from api.v1.views import app_views
from flask import Flask, make_response, jsonify, render_template
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def close_db_api(error):
    """close the db storage"""
    storage.close()


@app.errorhandler(404)
def not_found_api(error):
    """handle 404 error"""
    return make_response(jsonify({'error': 'Not found'}), 404)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SWAGGER'] = {
        'title': 'skyspringhomes Restful API',
        'uiversion': 3
}

Swagger(app)

if __name__ == "__main__":
    """main entry"""
    app.run(host='0.0.0.0', port='5000', threaded=True)
