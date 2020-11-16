import { Distribution } from './stats-distribution.interface';

/**
 * Reports both current and historical statistics for aggregate
 * tree cover area and loss.
 * 
 * Example: "Total hectares of tree cover loss in 2001 by a consumer brand"
*/
export interface TreeCoverAggregateStats {

    /** Hectares of forest area. */    
    forest_area: number;

    /** Hectares of land area. */    
    land_area: number;

    /** Portion of forest remaining. */    
    remaining_proportion_of_forest: number;

    /** The current risk score. */    
    risk_score_current: number;

    /** The future risk score. */    
    risk_score_future: number;

    /** The past risk score. */    
    risk_score_past: Distribution;

    /** Hectares of tree cover loss in 2001. */
    treeloss_2001: Distribution;

    /** Hectares of tree cover loss in 2002. */
    treeloss_2002: Distribution;

    /** Hectares of tree cover loss in 2003. */
    treeloss_2003: Distribution;

    /** Hectares of tree cover loss in 2004. */
    treeloss_2004: Distribution;

    /** Hectares of tree cover loss in 2005. */
    treeloss_2005: Distribution;

    /** Hectares of tree cover loss in 2006. */
    treeloss_2006: Distribution;

    /** Hectares of tree cover loss in 2007. */
    treeloss_2007: Distribution;

    /** Hectares of tree cover loss in 2008. */
    treeloss_2008: Distribution;

    /** Hectares of tree cover loss in 2009. */ 
    treeloss_2009: Distribution;

    /** Hectares of tree cover loss in 2010. */
    treeloss_2010: Distribution;

    /** Hectares of tree cover loss in 2011. */ 
    treeloss_2011: Distribution;

    /** Hectares of tree cover loss in 2012. */
    treeloss_2012: Distribution;

    /** Hectares of tree cover loss in 2013. */
    treeloss_2013: Distribution;

    /** Hectares of tree cover loss in 2014. */
    treeloss_2014: Distribution;

    /** Hectares of tree cover loss in 2015. */ 
    treeloss_2015: Distribution;

    /** Hectares of tree cover loss in 2016 */
    treeloss_2016: Distribution;

    /** Hectares of tree cover loss in 2017 */
    treeloss_2017: Distribution;

    /** Hectares of tree cover loss in 2018. */
    treeloss_2018: Distribution;

    /** Hectares of tree cover loss in 2019. */
    treeloss_2019: Distribution;

    /** Total hectares of tree cover lost from 2001 to the present. */
    treeloss_sum: Distribution;

    /** Portion of tree cover remaining relative to total forest area. */
    treeloss_sum_proportion_of_forest: number;

    /** Portion of tree cover remaining relative to total land area. */
    treeloss_sum_proportion_of_land: number;
}