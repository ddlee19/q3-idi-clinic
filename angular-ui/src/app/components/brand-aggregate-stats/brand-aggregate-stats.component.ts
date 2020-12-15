import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service'
import { BrandAggregateStats } from '../../interfaces/brands/brand-agg-stats.interface'


/** A component for a view of aggregate brand statistics. */
@Component({
  selector: 'app-brand-aggregate-stats',
  templateUrl: './brand-aggregate-stats.component.html',
  styleUrls: ['./brand-aggregate-stats.component.css']
})
export class BrandAggregateStatsComponent implements OnInit {

  /** A reference to the BrandAggregateStats instance */
  aggBrandStats: BrandAggregateStats;

  /** Data used to build the box-and-whisker plot (i.e., an array of datasets)*/
  boxPlotData: number[][] = [];

  /** Labels to distinguish between different box-and-whisker plot datasets */
  boxPlotLabels: string[] = ["RSPO-Cert", "Non-RSPO", "Total Num of Mills"];

  /** The title of the box-and-whisker plot */
  boxPlotTitle: string = "Distribution of Mills Per Brand"

  /** The legend label used for all box-and-whisker plot datasets */
  boxPlotLegendLabel: string = 'RSPO-Certification Status'

  /** The title of the line chart */
  lineChartTitle: string = "Average Tree Cover Loss Per Mill Per Brand Since 2001";
  
 /** 
   * The orientation of the box-and-whisker plot. Choices include "boxplot",
   * which creates a vertical plot, or "horizontalBoxplot."  
   */
  boxPlotType: string = 'boxplot';

  /**
  * Gets aggregate consumer brand data from the server.
  */
  private async getAggregateBrandData(): Promise<void> {
    this.aggBrandStats = await this.apiService.getBrandAggregateStats();

    // Temp variables to hold data from class variables
    var numRSPOMills_ = [];
    var numNonRSPOMills_ = [];
    var numMills_ = [];

    for(let i = 0; i < this.aggBrandStats.brands.length; i++) {

      numRSPOMills_.push(this.aggBrandStats.brands[i].rspo_mill_count)
      numNonRSPOMills_.push(this.aggBrandStats.brands[i].nonrspo_mill_count)
      numMills_.push(this.aggBrandStats.brands[i].mill_count)
    }

    this.boxPlotData.push(numRSPOMills_)
    this.boxPlotData.push(numNonRSPOMills_)
    this.boxPlotData.push(numMills_)
  }

  /**
   * The class constructor
   * 
   * @param apiService: An injected instance of the ApiService
   */
  constructor(private apiService: ApiService) {}

 /** 
   * Calls the ApiService to retrieve aggregate brand statistics
   * when Angular begins initializing the component view.
   */
  ngOnInit(): void {
    this.getAggregateBrandData();
  }
}
