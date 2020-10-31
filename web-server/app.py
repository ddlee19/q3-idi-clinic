# app.py
#
# Main application driver for Flask framework.
#
##


import os
import requests
import json

from flask import Flask, jsonify, render_template, abort, make_response
from flask_cors import CORS, cross_origin
from app_util import build_mills_records, parse_brand_aggregations, parse_brand_filters, parse_brand_records
from log_util import logger
from folium_map.map_builder import get_folium_map, get_tile_urls

MILLS_URL = "https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson"

app = Flask(__name__)
cors = CORS(app)
config = {'host': os.environ.get('APP_HOST', '0.0.0.0'), 
          'port': os.environ.get("PORT", 5000),
          'CORS_HEADERS': 'Content-Type'}
mills_records = build_mills_records({},
                                    MILLS_URL,
                                    {'country': 'Indonesia'})
brand_aggregations = parse_brand_aggregations()
brand_filters = parse_brand_filters()
brand_records = parse_brand_records()


@app.route("/api/v1.0/mills", methods=['GET'])
def get_mills():
    return jsonify(mills_records)


@app.route('/api/v1.0/mills/<int:mill_id>', methods=['GET'])
def get_mill(mill_id):
    if mill_id not in mills_records:
        abort(404)
    return jsonify({'mill': mills_records[mill_id]})


@app.route("/api/v1.0/folium-map", methods=['GET'])
def get_folium():
    html = get_folium_map(mills_records)
    return jsonify({'html': html})


@app.route("/api/v1.0/tile-urls", methods=['GET'])
@cross_origin()
def get_tiles():
    return jsonify(get_tile_urls())


@app.route('/api/v1.0/brands/<string:brand_id>', methods=['GET'])
def get_brand(brand_id):
    if brand_id not in brand_records:
        abort(404)

    brand_mills = []
    for r in mills_records.values():
        if str(r["properties"]["consumer_brand_id"]) == brand_id:
            brand_mills.append(r)

    brand = brand_records[brand_id]
    brand["mills"] = brand_mills
    return jsonify(brand)


@app.route("/api/v1.0/brands/stats", methods=['GET'])
@cross_origin()
def get_brand_stats():
    return jsonify(brand_aggregations)


@app.route("/api/v1.0/brands", methods=['GET'])
@cross_origin()
def get_brand_filters():
    return jsonify(brand_filters)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=config.get('host'), port=config.get('port'))
