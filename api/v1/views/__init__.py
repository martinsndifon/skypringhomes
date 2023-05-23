#!/usr/bin/python3
"""Blueprint for api"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.rent import *
from api.v1.views.sale import *
from api.v1.views.serviced import *
