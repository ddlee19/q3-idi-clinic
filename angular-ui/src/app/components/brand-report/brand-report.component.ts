import { Component, OnInit } from '@angular/core';
import { ParamMap, ActivatedRoute, Router } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import { DetailedBrand } from '../../interfaces/brands/brand-detailed.interface';
import { ApiService } from '../../services/api.service';


/** A component for a detailed/report view of a consumer brand. */
@Component({
  selector: 'app-brand-report',
  templateUrl: './brand-report.component.html',
  styleUrls: ['./brand-report.component.css']
})
export class BrandReportComponent implements OnInit {

  /** A reference to the brand */
  brand: DetailedBrand;

  /** Data used to build the plot (i.e., an array of datasets) */
  boxPlotData: number[][] = [];

  /** The title of the box-and-whisker plot */
  boxPlotTitle: string = "Distribution of Current Risk Score of Mills";
  
  /** Labels to distinguish between different box-and-whisker plot datasets */
  boxPlotLabels: string[] = ["Current Risk Score"];

  /** The legend label used for all datasets */
  boxPlotLegendLabel: string = "Current Risk Score";

  /** 
   * The orientation of the box-and-whisker plot. Choices include "boxplot",
   * which creates a vertical plot, or "horizontalBoxplot."  
   */
  boxPlotType: string = "horizontalBoxplot";

  /** The title of the line chart */
  lineChartTitle: string = "Average Tree Cover Loss Per Mill Since 2001";

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
      this.boxPlotData.push(Array.from(this.brand.mills, mill => mill.risk_score_current))
    })
  }

  /**
   * Navigates to a section of the brand report.
   * 
   * @param section: the section name
   */
  public navigateToSection(section: string) {
    window.location.hash = '';
    window.location.hash = section;
  }
  
 /**
 * Closes the report view for the selected brand by navigating back to
 * the selected brand summary card.
 */
  closeBrand(): void {
    this.router.navigate([`/brands-summary/${this.brand.brandid}`]);
  }
  
  /**
   * The class constructor
   * 
   * @param apiService: An injected instance of the ApiService
   * @param route: An injected instance of the ActivatedRoute
   * @param router: An injected instance of the Angular Router
   */
  constructor(
    private apiService: ApiService,
    private route: ActivatedRoute,
    private router: Router) {}

 /** 
   * Calls the ApiService to retrieve the brand specified in the URL
   * when Angular begins initializing the component view.
   */
  ngOnInit(): void {
    this.getBrand();
  }
}
