#!/usr/bin/python3
"""image utility module"""

import os

def get_first_image(directory):
    """returns the first image in a directory"""
    image_files = os.listdir('/home/vagrant/alx/skyspringhomes/web_dynamic' + directory)
    image_files.sort()
    return image_files[0]
