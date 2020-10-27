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
