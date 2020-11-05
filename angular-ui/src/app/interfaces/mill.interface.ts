/**
 * A detailed represenation of a palm oil mill. 
*/
export interface Mill {
    properties: MillProperties;
    geometry: object;
    id: string;
    type: string;
}

/**
 * The properties associated with a mill.
*/
export interface MillProperties {
    brand: [string];
    country: string;
    district: string;
    latitude: number;
    longitude: number;
    objectid: number;
    mill_co: string;
    mill_name: string;
    parent_co: string;
    province: string;
    risk_score_current: number;
    risk_score_future: number;
    risk_score_past: number;
    rspo: string;
    umlid: string;
}