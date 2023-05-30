#!/usr/bin/python3
'''This script contains index view '''
from flask import jsonify
from api.v1.views import app_views



@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returns JSON representation of the data"""
    return jsonify(status="OK")

