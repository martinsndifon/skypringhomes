#!/usr/bin/python3
"""API service apartment module"""

from api.v1.views import app_views
from datetime import datetime
from flask import jsonify, make_response, request, abort
from flasgger.utils import swag_from
from models import storage
from models.serviced import Serviced
import os
import shutil


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

    description = request.form.get('description')
    location = request.form.get('location')
    price = request.form.get('price')
    if not price or not location:
        abort(400, description="Price or location cannot be null")

    serviced_prop = Serviced(description=description, location=location,
                             price=price)

    # Handle the saving of media files
    prop_id = serviced_prop.id

    # Access uploaded images separately
    if 'images' in request.files:
        images = request.files.getlist('images')
        for image in images:
            base_dir = '/home/vagrant/alx/skyspringhomes/media_storage/serviced/images/'
            os.makedirs(base_dir, exist_ok=True)

            prop_dir = os.path.join(base_dir, prop_id)
            os.makedirs(prop_dir, exist_ok=True)

            filename = image.filename
            image.save(os.path.join(prop_dir, filename))

    # Acess uploaded videos separately
    if 'videos' in request.files:
        videos = request.files.getlist('videos')
        for video in videos:
            base_dir = '/home/vagrant/alx/skyspringhomes/media_storage/serviced/videos/'
            os.makedirs(base_dir, exist_ok=True)

            prop_dir = os.path.join(base_dir, prop_id)
            os.makedirs(prop_dir, exist_ok=True)

            filename = video.filename
            video.save(os.path.join(prop_dir, filename))

    serviced_prop.save()
    return make_response(jsonify(serviced_prop.to_dict()), 201)


@app_views.route('/service_apartments/<serviced_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/serviced/put_serviced.yml', methods=['PUT'])
def put_serviced(serviced_id):
    """Updates a serviced property in the db"""

    serviced_prop = storage.get(Serviced, serviced_id)
    if not serviced_prop:
        abort(404)

    # Handle update for db information
    ignore = ['id', 'created_at']

    data = request.form
    for key, value in data.items():
        if key not in ignore:
            setattr(serviced_prop, key, value)
    setattr(serviced_prop, 'updated_at', datetime.utcnow())

    # Handle update for images/videos
    if 'images' in request.files:
        image_path = serviced_prop.image_path
        # Delete the existing dir
        if os.path.exists(image_path):
            shutil.rmtree(image_path)
        else:
            pass
        # Create a new dir with updated images
        images = request.files.getlist('images')
        for image in images:
            base_dir = '/home/vagrant/alx/skyspringhomes/media_storage/serviced/images/'
            os.makedirs(base_dir, exist_ok=True)

            prop_dir = os.path.join(base_dir, serviced_id)
            os.makedirs(prop_dir, exist_ok=True)

            filename = image.filename
            image.save(os.path.join(prop_dir, filename))

    if 'videos' in request.files:
        video_path = serviced_prop.video_path
        # Delete the existing dir
        if os.path.exists(video_path):
            shutil.rmtree(video_path)
        else:
            pass
        # Create a new dir with updated videos
        videos = request.files.getlist('videos')
        for video in videos:
            base_dir = '/home/vagrant/alx/skyspringhomes/media_storage/serviced/videos/'
            os.makedirs(base_dir, exist_ok=True)

            prop_dir = os.path.join(base_dir, serviced_id)
            os.makedirs(prop_dir, exist_ok=True)

            filename = video.filename
            video.save(os.path.join(prop_dir, filename))

    storage.save()
    return make_response(jsonify(serviced_prop.to_dict()), 200)


@app_views.route('/service_apartments/<serviced_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/serviced/delete_serviced.yml', methods=['DELETE'])
def delete_serviced(serviced_id):
    """Deletes a serviced property from the db"""
    
    serviced_prop = storage.get(Serviced, serviced_id)
    if not serviced_prop:
        abort(404)
    
    # Handle deletion of image/videos from file system
    image_path = serviced_prop.image_path
    video_path = serviced_prop.video_path

    if os.path.exists(image_path):
        shutil.rmtree(image_path)
    else:
        pass

    if os.path.exists(video_path):
        shutil.rmtree(video_path)
    else:
        pass

    # Handle deletion of object from the db
    storage.delete(serviced_prop)
    storage.save()

    return make_response(jsonify({}), 200)
