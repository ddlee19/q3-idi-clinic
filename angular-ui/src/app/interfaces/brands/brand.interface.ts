import { TreeCoverStats } from '../stats/stats-treecover.interface';

/**
 * A representation of a consumer brand.
 */
export interface Brand {

    /** The country where the brand is headquartered. */
    country: string;

    /** The number of countries from which the brand sources mills' palm oil. */
    num_countries_of_operation: string;

    /** The unique identifier for the brand. */
    id: number;

    /** The number of mills affiliated with the brand. */
    mill_count: number;

    /** The number of non-RSPO certified mills affiliated with the brand. */
    mill_count_non_rspo: number;

    /** The number of RSPO-certified mills affiliated with the brand. */
    mill_count_rspo: number;

    /** The brand/company name. */
    name: string;

    /** The average of the brand mills' future risk scores. */
    risk_score_future_mean: number;

    /** The date that the brand became an RSPO member, if applicable. */
    rspo_member_since: string;

    /** Tree cover statistics for brand's mills. */
    stats: TreeCoverStats;
}