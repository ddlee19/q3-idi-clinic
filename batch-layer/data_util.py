# utils.py
#
# Data wrangling utilities and functions.
#
##

import os
import requests
import json

import pandas as pd

from log_util import logger
from storage_util import write_json, write_df


INPUT_CONSUMER_PATH = '../data/brands.tsv'
MILLS_API_URL = "https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson"
OUTPUT_MILLS_PATH = './output/mills.json'
OUTPUT_CONSUMER_PATH = './output/consumer.csv'

"""Fetch mills data from remote API
This is run automatically the first time the server starts
"""
def build_mills_data():
    mills_dict = {}
    res = {}
    params = {'country': 'Indonesia'}
    if os.path.exists(OUTPUT_MILLS_PATH):
        with open(OUTPUT_MILLS_PATH, 'r') as f:
            res = json.load(f)
        logger.info("Reading mills from local JSON file.")
    elif len(mills_dict) == 0:
        logger.info("Started parsing mills from opendata API.")
        # Request mills from opendata.arcgis.com
        req = requests.get(MILLS_API_URL, params=params)
        res_json = json.loads(req.text)

        # Handle empty response or missing mills data
        if 'features' not in res_json or len(res_json['features']) == 0:
            logger.error('Missing mills data')
            pass

        # Extract mills properties from response JSON
        mills = res_json['features']
        mills_dict = {x["properties"]["objectid"] : x["properties"] for x in mills}
        res = {k: v for k,v in mills_dict.items() if v['country'] in params['country']}
        write_json(res, OUTPUT_MILLS_PATH)

    df = pd.DataFrame.from_dict(res, orient='index') 
    return df

"""Fetch consumer brand data from TSV
"""
def build_consumer_data():
    res = None
    if os.path.exists(OUTPUT_CONSUMER_PATH):
        res = pd.read_csv(OUTPUT_CONSUMER_PATH)
        logger.info("Reading consumer data from local CSV file.")
    else:
        logger.info("Started parsing consumer data from TSV.")
        df = pd.read_csv(INPUT_CONSUMER_PATH, sep='\t')

        # Drop mills not on in indonesia
        df = df[df['Country'] == 'indonesia']
        # Keep wanted columns
        df = df[['UMLID', 'Mill Name', 'Mill Company', 'Parent Company', 'Province', 'District','Latitude', 'Longitude', 'RSPO']]
        # Drop mills not on the UML
        df = df[df['UMLID'].isna() == False]
        # Rename columns
        mapper = {'UMLID': ' uml',
                'Mill Name': 'mill_name',
                'Mill Company': 'mill_co',
                'Parent Company': 'parent_co',
                'Province': 'province',
                'District': 'district',
                'Latitude': 'lat',
                'Longitude': 'long',
                'RSPO': 'rspo'}
        res = df.rename(columns=mapper)

        write_df(res, OUTPUT_CONSUMER_PATH)
    
    return res

