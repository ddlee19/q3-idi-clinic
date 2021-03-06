import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { MapComponent } from './components/map/map.component';
import { NavComponent } from './components/nav/nav.component';
import { BrandAggregateStatsComponent } from './components/brand-aggregate-stats/brand-aggregate-stats.component';
import { BrandAggTreeLossChartComponent } from './components/brand-agg-tree-loss-chart/brand-agg-tree-loss-chart.component';
import { BrandFilterComponent } from './components/brand-filter/brand-filter.component';
import { BrandComponent } from './components/brand/brand.component';
import { AboutComponent } from './components/about/about.component';
import { BrandReportComponent } from './components/brand-report/brand-report.component';
import { BoxAndWhiskerPlotComponent } from './components/box-and-whisker-plot/box-and-whisker-plot.component';

/** The root module */
@NgModule({
  declarations: [
    AppComponent,
    MapComponent,
    NavComponent,
    BrandAggregateStatsComponent,
    BrandAggTreeLossChartComponent,
    BrandFilterComponent,
    BrandComponent,
    AboutComponent,
    BrandReportComponent,
    BoxAndWhiskerPlotComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
