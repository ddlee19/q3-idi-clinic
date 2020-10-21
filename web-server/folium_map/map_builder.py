import os
import ee
import folium
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


def create_layer_from_ee_img(
    ee_image, 
    name, 
    vis_params, 
    attribution,
    min_zoom,
    max_zoom):
    '''
    Creates a raster TileLayer from a Google Earth image.
    '''
    tile_url = ee_image.getMapId(vis_params)["tile_fetcher"].url_format
    return folium.raster_layers.TileLayer(
        tiles = tile_url,
        attr = attribution,
        name = name,
        overlay = True,
        control = True,
        min_zoom=min_zoom,
        max_zoom=max_zoom
    )


def add_treeloss_layers_to_map(folium_map, gfc_image, attr, loss_params):
    '''
    Adds trecover losses for each year from 2001 to 2019 as separate
    layers on the map.
    '''
    lossyears = list(range(1, 20))

    for year in lossyears:
        lossyear = ee.List([year])
        replacementValue = ee.List([1])
        lossyearMask = gfc_image.remap(lossyear, 
                                       replacementValue, 
                                       bandName="lossyear")
        loss_img = gfc_image.mask(lossyearMask)
        formattedYear = f"2{str(year).rjust(3, '0')}"

        loss_tilelayer = create_layer_from_ee_img(
            ee_image=loss_img, 
            name=loss_params['name'] + f" {formattedYear}", 
            vis_params=loss_params["visual_params"], 
            attribution=attr,
            min_zoom=loss_params["min_zoom"],
            max_zoom=loss_params["max_zoom"])

        loss_tilelayer.add_to(folium_map)


def add_mills_markers_to_map(folium_map, mills_records):
    '''
    Adds mills markers to the map as a FeatureGroup layer.
    '''

    feature_group_layer = folium.map.FeatureGroup("mills")
    for _, mill in mills_records.items():
        folium.map.Marker(
            location=(mill["latitude"], mill["longitude"]),
            popup=f'''
			<div>
				<h4>
					{mill["mill_name"]}<br/>
					<span style="color:grey;">
						{mill["sub_state"].upper()}, {mill["state"].upper()}
					</span>
				</h4>
			<div>
		''',
        icon=folium.Icon(color='darkblue')
        ).add_to(feature_group_layer)

    feature_group_layer.add_to(folium_map)


def get_folium_map(mills_records):
    '''
    Creates a Folium map with raster layers specified in local
    configuration settings, as well as a mills FeatureGroup layer.
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

    # Create base map
    map_start = map_config["map_start"]
    folium_map = folium.Map(
        location=(map_start["latitude"], map_start["longitude"]),
        zoom_start=map_start["zoom"])

    # Add treecover raster layer specified in configuration to map
    treecover_params = map_config["layers"]["treecover2000"]
    
    treecover_tilelayer = create_layer_from_ee_img(
        ee_image=gfc_img_masked, 
        name=treecover_params["name"], 
        vis_params=treecover_params["visual_params"], 
        attribution=map_config["attribution"],
        min_zoom=treecover_params["min_zoom"],
        max_zoom=treecover_params["max_zoom"])

    treecover_tilelayer.add_to(folium_map)

    # Add treecover losses from 2001-2019 to map
    loss_params = map_config["layers"]["treecoverloss"]
    attr = map_config["attribution"]
    add_treeloss_layers_to_map(folium_map, gfc_img_masked, attr, loss_params)

    # Add mill markers to map as FeatureGroup layer
    add_mills_markers_to_map(folium_map, mills_records)

    # Add a layer control panel to the map.
    folium_map.add_child(folium.LayerControl())

    return folium_map._repr_html_()
