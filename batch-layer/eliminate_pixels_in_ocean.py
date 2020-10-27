# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 18:19:38 2020

@author: danie
"""
import json
import pandas as pd
from shapely.geometry import MultiPolygon, Polygon
#import geopandas as gpd


df = pd.read_csv('Mills_Treeloss.csv')
nrows = df.shape[0]

#counter of rows not in expected Polygon format
unexp_form = 0

#list to hold Polygons of all 1095 rows
mills_polygons = []

for i in range(nrows):

    #process each row in tree loss df to get Polygon data in form usable by Shapely
    row_geo = df.loc[i,'geometry']
    geo_dict = eval(row_geo)
    
    #check for irregular formats of dictionaries holding geometry data
    if len(geo_dict['coordinates']) > 1:
        print('Unexpected format!')
        unexp_form += 1
        
    #no irregularities from above
    print('unexpected forms:', unexp_form)
    
    coords = geo_dict['coordinates'][0]
    
    polygon_data = []
    
    for coord in coords:
        polygon_data.append(tuple(coord))

    mills_polygons.append(Polygon(polygon_data))
    


# Read in json file with Indonesian borders in MultiPolygon form
with open('stanford-py486tm4357-geojson.json', 'rb') as file:
    border_json = json.load(file)
    indo_multipolygon = border_json['features'][0]['geometry']['coordinates']

# Check for irregularities in format of Polygons    
for i in range(len(indo_multipolygon)):
    if len(indo_multipolygon[i]) > 1:
        print(str(i) + ': has more than 1 element, potentially holes')
    
#Indonesia MultiPolygon is made up of 6044 individual Polygons
print(len(indo_multipolygon))

#First Polygon
first_polygon = Polygon(indo_multipolygon[0][0])


print(gpd.GeoSeries([first_polygon]).to_json())
