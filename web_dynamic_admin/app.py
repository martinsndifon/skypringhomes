#!/usr/bin/python3
"""flask app"""

from models import storage
from web_dynamic_admin.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from web_dynamic_admin.utils.image_utils import get_first_image

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/skyspringhomes/*": {"origins": "*"}})

@app.teardown_appcontext
def close_db_admin(error):
    """close the db storage"""
    storage.close()


@app.errorhandler(404)
def not_found_admin(error):
    """handle 404 error"""
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.template_global()
def first_image_admin(directory):
    return get_first_image(directory)


if __name__ == "__main__":
    """main entry"""
    app.run(host='0.0.0.0', port='3000', threaded=True)
