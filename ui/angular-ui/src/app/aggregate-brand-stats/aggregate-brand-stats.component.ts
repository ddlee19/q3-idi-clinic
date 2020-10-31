import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service'
import { AggregateBrandStats } from '../interfaces/brand-stats.interface'


@Component({
  selector: 'app-aggregate-brand-stats',
  templateUrl: './aggregate-brand-stats.component.html',
  styleUrls: ['./aggregate-brand-stats.component.css']
})
export class AggregateBrandStatsComponent implements OnInit {

  aggBrandStats: AggregateBrandStats;

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
