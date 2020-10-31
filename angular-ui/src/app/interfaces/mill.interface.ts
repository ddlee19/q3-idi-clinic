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
    objectid: number;
    mill_name: string;
    latitude: number;
    longitude: number;
    rspo_model: string;
    consumer_brand_id: number;
    relative_score: number;
    absolute_score: number;
    cert: string;
    id: string;
    prnt_comp: string;
    country: string;
    state: string;
    sub_state: string;
    alt_name: string;
    address: string;
    globalid: string;
    Group_Name: string;
}