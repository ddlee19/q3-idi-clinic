import { Mill } from "../mill.interface"
import { Brand } from "./brand.interface"

/**
 * A detailed representation of a single consumer brand.
*/
export interface DetailedBrand extends Brand {

    /** Information about the brand's services and history */
    description: string;

    /** A link to the brand's website */
    externalLink: string;

    /** The list of mills belonging to the brand */
    mills: Mill[];
}