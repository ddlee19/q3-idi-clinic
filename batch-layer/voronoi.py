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

BUFFER_SIZE = 5000
BUFFER_RES = 12

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

        self.point_map = self.build_ptr_map(self._vor)
        self.region_map = self.build_region_map(self._vor)
        self.polygon_map = self.build_polygon_map(self._vor)
        self.buffered_points = self.build_point_buffer(self._vor)

    def build_geom_list(self, gdf):
        x_l = gdf.geometry.x.tolist()
        y_l = gdf.geometry.y.tolist()
        pts_l = [[x_l[i], y_l[i]] for i in range(len(x_l))]
        return np.array(pts_l)

    def build_ptr_map(self, vor):
        point_map = {}
        for i, pt_coords in enumerate(vor.points):
            region_assigned = vor.point_region[i]

            point_map[i] = {
                'idx': i,
                'coords': pt_coords,
                'region_assigned': region_assigned}
        return point_map

    def build_region_map(self, vor):
        regions = {}

        # vor.regions contains a lisst of vertices for each region.
        # var.vertices contains a list of vertix coordinates.
        for i, vertices in enumerate(vor.regions):
            vtx_coords = [tuple(vor.vertices[v]) for v in vertices]
            regions[i] = {'vertices': vertices, 'vtx_coords': vtx_coords}

        return regions

    def build_polygon_map(self, vor):
        for k, v in self.region_map.items():
            coords = v['vtx_coords']

            polygon = Polygon()
            # (A LinearRing must have at least 3 coordinate tuples)
            if len(coords) >= 3:
                polygon = Polygon(coords)
            self.region_map[k]['polygon'] = polygon

    def build_point_buffer(self, vor):
        for k, point in self.point_map.items():
            x = point['coords'][0]
            y = point['coords'][1]

            buff_point = Point(x, y).buffer(BUFFER_SIZE, resolution=BUFFER_RES)
            self.point_map[k]['buffer'] = buff_point
