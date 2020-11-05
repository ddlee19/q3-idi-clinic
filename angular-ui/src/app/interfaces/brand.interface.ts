import { Mill } from "./mill.interface"

/**
 * A detailed representation of a single consumer brand.
*/
export interface Brand {
    country: string;
    description: string;
    externalLink: string;
    id: string;
    mills: Mill[];
    name: string;
    rspo_member_since: string;
}