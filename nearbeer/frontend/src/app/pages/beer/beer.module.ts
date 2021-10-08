import { IonicModule } from '@ionic/angular';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { BeerPage } from './beer.page';
import { BeerInfoComponentModule } from '../../components/beer-info/beer-info.module'
//import { ExploreContainerComponentModule } from '../explore-container/explore-container.module';
import { IonicSelectableModule } from 'ionic-selectable';
import { BeerRoutingModule } from './beer-routing.module';

@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    BeerInfoComponentModule,
  //  ExploreContainerComponentModule,
    IonicSelectableModule,
    BeerRoutingModule,
   
  ],
  //schemas: [ CUSTOM_ELEMENTS_SCHEMA ],
  declarations: [BeerPage]
})
export class BeerPageModule {}
