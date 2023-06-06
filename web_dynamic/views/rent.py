#!/usr/bin/python3
"""Listing description module"""

from web_dynamic.views import app_views
from flask import render_template, abort
from models import storage
from models.rent import Rent
import uuid
import os


@app_views.route('/rent/<rent_id>', methods=['GET'], strict_slashes=False)
def get_rented_prop(rent_id):
    """Returns the description of a rented property"""
    cache_id = uuid.uuid4()
    rented_prop = storage.get(Rent, rent_id)
    if not rented_prop:
        abort(404)

    base_dir = '/home/vagrant/alx/skyspringhomes/web_dynamic'
    directory_path = rented_prop.image_path
    image_files =os.listdir(base_dir + directory_path)
    image_files.sort()
    total_images = len(image_files)

    return render_template('rent_prop_description.html',
                           rent=rented_prop,
                           image_files=image_files,
                           total_images=total_images,
                           cache_id=cache_id)
