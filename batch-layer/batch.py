# batch.py
#
# Main application driver for batch layer data wrangling
# and computation processes.
#
##
import os

import ee
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

from data_util import (build_uml_data, build_brand_data)
from log_util import logger

from data_util_a import build_uml_boundaries_data

PROJECT = 'idi-development'
SERVICE_ACCOUNT = 'idi-service-acct-development@idi-development.iam.gserviceaccount.com'
KEY = 'privatekey.json'
OUTPUT_DIR = './output'
INPUT_DIR = './input'
MILLS_API_URL = "https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson"
UML_QUERY = {'country': 'Indonesia'}
OUTPUT_UML_FNAME = 'umls.json'
OUTPUT_BRAND_FNAME = 'brands.csv'
INPUT_BRAND_FNAME = 'complete_match_update.tsv'
OUTPUT_BOUNDARIES_FNAME = 'boundaries.geojson'
MILL_RADIUS_IN_M = 50000

# Authenticate with the service account and initialize Earth Engine
credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY)
ee.Initialize(credentials)
session = AuthorizedSession(credentials)

"""Builds UML data from API
"""
def load_uml_data():
    output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_UML_FNAME)
    return build_uml_data(output_file_path, MILLS_API_URL, UML_QUERY)

"""Fetch brand data from TSV
"""
def load_brand_data():
    input_file_path = os.path.join(INPUT_DIR, INPUT_BRAND_FNAME)
    output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_BRAND_FNAME)
    return build_brand_data(input_file_path, output_file_path)

def load_uml_boundaries_data():
    input_file_path = os.path.join(OUTPUT_DIR, OUTPUT_UML_FNAME)
    output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_BOUNDARIES_FNAME)
    radius = MILL_RADIUS_IN_M
    return build_uml_boundaries_data(input_file_path, output_file_path, radius)

def load_uml_loss_data():
    pass

def load_uml_risk_data():
    pass

def load_big_table():
    pass

def generate_aggregations(table):
    pass

if __name__ == '__main__':
    try:
        os.mkdir(OUTPUT_DIR)
    except FileExistsError:
        logger.info('Output directory already exists.')

    uml_df = load_uml_data()
    logger.info("UML data shape: %s" % str(uml_df.shape))

    brand_df = load_brand_data()
    logger.info("Brand data shape: %s" % str(brand_df.shape))

    ## TODO AMANDA: input: umls.json, output: boundaries.geojson
    # This code should read the output/umls.json file, use EE to
    # calculate the polygon shapes (and probably water/land/intersection areas
    # when available), then write the output to geojson. Return geopandas df
    # with UML ID, lat/lon, and polygon shapes.
    uml_boundaries_geodf = load_uml_boundaries_data()
    logger.info("UML boundaries data shape: %s" % str(uml_boundaries_geodf.shape))

    ## TODO AMANDA: input: boundaries.geojson, output: loss.csv
    # This code reads in the boundaries file, then computes yearly tree cover
    # loss with EE. The result shows uml_id with loss for each year in columns
    uml_loss_by_year_df = load_uml_loss_data()

    ## TODO AMANDA: input: loss.csv, output: risk.csv
    # This code reads in the loss file, then generates risk scores. The output
    # is a taable of uml_id as the index, and columns for corresponding scores
    uml_risk_df = load_uml_risk_data()

    ## TODO TIM: input: all of the above, output bigtable for aggregations
    # This code reads in and merges the output from above to create the big table used for aggregaations
    big_table_df = load_big_table()

    ## TODO TIM: input: all of the above, output bigtable for aggregations
    # This code reads in and merges the output from above to create the big table used for aggregaations
    generate_aggregations(big_table_df)
