# storage_utils_a.py
#
# Utilities for storing and retrieving data.
#
##

import os
import json

import pandas as pd

from log_util import logger

"""Writes mills geodataframe to geojson.
"""
def write_geojson(mills_gdf, path):
    try:
        os.mkdir('output')
    except FileExistsError:
        pass

    mills_gdf.to_file(path, driver='GeoJSON')

    logger.info('Completed writing %s' % path)
