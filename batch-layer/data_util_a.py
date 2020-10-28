import pandas as pd
import json
import geopandas as gpd
import os

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

            # Convert to GeoDataFrame
            mills_gdf = gpd.GeoDataFrame(
                            mills_df[['globalid', 'latitude', 'longitude']],
                            geometry=gpd.points_from_xy(mills_df.longitude,
                                                        mills_df.latitude))

            # Set CRS initially to epsg:4326 (lat/lon in degrees)
            mills_gdf.set_crs(epsg=4326, inplace=True)

            # Convert to CRS epsg:4326 (lat/lon in meters) and create buffer
            mills_gdf.to_crs('epsg:3395', inplace=True)
            mills_gdf['geometry']= mills_gdf.buffer(radius)

            # Write geodataframe out to geojson
            write_geojson(mills_gdf, output_file_path)

        except Exception as e:
            print(e)
            logger.error("Failed to read mills data from local json file.")

    return mills_gdf
