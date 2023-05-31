#!/usr/bin/python3
"""Sale post form module"""

from web_dynamic_admin.views import app_views
from flask import jsonify, render_template
import uuid


@app_views.route('/sale-post', methods=['GET'], strict_slashes=False)
def sale_post():
    """Returns the sale post form"""
    cache_id = uuid.uuid4()
    return render_template('sale_post_form.html', cache_id=cache_id)
