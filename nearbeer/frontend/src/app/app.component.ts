import { Component } from '@angular/core';
import { Plugins } from '@capacitor/core';
const { SplashScreen } = Plugins;

SplashScreen.hide();

  SplashScreen.show({
     autoHide: false
  });
  
  SplashScreen.show({
    showDuration: 5000,
    autoHide: true
  });


@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  constructor() {};
}
