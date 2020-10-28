import pandas as pd
import json
import geopandas as gpd
import os
import ee
import requests

from storage_util import write_json, write_df
from storage_util_a import write_geojson

from log_util import logger


"""Compute mill boundaries.
"""

def build_uml_boundaries_data(input_file_path, output_file_path, radius):

    if os.path.exists(output_file_path):
        mills_gdf = gpd.read_file(output_file_path)
        logger.info("Reading UML boundaries data from local geojson file.")
        pass
    else:
        logger.info("Started reading mills data from json.")
        try:
            mills_df = pd.read_json(input_file_path, orient='index')

            # Rename column for 'id' as 'UMLid'
            mills_df.rename(columns={"id": "UMLid"}, inplace=True)

            # Convert to GeoDataFrame
            mills_gdf = gpd.GeoDataFrame(
                            mills_df[['UMLid', 'latitude', 'longitude']],
                            geometry=gpd.points_from_xy(mills_df.longitude,
                                                        mills_df.latitude))

            # Set CRS initially to epsg:4326 (lat/lon in degrees)
            mills_gdf.set_crs(epsg=4326, inplace=True)

            # Convert to CRS epsg:3395 (lat/lon in meters) and create buffer,
            # then convert back to CRS epsg:4326.
            mills_gdf.to_crs('epsg:3395', inplace=True)
            mills_gdf['geometry']= mills_gdf.buffer(radius)
            mills_gdf.to_crs('epsg:4326', inplace=True)

            # Write geodataframe out to geojson
            write_geojson(mills_gdf, output_file_path)

        except Exception as e:
            print(e)
            logger.error("Failed to read mills data from local json file.")

    return mills_gdf


"""Use Google Earth Engine API to compute tree cover loss (from Hansen data)
within mill boundaries each year from 2001 to 2019.
"""
def build_uml_loss_data(input_file_path, output_file_path, area_factor = 1):
    mill_loss_data = None
    if os.path.exists(output_file_path):
        mill_loss_data = pd.read_csv(output_file_path)
        logger.info("Reading UML loss data from local csv file.")
        pass
    else:
        # Earth Engine Initialization
        try:
            ee.Initialize()
            logger.info("Earth Engine initialization complete.")
        except Exception as e:
            print(e)
            logger.info('Authentication required.')
            ee.Authenticate()
            ee.Initialize()
            logger.info("Earth Engine initialization complete.")

        try:
            logger.info("Loading GFC data.")
            # Load the Global Forest Change dataset as a GEE image
            gfc_img = ee.Image("UMD/hansen/global_forest_change_2019_v1_7")

            # Retrieve Indonesian mill data from API endpoint
            r = requests.get("https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson?where=country%20%3D%20'Indonesia'")
            mills = r.json()['features']

            # Create list of feature geometries consisting of circular areas
            # around mills, with each having a radius of 50 km
            radiusInKm = 50
            kmToMetersConversionFactor = 1000
            mill_areas = ee.FeatureCollection(mills, "geometry").map(
                    lambda mill: mill.buffer(radiusInKm * kmToMetersConversionFactor))

            # Compute cumulative tree cover loss per mill area across **all** lossyears
            # NOTE: The resulting sum is a decimal number because a weighted reduction
            # is performed:
            # https://developers.google.com/earth-engine/guides/reducers_weighting.
            # The sum is a weighted aggregation of the bitmap property "loss," which is
            # either 0 or 1, but one could calculate area by passing in an area conversion
            # factor
            logger.info("Computing tree cover loss.")
            lossdict = gfc_img.select('loss').reduceRegions(
                collection=mill_areas,
                reducer=ee.Reducer.sum(),
                scale=30
                )

            # Store mill info in a dataframe.
            column_names = ["UMLid"]
            mrows = []

            for mill in lossdict.getInfo()["features"]:
                mrows.append([mill['properties']['id']])

            mill_loss_data = pd.DataFrame(columns = column_names, data = mrows)

            # Compute cumulative tree cover loss per mill area per year
            # Add a column to the data frame for each year.
            lossyears = list(range(1, 20))

            for year in lossyears:
                lossyear = ee.List([year])
                replacementValue = ee.List([1])
                lossyearMask = gfc_img.remap(lossyear, replacementValue, bandName="lossyear")
                maskedImage = gfc_img.mask(lossyearMask)

                millLossesInYear = maskedImage.select('loss').reduceRegions(
                    collection=mill_areas,
                    reducer=ee.Reducer.sum(),
                    scale=30
                    )

                col_name = "treeloss_20" + str(year).zfill(2)
                loss = []
                for Mill in millLossesInYear.getInfo()["features"]:
                    loss.append(area_factor*Mill['properties']['sum'])

                mill_loss_data[col_name] = loss

            write_df(mill_loss_data, output_file_path, index = False)
        except Exception as e:
            print(e)
            logger.error("Failed to compute loss.")


    return mill_loss_data
