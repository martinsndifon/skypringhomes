#!/usr/bin/python3
"""Blueprint for the flask app views"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/skyspringhomes/admin')
auth = Blueprint('auth', __name__, url_prefix='/skyspringhomes/admin')

from web_dynamic_admin.views.index import *
from web_dynamic_admin.views.rent import *
from web_dynamic_admin.views.sale import *
from web_dynamic_admin.views.serviced import *
from web_dynamic_admin.views.rent_post import *
from web_dynamic_admin.views.sale_post import *
from web_dynamic_admin.views.serviced_post import *
from web_dynamic_admin.views.rent_put import *
from web_dynamic_admin.views.sale_put import *
from web_dynamic_admin.views.serviced_put import *
from web_dynamic_admin.views.auth import *
