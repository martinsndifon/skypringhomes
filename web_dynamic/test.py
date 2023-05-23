#!/usr/bin/python3
"""test module for flask app"""

from models import storage
from models.renttype import RentType
from flask import Flask

app = Flask(__name__)

@app.teardown_appcontext
def close_session(exception=None):
    """close the current session"""
    storage.close()

@app.route('/rent_type', strict_slashes=False)
def list_renttypes():
    """List all rent types available"""
    types = storage.all(RentType)
    for i in types:
        print(i)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
