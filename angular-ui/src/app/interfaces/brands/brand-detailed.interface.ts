import { Brand } from "./brand.interface"
import { MillProperties } from "../mill.interface"
import { Supplier } from '../supplier.interface'
import { TreeCoverAggregateStats } from '../stats/stats-treecover-agg.interface'
import { TreeCoverAverageStats } from '../stats/stats-treecover-avg.interface'

/**
 * A detailed representation of a single consumer brand.
*/
export interface DetailedBrand extends Brand {

    /** 
     * Statistics for treecover loss at the brand level. To derive these
     * statistics, all mills associated with the brand had their geometries
     * dissolved into one multipolygon (otherwise the geometries significantly
     * overlapped). Then tree cover area and loss over time was computed within
     * that multipolygon.
    */
    agg_stats: TreeCoverAggregateStats;

    /** 
     * Tree cover statistics for the brand's mills. Unlike 'agg_stats', these
     * statistics are computed by taking the average, median, max, etc. of the
     * brands' mills individual tree cover losses and areas.
    */
    avg_stats: TreeCoverAverageStats;

    /** The number of countries from which the brand sources mills' palm oil. */
    country_count: string;

    /** Information about the brand's services and history. */
    description: string;

    /** A link to the brand's website. */
    externalLink: string;

    /** The list of mills associated with the brand. */
    mills: MillProperties[];

    /** The date that the brand became an RSPO member, if applicable. */
    rspo_member_since: string;

    /** The list of suppliers/mill parent companies associated with the brand. */
    suppliers: Supplier[];
}