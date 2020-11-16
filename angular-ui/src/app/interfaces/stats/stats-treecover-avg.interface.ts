import { Distribution } from './stats-distribution.interface';

/**
 * Reports both current and historical statistics for tree cover area and loss.

 * Example: "Average hectares of tree cover loss per mill for a 
             consumer brand in 2001"
*/
export interface TreeCoverAverageStats {

    /** Summary statistics for forest area. */    
    forest_area: Distribution;

    /** Summary statistics for land area. */    
    land_area: Distribution;

    /** Summary statistics for the portion of forest remaining. */    
    remaining_proportion_of_forest: Distribution;

    /** Summary statistics for current risk score. */    
    risk_score_current: Distribution;

    /** Summary statistics for future risk score. */    
    risk_score_future: Distribution;

    /** Summary statistics for past risk score. */    
    risk_score_past: Distribution;

    /** Summary statistics for tree cover loss in 2001. */
    treeloss_2001: Distribution;

    /** Summary statistics for tree cover loss in 2002. */
    treeloss_2002: Distribution;

    /** Summary statistics for tree cover loss in 2003. */
    treeloss_2003: Distribution;

    /** Summary statistics for tree cover loss in 2004. */
    treeloss_2004: Distribution;

    /** Summary statistics for tree cover loss in 2005. */
    treeloss_2005: Distribution;

    /** Summary statistics for tree cover loss in 2006. */
    treeloss_2006: Distribution;

    /** Summary statistics for tree cover loss in 2007. */
    treeloss_2007: Distribution;

    /** Summary statistics for tree cover loss in 2008. */
    treeloss_2008: Distribution;

    /** Summary statistics for tree cover loss in 2009. */ 
    treeloss_2009: Distribution;

    /** Summary statistics for tree cover loss in 2010. */
    treeloss_2010: Distribution;

    /** Summary statistics for tree cover loss in 2011. */ 
    treeloss_2011: Distribution;

    /** Summary statistics for tree cover loss in 2012. */
    treeloss_2012: Distribution;

    /** Summary statistics for tree cover loss in 2013. */
    treeloss_2013: Distribution;

    /** Summary statistics for tree cover loss in 2014. */
    treeloss_2014: Distribution;

    /** Summary statistics for tree cover loss in 2015. */ 
    treeloss_2015: Distribution;

    /** Summary statistics for tree cover loss in 2016 */
    treeloss_2016: Distribution;

    /** Summary statistics for tree cover loss in 2017 */
    treeloss_2017: Distribution;

    /** Summary statistics for tree cover loss in 2018. */
    treeloss_2018: Distribution;

    /** Summary statistics for tree cover loss in 2019. */
    treeloss_2019: Distribution;

    /** Summary statistics for hectacres of tree cover lost since 2001. */
    treeloss_sum: Distribution;

    /** Summary statistics for tree cover remaining relative to total forest area. */
    treeloss_sum_proportion_of_forest: Distribution;

    /** Summary statistics for tree cover remaining relative to total land area. */
    treeloss_sum_proportion_of_land: Distribution;
}