#!/usr/bin/python3
"""Admin listing modification module"""

from web_dynamic_admin.views import app_views
from flask import render_template, abort
from models import storage
from models.serviced import Serviced
import uuid
# import os


@app_views.route('/mod/service_apartments/<id>', methods=['GET'], strict_slashes=False)
def serviced_prop_mod(id):
    """Returns the put form for a service apartments"""
    cache_id = uuid.uuid4()
    serviced_prop = storage.get(Serviced, id)
    if not serviced_prop:
        abort(404)

    # base_dir = '/home/vagrant/alx/skyspringhomes/web_dynamic_admin'
    # directory_path = sale_prop.image_path
    # image_files =os.listdir(base_dir + directory_path)

    return render_template('put_serviced_prop.html',
                           serviced=serviced_prop,
                           cache_id=cache_id)
