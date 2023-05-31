#!/usr/bin/python3
"""Admin listing description module"""

from web_dynamic_admin.views import app_views
from flask import render_template, abort
from models import storage
from models.sale import Sale
import uuid
import os


@app_views.route('/sale/<sale_id>', methods=['GET'], strict_slashes=False)
def get_sale_prop_admin(sale_id):
    """Returns the description page of sale property"""
    cache_id = uuid.uuid4()
    sale_prop = storage.get(Sale, sale_id)
    if not sale_prop:
        abort(404)

    base_dir = '/home/vagrant/alx/skyspringhomes/web_dynamic_admin'
    directory_path = sale_prop.image_path
    image_files =os.listdir(base_dir + directory_path)
    total_images = len(image_files)

    return render_template('admin_sale_prop_description.html',
                           sale=sale_prop,
                           image_files=image_files,
                           total_images=total_images,
                           cache_id=cache_id)
