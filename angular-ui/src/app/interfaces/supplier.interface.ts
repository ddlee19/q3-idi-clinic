/**
 * A detailed representation of a palm oil supplier/parent company.
*/
export interface Supplier {

    /** The country in which the supplier is based. */
    country: string;

    /** The name of the supplier. */
    name: string;

    /** The number of mills managed by the supplier. */
    mill_count: number;
}