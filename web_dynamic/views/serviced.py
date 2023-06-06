#!/usr/bin/python3
"""Listing description module"""

from web_dynamic.views import app_views
from flask import render_template, abort
from models import storage
from models.serviced import Serviced
import uuid
import os


@app_views.route('/service_apartments/<serviced_id>', methods=['GET'], strict_slashes=False)
def get_serviced_prop(serviced_id):
    """Returns the description of a serviced property"""
    cache_id = uuid.uuid4()
    serviced_prop = storage.get(Serviced, serviced_id)
    if not serviced_prop:
        abort(404)

    base_dir = '/home/vagrant/alx/skyspringhomes/web_dynamic'
    directory_path = serviced_prop.image_path
    image_files =os.listdir(base_dir + directory_path)
    image_files.sort()
    total_images = len(image_files)

    return render_template('serviced_prop_description.html',
                           serviced=serviced_prop,
                           image_files=image_files,
                           total_images=total_images,
                           cache_id=cache_id)
