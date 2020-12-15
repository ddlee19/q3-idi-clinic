import { BrandAggregateStatsComponent } from './components/brand-aggregate-stats/brand-aggregate-stats.component';
import { BrandComponent } from './components/brand/brand.component';
import { BrandReportComponent } from './components/brand-report/brand-report.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

/** The list of available URL routes in the app */
const routes: Routes = [
  { path: 'brands-report/:brand-id', component: BrandReportComponent },
  { path: 'brands-summary/:brand-id', component: BrandComponent },
  { path: 'brands-summary', component: BrandAggregateStatsComponent },
  { path: '**',   redirectTo: '/brands-summary', pathMatch: 'full' }
];

/** Handles in-app navigation */
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
