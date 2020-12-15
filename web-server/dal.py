# DAL.py
#
# The data access layer (DAL) for CSV and JSON files generated by the batch
# layer. Loads files into Pandas DataFrames and then queries those DataFrames
# to return dictionaries of data for the Flask API to JSONify. Please see
# the sample payloads provided under the web-server directory and the GitHub
# API documentation for more details.
##

import os

import pandas as pd
import geopandas as gpd
from shapely import wkt
from attr_collections import *


class DAL:

    def __init__(self, input_path):
        '''
        The constructor for the DAL class. Loads data files for processing and
        fills in missing values to prevent DataFrame operation errors.

        Parameters:
            None

        Returns:
            (DAL): a new instance of the class
        '''
        p = input_path
        self._brands = pd.read_csv(os.path.join(p, "uniquebrands.csv"))
        self._brand_mills_full = pd.read_csv(os.path.join(p, "brands.csv"))
        self._brand_mills_thin = pd.read_csv(os.path.join(p, 
                                                        "brand_mills.csv"))
        self._mills = pd.read_csv(os.path.join(p, "uniquemills.csv"))\
                        .query("geometry == geometry")

        ids = list(self._brand_mills_thin.umlid)
        self._mills_with_brands = self._mills.query("umlid in @ids")

        self._mills.rspo_model.fillna("", inplace=True)
        self._brand_mills_full.rspo_model.fillna("", inplace=True)


    def get_brand(self, brand_id):
        '''
        Retrieves a detailed version of a single brand by id.

        Parameters:
            brand_id (int): the unique identifier for the brand

        Returns:
            (dict): a dictionary representing the brand
        '''
        brand = self._brands.query("brandid == @brand_id")
        mills = self.get_mills_for_brand(brand_id)
        suppliers = self.get_suppliers_for_mills(mills)

        payload = brand[BRAND_ATTRS].to_dict(orient="records")[0]
        payload["agg_stats"] = brand[AGG_TREECOVER_STATS].to_dict(orient="records")[0]
        payload["avg_stats"] = self.summarize_mills(mills)[MILL_SUMMARY_ATTRS].to_dict()
        payload["country_count"] = len(mills.country.unique())
        payload["supplier_count"] = len(suppliers)
        payload["mills"] = mills[MILLSHORT_ATTRS].to_dict(orient="records")
        payload["suppliers"] = suppliers.to_dict(orient="records")

        return payload


    def get_brands(self, uml_id=None):
        '''
        Retrieves a list of brands in a shortened/abbreviated form. By default
        all brands are returned, but when a valid UML mill id is provided,
        the result set is filtered to include only those brands associated with
        the UML mill.

        Parameters:
            uml_id (str): the UML id. Defaults to None.

        Returns:
            (dict): a dictionary representing the brands
        '''
        if self.is_valid_uml_mill(uml_id):
            # Valid UML id provided
            brand_names = self._brand_mills_full.query("umlid == @uml_id").brand.tolist()
            chosen_brands = self._brands.query("brand in @brand_names")

        elif not uml_id:
            # No UML id provided
            chosen_brands = self._brands

        else:
            # Invalid UML id provided
            return []

        risk_scores = (self._mills_with_brands[["umlid", "risk_score_current"]]
                        .set_index("umlid"))

        avg_risk_scores = (self._brand_mills_thin[["brandid", "umlid"]]
                                .join(risk_scores, on="umlid")
                                .groupby("brandid")
                                .mean()
                                .risk_score_current
                                .round(3)
                                .to_frame()
                                .rename(columns={"risk_score_current": "avg_risk_score_current"}))

        return (chosen_brands[BRANDSHORT_ATTRS]
                .join(avg_risk_scores, on="brandid")
                .sort_values("avg_risk_score_current", ascending=False)
                .to_dict(orient="records"))


    def get_brands_aggregate_stats(self):
        '''
        Retrieves statistics computed across *all* consumer brands.

        Parameters:
            None

        Returns:
            (dict): a dictionary representing brand aggregate info
        '''
        summary_df = self.get_mills_treecover_stats_for_brands()

        payload = {}
        payload["brands"] = self.get_brands()
        payload["avg_hectares_lost_per_brand"] = int(self._brands["treeloss_sum"].mean())
        payload["dist_of_brand_avgs_for_treecover"] = summary_df.to_dict()
        payload["mill_dist_all"] = self.get_mill_dist_for_brands()
        payload["mill_dist_non_rspo"] = self.get_mill_dist_for_brands(rspo_filter="non-rspo")  
        payload["mill_dist_rspo"] = self.get_mill_dist_for_brands(rspo_filter="rspo")        
        payload["total_num_countries"] = len(self._mills_with_brands["country"].unique())
        payload["total_num_mills"] = len(self._mills["umlid"].unique())
        payload["total_num_mills_with_brands"] = len(self._mills_with_brands["umlid"].unique())
        payload["total_num_suppliers"] = len(self._mills_with_brands["prnt_comp"].unique())

        return payload


    def get_brands_dist_for_mills(self):
        '''
        Calculates the min, max, mean, standard deviation, and lower, middle, 
        and upper quartiles of brands per mill.

        Parameters:
            None

        Returns:
            (dict): a dictionary containing the descriptive statistics above
        '''
        mill_brand_names = (self._brand_mills_full[["umlid", "brand"]]
                                .set_index("umlid"))

        mill_brands = (self._mills
                        .join(mill_brand_names, on="umlid")
                        .groupby("umlid")
                        .agg({"brand":lambda b: len(list(b))}))

        mill_brands.columns = ["brand_count"]

        brands_per_mill_df = (mill_brands["brand_count"]
                                .describe()
                                .to_frame()
                                .transpose()
                                .iloc[0])

        return {
            "max": int(brands_per_mill_df["max"]),
            "mean": brands_per_mill_df["mean"],
            "min": int(brands_per_mill_df["min"]),
            "quartile_1": int(brands_per_mill_df["25%"]),
            "quartile_2": int(brands_per_mill_df["50%"]),
            "quartile_3": int(brands_per_mill_df["75%"]),
            "std": brands_per_mill_df["std"]
        }


    def get_mill(self, uml_id):
        '''
        Retrieves a detailed represenation of a UML mill by id

        Parameters:
            uml_id (str): the UML id

        Returns:
            (dict): a dictionary representing the brands
        '''
        chosen_mill = self._mills.query("umlid == @uml_id")
        payload = chosen_mill[MILL_ATTRS].to_dict(orient="records")[0]
        payload["brands"] = self.get_brands(uml_id)

        return payload


    def get_mills(self):
        '''
        Creates a GeoJSON FeatureCollection holding all mills from the UML.

        Parameters:
            None

        Returns:
            (str): A serialized GeoJSON FeatureCollection representing the mills
        '''
        mill_brand_ids = (self._brand_mills_thin[["umlid", "brandid"]]
                            .set_index("umlid"))

        brand_ids_list_func = lambda b: list(b.astype(int)) if b.any() else []

        mill_brands = (self._mills
                        .join(mill_brand_ids, on="umlid")
                        .groupby("umlid")
                        .agg({"brandid": brand_ids_list_func}))
                        
        mill_brands.columns = ["brand_ids"]

        mills = self._mills.join(mill_brands, on="umlid")[MILL_ATTRS + ["brand_ids"]]
        
        gdf = gpd.GeoDataFrame(mills)
        gdf["geometry"] = gdf["geometry"].apply(wkt.loads)
        gdf.set_geometry("geometry")
        return gdf.to_json()


    def get_mills_for_brand(self, brand_id):
        '''
        Retrieves the UML mills for a given brand.

        Parameters:
            brand_id (int): the brand id

        Returns:
            (pd.DataFrame): the mills
        '''
        ids = list(self._brand_mills_thin.query("brandid == @brand_id").umlid)
        mills = (self._mills
                    .query("umlid in @ids")
                    .sort_values(by="risk_score_current", ascending=False))

        return mills
        

    def get_mills_aggregate_stats(self):
        '''
        Retrieves summary statistics computed across all UML mills.

        Parameters:
            None

        Returns:
            (dict): a dictionary contaiing the mill summary information.
        '''
        summary_df = self.summarize_mills(self._mills)
        payload = {}
        payload["avg_stats"] = summary_df[MILL_SUMMARY_ATTRS].to_dict()
        payload["brand_dist"] = self.get_brands_dist_for_mills()
        payload["total_num_mills"] = len(self._mills["umlid"].unique())

        return payload


    def get_mill_dist_for_brands(self, rspo_filter=None):
        '''
        Calculates the min, max, mean, standard deviation, and lower, middle, 
        and upper quartiles of mills per brand, optionally by the mills'
        RSPO certification status (i.e., "rspo" or "non-rspo" only).

        Parameters:
            rspo_filter (str): Optional parameter indicating the RSPO
                               certification status to filter by ("rspo" or
                               "non-rspo"). Defaults to None.

        Returns:
            (dict): a dictionary containing the descriptive statistics above

        '''
        if rspo_filter == "rspo":
            mills = self._brand_mills_full.query("rspo_model != ''")
        elif rspo_filter == "non-rspo":
            mills = self._brand_mills_full.query("rspo_model == ''")
        else:
            mills = self._brand_mills_full

        mills_per_brand_df = mills.brand.value_counts().to_frame()
        mills_per_brand_df.columns = ["mill_count"]
        mill_dist_stats = mills_per_brand_df.describe().transpose().iloc[0]

        return {
            "max": int(mill_dist_stats["max"]),
            "mean": mill_dist_stats["mean"],
            "min": int(mill_dist_stats["min"]),
            "quartile_1": int(mill_dist_stats["25%"]),
            "quartile_2": int(mill_dist_stats["50%"]),
            "quartile_3": int(mill_dist_stats["75%"]),
            "std": mill_dist_stats["std"]
        }


    def get_mills_treecover_stats_for_brands(self):
        '''
        Generates statistics for the mean, median, max, min, and standard
        deviation of treecover properties across consumer brands' mills.

        Parameters:
            None

        Returns:
            (pd.DataFrame): a DataFrame showing the above descriptive statistics
        '''
        mills = self._mills_with_brands.set_index("umlid")[MILL_SUMMARY_ATTRS]
        brand_mill_stats = self._brand_mills_full.join(mills, on="umlid")
        brand_mill_stats.drop("brandid", axis=1, inplace=True)

        summary_df = brand_mill_stats.groupby("brand").mean().describe()
        summary_df.drop(["count"], axis=0, inplace=True)
        summary_df.rename(index=DISTRIBUTION_ATTR_MAP, inplace=True)

        return summary_df


    def get_suppliers_for_mills(self, mills):
        '''
        Retrieves a shortened/abbreviated version of the suppliers
        associated with a list of mills.

        Parameters:
            mills (pd.DataFrame): a DataFrame containing mill information

        Returns:
            (pd.DataFrame): a DataFrame holding the mills' suppliers (also 
                            known as parent companies)
        '''
        suppliers = (mills[["country", "prnt_comp"]]
                        .query("prnt_comp != 'unknown'")
                        .drop_duplicates()
                        .sort_values(by=["country", "prnt_comp"])
                        .rename(columns={"prnt_comp": "name"}))

        supplier_mill_counts = (mills["prnt_comp"]
                                    .value_counts()
                                    .to_frame()
                                    .rename(columns={
                                        "prnt_comp" : "mill_count"
                                    }))

        suppliers = (suppliers
                        .join(supplier_mill_counts, on="name")
                        .sort_values(by="mill_count", ascending=False))

        return suppliers


    def is_valid_brand(self, brand_id):
        '''
        Returns a boolean indicating whether the given brand exists.

        Parameters:
            brand_id (int): the unique identifier for a brand

        Returns:
            (bool): the boolean
        '''
        return brand_id in list(self._brands.brandid)


    def is_valid_uml_mill(self, uml_id):
        '''
        Returns a boolean indicating whether the given UML mill exists.
    
        Parameters:
            uml_id (str): the UML id

        Returns:
            (bool): the boolean
        '''
        return uml_id in list(self._mills.umlid)

    
    def summarize_mills(self, mills):
        '''
        Retrieves summary statistics for a given list of mills.

        Parameters:
            mills (pd.DataFrame): a DataFrame containing mill information

        Returns:
            (pd.DataFrame): a DataFrame contaiing the mill summary information
        '''
        mill_summary = mills.select_dtypes(include=['float64', 'int64']).describe()
        mill_summary.drop("count", axis=0, inplace=True)
        mill_summary.rename(index=DISTRIBUTION_ATTR_MAP, inplace=True)

        return mill_summary
