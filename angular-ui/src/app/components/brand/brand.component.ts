import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service'
import { DetailedBrand } from '../../interfaces/brands/brand-detailed.interface';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-brand',
  templateUrl: './brand.component.html',
  styleUrls: ['./brand.component.css']
})
export class BrandComponent implements OnInit {

  brand: DetailedBrand;

  /**
  * Parses a consumer brand id from the URL and then retrieves the
  * corresponding brand from the API server to display in the UI.
  */
 private async getBrand(): Promise<void> {
  this.route.paramMap.pipe(
    switchMap((params: ParamMap) => {
      let id = params.get("brand-id");
      return this.apiService.getBrand(id);
    }))
    .subscribe(brand => {
      this.brand = brand;
    })
  }


 /**
 * Closes the summary card for the selected brand by navigating back to
 * the main brands summary card.
 */
 closeBrand(): void {
    this.router.navigate(['/brands-summary']);
  }
  

  /** Constructs a new instance of an individual brand summary card*/
  constructor(
    private apiService: ApiService,
    private route: ActivatedRoute,
    private router: Router) {}

  ngOnInit(): void { 
    this.getBrand();
  }
}
