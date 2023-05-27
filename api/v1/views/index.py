#!/usr/bin/python3
"""API status module"""

from api.v1.views import app_views
from datetime import datetime
from flasgger.utils import swag_from
from flask import jsonify
from models import storage
from models.rent_type import RentType
from models.rent import Rent
from models.sale import Sale
from models.serviced import Serviced


@app_views.route('/status', methods=['GET'], strict_slashes=False)
@swag_from('documentation/index/get_status.yml', methods=['GET'])
def status():
    """Status of the API"""
    return jsonify({"status": "Ok"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
@swag_from('documentation/index/get_stats.yml', methods=['GET'])
def stats():
    """Returns the number of listings for each listing type"""
    classes = [Rent, Sale, Serviced]
    names = ['for_rent', 'for_sale', 'service_apartments']

    objs = {}
    for i in range(len(classes)):
        objs[names[i]] = storage.count(classes[i])

    return jsonify(objs)


@app_views.route('/properties', methods=['GET'], strict_slashes=False)
@swag_from('documentation/index/get_properties.yml', methods=['GET'])
def properties_api():
    """Returns the list of all properties in the database"""
    all_props = []
    rented_prop = storage.all(Rent).values()
    for prop in rented_prop:
        all_props.append(prop.to_dict())

    sale_prop = storage.all(Sale).values()
    for prop in sale_prop:
        all_props.append(prop.to_dict())

    service_prop = storage.all(Serviced).values()
    for prop in service_prop:
        all_props.append(prop.to_dict())

    all_props = sorted(all_props, key=lambda x: datetime.fromisoformat(
                       x['updated_at']), reverse=True)

    return jsonify(all_props)
