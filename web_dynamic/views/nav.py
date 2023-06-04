#!/usr/bin/python3
"""Views for navbar links"""

from web_dynamic.views import app_views
from flask import render_template
import uuid


@app_views.route('/about', methods=['GET'], strict_slashes=False)
def about():
    """Returns the about page"""
    cache_id = uuid.uuid4()

    return render_template('about.html',
                           cache_id=cache_id)



@app_views.route('/services', methods=['GET'], strict_slashes=False)
def services():
    """Returns the services page"""
    cache_id = uuid.uuid4()

    return render_template('services.html',
                           cache_id=cache_id)


@app_views.route('/contact', methods=['GET'], strict_slashes=False)
def contact():
    """Returns the contact us page"""
    cache_id = uuid.uuid4()

    return render_template('contact.html',
                           cache_id=cache_id)
