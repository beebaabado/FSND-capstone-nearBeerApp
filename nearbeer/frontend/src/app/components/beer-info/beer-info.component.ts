import { Component, OnInit } from '@angular/core';
import { PopoverController, } from '@ionic/angular';

@Component({
  selector: 'app-beer-info',
  templateUrl: './beer-info.component.html',
  styleUrls: ['./beer-info.component.scss'],
})
export class BeerInfoComponent implements OnInit {
  
  user_rating:string = "0.00";
  beer_id:string = "";
  
  constructor(private popoverController: PopoverController) { }

  ngOnInit() {
    console.log("Beer info component");
    console.log("Rating: ", this.user_rating);
    console.log("ID: ", this.beer_id);
  }

  // maybe update before dismissing ???
  setUserRatingEventTriggered(event: any) {
    console.log ("USER RATING: ", this.user_rating, this.beer_id);
  }
  
  onSave(){
    //need to validate input
    const result = {"user_rating": this.user_rating, "id":this.beer_id};
    this.popoverController.dismiss(result);
  }

  onCancel(){
    console.log("Popover cancel.");
    this.popoverController.dismiss();
  }    

}
