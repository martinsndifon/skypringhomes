#!/usr/bin/python3
"""API rent module"""

from api.v1.views import app_views
from datetime import datetime
from flask import jsonify, make_response, request, abort
from flasgger.utils import swag_from
from models import storage
from models.rent_type import RentType
from models.rent import Rent
import os
import shutil


@app_views.route('/rent', methods=['GET'], strict_slashes=False)
@swag_from('documentation/rent/get_rent.yml', methods=['GET'])
def get_rented_props():
    """Retrieves all properties for rent"""
    rented_props = storage.all(Rent).values()
    list_rent = []
    for prop in rented_props:
        list_rent.append(prop.to_dict())
    
    list_rent = sorted(list_rent, key=lambda x: datetime.fromisoformat(
                       x['updated_at']), reverse=True)

    return jsonify(list_rent)


@app_views.route('/rent/<rent_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/rent/get_id_rent.yml', methods=['GET'])
def get_rented_prop(rent_id):
    """Retrieves a single rented property"""
    rented_prop = storage.get(Rent, rent_id)
    if not rented_prop:
        abort(404)

    return jsonify(rented_prop.to_dict())


@app_views.route('/rent/type/<rent_type>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/rent/get_rent_type.yml', methods=['GET'])
def get_rent(rent_type):
    """Retrieves all rented properties of a particular type"""
    typed_props = storage.all(Rent, rent_type)
    if not typed_props:
        return jsonify({"report": "no listings for rent_type <{}>".format(rent_type)})
    
    list_renttype = []
    for prop in typed_props.values():
        list_renttype.append(prop.to_dict())

    list_renttype = sorted(list_renttype, key=lambda x: datetime.fromisoformat(
                       x['updated_at']), reverse=True)

    return jsonify(list_renttype)
    

@app_views.route('/rent', methods=['POST'], strict_slashes=False)
@swag_from('documentation/rent/post_rent.yml', methods=['POST'])
def post_rent():
    """Creates a new rented property in the db"""
    data = request.form

    description = data.get('description')
    location = data.get('location')
    if not location:
        abort(400, description="Location cannot be null")

    price = data.get('price')
    if not price:
        abort(400, description="Price cannot be null")

    rent_type = data.get('rent_type')
    if not rent_type:
        abort(400, description="Rent_type cannot be null")

    rented_prop = Rent(description=description, location=location, price=price,
                       rent_type=rent_type)

    rented_prop.save()
    return make_response(jsonify(rented_prop.to_dict()), 201)


@app_views.route('/rent/<rent_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/rent/put_rent.yml', methods=['PUT'])
def put_rent(rent_id):
    """Updates a rented property in the db"""

    rented_prop = storage.get(Rent, rent_id)
    if not rented_prop:
        abort(404)
    
    ignore = ['id', 'created_at']

    data = request.json
    for key, value in data.items():
        if key not in ignore:
            setattr(rented_prop, key, value)
    setattr(rented_prop, 'updated_at', datetime.utcnow())
    storage.save()
    return make_response(jsonify(rented_prop.to_dict()), 200)


@app_views.route('/rent/<rent_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/rent/delete_rent.yml', methods=['DELETE'])
def delete_rent(rent_id):
    """Deletes a rented property from the db"""
    
    rented_prop = storage.get(Rent, rent_id)
    if not rented_prop:
        abort(404)
    
    storage.delete(rented_prop)
    storage.save()

    return make_response(jsonify({}), 200)
