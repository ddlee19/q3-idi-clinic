/**
 *  Summary statistics for a data distribution.
*/
export interface Distribution {

    /** The maximum */
    max: number;

    /** The mean/average */
    mean: number;

    /** The minimum */
    min: number;

    /** The first/lower quartile */
    quartile_1: number;

    /** The second/middle quartile (i.e., the median) */
    quartile_2: number;

    /** The third/upper quartile */
    quartile_3: number;

    /** The standard deviation */
    std: number;
}