# db_utils.py
#
# Utilities for storing and retrieving data.
#
##

import os
import json

from log_util import logger

"""Stores mills data from remote API call in a temporary directory
This is run automatically the first time the server starts
"""
def persist_mills_data(mills):
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open(os.path.join(os.getcwd(), 'temp','mills.json'), 'w') as f:
        f.write(json.dumps(mills))

    logger.info('Completed writing mills JSON')
