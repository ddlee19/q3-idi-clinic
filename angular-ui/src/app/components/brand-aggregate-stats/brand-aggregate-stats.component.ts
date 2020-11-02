import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service'
import { BrandAggregateStats } from '../../interfaces/brand-stats.interface'


@Component({
  selector: 'app-brand-aggregate-stats',
  templateUrl: './brand-aggregate-stats.component.html',
  styleUrls: ['./brand-aggregate-stats.component.css']
})
export class BrandAggregateStatsComponent implements OnInit {

  aggBrandStats: BrandAggregateStats;

  /**
  * Gets aggregate consumer brand data from the server.
  */
  private async getAggregateBrandData(): Promise<void> {
    this.aggBrandStats = await this.apiService.getAggregateBrandData();
  }

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.getAggregateBrandData();
  }
}
