#!/usr/bin/python3
"""Listing description module"""

from web_dynamic.views import app_views
from flask import render_template, abort
from models import storage
from models.sale import Sale
import uuid
import os


@app_views.route('/sale/<sale_id>', methods=['GET'], strict_slashes=False)
def get_sale_prop(sale_id):
    """Returns sale property description"""
    cache_id = uuid.uuid4()
    sale_prop = storage.get(Sale, sale_id)
    if not sale_prop:
        abort(404)

    base_dir = '/home/vagrant/alx/skyspringhomes/web_dynamic'
    directory_path = sale_prop.image_path
    image_files =os.listdir(base_dir + directory_path)
    image_files.sort()
    total_images = len(image_files)

    return render_template('sale_prop_description.html',
                           sale=sale_prop,
                           image_files=image_files,
                           total_images=total_images,
                           cache_id=cache_id)
