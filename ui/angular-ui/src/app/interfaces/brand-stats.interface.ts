export interface AggregateBrandStats {
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

export interface BrandRank {
    brandId: number,
    name: string,
    country: string,
    category: string,
    absoluteScore: number,
    totalHectaresLost: number
}