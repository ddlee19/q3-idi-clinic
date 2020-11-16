/**
 * A representation of a consumer brand.
 */
export interface Brand {

    /** The brand/company name. */
    brand: string;

    /** The unique identifier for the brand. */
    brandid: number;

    /** The country where the brand is headquartered. */
    country: string;

    /** The number of mills affiliated with the brand. */
    mill_count: number;

    /** The number of non-RSPO certified mills affiliated with the brand. */
    nonrspo_mill_count: number;

    /** The brand's current risk score. */
    risk_score_current: number;

    /** The brand's future risk score. */
    risk_score_future: number;

    /** The brand's past risk score. */
    risk_score_past: number;

    /** The number of RSPO-certified mills affiliated with the brand. */
    rspo_mill_count: number;
}