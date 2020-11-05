import pandas as pd

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
        "rspo_member_since"
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


    def __init__(self):
        self._mills = pd.read_csv("../sample_data/mills.csv")
        self._brands = pd.read_csv("../sample_data/brands.csv")
        self._uniquemills = pd.read_csv("../sample_data/uniquemills.csv")


    def get_aggregate_brand_stats(self):
        '''
        Retrieves statistics computed across *all* consumer brands.
        '''
        df = self._mills
        summary_df = df.select_dtypes(include=['float64']).describe()
        summary_df.drop('count', axis=0, inplace=True)
        payload = summary_df.to_dict(orient="records")

        return payload



    def get_aggregate_mill_stats(self):
        '''
        Retrieves statistics computed across *all* mills.
        '''
        df = self._uniquemills
        summary_df = df.select_dtypes(include=['float64']).describe()
        summary_df.drop('count', axis=0, inplace=True)
        summary_df.drop(columns=['latitude_x', 'latitude_y', 'longitude_x', 'longitude_y'], inplace=True)
        payload = summary_df.to_dict(orient="records")

        return payload


    def get_brand(self, brand_name):
        '''
        Retrieves a Brand entity by name.
        '''
        chosen_brand = self._brands.query("name == @brand_name")
        chosen_brand_mills = self._mills.query("brand == @brand_name")
        chosen_brand_mill_shorts = chosen_brand_mills[self.MILLSHORT_ATTRS]

        payload = chosen_brand[self.BRAND_ATTRS].to_dict(orient="records")[0]
        payload["mills"] = chosen_brand_mill_shorts.to_dict(orient="records")

        # Implementing this week:
        # payload["treecover_stats"] = {...}

        return payload


    def get_mill(self, mill_id):
        '''
        Retrieves a mill by its unique identifier.
        '''
        chosen_mill = self._mills.query("umlid == @mill_id")
        chosen_mill_brands = self._brands.query("name in @chosen_mill.brand")
        chosen_mill_brand_shorts = chosen_mill_brands[self.BRANDSHORT_ATTRS]

        payload = chosen_mill[self.MILL_ATTRS].to_dict(orient="records")[0]
        payload["brands"] = chosen_mill_brand_shorts.to_dict(orient="records")
        return payload


    def get_mills(self):
        '''
        Retrieves all mills.
        '''
        mill_brands = self._mills.groupby("umlid").agg({"brand":lambda b: list(b)})
        unique_mills = self._mills.drop_duplicates("umlid")[self.MILL_ATTRS]
        mills = unique_mills.join(mill_brands, on="umlid")

        mill_features = []
        for m in mills.to_dict(orient="records"):
            feature = {}
            feature["type"] = "Feature"
            feature["properties"] = m
            feature["geometry"] = m["geometry"]
            mill_features.append(feature)

        return mill_features


    def get_brand_shorts(self, mill_id=None):
        '''
        Retrieves a list of BrandShort entities, optionally by mill id.
        '''     
        if self.is_valid_mill_id(mill_id):
            brand_names = self._mills.query("umlid == @mill_id").brand.tolist()
            chosen_brands = self._brands.query("name in @brand_names")
        else:
            chosen_brands = self._brands

        return chosen_brands[self.BRANDSHORT_ATTRS].to_dict(orient="records")


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

