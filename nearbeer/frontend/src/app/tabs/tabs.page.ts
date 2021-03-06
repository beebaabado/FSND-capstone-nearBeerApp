import { Component } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-tabs',
  templateUrl: 'tabs.page.html',
  styleUrls: ['tabs.page.scss']
})
export class TabsPage {

  constructor(public auth: AuthService) {}

  ngOnInit() {
    try {
       this.auth.getUserName();
    }
    catch(err){
      console.log(err);
    } 
  }

}
