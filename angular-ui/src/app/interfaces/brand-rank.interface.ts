/**
 * Summarizes comparative statistics and rank for a consumer brand.
 */
export interface BrandRank {
    brandId: number,
    name: string,
    country: string,
    category: string,
    absoluteScore: number,
    totalHectaresLost: number
}