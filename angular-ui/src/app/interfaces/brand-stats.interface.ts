import { BrandRank } from './brand-rank.interface';

/**
 * Reports statistics calculated across all consumer brands.
*/
export interface BrandAggregateStats {
    totalNumCountries: number;
    totalNumConsumerBrands: number;
    totalNumSuppliers: number;
    totalNumMills: number;
    netTreeLoss: number;
    totalTreeLossByYear: object;
    totalTreeGainByYear: object;
    topBrands: BrandRank[];
    bottomBrands: BrandRank[];
}