import { NgModule,CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BeerCardComponent } from './beer-card.component'

@NgModule({
  declarations: [BeerCardComponent,],
  imports: [
    CommonModule,
  ],
  exports: [
    BeerCardComponent,
  ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ]
})
export class BeerCardComponentModule { }
