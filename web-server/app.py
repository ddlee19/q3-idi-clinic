# app.py
#
# Main application driver for Flask framework.
#
##


import os
import requests
import json

from flask import Flask, jsonify, render_template, abort, make_response
from app_util import build_mills_records
from log_util import logger

from folium_demo import get_folium_html

MILLS_URL = "https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson"

app = Flask(__name__)
config = {'host': os.environ.get('APP_HOST', '0.0.0.0'), 
          'port': os.environ.get("PORT", 5000)}
mills_records = build_mills_records({},
                                    MILLS_URL,
                                    {'country': 'Indonesia'})


@app.route("/api/v1.0/mills", methods=['GET'])
def get_mills():
    return jsonify({'mills': mills_records})


@app.route('/api/v1.0/mills/<int:mill_id>', methods=['GET'])
def get_mill(mill_id):
    if mill_id not in mills_records:
        abort(404)
    return jsonify({'mill': mills_records[mill_id]})


@app.route("/api/v1.0/folium-test", methods=['GET'])
def get_folium():
    return jsonify({'html': get_folium_html()})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=config.get('host'), port=config.get('port'))
