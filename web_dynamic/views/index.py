#!/usr/bin/python3
"""API status module"""

from web_dynamic.views import app_views
from datetime import datetime
from flask import jsonify, render_template
from models import storage
from models.rent_type import RentType
from models.rent import Rent
from models.sale import Sale
from models.serviced import Serviced
import uuid
import os


@app_views.route('/home', methods=['GET'], strict_slashes=False)
def properties():
    """Returns the list of all properties in the database"""
    cache_id = uuid.uuid4()
    all_props = []

    rented_prop = storage.all(Rent).values()
    list_rent = []
    for prop in rented_prop:
        list_rent.append(prop.to_dict())
        all_props.append(prop.to_dict())

    list_rent = sorted(list_rent, key=lambda x: datetime.fromisoformat(
                       x['updated_at']), reverse=True)


    sale_prop = storage.all(Sale).values()
    list_sale = []
    for prop in sale_prop:
        list_sale.append(prop.to_dict())
        all_props.append(prop.to_dict())

    list_sale = sorted(list_sale, key=lambda x: datetime.fromisoformat(
                       x['updated_at']), reverse=True)


    service_prop = storage.all(Serviced).values()
    list_serviced = []
    for prop in service_prop:
        list_serviced.append(prop.to_dict())
        all_props.append(prop.to_dict())

    list_serviced = sorted(list_serviced, key=lambda x: datetime.fromisoformat(
                           x['updated_at']), reverse=True)


    all_props = sorted(all_props, key=lambda x: datetime.fromisoformat(
                       x['updated_at']), reverse=True)

    return render_template('index.html',
                           rent=list_rent,
                           sale=list_sale,
                           serviced=list_serviced,
                           all=all_props,
                           cache_id=cache_id)
