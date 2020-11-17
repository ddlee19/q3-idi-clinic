# voronoi.py
#
# Implements a Voronoi diagram for partitioning point data.
#
##

import json

import numpy as np
import geopandas as gpd
import pandas as pd
from scipy.spatial import Voronoi
from shapely.geometry import Point, Polygon


class Vor():
    def __init__(self, data=None):
        if data is not None:
            self.uml = data[['latitude', 'longitude']]
        else:
            data = {}
            try:
                with open('../data/umls.json', 'r') as f:
                    data = json.load(f)
            except Exception as e:
                logger.error("Failed to read UML file.")

            self.uml = pd.DataFrame.from_dict(data, orient='index',
                columns=['latitude', 'longitude'])

        self.latlon_gdf = gpd.GeoDataFrame(self.uml, 
            geometry=gpd.points_from_xy(self.uml.longitude, self.uml.latitude),
            crs={'init' :'epsg:4326'})
        self.xy_gdf = self.latlon_gdf.to_crs("EPSG:3395")
        self.xy_pts = self.build_geom_list(self.xy_gdf)
        self._vor = Voronoi(self.xy_pts)
        self.point_records = {}
        self.pt_to_region_map = self.build_ptr_map()

        # self.region_geometry = self.build_region_geometry()

    def build_geom_list(self, gdf):
        x_l = gdf.geometry.x.tolist()
        y_l = gdf.geometry.y.tolist()
        pts_l = [[x_l[i], y_l[i]] for i in range(len(x_l))]
        return np.array(pts_l)

    def build_ptr_map(self):
        vor = self._vor
        for i, pt_coords in enumerate(vor.points):
            region_assigned = vor.point_region[i]

            self.point_records[i] = {
                'coords': pt_coords,
                'region_assigned': region_assigned
            }

    # def build_region_geometry(self):
        
