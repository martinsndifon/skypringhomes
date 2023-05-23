#!/usr/bin/python3
"""API service apartment module"""

from api.v1.views import app_views
from datetime import datetime
from flask import jsonify, make_response, request, abort
from flasgger.utils import swag_from
from models import storage
from models.serviced import Serviced


@app_views.route('/service_apartments', methods=['GET'], strict_slashes=False)
@swag_from('documentation/serviced/get_serviced.yml', methods=['GET'])
def get_serviced_props():
    """Retrieves all service apartments"""
    serviced_props = storage.all(Serviced).values()
    list_serviced = []
    for prop in serviced_props:
        list_serviced.append(prop.to_dict())
    
    list_serviced = sorted(list_serviced, key=lambda x: datetime.fromisoformat(
                       x['updated_at']), reverse=True)

    return jsonify(list_serviced)


@app_views.route('/service_apartments/<serviced_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/serviced/get_id_serviced.yml', methods=['GET'])
def get_serviced_prop(serviced_id):
    """Retrieves a single serviced property"""
    serviced_prop = storage.get(Serviced, serviced_id)
    if not serviced_prop:
        abort(404)

    return jsonify(serviced_prop.to_dict())


@app_views.route('/service_apartments', methods=['POST'], strict_slashes=False)
@swag_from('documentation/serviced/post_serviced.yml', methods=['POST'])
def post_serviced():
    """Creates a new serviced property in the db"""
    data = request.json

    description = data.get('description')
    location = data.get('location')
    if not location:
        abort(400, description="Location cannot be null")

    price = data.get('price')
    if not price:
        abort(400, description="Price cannot be null")

    serviced_prop = Serviced(description=description, location=location,
                             price=price)

    serviced_prop.save()
    return make_response(jsonify(serviced_prop.to_dict()), 201)


@app_views.route('/service_apartments/<serviced_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/serviced/put_serviced.yml', methods=['PUT'])
def put_serviced(serviced_id):
    """Updates a serviced property in the db"""

    serviced_prop = storage.get(Serviced, serviced_id)
    if not serviced_prop:
        abort(404)
    
    ignore = ['id', 'created_at']

    data = request.json
    for key, value in data.items():
        if key not in ignore:
            setattr(serviced_prop, key, value)
    setattr(serviced_prop, 'updated_at', datetime.utcnow())
    storage.save()
    return make_response(jsonify(serviced_prop.to_dict()), 200)


@app_views.route('/service_apartments/<serviced_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/serviced/delete_serviced.yml', methods=['DELETE'])
def delete_serviced(serviced_id):
    """Deletes a serviced property from the db"""
    
    serviced_prop = storage.get(Serviced, serviced_id)
    if not serviced_prop:
        abort(404)
    
    storage.delete(serviced_prop)
    storage.save()

    return make_response(jsonify({}), 200)
