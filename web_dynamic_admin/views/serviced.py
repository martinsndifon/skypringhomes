#!/usr/bin/python3
"""Admin listing description module"""

from web_dynamic_admin.views import app_views
from flask import render_template, abort
from flask_login import login_required
from models import storage
from models.serviced import Serviced
import uuid
import os


@app_views.route('/service_apartments/<serviced_id>', methods=['GET'], strict_slashes=False)
@login_required
def get_serviced_prop_admin(serviced_id):
    """Returns the description page of serviced property"""
    cache_id = uuid.uuid4()
    serviced_prop = storage.get(Serviced, serviced_id)
    if not serviced_prop:
        abort(404)

    base_dir = '/home/vagrant/alx/skyspringhomes/web_dynamic_admin'
    directory_path = serviced_prop.image_path
    image_files =os.listdir(base_dir + directory_path)
    total_images = len(image_files)

    return render_template('admin_serviced_prop_description.html',
                           serviced=serviced_prop,
                           image_files=image_files,
                           total_images=total_images,
                           cache_id=cache_id)
