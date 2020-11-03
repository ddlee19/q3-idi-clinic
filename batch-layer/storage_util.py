# db_utils.py
#
# Utilities for storing and retrieving data.
#
##

import os
import json

import pandas as pd

from log_util import logger


"""Writes JSON data to file
"""
def write_json(mills, path):
    try:
        with open(path, 'w') as f:
            f.write(json.dumps(mills))
        logger.info('Completed writing %s' % path)
    except Exception as e:
        logger.error('Failed writing %s' % path)


"""Writes dataframe to csv file
"""
def write_df(df, path, index=False):
    try:
        df.to_csv(path, index=index)
        logger.info('Completed writing %s' % path)
    except Exception as e:
        logger.error('Failed writing %s' % path)


"""Writes geodataframe to geojson.
"""
def write_geojson(mills_gdf, path):
    try:
        mills_gdf.to_file(path, driver='GeoJSON')
        logger.info('Completed writing %s' % path)
    except Exception as e:
        logger.error('Failed writing %s' % path)
