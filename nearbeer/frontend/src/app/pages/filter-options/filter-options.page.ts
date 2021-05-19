import { Component, OnInit } from '@angular/core';
import { IonRange} from '@ionic/angular';
import { Router } from '@angular/router';
import { NavparamService } from 'src/app/services/navparam.service';

@Component({
  selector: 'app-filter-options',
  templateUrl: './filter-options.page.html',
  styleUrls: ['./filter-options.page.scss'],
})
export class FilterOptionsPage implements OnInit {

  selectedRating:number = 0.00;
  
  data: any;

  constructor(
    private navParamService: NavparamService,
    private router: Router,
    ) { }

  ionViewWillEnter() {
    // Use data service to get data passed from another page
    this.data = this.navParamService.getNavData("listByVenues");
    console.log("Passed data:", this.data);
  }

  ngOnInit() {
  }

  goBack() {
    this.router.navigate(['/tabs/beers']);
  }
  
  selectedRatingChanged(event: {
    component: IonRange,
    value: any
  }) 
  {
    console.log(this.selectedRating);
  }
  
  applyFilters(){
    alert("TODO Apply search filters.");
  }
}
