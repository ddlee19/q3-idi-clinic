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

BUFFER_SIZE = 50000
BUFFER_RES = 4

class Vor():
     """Generates Voronoi partitions from UML lat/lon coordinates."""
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
                columns=['umlid','latitude', 'longitude'])

        self.latlon_gdf = gpd.GeoDataFrame(self.uml,
            geometry=gpd.points_from_xy(self.uml.longitude, self.uml.latitude),
            crs={'init' :'epsg:4326'})
        self.xy_gdf = self.latlon_gdf.to_crs("EPSG:3395")
        self.xy_pts = self.build_geom_list(self.xy_gdf)
        self._vor = Voronoi(self.xy_pts)

        self.point_map = self.build_ptr_map(self._vor)
        self.region_map = self.build_region_map(self._vor)
        self.buffered_points = self.build_point_buffer(self._vor)

        self.gen_intersections()
        self.output = self.gen_output()

    def build_geom_list(self, gdf):
        """Converts geometries to np array."""
        x_l = gdf.geometry.x.tolist()
        y_l = gdf.geometry.y.tolist()
        pts_l = [[x_l[i], y_l[i]] for i in range(len(x_l))]
        return np.array(pts_l)

    def build_ptr_map(self, vor):
        """Adds point coordinates and assigned regions to point dictionary."""
        point_map = {}
        for i, pt_coords in enumerate(vor.points):
            region_assigned = vor.point_region[i]

            point_map[i] = {
                'coords': pt_coords,
                'region_assigned': region_assigned}
        return point_map

    def build_region_map(self, vor):
        """Maps points to their polygon coordinates."""
        regions = {}

        # vor.regions contains a lisst of vertices for each region.
        # var.vertices contains a list of vertix coordinates.
        for i, vertices in enumerate(vor.regions):
            vtx_coords = [tuple(vor.vertices[v]) for v in vertices]
            regions[i] = {'vertices': vertices, 'vtx_coords': vtx_coords}

        return regions

    def build_point_buffer(self, vor):
        """Generates buffer surrounding x,y point."""
        for k, point in self.point_map.items():
            x = point['coords'][0]
            y = point['coords'][1]

            buff_point = Point(x, y).buffer(BUFFER_SIZE, resolution=BUFFER_RES)
            self.point_map[k]['buffer'] = buff_point

    def gen_intersections(self):
        """Generates intersections of partitions and buffer."""
        for k, pt in self.point_map.items():
            self.point_map[k]['boundary_coords'] = None
            r_idx = pt['region_assigned']
            r_poly = self.region_map[r_idx]['polygon']
            b_poly = self.point_map[k]['buffer']

            try:
                intsc = r_poly.intersection(b_poly)
                boundary = Polygon(intsc.boundary.coords[:])
                self.point_map[k]['boundary_shape'] = boundary
                self.point_map[k]['boundary_coords'] = boundary.exterior.coords[:]
            except Exception as e:
                print(k)
                pass

    def gen_output(self):
        """Main class driver, generates output file."""
        df = pd.DataFrame(self.point_map.values())
        df = df [['region_assigned', 'boundary_shape']]

        df2 = self.xy_gdf.reset_index(drop=True)
        df2 = df2[['umlid']]

        idx_merge = df2.join(df)

        gdf = gpd.GeoDataFrame(idx_merge,
                            geometry='boundary_shape',
                            crs={'init' :'epsg:3395'})

        # # Todo: Incomplete  geometries for mills. See issues with 
        # # intersections in shapely docs

        # filter missing or empty geometries
        s = gdf['boundary_shape']
        gdf = gdf[~(s.is_empty | s.isna())]

        gdf = gdf.to_crs("EPSG:4326")
        return gdf
