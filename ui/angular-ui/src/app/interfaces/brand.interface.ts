import { Mill } from "./mill.interface"

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

export interface Supplier {
    id: string;
    name: string;
    country: string;
}