#!/usr/bin/python3
"""Service apartment post form module"""

from web_dynamic_admin.views import app_views
from flask import jsonify, render_template
from flask_login import login_required
import uuid


@app_views.route('/serviced-post', methods=['GET'], strict_slashes=False)
@login_required
def serviced_post():
    """Returns the serviced post form"""
    cache_id = uuid.uuid4()
    return render_template('serviced_post_form.html', cache_id=cache_id)
