#!/usr/bin/python3
"""Admin listing modification module"""

from web_dynamic_admin.views import app_views
from flask import render_template, abort
from models import storage
from models.sale import Sale
import uuid
# import os


@app_views.route('/mod/sale/<sale_id>', methods=['GET'], strict_slashes=False)
def sale_prop_mod(sale_id):
    """Returns the put form for a sale property"""
    cache_id = uuid.uuid4()
    sale_prop = storage.get(Sale, sale_id)
    if not sale_prop:
        abort(404)

    # base_dir = '/home/vagrant/alx/skyspringhomes/web_dynamic_admin'
    # directory_path = sale_prop.image_path
    # image_files =os.listdir(base_dir + directory_path)

    return render_template('put_sale_prop.html',
                           sale=sale_prop,
                           cache_id=cache_id)
