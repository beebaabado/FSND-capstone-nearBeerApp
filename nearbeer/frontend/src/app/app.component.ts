import { Component } from '@angular/core';
import { Plugins } from '@capacitor/core';
const { SplashScreen } = Plugins;
import { AuthService } from './services/auth.service';
import { Platform } from '@ionic/angular';

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
  constructor(
    private auth: AuthService,
    private platform: Platform
  ) {
    this.initializeApp();
  };

  initializeApp() {
    this.platform.ready().then(() => {
      // Perform required auth actions
      this.auth.load_jwts();
      this.auth.check_token_fragment();
    });
  }
}
