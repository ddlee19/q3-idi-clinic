import { AfterViewInit, Component, Input } from '@angular/core';
import * as CJS from 'chart.js'
import "chartjs-chart-box-and-violin-plot/build/Chart.BoxPlot.js";


@Component({
  selector: 'app-box-and-whisker-plot',
  templateUrl: './box-and-whisker-plot.component.html',
  styleUrls: ['./box-and-whisker-plot.component.css']
})
export class BoxAndWhiskerPlotComponent implements AfterViewInit {

  @Input() chartTitle: string;
  @Input() chartLabels: string[];
  @Input() boxPlotData: number[][];
  @Input() plotType: string;
  @Input() legendLabel: string;


    private initMap(){

    let canvasElement = <HTMLCanvasElement>document.getElementById("box-and-whisker");
    let ctx = canvasElement.getContext('2d');
    
    let data = {
      labels: this.chartLabels,
      datasets: [
        {
          label: this.legendLabel,
          backgroundColor: "rgba(210, 77, 87, 1)",
          borderColor: "rgba(210, 77, 87, 1)",
          borderWidth: 1,
          outlierColor: "red",
          padding: 5,
          itemRadius: 0,
          data: this.boxPlotData
        }
      ]
    };
  
    let chart = new CJS.Chart(ctx, {
        type: this.plotType,
        data: data,
        options: {
          responsive: true,
          legend: {
            position: "top"
          }
        }
    });
  }

  constructor() { }

  ngAfterViewInit(): void {
    this.initMap();
  }
}
