import os
import requests

from flask import Flask, jsonify, render_template, abort, make_response


app = Flask(__name__)

mills = [
    {
        'id': 1,
        'title': u'Palm Oil Mill',
        'description': u'Large producer of palm oil.', 
        'latitude': 91.8975,
        'longitude': -45.2345
    },
    {
        'id': 2,
        'title': u'Palm Oil Mill Two',
        'description': u'Large producer of palm oil.', 
        'latitude': 91.8974,
        'longitude': -45.2346
    }
]


@app.route("/api/v1.0/mills", methods=['GET'])
def get_mills():
    return jsonify({'mills': mills})


@app.route('/api/v1.0/mills/<int:mill_id>', methods=['GET'])
def get_task(mill_id):
    mill = [mill for mill in mills if mill['id'] == mill_id]
    if len(mill) == 0:
        abort(404)
    return jsonify({'mill': mill[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
