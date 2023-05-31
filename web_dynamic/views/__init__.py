#!/usr/bin/python3
"""Blueprint for the flask app views"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/skyspringhomes')

from web_dynamic.views.index import *
from web_dynamic.views.rent import *
from web_dynamic.views.sale import *
from web_dynamic.views.serviced import *
