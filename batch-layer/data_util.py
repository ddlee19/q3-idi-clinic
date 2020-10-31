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



"""Builds json data from API
"""
def build_uml_data(output_path, mills_api_url, request_params):
    res = {}
    if os.path.exists(output_path):
        logger.info("Reading UML mills from local file.")
        try:
            with open(output_path, 'r') as f:
                res = json.load(f)
        except Exception as e:
            logger.error("Failed to read UML file.")
            pass
    else:
        try:
            mills_dict = {}
            # Request mills from opendata.arcgis.com
            req = requests.get(mills_api_url, params=request_params)
            res_json = json.loads(req.text)

            # Handle empty response or missing mills data
            if 'features' not in res_json or len(res_json['features']) == 0:
                logger.error('Missing mills data')
                pass

            # Extract mills properties from response JSON
            mills = res_json['features']
            mills_dict = {x["properties"]["objectid"] : x["properties"] for x in mills}
            res = {k: v for k,v in mills_dict.items() if \
                    v['country'] in request_params['country']}
            write_json(res, output_path)

        except Exception as e:
            print(e)
            logger.error("Failed to read UML mills from API.")

    return pd.DataFrame.from_dict(res, orient='index') 


"""Fetch brand data from TSV
"""
def build_brand_data(input_path, output_path):
    res = None
    if os.path.exists(output_path):
        res = pd.read_csv(output_path)
        logger.info("Reading brand data from local CSV file.")
    else:
        logger.info("Started parsing brand data from TSV.")
        df = pd.read_csv(input_path, sep='\t')

        # Drop mills not on in indonesia or null rows
        df = df[df['Country'].notnull()]
        df = df[df['Country'] == 'indonesia']

        # Keep wanted columns
        df = df[['idx','UMLID', 'Consumer Company', 'Mill Name', 'Mill Company', 'Parent Company', 'Province', 'District','Latitude', 'Longitude', 'RSPO']]

        # Rename columns
        mapper = {
                'idx': 'idx',
                'UMLID': 'umlid',
                'Consumer Company': 'brand',
                'Mill Name': 'mill_name',
                'Mill Company': 'mill_co',
                'Parent Company': 'parent_co',
                'Province': 'province',
                'District': 'district',
                'Latitude': 'lat',
                'Longitude': 'long',
                'RSPO': 'rspo'}
        df = df.rename(columns=mapper)
        df.reset_index(drop=True, inplace=True)

        # Create df1 where each row has a company and mill idx
        df1 = df[df['brand'].notnull()].loc[:,['idx', 'brand']]

        # Create df2 where each row has a uml and mill idx, mill info
        df2 = df[df['umlid'].notnull()]

        # Merge and filter unique id/company tuples
        dfm = df1.merge(df2, on='idx', how='left')
        dfm = dfm[(dfm['brand_x'].notnull()) & (dfm['umlid'].notnull())]

        # Clean up merged dataset
        dfm.reset_index(drop=True, inplace=True)
        dfm.drop_duplicates(subset=['brand_x', 'umlid'], inplace=True)
        dfm.drop(columns=['brand_y'], inplace=True)
        dfm.rename(columns={'brand_x': 'brand'}, inplace=True)

        res = dfm
        write_df(res, output_path, index=False)

    return res

