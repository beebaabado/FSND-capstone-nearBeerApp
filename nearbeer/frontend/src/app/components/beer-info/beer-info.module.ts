import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BeerInfoComponent } from './beer-info.component'
import { FormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';

@NgModule({
  declarations: [BeerInfoComponent,],
  imports: [
    CommonModule,
    IonicModule,
    FormsModule,
  ],
  exports: [
    BeerInfoComponent,
  ],  
})
export class BeerInfoComponentModule { }
