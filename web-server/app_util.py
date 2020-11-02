# app_util.py
#
# Application-specific utilities and functions.
#
##

import os
import requests
import json
import ee
import random
from flask import abort
from log_util import logger
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

MILLS_PATH = './data/mills.json'

"""Fetch mills data from local file storage. This data is held in memory.
"""
def get_mills_records():

    if os.path.exists(MILLS_PATH):
        logger.info("Reading mills from local JSON file.")
        with open(MILLS_PATH, 'r') as f:
            return json.load(f)
    else:
        logger.error("Missing mills data.")
        abort(404)
        

def authenticate_to_ee():
    '''
    Authenticates to Google Earth Engine (GEE) using a Google Cloud Platform
    service account and initializes the GEE class instance.
    '''
    SERVICE_ACCOUNT = 'idi-service-acct-development@idi-development.iam.gserviceaccount.com'
    KEY = './private-key.json'
    credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY)
    ee.Initialize(credentials)


def add_mill_radii(mills):
    '''
    Generates GeoJSON geometries for the radii around the mills.
    '''
    radius_in_km = 50
    km_to_m = 1000
    mill_areas = ee.FeatureCollection(mills, "geometry").map(lambda mill: mill.buffer(radius_in_km * km_to_m))
    return mill_areas.getInfo()


"""Fetch mills data from remote API
This is run automatically the first time the server starts
"""
def build_mills_records(mills_dict, remote_endpoint, query_params):
    authenticate_to_ee()
    res = {}
    if os.path.exists('./temp/mills.json'):
        with open('./temp/mills.json', 'r') as f:
            res = json.load(f)
        logger.info("Completed reading mills from local JSON file.")

    elif len(mills_dict) == 0:    
        # Request mills from opendata.arcgis.com
        logger.info("Started parsing mills from opendata API.")
        req = requests.get(remote_endpoint, params=query_params)
        res_json = json.loads(req.text)

        # Handle empty response or missing mills data
        if 'features' not in res_json or len(res_json['features']) == 0:
            abort(404)

        # Add 50 km radii around mills
        mills = res_json['features']
        mill_features = add_mill_radii(mills)["features"]

        # Extract mills properties from response JSON and save to dictionary
        # while adding new properties for testing
        for mf in mill_features:
            if mf["properties"]["country"] in query_params['country']:
                mf["properties"]["relative_score"] = random.gauss(0, 1)
                mf["properties"]["absolute_score"] = random.randint(1, 5)
                mf["properties"]["consumer_brand_id"] = random.randint(1, 15)
                res[mf["properties"]["objectid"]] = mf

        logger.info("Completed parsing mills from opendata API.")

    logger.info("Completed updating mills records.")
    return res


def parse_brand_aggregations():
    '''
    Parses a JSON file to return mock consumer brand aggregation statistics.
    '''
    if os.path.exists('./temp/brand_agg.json'):
        with open('./temp/brand_agg.json', 'r') as f:
            return json.load(f)


def parse_brand_filters():
    '''
    Parses a JSON file to return mock consumer brand filter data.
    '''
    if os.path.exists('./temp/brand_filters.json'):
        with open('./temp/brand_filters.json', 'r') as f:
            return json.load(f)


def parse_brand_records():
    '''
    Parses a JSON file to return mock consumer brand records.
    '''
    if os.path.exists('./temp/brands.json'):
        with open('./temp/brands.json', 'r') as f:
            return json.load(f)
