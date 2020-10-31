# db_utils.py
#
# Utilities for storing and retrieving data.
#
##

import os
import json

import pandas as pd

from log_util import logger



"""Stores mills data from remote API call in a temporary directory
This is run automatically the first time the server starts
"""
def write_json(mills, path):
    try:
        os.mkdir('output')
    except FileExistsError:
        pass

    with open(path, 'w') as f:
        f.write(json.dumps(mills))

    logger.info('Completed writing %s' % path)



"""Stores consumer data locally
"""
def write_df(df, path, index):
    try:
        os.mkdir('output')
    except FileExistsError:
        pass

    df.to_csv(path, index=index)

    logger.info('Completed writing %s' % path)
