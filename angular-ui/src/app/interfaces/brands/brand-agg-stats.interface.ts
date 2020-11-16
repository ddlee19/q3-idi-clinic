import { Brand } from './brand.interface';
import { Distribution } from '../stats/stats-distribution.interface';
import { TreeCoverAverageStats } from '../stats/stats-treecover-avg.interface';

/**
 * Reports statistics calculated across all consumer brands.
*/
export interface BrandAggregateStats {

    /** The average number of hectares lost per brand */
    avg_hectares_lost_per_brand: number;

    /** A list of all brands in the supply chain */
    brands: Brand[];

    /** 
     * Computes average tree cover loss (or gain or forest remaining, etc.) per
     * mill for each brand and then records the distribution of those averages.
    */
    dist_of_brand_avgs_for_treecover: TreeCoverAverageStats;

    /** The mean, median, etc. number of mills per brand */
    mill_dist_all: Distribution;

    /** The mean, median, etc. number of non-RSPO certified mills per brand */ 
    mill_dist_non_rspo: Distribution;

    /** The mean, median, etc. number of RSPO-certified mills per brand */
    mill_dist_rspo: Distribution;

    /** The total number of palm-oil producing countries in the supply chain */
    total_num_countries: number;

    /** The total number of UML mills */
    total_num_mills: number;

    /** The total number of UML mills affiliated with consumer brands */
    total_num_mills_with_brands: number;

    /** The total number of suppliers/mill parent companies in the supply chain */
    total_num_suppliers: number;
}