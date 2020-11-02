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

def build_uml_boundaries_data(output_file_path, uml_df, radius):

    if os.path.exists(output_file_path):
        uml_gdf = gpd.read_file(output_file_path)
        logger.info("Reading UML boundaries data from local geojson file.")
        pass
    else:
        logger.info("Started reading mills data from json.")
        try:
            # Rename column for 'id' as 'umlid'
            uml_df.rename(columns={"id": "umlid"}, inplace=True)

            # Convert to GeoDataFrame
            uml_gdf = gpd.GeoDataFrame(
                            uml_df[['umlid', 'latitude', 'longitude']],
                            geometry=gpd.points_from_xy(uml_df.longitude,
                                                        uml_df.latitude))

            # Set CRS initially to epsg:4326 (lat/lon in degrees)
            uml_gdf.set_crs(epsg=4326, inplace=True)

            # Convert to CRS epsg:3395 (lat/lon in meters) and create buffer,
            # then convert back to CRS epsg:4326.
            uml_gdf.to_crs('epsg:3395', inplace=True)
            uml_gdf['geometry']= uml_gdf.buffer(radius, resolution = 10)
            uml_gdf.to_crs('epsg:4326', inplace=True)

            # Write geodataframe out to geojson
            write_geojson(uml_gdf, output_file_path)

        except Exception as e:
            print(e)
            logger.error("Failed to read mills data from local json file.")

    return uml_gdf


"""Use Google Earth Engine API to compute area and tree cover loss
(from Hansen data) within mill boundaries each year from 2001 to 2019.
"""
def build_uml_loss_data(input_file_path,
                        output_file_path,
                        GFC_DATASET_NAME,
                        area_factor = 1):
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
            gfc_img = ee.Image(GFC_DATASET_NAME)

            # Open geojson file and convert data to Earth Engine Feature
            # Collection.
            with open(input_file_path) as f:
                data = json.load(f)
            mills = data['features']
            mill_areas = ee.FeatureCollection(mills)

            # Compute cumulative tree cover loss per mill area across **all**
            # lossyears
            # NOTE: The resulting sum is a decimal number because a weighted
            # reduction is performed:
            # https://developers.google.com/earth-engine/guides/reducers_weighting.
            # The sum is a weighted aggregation of the bitmap property "loss,"
            # which is either 0 or 1.  We then convert to hectares using the
            # area_factor parameter.
            logger.info("Computing tree cover loss sum.")
            _lossdict = gfc_img.select('loss').reduceRegions(
                collection=mill_areas,
                reducer=ee.Reducer.sum(),
                scale=30
                )

            # Store mill info in a dataframe.
            column_names = ["umlid", "treeloss_sum"]
            mrows = []

            lossdict = _lossdict.getInfo()["features"]
            for mill in lossdict:
                mrows.append([mill['properties']['umlid'],
                              area_factor*mill['properties']['sum']])

            mill_loss_data = pd.DataFrame(columns = column_names, data = mrows)
            logger.info("Tree cover loss sum computation complete.")


            logger.info("Computing yearly tree cover loss.")
            # Compute land area per mill area and add a column to data frame.
            # Compute histogram of datamask layer per mill area.
            _landTypedict = gfc_img.select('datamask').reduceRegions(
                            collection=mill_areas,
                            reducer=ee.Reducer.fixedHistogram(0, 3, 3),
                            scale=30
                            )

            # Extract the area where land has been mapped for each mill boundary.
            land_areas = []
            landTypedict = _landTypedict.getInfo()["features"]
            for mill in landTypedict:
                land_areas.append(area_factor*mill["properties"]['histogram'][1][1])

            mill_loss_data['land_area'] = land_areas


            # Compute the area where treecover2000 is greater than or equal to 30%.
            _treecoverdict = gfc_img.select('treecover2000').reduceRegions(
                             collection=mill_areas,
                             reducer=ee.Reducer.fixedHistogram(30, 101, 1),
                             scale=30
                             )
            # Extract the area for each mill boundary.
            treecover2000_area = []
            treecoverdict = _treecoverdict.getInfo()["features"]
            for mill in treecoverdict:
                treecover2000_area.append(area_factor*mill["properties"]['histogram'][0][1])

            mill_loss_data['treecover2000_area'] = treecover2000_area


            # Compute cumulative tree cover loss area per mill per year
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
                logger.info("Tree cover loss computation for {} complete.".format(2000 + year))
            logger.info("Yearly tree cover loss computation complete.")

            #Compute the total tree cover loss for each mill as a proportion of
            #land area and add to dataframe.
            mill_loss_data['loss_proportion_of_land'] = (
                            mill_loss_data['treeloss_sum']/mill_loss_data['land_area'])


            #Compute the total tree cover loss for each mill as a proportion of
            #forest in 2000 and add to dataframe.
            mill_loss_data['loss_proportion_of_forest'] = (
                            mill_loss_data['treeloss_sum']/mill_loss_data['treecover2000_area'])


            #Compute the proportion of forest area that is remaining
            #(1 - proportion of forest lost).
            mill_loss_data['remaining_proportion_of_forest'] = (
                            1 - mill_loss_data['loss_proportion_of_forest'])

            logger.info("Writing tree cover loss data to file.")
            write_df(mill_loss_data, output_file_path, index = False)

        except Exception as e:
            print(e)
            logger.error("Failed to compute loss.")

    return mill_loss_data

"""Computes current, past, and future risk scores per mill.
"""
def build_uml_risk_data(input_file_path, output_file_path, years = [2018, 2019]):
    risk_df = None
    if os.path.exists(output_file_path):
        risk_df = pd.read_csv(output_file_path)
        logger.info("Reading UML risk data from local csv file.")
        pass
    else:
        logger.info("Started reading mill loss data from csv.")
        try:
            loss_df = pd.read_csv(input_file_path)

            # Create a new column that is the z-score for the tree loss proportion.
            mu = loss_df['loss_proportion_of_forest'].mean()
            sd = loss_df['loss_proportion_of_forest'].std()
            loss_df['past_risk_z'] = (loss_df['loss_proportion_of_forest'] - mu)/sd

            # Create a new column that is the risk (1-5) associated with z-score
            # of past tree loss
            loss_df['risk_score_past'] = 5*(loss_df['past_risk_z'] > 1) + \
                  4*(loss_df['past_risk_z'].between(0.5, 1)) + \
                  3*(loss_df['past_risk_z'].between(-0.5, 0.5)) + \
                  2*(loss_df['past_risk_z'].between(-1, -0.5)) + \
                  1*(loss_df['past_risk_z'] < -1)

            # Create a new column that is the z-score for the remaining
            # tree cover proportion.
            mu = loss_df['remaining_proportion_of_forest'].mean()
            sd = loss_df['remaining_proportion_of_forest'].std()
            loss_df['future_risk_z'] = (loss_df['remaining_proportion_of_forest'] - mu)/sd

            # Create a new column that is the risk (1-5) associated with z-score
            # of past tree loss
            loss_df['risk_score_future'] = 5*(loss_df['future_risk_z'] > 1) + \
                  4*(loss_df['future_risk_z'].between(0.5, 1)) + \
                  3*(loss_df['future_risk_z'].between(-0.5, 0.5)) + \
                  2*(loss_df['future_risk_z'].between(-1, -0.5)) + \
                  1*(loss_df['future_risk_z'] < -1)


            # Create a new column that is the mean treeloss for specified years.
            mean_col = 'mean_loss_'
            for year in years:
                mean_col += str(year)

            col_list = ['treeloss_' + str(year) for year in years]
            loss_df[mean_col] = loss_df.loc[:, col_list].mean(axis=1)

            # Create a new column that is the z-score for the mean treeloss.
            z_col = mean_col + "_z"
            mu = loss_df[mean_col].mean()
            sd = loss_df[mean_col].std()
            loss_df[z_col] = (loss_df[mean_col] - mu)/sd

            # Convert z-score to risk (1-5)
            loss_df['risk_score_current'] = 5*(loss_df[z_col] > 1) + \
                  4*(loss_df[z_col].between(0.5, 1)) + \
                  3*(loss_df[z_col].between(-0.5, 0.5)) + \
                  2*(loss_df[z_col].between(-1, -0.5)) + \
                  1*(loss_df[z_col] < -1)

            # risk_df includes UMLid and risk_score columns only
            risk_df = loss_df.loc[:, ['umlid',
                                      'risk_score_current',
                                      'risk_score_past',
                                      'risk_score_future']]

            # Write out risk_df to CSV
            write_df(risk_df, output_file_path, index = False)

        except Exception as e:
            print(e)
            logger.error("Failed to compute risk.")

    return risk_df
