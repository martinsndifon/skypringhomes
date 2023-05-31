#!/usr/bin/python3
"""Rent post form module"""

from web_dynamic_admin.views import app_views
from flask import jsonify, render_template
import uuid


@app_views.route('/rent-post', methods=['GET'], strict_slashes=False)
def rent_post():
    """Returns the rent post form"""
    cache_id = uuid.uuid4()
    return render_template('rent_post_form.html', cache_id=cache_id)
