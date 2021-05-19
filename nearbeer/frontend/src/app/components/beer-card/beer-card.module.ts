import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BeerCardComponent } from './beer-card.component'

@NgModule({
  declarations: [BeerCardComponent,],
  imports: [
    CommonModule,
  ],
  exports: [
    BeerCardComponent,
  ]
})
export class BeerCardComponentModule { }
