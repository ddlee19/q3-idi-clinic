import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BrandAggregateStatsComponent } from './components/brand-aggregate-stats/brand-aggregate-stats.component';
import { BrandComponent } from './components/brand/brand.component';


const routes: Routes = [
  { path: 'brands-summary/:brand-id', component: BrandComponent },
  { path: 'brands-summary', component: BrandAggregateStatsComponent },
  { path: '**',   redirectTo: '/brands-summary', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
