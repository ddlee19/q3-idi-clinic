# app.py
#
# Main application driver for Flask framework.
#
##

import sys
import os
import requests

from flask import Flask, jsonify, render_template, abort, make_response, request
from flask_cors import CORS, cross_origin
from log_util import logger
from dal import DAL


app = Flask(__name__)
cors = CORS(app)
config = {'host': os.environ.get('APP_HOST', '0.0.0.0'), 
          'port': os.environ.get("PORT", 5000),
          'CORS_HEADERS': 'Content-Type'}


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/api/v1.0/brands/<int:brand_id>', methods=['GET'])
@cross_origin()
def get_brand(brand_id):
    '''
    Retrieves a single consumer brand by id.

    Parameters:
        brand_id (int): the unique identifier for the brand

    Returns:
        JSON
    '''
    if not dal.is_valid_brand(brand_id):
        abort(404)
    return jsonify(dal.get_brand(brand_id))


@app.route('/api/v1.0/brands', methods=['GET'])
@cross_origin()
def get_brands():
    '''
    Retrieves a list of consumer brands.  All brands are returned
    by default, but one may restrict the result set to all brands associated
    with a UML mill instead by using a query parameter when calling the API
    endpoint (e.g., "/api/v1.0/brands?uml_id=po1000000316").

    Parameters:
        None

    Returns:
        JSON
    '''
    uml_id = request.args.get("uml_id")
    return jsonify(dal.get_brands(uml_id))


@app.route("/api/v1.0/brands/stats", methods=['GET'])
@cross_origin()
def get_aggregate_brand_stats():
    '''
    Retrieves statistics computed across all consumer brands.

    Parameters:
        None

    Returns:
        JSON
    '''
    return jsonify(dal.get_brands_aggregate_stats())


@app.route('/api/v1.0/mills/<string:uml_id>', methods=['GET'])
@cross_origin()
def get_mill(uml_id):
    '''
    Retrieves a detailed representation of a mill on the UML
    (Universal Mill List) by its UML id.

    Parameters:
        uml_id (int): the UML id

    Returns:
        JSON
    '''
    if not dal.is_valid_uml_mill(uml_id):
        abort(404)
    return jsonify(dal.get_mill(uml_id))


@app.route("/api/v1.0/mills", methods=['GET'])
@cross_origin()
def get_mills():
    '''
    Retrieves all mills from the UML list as a GeoJSON feature collection.

    Parameters:
        None

    Returns:
        JSON
    '''
    return dal.get_mills()


@app.route("/api/v1.0/mills/stats", methods=['GET'])
@cross_origin()
def get_mill_stats():
    '''
    Retrieves statistics computed across all UML mills.

    Parameters:
        None

    Returns:
        JSON
    '''
    return jsonify(dal.get_mills_aggregate_stats())


@app.errorhandler(404)
@cross_origin()
def not_found(error):
    '''
    Generates an error response with a "404 - Not Found" status code
    if the API receives a request for a non-existent resource/endpoint.

    Parameters:
        error (Exception): The exception caught by the error handler

    Returns:
        (flask.Flask.response_class): the response message
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == 'docker':
            input_path = './'
        elif sys.argv[1] == 'local':
            input_path = '../data/'
        dal = DAL(input_path)
        app.run(host=config.get('host'), port=config.get('port'))
    else:
        logger.error('Invalid run arguments. Example: python app.py local')
        sys.exit(1)
