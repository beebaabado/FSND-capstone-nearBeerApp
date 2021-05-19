import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { FilterOptionsPageRoutingModule } from './filter-options-routing.module';

import { FilterOptionsPage } from './filter-options.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    FilterOptionsPageRoutingModule
  ],
  declarations: [FilterOptionsPage]
})
export class FilterOptionsPageModule {}
