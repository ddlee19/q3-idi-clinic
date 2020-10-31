import { Mill } from "./mill.interface"
import { Supplier } from './supplier.interface';

/**
 * A detailed representation of a single consumer brand.
*/
export interface Brand {
    id: string;
    name: string;
    country: string;
    description: string;
    externalLink: string;
    suppliers: Supplier[];
    weightedAvgScore: number;
    mills: Mill[];
}