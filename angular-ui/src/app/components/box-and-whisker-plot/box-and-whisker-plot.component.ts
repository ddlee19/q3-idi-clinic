import { AfterViewInit, Component, Input } from '@angular/core';
import * as CJS from 'chart.js'
import "chartjs-chart-box-and-violin-plot/build/Chart.BoxPlot.js";


/** A component for a general box-and-whisker plot. */
@Component({
  selector: 'app-box-and-whisker-plot',
  templateUrl: './box-and-whisker-plot.component.html',
  styleUrls: ['./box-and-whisker-plot.component.css']
})
export class BoxAndWhiskerPlotComponent implements AfterViewInit {
  
  /** Data used to build the plot (i.e., an array of datasets) */
  @Input() boxPlotData: number[][];

  /** Labels to distinguish between different box-and-whisker plot datasets */
  @Input() boxPlotLabels: string[];

  /** The title of the box-and-whisker plot */
  @Input() boxPlotTitle: string;

  /** The legend label used for all datasets */
  @Input() boxPlotLegendLabel: string;

  /** 
   * The orientation of the box-and-whisker plot. Choices include "boxplot",
   * which creates a vertical plot, or "horizontalBoxplot."  
   */
  @Input() boxPlotType: string;

  /** 
   * Creates a new box-and-whisker plot. 
   */
  private plot(){
    
    // Get plot canvas element from the DOM
    let plotHtmlId = "box-and-whisker"
    let canvasElement = <HTMLCanvasElement>document.getElementById(plotHtmlId);
    let ctx = canvasElement.getContext('2d');
    
    // Set data for plot
    let data = {
      labels: this.boxPlotLabels,
      datasets: [
        {
          label: this.boxPlotLegendLabel,
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

  // Instantiate plot
  let chart = new CJS.Chart(ctx, {
      type: this.boxPlotType,
      data: data,
      options: {
        responsive: true,
        legend: {
          position: "top"
        }
      }
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
