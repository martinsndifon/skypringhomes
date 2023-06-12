#!/usr/bin/python3
"""create new admin user"""

from models import storage
from models.admin import Admin
from werkzeug.security import generate_password_hash

name = ''
email = ''
password = ''

admin = Admin(name=name, email=email, password=generate_password_hash(password, method='sha256'))
admin.save()
