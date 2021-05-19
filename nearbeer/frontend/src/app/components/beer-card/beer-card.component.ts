import { Component, OnInit, ViewChild, ElementRef} from '@angular/core';
import { NavParams } from '@ionic/angular'
import { Beer } from '../../types/beer'

@Component({
  selector: 'app-beer-card',
  templateUrl: './beer-card.component.html',
  styleUrls: ['./beer-card.component.scss'],
})
export class BeerCardComponent implements OnInit {

  beer = new Beer();
  beerItem: any;
  hideCard = false;

  //@ViewChild('beerCard', {static: false}) card:  IonCard;
  constructor(public navParams: NavParams) { 
    console.log ("Beer Card Constructor: ");
    this.beer = this.navParams.get("beer");
  };

  ngOnInit() {}

  display() {
    this.hideCard = false;
  }
  
}
