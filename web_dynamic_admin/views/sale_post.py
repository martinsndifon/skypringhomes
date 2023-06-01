#!/usr/bin/python3
"""Sale post form module"""

from web_dynamic_admin.views import app_views
from flask import jsonify, render_template
from flask_login import login_required
import uuid


@app_views.route('/sale-post', methods=['GET'], strict_slashes=False)
@login_required
def sale_post():
    """Returns the sale post form"""
    cache_id = uuid.uuid4()
    return render_template('sale_post_form.html', cache_id=cache_id)
