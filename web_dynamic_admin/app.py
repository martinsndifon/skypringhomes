#!/usr/bin/python3
"""Admin flask app"""

from models import storage
from models.admin import Admin
from web_dynamic_admin.views import app_views
from web_dynamic_admin.views import auth
from flask import Flask, make_response, jsonify, render_template
from flask_cors import CORS
from flask_login import LoginManager
from web_dynamic_admin.utils.image_utils import get_first_image
from web_dynamic_admin.utils.time_format import time_format
from web_dynamic_admin.utils.price_format import price_format

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myloginsessionsecretkey'
app.register_blueprint(app_views)
app.register_blueprint(auth)
cors = CORS(app, resources={r"/skyspringhomes/admin/*": {"origins": "*"}})

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return storage.get(Admin, user_id)

@app.teardown_appcontext
def close_db_admin(error):
    """close the db storage"""
    storage.close()


@app.errorhandler(404)
def not_found_admin(error):
    """handle 404 error"""
    return render_template('404.html')


@app.template_global()
def first_image_admin(directory):
    return get_first_image(directory)


@app.template_global()
def time_format_admin(time):
    return time_format(time)


@app.template_global()
def price_format_admin(price):
    return price_format(price)


if __name__ == "__main__":
    """main entry"""
    app.run(host='0.0.0.0', port='3000', threaded=True)
