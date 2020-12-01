import { AfterViewInit, Component } from '@angular/core';
import * as CJS from 'chart.js'
import "chartjs-chart-box-and-violin-plot/build/Chart.BoxPlot.js";

@Component({
  selector: 'app-box-and-whisker-plot',
  templateUrl: './box-and-whisker-plot.component.html',
  styleUrls: ['./box-and-whisker-plot.component.css']
})
export class BoxAndWhiskerPlotComponent implements AfterViewInit {

  // EXAMPLE FROM:
  // https://github.com/datavisyn/chartjs-chart-box-and-violin-plot
  randomValues(count, min, max) {
    const delta = max - min;
    return Array.from({ length: count }).map(() => Math.random() * delta + min);
  }

  private initMap(){

    let canvasElement = <HTMLCanvasElement>document.getElementById('box-and-whisker');
    let ctx = canvasElement.getContext('2d');

    let data = {
      labels: ["January", "February", "March", "April", "May", "June", "July"],
      datasets: [
        {
          label: "Dataset 1",
          backgroundColor: "rgba(255,0,0,0.5)",
          borderColor: "red",
          borderWidth: 1,
          outlierColor: "#999999",
          padding: 10,
          itemRadius: 0,
          data: [
            this.randomValues(100, 0, 100),
            this.randomValues(100, 0, 20),
            this.randomValues(100, 20, 70),
            this.randomValues(100, 60, 100),
            this.randomValues(40, 50, 100),
            this.randomValues(100, 60, 120),
            this.randomValues(100, 80, 100)
          ]
        },
        {
          label: "Dataset 2",
          backgroundColor: "rgba(0,0,255,0.5)",
          borderColor: "blue",
          borderWidth: 1,
          outlierColor: "#999999",
          padding: 10,
          itemRadius: 0,
          data: [
            this.randomValues(100, 60, 100),
            this.randomValues(100, 0, 100),
            this.randomValues(100, 0, 20),
            this.randomValues(100, 20, 70),
            this.randomValues(40, 60, 120),
            this.randomValues(100, 20, 100),
            this.randomValues(100, 80, 100)
          ]
        }
      ]
    };
  
    let chart = new CJS.Chart(ctx, {
        type: 'boxplot',
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
