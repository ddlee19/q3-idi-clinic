import { Brand } from "./brand.interface"
import { MillProperties } from "../mill.interface"
import { Supplier } from '../supplier.interface'

/**
 * A detailed representation of a single consumer brand.
*/
export interface DetailedBrand extends Brand {

    /** Information about the brand's services and history. */
    description: string;

    /** A link to the brand's website. */
    externalLink: string;

    /** The list of mills associated with the brand. */
    mills: MillProperties[];

    /** The list of suppliers/mill parent companies associated with the brand. */
    suppliers: Supplier[];
}