#!/usr/bin/python3
"""Admin listing modification module"""

from web_dynamic_admin.views import app_views
from flask import render_template, abort
from flask_login import login_required
from models import storage
from models.rent import Rent
import uuid
# import os


@app_views.route('/mod/rent/<rent_id>', methods=['GET'], strict_slashes=False)
@login_required
def rented_prop_mod(rent_id):
    """Returns the put form for a rented property"""
    cache_id = uuid.uuid4()
    rented_prop = storage.get(Rent, rent_id)
    if not rented_prop:
        abort(404)

    # base_dir = '/home/vagrant/alx/skyspringhomes/web_dynamic_admin'
    # directory_path = rented_prop.image_path
    # image_files =os.listdir(base_dir + directory_path)

    return render_template('put_rent_prop.html',
                           rent=rented_prop,
                           cache_id=cache_id)
