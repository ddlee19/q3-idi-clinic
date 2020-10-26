# batch.py
#
# Main application driver for batch layer data wrangling
# and computation processes.
#
##


import ee
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

from data_util import build_consumer_data, build_mills_data

PROJECT = 'idi-development'
SERVICE_ACCOUNT = 'idi-service-acct-development@idi-development.iam.gserviceaccount.com'
KEY = 'privatekey.json'


# Authenticate with the service account and initialize Earth Engine
credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY)
ee.Initialize(credentials)
session = AuthorizedSession(credentials)

def load_consumer_data():
    return build_consumer_data()

def load_mills_data():
    return build_mills_data()

if __name__ == '__main__':
    c_df = load_consumer_data()
    m_df = load_mills_data()
    print(c_df.shape, m_df.shape)


