/**
 * Represents a GeoJSON feature collection of palm oil mills.
*/
export interface MillFeatureCollection {

    /** The list of mill features in the feature collection. */
    features: Mill[];

    /** The GeoJSON data type, here a "FeatureCollection." */
    type: string;
}

/**
 * Represents a palm oil mill GeoJSON feature.
*/
export interface Mill {
    
    /** The GeoJSON geometry for the circular area surrounding the mill. */
    geometry: object;

    /** The umlid, the unique identifier for the mill provided by the Universal Mill List (UML).*/
    id: string;

    /** The mill feature properties. */
    properties: MillProperties;

    /** The GeoJSON data type, here a "Feature." */
    type: string;
}

/**
 * The properties associated with a palm oil mill.
*/
export interface MillProperties {

    /** The names of all consumer brands associated with the mill. */
    brand: string[];

    /** The country in which the mill is located. */
    country: string;

    /** The mill's latitude. */
    latitude: number;

    /** The country in which the mill is located. */
    longitude: number;

    /** The name of the mill's company. */   
    mill_co: string;

    /** The mill name. */
    mill_name: string;

    /** The country in which the mill is located. */
    parent_co: string;

    /** The mill's current deforestation risk (1-5). A score of 1 is lowest risk while 5 is highest. */
    risk_score_current: number;

    /** The mill's projected deforestation risk (1-5). A score of 1 is lowest risk while 5 is highest. */
    risk_score_future: number;

    /** The mill's past deforestation risk (1-5). A score of 1 is lowest risk while 5 is highest. */
    risk_score_past: number;

    /** The mill's RSPO-certification type, if applicable. */
    rspo: string;

    /** The state in which the mill is located. */
    state: string;

    /** The sub-state in which the mill is located. */
    sub_state: string;

    /** The unique identifier for the mill provided by the Universal Mill List (UML). */
    umlid: string;
}