import os
import requests
import json

from flask import Flask, jsonify, render_template, abort, make_response

MILLS_URL = "https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson"
app = Flask(__name__)


@app.route("/api/v1.0/mills", methods=['GET'])
def get_mills():
    payload = {'country': 'Indonesia'}
    req = requests.get(MILLS_URL, params=payload)
    res_json = json.loads(req.text)

    if 'features' not in res_json or len(res_json['features']) == 0:
        abort(404)

    mills = res_json['features']
    mills_dict = {x["properties"]["objectid"] : x["properties"] for x in mills}
    return jsonify({'mills': mills_dict})


@app.route('/api/v1.0/mills/<int:mill_id>', methods=['GET'])
def get_task(mill_id):
    mills = []
    mill = [mill for mill in mills if mill['id'] == mill_id]
    if len(mill) == 0:
        abort(404)
    return jsonify({'mill': mill[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
