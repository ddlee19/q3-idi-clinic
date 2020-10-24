import argparse
import ee
import requests
import pandas as pd


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--output',
                        default = 'Mills_Treeloss.csv',
                        help='Path of the output csv file')

    args = parser.parse_args()

    # Initialize a connection to Earth Engine.
    # Authenticate if required.
    try:
        ee.Initialize()
        print('Initialization complete.')
    except:
        print('Authentication required.')
        ee.Authenticate()
        ee.Initialize()

    # Load the Global Forest Change dataset as a GEE image
    gfc_img = ee.Image("UMD/hansen/global_forest_change_2019_v1_7")

    # Retrieve Indonesian mill data from API endpoint
    r = requests.get("https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson?where=country%20%3D%20'Indonesia'")
    mills = r.json()['features']

    # Create list of feature geometries consisting of circular areas around mills, with each having a radius of 50 km
    radiusInKm = 50
    kmToMetersConversionFactor = 1000
    mill_areas = ee.FeatureCollection(mills, "geometry").map(lambda mill: mill.buffer(radiusInKm * kmToMetersConversionFactor))

    # Compute cumulative tree cover loss per mill area across **all** lossyears
    # NOTE: The resulting sum is a decimal number because a weighted reduction is performed:
    # https://developers.google.com/earth-engine/guides/reducers_weighting.  The sum
    # is a weighted aggregation of the bitmap property "loss," which is either 0 or 1,
    # but one could calculate area

    lossdict = gfc_img.select('loss').reduceRegions(
        collection=mill_areas,
        reducer=ee.Reducer.sum(),
        scale=30
        )

    # Store mill info in a dataframe.
    column_names = ["id", "Group_Name", "address", "alt_name", "cert", "country",
                    "globalid", "property_id", "latitude", "longitude", "mill_name",
                    "objectid", "prnt_comp", "rspo_model", "state", "sub_state",
                    "geometry", "treeloss_sum"]

    mrows = []


    for mill in lossdict.getInfo()["features"]:
        mrows.append([
            mill['id'],
            mill['properties']['Group_Name'],
            mill['properties']['address'],
            mill['properties']['alt_name'],
            mill['properties']['cert'],
            mill['properties']['country'],
            mill['properties']['globalid'],
            mill['properties']['id'],
            mill['properties']['latitude'],
            mill['properties']['longitude'],
            mill['properties']['mill_name'],
            mill['properties']['objectid'],
            mill['properties']['prnt_comp'],
            mill['properties']['rspo_model'],
            mill['properties']['state'],
            mill['properties']['sub_state'],
            mill['geometry'],
            mill['properties']['sum'],
            ])
    mills_data = pd.DataFrame(columns = column_names, data = mrows)

    # Compute cumulative tree cover loss per mill area per year
    # Add a column to the data frame for each year.
    firstMillLosses = {}
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
            loss.append(Mill['properties']['sum'])
        mills_data[col_name] = loss

    # Save data as csv.
    mills_data.to_csv(args.output, index = False)




if __name__ == '__main__': main()
