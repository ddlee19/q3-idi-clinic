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
import pandas as pd
import geopandas as gpd

from data_util import (build_uml_data,
                        build_brand_data,
                        build_uml_boundaries_data,
                        build_loss_data,
                        build_risk_data)
from log_util import logger

PROJECT = 'idi-development'
SERVICE_ACCOUNT = 'idi-service-acct-development@idi-development.iam.gserviceaccount.com'
KEY = 'privatekey.json'
OUTPUT_DIR = './output'
INPUT_DIR = './input'
MILLS_API_URL = "https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson"
UML_QUERY = {'country': 'Indonesia'}
OUTPUT_UML_FNAME = 'umls.json'
OUTPUT_BRAND_FNAME = 'brands.csv'
INPUT_BRAND_MATCH_FNAME = 'complete_match_update.tsv'
INPUT_BRAND_INFO_FNAME = 'brand_info.csv'
OUTPUT_UML_BOUNDARIES_FNAME = 'uml_boundaries.geojson'
OUTPUT_BIGTABLE_FNAME = 'bigtable.csv'
MILL_AREAS_RES = 12
GFC_DATASET_NAME = "UMD/hansen/global_forest_change_2019_v1_7"
OUTPUT_UML_LOSS_FNAME = 'uml_loss.csv'
MILL_RADIUS_IN_M = 50000
MILL_AREA_FACTOR = 0.09      # 1 pixel is 0.09 hectares
OUTPUT_UML_RISK_FNAME = 'uml_risk.csv'
RISK_YEARS_INCLUDED = [2018, 2019]
OUTPUT_BRAND_BOUNDARIES_FNAME = 'brand_boundaries.geojson'
OUTPUT_BRAND_LOSS_FNAME = 'brand_loss.csv'
OUTPUT_UNIQUE_MILLS_FNAME = 'uniquemills.csv'
OUTPUT_UNIQUE_BRANDS_FNAME = 'uniquebrands.csv'
OUTPUT_MATCHES_FNAME = 'brand_mills.csv'


# Authenticate with the service account and initialize Earth Engine
credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY)
ee.Initialize(credentials)
session = AuthorizedSession(credentials)

data = {}
"""Builds UML data from API
"""
def load_uml_data():
    output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_UML_FNAME)
    return build_uml_data(output_file_path, MILLS_API_URL, UML_QUERY)

"""Fetch brand data from TSV
"""
def load_brand_data():
    input_file_path = os.path.join(INPUT_DIR, INPUT_BRAND_MATCH_FNAME)
    input_brand_info_file_path = os.path.join(INPUT_DIR, INPUT_BRAND_INFO_FNAME)
    output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_BRAND_FNAME)
    return build_brand_data(input_file_path, input_brand_info_file_path, output_file_path)

"""Builds UML boundaries
"""
def load_uml_boundaries_data():
    input_file_path = os.path.join(OUTPUT_DIR, OUTPUT_UML_FNAME)
    output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_UML_BOUNDARIES_FNAME)
    return build_uml_boundaries_data(output_file_path,
                                     input_file_path,
                                     MILL_RADIUS_IN_M,
                                     MILL_AREAS_RES)

"""Builds loss data for each year 2001-2019
"""
def load_uml_loss_data():
    input_file_path = os.path.join(OUTPUT_DIR, OUTPUT_UML_BOUNDARIES_FNAME)
    output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_UML_LOSS_FNAME)
    return build_loss_data(input_file_path,
                               output_file_path,
                               GFC_DATASET_NAME,
                               'umlid',
                               area_factor = MILL_AREA_FACTOR)
"""Calculates risk scores
"""
def load_uml_risk_data():
    input_file_path = os.path.join(OUTPUT_DIR, OUTPUT_UML_LOSS_FNAME)
    output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_UML_RISK_FNAME)
    years = RISK_YEARS_INCLUDED
    return build_risk_data(input_file_path,
                                output_file_path,
                                'umlid',
                                years=years)


"""Bigtable class for handling data merging and aggregations
"""
class Bigtable():
    def __init__(self, dfs={}):
        self.out_bigtable = os.path.join(OUTPUT_DIR, OUTPUT_BIGTABLE_FNAME)
        self.brands = dfs.get('brands', load_brand_data())
        self.uml =  dfs.get('uml', load_uml_data())
        self.uml_geo = dfs.get('uml_geo', load_uml_boundaries_data())
        self.uml_loss = dfs.get('uml_loss', load_uml_loss_data())
        self.uml_risk = dfs.get('uml_risk', load_uml_risk_data())
        self.out_uml = os.path.join(OUTPUT_DIR, OUTPUT_UNIQUE_MILLS_FNAME)
        self.out_brands = os.path.join(OUTPUT_DIR, OUTPUT_UNIQUE_BRANDS_FNAME)
        self.out_matches = os.path.join(OUTPUT_DIR, OUTPUT_MATCHES_FNAME)

        self.fix()
        self.build_unique_mills()
        self.build_big_table()
        self.generate_aggregations()


    def fix(self):
        self.uml['umlid'] = self.uml.umlid.str.lower()
        self.uml_risk.umlid = self.uml_risk.umlid.str.lower()
        self.uml_loss.umlid = self.uml_loss.umlid.str.lower()
        self.uml_geo.umlid = self.uml_geo.umlid.str.lower()


    def build_unique_mills(self):
        df1 = self.uml.drop(columns=['objectid']).merge(
                                self.uml_risk, on='umlid', how='left')
        df2 = self.uml_loss.merge(self.uml_geo.drop(
                    columns=['latitude', 'longitude']), on='umlid', how='left')
        self.unique_mills = df1.merge(df2, on='umlid', how='left')


    def write_uniquemills(self):
        self.unique_mills.to_csv(self.out_uml)

    def build_big_table(self):
        df0 = self.brands.merge(self.uml[['umlid', 'cert']], on='umlid', how='left')
        df1 = df0.merge(self.uml_risk, on='umlid', how='left')
        df2 = df1.merge(self.uml_loss, on='umlid', how='left')
        self.bigtable = df2.merge(self.uml_geo, on='umlid', how='left')

    def write_bigtable(self):
        self.bigtable.to_csv(self.out_bigtable)

    def generate_aggregations(self):
        self.aggregate_geom_by_brand()
        self.aggregate_brand_stats()


    def aggregate_geom_by_brand(self):
        output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_BRAND_BOUNDARIES_FNAME)
        if os.path.exists(output_file_path):
            self.brand_geo = gpd.read_file(output_file_path)
        else:
            geo_bigtable = gpd.GeoDataFrame(self.bigtable, geometry='geometry')
            geo_bigtable = geo_bigtable[geo_bigtable['geometry'].notnull()]
            keep_cols = ['brandid', 'geometry']
            self.brand_geo = geo_bigtable[keep_cols].dissolve(by='brandid')
            self.write_brand_geo()

    def write_brand_geo(self):
        output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_BRAND_BOUNDARIES_FNAME)
        self.brand_geo.to_file(output_file_path, driver='GeoJSON')


    def aggregate_brand_stats(self):
        self.brand_loss = self.load_brand_loss()
        brand_groups = self.bigtable.groupby('brand')
        brand_df = brand_groups.agg(
            brandid=pd.NamedAgg(column='brandid', aggfunc='first'),
            mill_count=pd.NamedAgg(column='umlid', aggfunc='count'),
            mean_future_risk=pd.NamedAgg('risk_score_future', 'mean'),
            mean_past_risk=pd.NamedAgg('risk_score_past', 'mean'),
            mean_current_risk=pd.NamedAgg('risk_score_current', 'mean'),
            rspo_mill_count=pd.NamedAgg(column='cert', aggfunc=lambda x: x.value_counts()['RSPO Certified']),
            unique_parent_co=pd.NamedAgg(column='prnt_comp', aggfunc=lambda x: len(x.unique())),
            unique_group_name=pd.NamedAgg(column='group_name', aggfunc=lambda x: len(x.unique()))
        )
        brand_df['nonrspo_mill_count'] = brand_df['mill_count']-brand_df['rspo_mill_count']
        brand_cols = ['brandid',
                      'brand',
                      'country',
                      'rspo_member_since',
                      'external_link',
                      'description_attribution',
                      'description']
        unique_brands_df = self.brands[brand_cols].drop_duplicates()
        brand_df1 = brand_df.merge(unique_brands_df, on='brandid', how='left')
        self.brand_df = brand_df1.merge(self.brand_loss, on='brandid', how='left')

        self.brand_df = self.brand_df.sort_values(by='mill_count',
                                                          ascending=False)
        logger.info("Aggregated brands data shape: %s" % str(self.brand_df.shape))



    def load_brand_loss(self):
        input_file_path = os.path.join(OUTPUT_DIR, OUTPUT_BRAND_BOUNDARIES_FNAME)
        output_file_path = os.path.join(OUTPUT_DIR, OUTPUT_BRAND_LOSS_FNAME)
        return build_loss_data(input_file_path,
                                   output_file_path,
                                   GFC_DATASET_NAME,
                                   'brandid',
                                   area_factor = MILL_AREA_FACTOR)


    def write_uniquebrands(self):
        self.brand_df.to_csv(self.out_brands)

    def write_brand_mill_matches(self):
        self.brands[['brandid', 'umlid']].to_csv(self.out_matches)


if __name__ == '__main__':
    try:
        os.mkdir(OUTPUT_DIR)
    except FileExistsError:
        logger.info('Output directory already exists.')

    uml_df = load_uml_data()
    logger.info("UML data shape: %s" % str(uml_df.shape))

    brand_df = load_brand_data()
    logger.info("Brand data shape: %s" % str(brand_df.shape))

    ##
    # Input: umls.json, output: boundaries.geojson
    # This code should read the output/umls.json file, use EE to
    # calculate the polygon shapes (and probably water/land/intersection areas
    # when available), then write the output to geojson. Return geopandas df
    # with UML ID, lat/lon, and polygon shapes.
    uml_boundaries_geodf = load_uml_boundaries_data()
    logger.info("UML boundaries data shape: %s" % str(uml_boundaries_geodf.shape))

    ##
    # Input: boundaries.geojson, output: loss.csv
    # This code reads in the boundaries file, then computes yearly tree cover
    # loss with EE. The result shows uml_id with loss for each year in columns
    uml_loss_by_year_df = load_uml_loss_data()
    logger.info("UML loss data shape: %s" % str(uml_loss_by_year_df.shape))

    ##
    # Input: loss.csv, output: risk.csv
    # This code reads in the loss file, then generates risk scores. The output
    # is a table of uml_id as the index, and columns for corresponding scores
    uml_risk_df = load_uml_risk_data()
    logger.info("UML risk data shape: %s" % str(uml_risk_df.shape))

    ##
    # Input: all of the above, output bigtable.csv
    # This code reads in and merges the output from above to create the big table used for aggregations
    tables = {
        'out': os.path.join(OUTPUT_DIR, OUTPUT_BIGTABLE_FNAME),
        'brands': brand_df,
        'uml':  uml_df,
        'uml_geo': uml_boundaries_geodf,
        'uml_loss': uml_loss_by_year_df,
        'uml_risk': uml_risk_df}

    t = Bigtable(tables)
    t.write_bigtable()
    logger.info("Bigtable data shape: %s" % str(t.bigtable.shape))

    ##
    # Input: big table, output uniquemills.csv
    # This code merges all meta data, loss, and risk scores for each mill.
    t.write_uniquemills()
    logger.info("Unique mills data shape: %s" % str(t.unique_mills.shape))

    ##
    # Input: big table, output uniquebrands.csv
    # This code merges all info, meta data, and aggregated data for each brand.
    t.write_uniquebrands()
    logger.info("Unique brands data shape: %s" % str(t.brand_df.shape))

    ##
    # Input: brands.csv, output brand_mills.csv
    # This code produces pairs of brandid and umlid for matching brands and mills
    t.write_brand_mill_matches()
    logger.info("Brand_mills data shape: %s" % str(t.brands[['brandid', 'umlid']].shape))
