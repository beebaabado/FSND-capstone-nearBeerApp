import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { PopoverController , IonRange} from '@ionic/angular';
import { BeerCardComponent} from '../../components/beer-card/beer-card.component';
import { DatePipe } from '@angular/common';
import { Beer } from '../../types/beer'
import { Router } from '@angular/router';

@Component({
  selector: 'app-test',
  templateUrl: './test.page.html',
  styleUrls: ['./test.page.scss'],
})
export class TestPage implements OnInit {
  
  rating: number = 0;
  selectedRating: number = 0.00;
  selectX:number = 0.00;
  @ViewChild('ratingRange') ratingRange: ElementRef;
  @ViewChild('x') x: IonRange;
  @ViewChild('ddd') ddd: ElementRef;
  constructor(public popoverController: PopoverController, private router: Router) {
   }

   ngOnInit() {
  }

  async presentPopover(ev: any) {

    var today = new Date();
    const formattedDate = this.formatDate(today);
    var beer = new Beer({
      "id":5,    
      "rating":4.5,
      "brewery": "WeldWerks",
      "name": "10K IPA: Unite Edition",
      "style": "IPA",
      "venue": "Under the Sun",
      "abv": 8.2,
      "last_seen": formattedDate
     });

    const popover = await this.popoverController.create({
      component: BeerCardComponent,
      componentProps: {
        "beer": beer
       },
      cssClass: 'my-custom-class',
      event: ev,
      translucent: true
    });
   
    await popover.present();
    
    const { role } = await popover.onDidDismiss();
    this.gotoBeerPage();
    console.log('onDidDismiss resolved with role', role);
  }
  

  selectedRatingChanged(event: {
    component: IonRange,
    value: any
  }) 
  {
    console.log(this.selectedRating);
  }
  
  

  presentFilterMenu(){
    
  }

   

  gotoBeerPage() {
    this.router.navigate(['/tabs/beer']);
  }
  
  formatDate(date: Date) {
    var datepipe = new DatePipe("en-US");
    return datepipe.transform(date, 'mediumDate')
  }

//   initBeerCard() {
//     var today = new Date();
//     const formattedDate = this.formatDate(today);

//     this.beer.setValues({
//      "id":5,    
//      "rating":4.5,
//      "brewery": "WeldWerks",
//      "name": "10K IPA: Unite Edition",
//      "style": "IPA",
//      "venue": "Under the Sun",
//      "abv": 8.2,
//      "last_seen": formattedDate
//     });
//  } 

}
