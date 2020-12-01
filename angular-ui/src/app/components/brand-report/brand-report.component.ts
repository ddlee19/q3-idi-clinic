import { Component, OnInit } from '@angular/core';
import { ParamMap, ActivatedRoute, Router } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import { DetailedBrand } from 'src/app/interfaces/brands/brand-detailed.interface';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-brand-report',
  templateUrl: './brand-report.component.html',
  styleUrls: ['./brand-report.component.css']
})
export class BrandReportComponent implements OnInit {

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
 * Closes the report view for the selected brand by navigating back to
 * the selected brand summary card.
 */
 closeBrand(): void {
    this.router.navigate([`/brands-summary/${this.brand.brandid}`]);
  }
  
  /** Constructs a new instance of an individual brand summary card */
  constructor(
    private apiService: ApiService,
    private route: ActivatedRoute,
    private router: Router) {}


  ngOnInit(): void {
    this.getBrand();
  }
}
