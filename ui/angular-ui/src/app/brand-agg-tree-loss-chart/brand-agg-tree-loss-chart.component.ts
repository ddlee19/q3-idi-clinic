import { AfterViewInit, Component, Input } from '@angular/core';
import * as CJS from 'chart.js'

@Component({
  selector: 'app-brand-agg-tree-loss-chart',
  templateUrl: './brand-agg-tree-loss-chart.component.html',
  styleUrls: ['./brand-agg-tree-loss-chart.component.css']
})
export class BrandAggTreeLossChartComponent implements AfterViewInit {
  @Input() totalTreeLossByYear: object;

  private initMap(): void {
    let canvasElement = <HTMLCanvasElement>document.getElementById('agg-brand-tree-loss')
    let ctx = canvasElement.getContext('2d');
    let chart = new CJS.Chart(ctx, {
      type: 'line',
      data: {
          labels: Object.keys(this.totalTreeLossByYear),
          datasets: [{
              label: 'Tree Cover Loss Since 2002',
              backgroundColor: 'rgb(255, 99, 132)',
              borderColor: 'rgb(255, 99, 132)',
              data: Object.values(this.totalTreeLossByYear)
          }]
      },
      options: {}
    });
  }

  constructor() { }

  ngAfterViewInit(): void {
    this.initMap()
  }
}
