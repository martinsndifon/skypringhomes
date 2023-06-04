#!/usr/bin/python3
"""main website flask app"""

from models import storage
from web_dynamic.views import app_views
from flask import Flask, make_response, jsonify, render_template
from flask_cors import CORS
from web_dynamic.utils.image_utils import get_first_image
from web_dynamic.utils.time_format import time_format
from web_dynamic.utils.price_format import price_format

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/skyspringhomes/*": {"origins": "*"}})

@app.teardown_appcontext
def close_db(error):
    """close the db storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handle 404 error"""
    return render_template('404.html')

@app.template_global()
def first_image(directory):
    return get_first_image(directory)


@app.template_global()
def time_format_admin(time):
    return time_format(time)


@app.template_global()
def price_format_admin(price):
    return price_format(price)


if __name__ == "__main__":
    """main entry"""
    app.run(host='0.0.0.0', port='5001', threaded=True)
