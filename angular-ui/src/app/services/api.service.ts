import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TileUrl } from '../interfaces/tile-urls.interface';
import { MillFeatureCollection } from '../interfaces/mill.interface';
import { BrandAggregateStats } from '../interfaces/brands/brand-agg-stats.interface';
import { Brand } from '../interfaces/brands/brand.interface';
import { DetailedBrand } from '../interfaces/brands/brand-detailed.interface';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiBase: string = environment.apiBase

  /** GET aggregate consumer brand statistics from the server */
  getBrandAggregateStats(): Promise<BrandAggregateStats> {
      return this.http.get<BrandAggregateStats>(this.apiBase + "brands/stats").toPromise();
  }

  /** GET a consumer brand from the server by id */
  getBrand(brandName: string): Promise<DetailedBrand> {
    return this.http.get<DetailedBrand>(this.apiBase + "brands/" + brandName).toPromise();
  }

  /** GET a list of consumer brands from the server */
  getBrands(): Promise<Brand[]> {
    return this.http.get<Brand[]>(this.apiBase + "brands").toPromise();
  }

  /** GET mill data from the server */
  getMills(): Promise<MillFeatureCollection> {
      return this.http.get<MillFeatureCollection>(this.apiBase + "mills").toPromise();
  }

  /** GET tile urls from the server */
  getTileUrls(): Promise<TileUrl[]> {
    return this.http.get<TileUrl[]>(this.apiBase + "tile-urls").toPromise();
  }

  constructor(private http: HttpClient) { }
}
