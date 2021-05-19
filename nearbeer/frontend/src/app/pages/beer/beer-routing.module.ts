import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BeerPage } from './beer.page';
import { FilterOptionsPage } from '../filter-options/filter-options.page';

const routes: Routes = [
  { path: '', component: BeerPage},
  { path: 'filter-options', component: FilterOptionsPage},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BeerRoutingModule {}
