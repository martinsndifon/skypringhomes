#!/usr/bin/python3
"""create new admin user"""

from models import storage
from models.admin import Admin
from werkzeug.security import generate_password_hash

name = 'martins ndifon'
email = 'martinsndifon@gmail.com'
password = 'martinsndifon'

admin = Admin(name=name, email=email, password=generate_password_hash(password, method='sha256'))
admin.save()
