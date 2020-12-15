import { Brand } from '../interfaces/brands/brand.interface';
import { BrandAggregateStats } from '../interfaces/brands/brand-agg-stats.interface';
import { DetailedBrand } from '../interfaces/brands/brand-detailed.interface';
import { environment } from 'src/environments/environment';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MillFeatureCollection } from '../interfaces/mill.interface';
import { Observable } from 'rxjs';

/**
 * Provides access to an API endpoint serving palm oil mill and consumer brand 
 * data. The API base URL is set using an environmental variable.
*/
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  /** The base API url */
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

  /** Constructs a new instance of the ApiService */
  constructor(private http: HttpClient) { }
}
