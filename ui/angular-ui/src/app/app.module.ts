import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { MapComponent } from './map/map.component';
import { NavComponent } from './nav/nav.component';
import { AggregateBrandStatsComponent } from './aggregate-brand-stats/aggregate-brand-stats.component';
import { BrandAggTreeLossChartComponent } from './brand-agg-tree-loss-chart/brand-agg-tree-loss-chart.component';
import { BrandFilterComponent } from './brand-filter/brand-filter.component';
import { BrandComponent } from './brand/brand.component';

@NgModule({
  declarations: [
    AppComponent,
    MapComponent,
    NavComponent,
    AggregateBrandStatsComponent,
    BrandAggTreeLossChartComponent,
    BrandFilterComponent,
    BrandComponent
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
