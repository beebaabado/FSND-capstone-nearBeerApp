import { Component, OnInit } from '@angular/core';
import { IonDatetime } from '@ionic/angular';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  loginURL: string;
  firstLogin: boolean = false;

  constructor(public auth: AuthService) {
   this.user_login();
  }
  
  ngOnInit() {
    console.log("loginPage:ngInit");
    if (this.auth.isExpired()){
       this.firstLogin= true;
    }
  }
  user_login() {
    this.loginURL = this.auth.build_login_link('/tabs/login');
    this.auth.getExpiredTime();
    console.log("LoginPage:logingURL: ", this.loginURL);
  }
  
  /* 
   ionViewWillEnter() {
     
    // messing around with user login behavior when token is expired.
    // 
    console.log("loginPage:ionViewWillEnter");
    // logs out user if token is expired and prompts user for relogin
    if (this.firstLogin){
      this.user_login();
      this.firstLogin = false;
    }
    else if (this.auth.isExpired()) {
        this.user_login();
      }
  }
 */

}