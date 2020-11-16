# attr_collections.py
#
# Pandas DataFrame columns/attributes to select (or map to and from), 
# during the querying process.
##


AGG_TREECOVER_STATS = [
    "forest_area",
    "land_area",
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
    "treeloss_sum_proportion_of_land",
    "remaining_proportion_of_forest",
    "risk_score_current",
    "risk_score_future",
    "risk_score_past"
]

BRAND_ATTRS = [
    "brand",
    "brandid",
    "country",
    "description",
    "external_link",
    "mill_count",
    "nonrspo_mill_count",
    "rspo_member_since",
    "rspo_mill_count"   
]

BRANDSHORT_ATTRS = [
    "brand",
    "brandid",
    "country",
    "mill_count",
    "nonrspo_mill_count",
    "risk_score_current",
    "risk_score_future",
    "risk_score_past",
    "rspo_mill_count" 
]

DISTRIBUTION_ATTR_MAP = {
    "25%": "quartile_1",
    "50%": "quartile_2",
    "75%": "quartile_3",
    "max": "max",
    "mean": "mean",
    "min": "min",
    "std": "std"
}

MILL_ATTRS = [
    "address",
    "alt_name",
    "cert",
    "country",
    "forest_area",
    "geometry",
    "globalid",
    "group_name",
    "land_area",
    "latitude",
    "longitude",
    "mill_name",
    "prnt_comp",
    "remaining_proportion_of_forest",
    "risk_score_current",
    "risk_score_past",
    "risk_score_future",
    "rspo_model",
    "state",
    "sub_state",
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
    "treeloss_sum_proportion_of_land",
    "umlid"
]

MILLSHORT_ATTRS = [
    "country", 
    "mill_name",
    "prnt_comp", 
    "risk_score_current",
    "risk_score_past",
    "risk_score_future",
    "rspo_model",
    "state", 
    "sub_state", 
    "umlid"
]

MILL_SUMMARY_ATTRS = [
    "forest_area",
    "land_area",
    "remaining_proportion_of_forest",
    "risk_score_current",
    "risk_score_future",
    "risk_score_past",
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