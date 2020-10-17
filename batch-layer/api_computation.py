# Examples from https://github.com/google/earthengine-api/blob/master/python/examples/ipynb/Earth_Engine_REST_API_computation.ipynb

import json
from pprint import pprint

import ee
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

PROJECT = 'idi-development'
SERVICE_ACCOUNT = 'idi-service-acct-development@idi-development.iam.gserviceaccount.com'
KEY = 'privatekey.json'

# Authenticate with the service account and initialize Earth Engine
credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY)
ee.Initialize(credentials)
session = AuthorizedSession(credentials)

# Example 1: Define a computation. Note that the result of the computation is a FeatureCollection. To check that the computation can succeed without errors, get a value from the first Feature (the mean NDVI in the polygon).

# A collection of polygons.
states = ee.FeatureCollection('TIGER/2018/States')
maine = states.filter(ee.Filter.eq('NAME', 'Maine'))

# Imagery: NDVI vegetation index from MODIS.
band = 'NDVI'
images = ee.ImageCollection('MODIS/006/MOD13Q1').select(band)
image = images.first()

computation = image.reduceRegions(
  collection=maine, 
  reducer=ee.Reducer.mean().setOutputs([band]), 
  scale=image.projection().nominalScale()
)

# Print the value to test.
print(computation.first().get(band).getInfo())

# Serialize the computation.
serialized = ee.serializer.encode(computation, for_cloud_api=True)

# Send the request
# Make a POST request to the computeFeatures endpoint. Note that the request contains the Expression, which is the serialized computation.
url = 'https://earthengine.googleapis.com/v1alpha/projects/{}/table:computeFeatures'

response = session.post(
  url = url.format(PROJECT),
  data = json.dumps({'expression': serialized})
)

pprint(json.loads(response.content))
