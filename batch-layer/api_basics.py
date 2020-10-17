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

# Example 1: simple API call
url = 'https://earthengine.googleapis.com/v1alpha/projects/earthengine-public/assets/LANDSAT'
response = session.get(url)
pprint(json.loads(response.content))


# # Example 2: Get a list of images at a point
import urllib

coords = [-122.085, 37.422]

project = 'projects/earthengine-public'
asset_id = 'COPERNICUS/S2'
name = '{}/assets/{}'.format(project, asset_id)
url = 'https://earthengine.googleapis.com/v1alpha/{}:listImages?{}'.format(
  name, urllib.parse.urlencode({
    'startTime': '2017-04-01T00:00:00.000Z',
    'endTime': '2017-05-01T00:00:00.000Z',
    'region': '{"type":"Point", "coordinates":' + str(coords) + '}',
    'filter': 'CLOUDY_PIXEL_PERCENTAGE < 10',
}))

response = session.get(url)
content = response.content

for asset in json.loads(content)['images']:
    id = asset['id']
    cloud_cover = asset['properties']['CLOUDY_PIXEL_PERCENTAGE']
    print('%s : %s' % (id, cloud_cover))


# Example 3: Get pixels from one of the images
import numpy
import io

project = 'projects/earthengine-public'
asset_id = 'COPERNICUS/S2/20170430T190351_20170430T190351_T10SEG'
name = '{}/assets/{}'.format(project, asset_id)
url = 'https://earthengine.googleapis.com/v1alpha/{}:getPixels'.format(name)
body = json.dumps({
    'fileFormat': 'NPY',
    'bandIds': ['B2', 'B3', 'B4', 'B8'],
    'grid': {
        'affineTransform': {
            'scaleX': 10,
            'scaleY': -10,
            'translateX': 499980,
            'translateY': 4200000,
        },
        'dimensions': {'width': 256, 'height': 256},
    },
})

pixels_response = session.post(url, body)
pixels_content = pixels_response.content

array = numpy.load(io.BytesIO(pixels_content))
print('Shape: %s' % (array.shape,))
print('Data:')
print(array)
