# utils.py
#
# Data wrangling utilities and functions.
#
##

import os
import requests
import json

import pandas as pd
import geopandas as gpd
import ee
import numpy as np

from log_util import logger
from storage_util import (write_json, write_df, write_geojson)



"""Builds json data from API
"""
def build_uml_data(output_path, mills_api_url, request_params):
    res = {}
    if os.path.exists(output_path):
        logger.info("Reading UML mills from local file.")
        try:
            with open(output_path, 'r') as f:
                res = json.load(f)
        except Exception as e:
            logger.error("Failed to read UML file.")
            pass
    else:
        try:
            mills_dict = {}
            # Request mills from opendata.arcgis.com
            req = requests.get(mills_api_url, params=request_params)
            res_json = json.loads(req.text)

            # Handle empty response or missing mills data
            if 'features' not in res_json or len(res_json['features']) == 0:
                logger.error('Missing mills data')
                pass

            # Extract mills properties from response JSON
            mills = res_json['features']
            mills_dict = {x["properties"]["objectid"] : x["properties"] for x in mills}

            column_mapper = {'Group_Name':'group_name', 'id':'umlid'}
            for k,v in mills_dict.items():
                if v['country'] in request_params['country']:
                    for old, new in column_mapper.items():
                        v[new] = v.pop(old)
                    res[k] = v

            write_json(res, output_path)

        except Exception as e:
            print(e)
            logger.error("Failed to read UML mills from API.")

    return pd.DataFrame.from_dict(res, orient='index')


"""Fetch brand data from TSV
"""
def build_brand_data(input_path, input_brand_path, input_new_matches_path, output_path):
    res = None
    if os.path.exists(output_path):
        res = pd.read_csv(output_path)
        logger.info("Reading brand data from local CSV file.")
    else:
        logger.info("Started parsing brand data from TSV.")
        df = pd.read_csv(input_path, sep='\t')

        # Drop mills not on in indonesia or null rows
        df = df[df['Country'].notnull()]
        df = df[df['Country'] == 'indonesia']

        # Keep wanted columns
        df = df[['idx','UMLID', 'Consumer Company', 'Mill Name',
                'Mill Company', 'Parent Company', 'Province',
                'District', 'RSPO']]

        # Rename columns
        mapper = {
                'idx': 'idx',
                'UMLID': 'umlid',
                'Consumer Company': 'brand',
                'Mill Name': 'mill_name',
                'Mill Company': 'group_name',
                'Parent Company': 'prnt_comp',
                'Province': 'state',
                'District': 'sub_state',
                'RSPO': 'rspo_model'}
        df = df.rename(columns=mapper)
        df.reset_index(drop=True, inplace=True)

        # Create df1 where each row has a company and mill idx
        df1 = df[df['brand'].notnull()].loc[:,['idx', 'brand']]

        # Create df2 where each row has a uml and mill idx, mill info
        df2 = df[df['umlid'].notnull()]

        # Merge and filter unique id/company tuples
        dfm = df1.merge(df2, on='idx', how='left')
        dfm = dfm[(dfm['brand_x'].notnull()) & (dfm['umlid'].notnull())]

        # Clean up merged dataset
        dfm.reset_index(drop=True, inplace=True)
        dfm.drop_duplicates(subset=['brand_x', 'umlid'], inplace=True)
        dfm.drop(columns=['brand_y', 'idx'], inplace=True)
        dfm.rename(columns={'brand_x': 'brand'}, inplace=True)

        # Bring in new match dataset
        dfnew = pd.read_csv(input_new_matches_path)

        # Keep wanted columns
        dfnew = dfnew[['UMLID', 'Consumer Company', 'Mill Name',
                'Mill Company', 'Parent Company', 'Province',
                'District', 'RSPO']]

        # Rename columns
        del mapper['idx']
        dfnew = dfnew.rename(columns=mapper)
        dfnew.reset_index(drop=True, inplace=True)

        # Concatenate datasets
        dfm = pd.concat([dfm, dfnew])

        # Rename brands
        brand_mapper = {
                      'ferrero':'Ferrero',
                      'kellog':'Kellogg Company',
                      'pepsico':'PepsiCo',
                      'frieslandcampina':'Royal FrieslandCampina N.V.',
                      'johnson and johnson':'Johnson & Johnson',
                      'general mills':'General Mills, Inc',
                      'hershey':'The Hershey Company',
                      'loreal':"L'Oreal",
                      'procter and gamble':'The Procter & Gamble Company',
                      'colgate palmolive':'Colgate-Palmolive Company',
                      'nestle':'Nestlé',
                      'mars':'Mars, Incorporated',
                      'unilever':'Unilever'}

        for old, new in brand_mapper.items():
            dfm['brand'] = dfm['brand'].replace(old,new)

        # Merge brand info.
        df3 = pd.read_csv(input_brand_path)
        df3.rename(columns={'name':'brand', 'id':'brandid'}, inplace=True)
        dft = df3.merge(dfm, on='brand', how='right')
        res = dft
        write_df(res, output_path, index=False)

    return res


"""Compute mill boundaries.
"""
def build_uml_boundaries_data(output_file_path, input_file_path, radius, res):

    if os.path.exists(output_file_path):
        uml_gdf = gpd.read_file(output_file_path)
        logger.info("Reading UML boundaries data from local geojson file.")
        pass
    else:
        logger.info("Started reading mills data from json.")
        # Rename column for 'id' as 'umlid'
        uml_df = pd.read_json(input_file_path, orient='index')
        #uml_df.rename(columns={"id": "umlid"}, inplace=True)

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
        uml_gdf['geometry']= uml_gdf.buffer(radius, resolution = res)
        uml_gdf.to_crs('epsg:4326', inplace=True)

        # Write geodataframe out to geojson
        write_geojson(uml_gdf, output_file_path)

    return uml_gdf


"""Use Google Earth Engine API to compute area and tree cover loss
(from Hansen data) within mill boundaries each year from 2001 to 2019.
"""
def build_loss_data(input_file_path,
                        output_file_path,
                        GFC_DATASET_NAME,
                        id_col,
                        area_factor = 1):
    loss_data = None
    if os.path.exists(output_file_path):
        loss_data = pd.read_csv(output_file_path)
        logger.info("Reading loss data from {}.".format(output_file_path))
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


        logger.info("Computing loss and area for geometries from {}.".format(input_file_path))
        logger.info("Loading GFC data.")
        # Load the Global Forest Change dataset as a GEE image
        gfc_img = ee.Image(GFC_DATASET_NAME)

        # Open geojson file and convert data to Earth Engine Feature Collection.
        with open(input_file_path) as f:
            data = json.load(f)
        geoms = ee.FeatureCollection(data['features'])

        # Compute cumulative tree cover loss per geometry across **all**
        # lossyears
        # NOTE: The resulting sum is a decimal number because a weighted
        # reduction is performed:
        # https://developers.google.com/earth-engine/guides/reducers_weighting.
        # The sum is a weighted aggregation of the bitmap property "loss,"
        # which is either 0 or 1.  We then convert to an area using the
        # area_factor parameter.
        logger.info("Computing tree cover loss sum.")
        lossdict = reduce_sum(gfc_img, 'loss', geoms)

        # Store area info in a dataframe.
        column_names = [id_col, "treeloss_sum"]
        rows = []

        for area in lossdict:
            rows.append([area['properties'][id_col],
                          area_factor*area['properties']['sum']])

        loss_data = pd.DataFrame(columns = column_names, data = rows)

        # Compute land area within each geometric boundary and add a column to data
        # frame.  Compute histogram of datamask layer per mill area.
        logger.info("Computing areas of land and forest.")
        datamask_bins = (1, 2, 1)   # 1 bin of [1,2)
        landTypedict = reduce_hist(gfc_img, 'datamask', geoms, datamask_bins)
        logger.info("Land finished.")
        # Extract land area for each mill and add to dataframe.
        land_areas = []
        for area in landTypedict:
            land_areas.append(area_factor*area["properties"]['histogram'][0][1])

        loss_data['land_area'] = land_areas

        # Compute forested area for each area and add a column to dataframe.
        # Compute the area where treecover2000 is greater than or equal to 30%.
        treecover_bins = (30, 101, 1)   # 1 bin of [30,101)
        treecoverdict = reduce_hist(gfc_img, 'treecover2000', geoms, treecover_bins)

        # Extract the area for each area boundary and add to dataframe.
        treecover2000_area = []
        for area in treecoverdict:
            treecover2000_area.append(area_factor*area["properties"]['histogram'][0][1])

        loss_data['forest_area'] = treecover2000_area

        # Compute cumulative tree cover loss area per area per year
        # Add a column to the data frame for each year.
        logger.info("Computing yearly tree cover loss.")
        lossyears = list(range(1, 20))

        lossyear_bins = (1, 20, 19)     # 19 bins of 1 each from 1-19
        lossyeardict = reduce_hist(gfc_img, 'lossyear', geoms, lossyear_bins)

        for i, year in enumerate(lossyears):
            col_name = "treeloss_20" + str(year).zfill(2)
            loss = []
            for area in lossyeardict:
                loss.append(area_factor*area['properties']['histogram'][i][1])

            loss_data[col_name] = loss

        logger.info("Yearly tree cover loss computation complete.")


        #Compute the total tree cover loss for each mill as a proportion of
        #land area and add to dataframe.
        loss_data['treeloss_sum_proportion_of_land'] = (
                    loss_data['treeloss_sum']/loss_data['land_area'])


        #Compute the total tree cover loss for each mill as a proportion of
        #forest in 2000 and add to dataframe.
        loss_data['treeloss_sum_proportion_of_forest'] = (
                    loss_data['treeloss_sum']/loss_data['forest_area'])


        #Compute the proportion of forest area that is remaining
        #(1 - proportion of forest lost).
        loss_data['remaining_proportion_of_forest'] = (
                    1 - loss_data['treeloss_sum_proportion_of_forest'])

        logger.info("Writing tree cover loss data to file.")
        write_df(loss_data, output_file_path, index = False)

    return loss_data


"""Performs sum reduction over regions for a specified band.
"""
def reduce_sum(gfc_img, band, geoms):
    compdict = gfc_img.select(band).reduceRegions(
        collection=geoms,
        reducer=ee.Reducer.sum(),
        scale=30
        )
    return compdict.getInfo()["features"]


"""Performs histogram reduction over regions for a specified band and bins.
"""
def reduce_hist(gfc_img, band, geoms, bins):
    low, high, num_bins = bins
    compdict = gfc_img.select(band).reduceRegions(
                    collection=geoms,
                    reducer=ee.Reducer.fixedHistogram(low, high, num_bins),
                    scale=30
                    )
    return compdict.getInfo()["features"]


"""Computes current, past, and future risk scores per mill.
"""
def build_risk_data(input_file_path, output_file_path, id_col, years = [2018, 2019]):
    risk_df = None
    if os.path.exists(output_file_path):
        risk_df = pd.read_csv(output_file_path)
        logger.info("Reading risk data from local csv file.")
        pass
    else:
        logger.info("Started reading loss data from csv.")
        loss_df = pd.read_csv(input_file_path)

        # Create a new column that is the z-score for the sqrt tree loss proportion.
        loss_df['past_risk_z'] = get_z(loss_df, 'treeloss_sum_proportion_of_forest')

        # Create a new column that is the risk (1-5) associated with z-score
        # of past tree loss
        loss_df['risk_score_past'] = get_risk_from_z(loss_df, 'past_risk_z')


        # Create a new column that is the mean treeloss for specified years.
        mean_col = 'mean_loss_'
        for year in years:
            mean_col += str(year)

        col_list = ['treeloss_' + str(year) for year in years]
        loss_df[mean_col] = loss_df.loc[:, col_list].mean(axis=1)

        # Create a new colum that is the mean treeloss as a proportion of forest.
        mean_prop_sqrt_col = mean_col + '_proportion_sqrt'
        loss_df[mean_prop_sqrt_col] = np.sqrt(loss_df[mean_col]/loss_df['forest_area'])

        # Create a new column that is the z-score for the mean treeloss as a
        # proportion of forest.
        current_z_col = mean_prop_sqrt_col + "_z"
        loss_df[current_z_col] = get_z(loss_df, mean_prop_sqrt_col)

        # Convert z-score to risk (1-5)
        loss_df['risk_score_current'] = get_risk_from_z(loss_df, current_z_col)

        # Create a new column that is the z-score for the remaining
        # tree cover proportion.
        loss_df['remaining_forest_z'] = get_z(loss_df, 'remaining_proportion_of_forest')

        # Create a new column that is 0.5*remaining proportion of forest z-score,
        # and 0.5*z-score for the mean current treeloss proportion of forest.
        loss_df['future_risk_z'] = 0.5*loss_df['remaining_forest_z'] + \
                                          0.5*loss_df[current_z_col]

        # Create a new column that is the risk (1-5) associated with z-score
        # of past tree loss
        loss_df['risk_score_future'] = get_risk_from_z(loss_df, 'future_risk_z')

        # risk_df includes UMLid and risk_score columns only
        risk_df = loss_df.loc[:, [id_col,
                                  'risk_score_current',
                                  'risk_score_past',
                                  'risk_score_future']]

        # Write out risk_df to CSV
        write_df(risk_df, output_file_path, index = False)

    return risk_df


def get_risk_from_z(df, z_col):
    rv = 5*(df[z_col] > 1) + \
          4*(df[z_col].between(0.5, 1)) + \
          3*(df[z_col].between(-0.5, 0.5)) + \
          2*(df[z_col].between(-1, -0.5)) + \
          1*(df[z_col] < -1)

    return rv


def get_z(df, col):
    mu = df[col].mean()
    sd = df[col].std()
    return (df[col] - mu)/sd
