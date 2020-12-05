import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MillFeatureCollection } from '../interfaces/mill.interface';
import { BrandAggregateStats } from '../interfaces/brands/brand-agg-stats.interface';
import { Brand } from '../interfaces/brands/brand.interface';
import { DetailedBrand } from '../interfaces/brands/brand-detailed.interface';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';

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
  getBrand(brandName: string): Observable<DetailedBrand> {
    return this.http.get<DetailedBrand>(this.apiBase + "brands/" + brandName);
  }

  /** GET a list of consumer brands from the server */
  getBrands(): Promise<Brand[]> {
    return this.http.get<Brand[]>(this.apiBase + "brands").toPromise();
  }

  /** GET mill data from the server */
  getMills(): Promise<MillFeatureCollection> {
      return this.http.get<MillFeatureCollection>(this.apiBase + "mills").toPromise();
  }

  constructor(private http: HttpClient) { }
}
