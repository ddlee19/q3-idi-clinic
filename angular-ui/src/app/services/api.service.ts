import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TileUrl } from '../interfaces/tile-urls.interface';
import { Mill } from '../interfaces/mill.interface';
import { BrandAggregateStats } from '../interfaces/brand-stats.interface';
import { BrandFilter } from '../interfaces/brand-filter.interface';
import { Brand } from '../interfaces/brand.interface';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiBase = "http://localhost:5000/api/v1.0/"

  /** GET tile urls from the server */
  getTileUrls(): Promise<TileUrl[]> {
    return this.http.get<TileUrl[]>(this.apiBase + "tile-urls").toPromise();
  }

  /** GET mill data from the server */
  getMills(): Promise<Mill[]> {
      return this.http.get<Mill[]>(this.apiBase + "mills").toPromise();
  }

  /** GET aggregate consumer brand statistics from the server */
  getAggregateBrandData(): Promise<BrandAggregateStats> {
      return this.http.get<BrandAggregateStats>(this.apiBase + "brands/stats").toPromise();
  }

  /** GET brand filter choices from the server */
  getBrandFilters(): Promise<BrandFilter[]> {
    return this.http.get<BrandFilter[]>(this.apiBase + "brands").toPromise();
  }

  /** GET consumer brand from the server by id */
  getConsumerBrand(brandId: number): Promise<Brand> {
    return this.http.get<Brand>(this.apiBase + "brands/" + brandId).toPromise();
  }

  constructor(private http: HttpClient) { }
}
