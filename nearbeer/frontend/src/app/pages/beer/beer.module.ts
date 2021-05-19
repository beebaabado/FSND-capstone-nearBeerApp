import { IonicModule } from '@ionic/angular';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { BeerPage } from './beer.page';
import { BeerCardComponentModule } from '../../components/beer-card/beer-card.module'
//import { ExploreContainerComponentModule } from '../explore-container/explore-container.module';
import { IonicSelectableModule } from 'ionic-selectable';
import { BeerRoutingModule } from './beer-routing.module';

@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    BeerCardComponentModule,
  //  ExploreContainerComponentModule,
    IonicSelectableModule,
    BeerRoutingModule,
   
  ],
  declarations: [BeerPage]
})
export class BeerPageModule {}
