import pandas as pd
import geopandas as gpd
from shapely import wkt

class DataFactory:
    '''
    FIELDS TO SELECT FROM DATAFRAME
    '''
    BRAND_ATTRS = [
        "id",
        "name",
        "country",
        "description",
        "rspo_member_since",
        "external_link"
    ]

    BRANDSHORT_ATTRS = [
        "id",
        "name",
        "country",
        "rspo_member_since",
        "mill_count",
        "mill_count_rspo",
        "mill_count_non_rspo",
        "risk_score_future_mean"
    ]

    MILL_ATTRS = [
        "umlid", 
        "mill_name",
        "latitude",
        "longitude",
        "country", 
        "province", 
        "district",
        "mill_co",
        "parent_co",
        "rspo", 
        "risk_score_current",
        "risk_score_past",
        "risk_score_future",
        "geometry"
    ]

    MILLSHORT_ATTRS = [
        "umlid", 
        "mill_name", 
        "country", 
        "province", 
        "district", 
        "rspo", 
        "risk_score_current",
        "risk_score_past",
        "risk_score_future"
    ]

    MILL_SUMMARY_ATTRS = [
        "forest_area",
        "land_area",
        "remaining_proportion_of_forest",
        "treeloss_2001",
        "treeloss_2002",
        "treeloss_2003",
        "treeloss_2004",
        "treeloss_2005",
        "treeloss_2006",
        "treeloss_2007",
        "treeloss_2008",
        "treeloss_2009",
        "treeloss_2010",
        "treeloss_2011",
        "treeloss_2012",
        "treeloss_2013",
        "treeloss_2014",
        "treeloss_2015",
        "treeloss_2016",
        "treeloss_2017",
        "treeloss_2018",
        "treeloss_2019",
        "treeloss_sum",
        "treeloss_sum_proportion_of_forest",
        "treeloss_sum_proportion_of_land"
    ]

    DISTRIBUTION_ATTRS = [
        "quartile_1",
        "quartile_2",
        "quartile_3",
        "max",
        "mean",
        "min",
        "std"
    ]

    def __init__(self):
        self._mills = pd.read_csv("../sample_data/mills.csv")
        self._brands = pd.read_csv("../sample_data/brands.csv")
        self._uniquemills = pd.read_csv("../sample_data/uniquemills.csv")


    def get_aggregate_brand_stats(self):
        '''
        Retrieves statistics computed across *all* consumer brands.
        '''
        summary_df = self._mills.groupby("brand").mean().describe()
        summary_df.drop('count', axis=0, inplace=True)
        index_map = dict(zip(list(summary_df.index), self.DISTRIBUTION_ATTRS))
        summary_df.rename(index=index_map, inplace=True)

        payload = {}
        payload["brands"] = self.get_brands()
        payload["dist_of_brand_avgs_for_treecover"] = summary_df[self.MILL_SUMMARY_ATTRS].to_dict()
        payload["mill_dist_all"] = self.get_mill_dist_for_brands()
        payload["mill_dist_rspo"] = self.get_mill_dist_for_brands(rspo_filter="rspo")
        payload["mill_dist_non_rspo"] = self.get_mill_dist_for_brands(rspo_filter="non-rspo")
        payload["total_num_countries"] = len(self._mills["country"].unique())
        payload["total_num_mills"] = len(self._mills["umlid"].unique())
        payload["total_num_suppliers"] = len(self._mills["parent_co"].unique())

        return payload


    def get_aggregate_mill_stats(self):
        '''
        Retrieves statistics computed across *all* mills.
        '''
        # summary_df = self._mills.select_dtypes(include=['float64']).describe()
        # summary_df.drop('count', axis=0, inplace=True)
        # index_map = dict(zip(list(summary_df.index), self.DISTRIBUTION_ATTRS))
        # summary_df.rename(index=index_map, inplace=True)

        df = self._uniquemills
        summary_df = df.select_dtypes(include=['float64']).describe()
        summary_df.drop('count', axis=0, inplace=True)
        summary_df.drop(columns=['latitude_x', 'latitude_y', 'longitude_x', 'longitude_y'], inplace=True)
        payload = summary_df.to_dict()

        return payload


    def get_brand(self, brand_name):
        '''
        Retrieves a Brand entity by name.
        '''
        chosen_brand = self._brands.query("name == @brand_name")
        chosen_brand_mills = self._mills.query("brand == @brand_name")

        payload = chosen_brand[self.BRAND_ATTRS].to_dict(orient="records")[0]
        payload["mills"] = chosen_brand_mills[self.MILLSHORT_ATTRS].to_dict(orient="records")

        mill_summary = chosen_brand_mills.select_dtypes(include=['float64']).describe()
        mill_summary.drop("count", axis=0, inplace=True)
        payload["stats"] = mill_summary[self.MILL_SUMMARY_ATTRS].to_dict()

        return payload


    def get_brands(self, mill_id=None, sort_col=None):
        '''
        Retrieves a list of BrandShort entities, optionally by mill id.
        '''     
        if self.is_valid_mill_id(mill_id):
            brand_names = self._mills.query("umlid == @mill_id").brand.tolist()
            chosen_brands = self._brands.query("name in @brand_names")
        else:
            chosen_brands = self._brands

        mills_per_brand = self._mills.brand.value_counts().to_frame()
        mills_per_brand.columns = ["mill_count"]
        chosen_brands = chosen_brands.join(mills_per_brand, on="name")

        rspo_mill_ct = self._mills[["brand", "rspo"]].groupby("brand").count()
        rspo_mill_ct.columns = ["mill_count_rspo"]
        chosen_brands = chosen_brands.join(rspo_mill_ct, on="name")
        chosen_brands["mill_count_non_rspo"] = (
            chosen_brands["mill_count"] - chosen_brands["mill_count_rspo"]
        )

        brand_scores = (self._mills.groupby("brand")["risk_score_future"]
                            .mean()
                            .round(2)
                            .to_frame())
        brand_scores.columns = ["risk_score_future_mean"]
        chosen_brands = (chosen_brands
                            .join(brand_scores, on="name")
                            .sort_values("risk_score_future_mean", ascending=False))

        return chosen_brands[self.BRANDSHORT_ATTRS].to_dict(orient="records")


    def get_mill(self, mill_id):
        '''
        Retrieves a mill by its unique identifier.
        '''
        chosen_mill = self._mills.query("umlid == @mill_id").iloc[0]
        payload = chosen_mill[self.MILL_ATTRS].to_dict()
        payload["brands"] = self.get_brands(mill_id)

        return payload


    def get_mill_dist_for_brands(self, rspo_filter=None):
        '''
        Calculates the min, max, mean, median, and total number of mills
        across all brands, optionally by the mills' RSPO certification status.
        '''
        if rspo_filter == "rspo":
            mills = self._mills.query("rspo == rspo") # RSPO-certified mills
        elif rspo_filter == "non-rspo":
            mills = self._mills.query("rspo != rspo") # Non-RSPO-certified mills
        else:
            mills = self._mills

        mills_per_brand_df = mills.brand.value_counts().to_frame()
        mills_per_brand_df.columns = ["mill_count"]
        mill_dist_stats = mills_per_brand_df.describe().transpose().iloc[0]

        return {
            "max": int(mill_dist_stats["max"]),
            "mean": int(mill_dist_stats["mean"]),
            "min": int(mill_dist_stats["min"]),
            "quartile_1": int(mill_dist_stats["25%"]),
            "quartile_2": int(mill_dist_stats["50%"]),
            "quartile_3": int(mill_dist_stats["75%"]),
            "std": int(mill_dist_stats["std"])
        }


    def get_mills(self):
        '''
        Retrieves all mills.
        '''
        mill_brands = self._mills.groupby("umlid").agg({"brand":lambda b: list(b)})
        #unique_mills = self._mills.drop_duplicates("umlid")[self.MILL_ATTRS]
        mills = self._uniquemills.join(mill_brands, on="umlid")
        
        gdf = gpd.GeoDataFrame(mills)
        gdf["geometry"] = gdf["geometry"].apply(wkt.loads)
        gdf.set_geometry("geometry")
        return gdf.to_json()


    def is_valid_brand_name(self, brand_name):
        '''
        Returns a boolean indicating whether the given brand name is valid
        '''
        return brand_name in list(self._brands.name)


    def is_valid_mill_id(self, mill_id):
        '''
        Returns a boolean indicating whether the given mill id is valid
        '''
        return mill_id in list(self._mills.umlid)
