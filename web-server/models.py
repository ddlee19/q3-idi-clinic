from dataclasses import dataclass
from typing import List

@dataclass
class Distribution:
    '''
    Measures of order and central tendency for a given entity such
    as a mill, region, or brand.
    
    Example: The min, max, average, and median number of mills per brand.
    '''
    min_count: int
    max_count: int
    avg_count: int
    median_count: int


@dataclass
class RiskScores:
    '''
    Measures of past, current, and future risk for deforestation.
    '''
    current: int
    future: int
    past: int


# Note: Waiting to implement forest clearance metrics and projected losses
@dataclass
class TreeCoverStats:
    '''
    Statistics and data regarding tree cover loss over time for a specified
    entity such as a mill, region, brand.  Areas are given in hectacres.
    
    Example Statistic:
        The percentage of forest remaining within a mill's 50km area.
    '''
    land_area: float
    forest_area: float
    total_treeloss: float
    treeloss_per_land_area: float
    treeloss_per_forest_area: float
    remaining_treecover_forest: float
    years: List[int]
    loss_per_year: List[float]
    percent_cleared: float = None
    projected_loss: float = None
    projected_clearance_rate: float = None
    clearance_rates_per_year: List[int] = None

    @classmethod
    def from_df_row(cls, row):
        brand_short_attrs = ["id", "name", "country", "rspo_member_since"]
        return cls(**row[brand_short_attrs].to_dict())



@dataclass
class BrandShort:
    '''
    An abbreviated representation of a brand
    '''
    id: int
    name: str
    country: str
    rspo_member_since: str
    mill_count: int
    mill_count_rspo: int
    mill_count_non_rspo: int

    @classmethod
    def from_df_row(cls, row):
        brand_short_attrs = ["id", "name", "country", "rspo_member_since"]
        return cls(**row[brand_short_attrs].to_dict())


class MillShort:
    '''
    An abbreviated version of a mill.
    '''
    def __init__(self, mill_row):
        self.id = mill_row["id"]
        self.name = mill_row["name"]
        self.country = mill_row["country"]
        self.state = mill_row["state"]
        self.sub_state = mill_row["sub_state"]
        self.rspo_certification = mill_row["rspo_certification"]
        self.risk_scores = RiskScores(
            mill_row["risk_score_current"],
            mill_row["risk_score_future"],
            mill_row["risk_score_past"]
        )


@dataclass
class Brand:
    '''
    A representation of a consumer brand (e.g., General Mills, Inc.), defined
    as a retailer or consumer goods manufacturer.
    '''
    id: int
    name: str
    country: str
    description: str
    rspo_member_since: str
    external_link: str
    treecover_stats: TreeCoverStats
    mills: List[MillShort]


@dataclass
class BrandStats:
    '''
    A collection of brands and computed statistics on those brands
    '''
    brands: List[BrandShort]
    mill_distribution: Distribution
    treecover_stats_all: TreeCoverStats
    treecover_stats_rspo: TreeCoverStats
    treecover_stats_non_rspo: TreeCoverStats
    region_distribution: Distribution = None
    supplier_distribution: Distribution = None


@dataclass
class Mill:
    '''
    A palm oil mill.
    '''
    id: int
    name: str
    latitude: float
    longitude: float
    country: str
    state: str
    sub_state: str
    address_confidence: str
    group_name: str
    supplier_name: str
    rspo_certification: str
    risk_scores: RiskScores
    treecover_stats: TreeCoverStats
    brands: List[BrandShort]
    radius: object


@dataclass
class MillStats:
    '''
    A collection of mills and computed statistics on those mills
    '''
    brands: List[MillShort]
    brand_distribution: Distribution
    treecover_stats_all: TreeCoverStats
    treecover_stats_rspo: TreeCoverStats
    treecover_stats_non_rspo: TreeCoverStats
    supplier_distribution: Distribution = None