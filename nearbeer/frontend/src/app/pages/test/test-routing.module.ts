import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BeerPage } from '../beer/beer.page'
import { TestPage } from './test.page';

const routes: Routes = [
  { path: '', component: TestPage},
  { path: 'beer', component: BeerPage }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class TestPageRoutingModule {}
