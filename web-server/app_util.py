# app_util.py
#
# Application-specific utilities and functions.
#
##

import os
import requests
import json

from flask import abort
from log_util import logger
from db_util import persist_mills_data

"""Fetch mills data from remote API
This is run automatically the first time the server starts
"""
def build_mills_records(mills_dict, remote_endpoint, query_params):
    res = {}
    if os.path.exists('./temp/mills.json'):
        with open('./temp/mills.json', 'r') as f:
            res = json.load(f)
        logger.info("Completed reading mills from local JSON file.")
    elif len(mills_dict) == 0:
        logger.info("Started parsing mills from opendata API.")
        # Request mills from opendata.arcgis.com
        req = requests.get(remote_endpoint, params=query_params)
        res_json = json.loads(req.text)

        # Handle empty response or missing mills data
        if 'features' not in res_json or len(res_json['features']) == 0:
            abort(404)

        # Extract mills properties from response JSON
        mills = res_json['features']
        mills_dict = {x["properties"]["objectid"] : x["properties"] for x in mills}
        res = {k: v for k,v in mills_dict.items() if v['country'] in query_params['country']}
        persist_mills_data(res)
        logger.info("Completed parsing mills from opendata API.")

    logger.info("Completed updating mills records.")
    return res
