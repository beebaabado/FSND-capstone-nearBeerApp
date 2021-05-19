import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { FilterOptionsPage } from './filter-options.page';

const routes: Routes = [
  {
    path: '',
    component: FilterOptionsPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class FilterOptionsPageRoutingModule {}
