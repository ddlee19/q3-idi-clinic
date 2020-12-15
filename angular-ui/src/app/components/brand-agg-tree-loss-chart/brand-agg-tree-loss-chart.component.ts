import { AfterViewInit, Component, Input } from '@angular/core';
import { TreeCoverAverageStats } from 'src/app/interfaces/stats/stats-treecover-avg.interface';
import * as CJS from 'chart.js'

/** A component to represent a consumer brand aggregate tree loss line chart. */
@Component({
  selector: 'app-brand-agg-tree-loss-chart',
  templateUrl: './brand-agg-tree-loss-chart.component.html',
  styleUrls: ['./brand-agg-tree-loss-chart.component.css']
})
export class BrandAggTreeLossChartComponent implements AfterViewInit {

  /** The data source */
  @Input() treeCoverStats: TreeCoverAverageStats;

  /** The chart title */
  @Input() chartTitle: string;

  /** 
   * Creates a new line chart.
  */
  private plot(): void {
    let years = Array.from(new Array(19), (x, i) => i + 2001);

    let meanLosses = [];
    meanLosses.push(this.treeCoverStats.treeloss_2001.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2002.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2003.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2004.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2005.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2006.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2007.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2008.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2009.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2010.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2011.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2012.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2013.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2014.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2015.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2016.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2017.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2018.mean);
    meanLosses.push(this.treeCoverStats.treeloss_2019.mean);

    let canvasElement = <HTMLCanvasElement>document.getElementById('agg-brand-tree-loss');
    let ctx = canvasElement.getContext('2d');
    let chart = new CJS.Chart(ctx, {
      type: 'line',
      data: {
          labels: years,
          datasets: [{
              label: 'Loss in Hectares',
              backgroundColor: 'rgb(255, 99, 132)',
              borderColor: 'rgb(255, 99, 132)',
              data: meanLosses
          }]
      },
      options: {}
    });
  }

  /** The class constructor. */
  constructor() { }

   /** 
   * Creates a new plot after Angular has finished initializing
   * the component view.
   */
  ngAfterViewInit(): void {
    this.plot();
  }
}
