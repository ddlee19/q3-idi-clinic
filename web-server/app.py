# app.py
#
# Main application driver for Flask framework.
#
##


import os
import requests

from flask import Flask, jsonify, render_template, abort, make_response, request
from flask_cors import CORS, cross_origin
from utilities.log_util import logger
from utilities.map_builder import get_tile_urls
from data_factory import DataFactory


app = Flask(__name__)
cors = CORS(app)
config = {'host': os.environ.get('APP_HOST', '0.0.0.0'), 
          'port': os.environ.get("PORT", 5000),
          'CORS_HEADERS': 'Content-Type'}
factory = DataFactory()


@app.route('/api/v1.0/brands/<string:brand_name>', methods=['GET'])
@cross_origin()
def get_brand(brand_name):
    if not factory.is_valid_brand_name(brand_name):
        abort(404)
    return jsonify(factory.get_brand(brand_name))


@app.route('/api/v1.0/brands', methods=['GET'])
@cross_origin()
def get_brands():
    mill_id = request.args.get("mill_id")
    return jsonify(factory.get_brands(mill_id))


@app.route("/api/v1.0/brands/stats", methods=['GET'])
@cross_origin()
def get_aggregate_brand_stats():
   return jsonify(factory.get_aggregate_brand_stats())


@app.route('/api/v1.0/mills/<string:mill_id>', methods=['GET'])
@cross_origin()
def get_mill(mill_id):
    if not factory.is_valid_mill_id(mill_id):
        abort(404)
    return jsonify(factory.get_mill(mill_id))


@app.route("/api/v1.0/mills", methods=['GET'])
@cross_origin()
def get_mills():
    return factory.get_mills()


@app.route("/api/v1.0/mills/stats", methods=['GET'])
@cross_origin()
def get_mill_stats():
    return jsonify(factory.get_aggregate_mill_stats())


@app.route("/api/v1.0/tile-urls", methods=['GET'])
@cross_origin()
def get_tiles():
    return jsonify(get_tile_urls())


@app.errorhandler(404)
@cross_origin()
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.run(host=config.get('host'), port=config.get('port'))
