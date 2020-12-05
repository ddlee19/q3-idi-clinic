import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service'
import { BrandAggregateStats } from '../../interfaces/brands/brand-agg-stats.interface'


@Component({
  selector: 'app-brand-aggregate-stats',
  templateUrl: './brand-aggregate-stats.component.html',
  styleUrls: ['./brand-aggregate-stats.component.css']
})
export class BrandAggregateStatsComponent implements OnInit {

  aggBrandStats: BrandAggregateStats;
  lineChartTitle: string = "Average Tree Cover Loss Per Mill Per Brand Since 2001";
  boxPlotTitle: string = "Distribution of Mills Per Brand"
  boxPlotData: number[][] = [];
  boxPlotLabels: string[] = ["RSPO-Cert", "Non-RSPO", "Total Num of Mills"];
  plotType: string = 'boxplot';
  legendLabel: string = 'RSPO-Certification Status'

  /**
  * Gets aggregate consumer brand data from the server.
  */
  private async getAggregateBrandData(): Promise<void> {
    this.aggBrandStats = await this.apiService.getBrandAggregateStats();

    // Temp variables to hold data of class variables
    var numRSPOMills_ = [];
    var numNonRSPOMills_ = [];
    var numMills_ = [];

    for(let i=0; i<this.aggBrandStats.brands.length; i++) {

      numRSPOMills_.push(this.aggBrandStats.brands[i].rspo_mill_count)
      numNonRSPOMills_.push(this.aggBrandStats.brands[i].nonrspo_mill_count)
      numMills_.push(this.aggBrandStats.brands[i].mill_count)
    }

    this.boxPlotData.push(numRSPOMills_)
    this.boxPlotData.push(numNonRSPOMills_)
    this.boxPlotData.push(numMills_)
  }

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.getAggregateBrandData();
  }
}
