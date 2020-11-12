import os
import ee
import json
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account


def authenticate_to_ee():
    '''
    Authenticates to Google Earth Engine (GEE) using a Google Cloud Platform
    service account and initializes the GEE class instance.
    '''
    SERVICE_ACCOUNT = 'idi-service-acct-development@idi-development.iam.gserviceaccount.com'
    KEY = './private-key.json'
    credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY)
    ee.Initialize(credentials)


def get_tile_url(ee_image, vis_params):
    '''
    Generates a tile url for a GEE image.
    '''
    return ee_image.getMapId(vis_params)["tile_fetcher"].url_format


def get_tile_urls():
    '''
    Generates tile urls for the tree cover 2000 and 
    '''
    # Authenticate
    authenticate_to_ee()

    # Parse map configuration settings
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(f"{dir_path}/config.json")
    map_config = json.load(f)
    f.close()

    # Get Google Earth Engine image
    gfc_img = ee.Image(map_config["gee_image"])
    gfc_img_masked = gfc_img.updateMask(gfc_img)

    # Initialize return payload
    layer_urls = []

    # Add url for treecover raster tile layer to dictionary
    treecover_params = map_config["layers"]["treecover2000"]
    treecover_url = get_tile_url(gfc_img_masked, treecover_params["visual_params"])
    layer_urls.append(
        { 
            "tileSetName": treecover_params["name"],
            "tileUrl": treecover_url 
        })

    # Add urls for treecover loss years to dictionary
    loss_years = list(range(1, 20))
    loss_params = map_config["layers"]["treecoverloss"]

    for year in loss_years:
        loss_year = ee.List([year])
        replacement_value = ee.List([1])
        loss_year_mask = gfc_img_masked.remap(loss_year, 
                                       replacement_value, 
                                       bandName="lossyear")
        loss_img = gfc_img_masked.mask(loss_year_mask)
        formatted_year = f"2{str(year).rjust(3, '0')}"
        layer_name = loss_params['name'] + f" {formatted_year}"

        loss_tilelayer_url = get_tile_url(loss_img, loss_params["visual_params"])
        layer_urls.append(
            { 
                "tileSetName": layer_name,
                "tileUrl": loss_tilelayer_url 
            })

    return layer_urls
