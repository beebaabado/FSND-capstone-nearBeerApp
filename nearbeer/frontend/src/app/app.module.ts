import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';
import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
//import { JwtModule} from "@auth0/angular-jwt"
import { UntappdServerService } from './services/untappd-server.service';
import { StorageService } from './services/storage.service';
import { ComponentsModule } from  './components/components.module';
import { IonicSelectableModule } from 'ionic-selectable';
import { IonicStorageModule} from '@ionic/storage-angular';  // angular has its own lib...other will use @ionic/storage
import { NavparamService } from './services/navparam.service'
import { NativeGeocoder } from '@ionic-native/native-geocoder/ngx';
import { JwtHelperService, JWT_OPTIONS} from '@auth0/angular-jwt';
//import { AgmCoreModule } from '@agm/core';

// export function tokenGetter() {
//   return localStorage.getItem("access_token");
// }

@NgModule({
  declarations: [AppComponent],
  entryComponents: [],
  imports: [BrowserModule, 
            ComponentsModule,
            IonicModule.forRoot(), 
            AppRoutingModule,
            HttpClientModule,
            IonicSelectableModule,
            IonicStorageModule.forRoot(),  
            //AgmCoreModule.forRoot({
            //  apiKey: 'AIzaSyCMUHnMfIZCOCJDg1I4yqFW8cc2s0BOQjg',
            //  libraries: ['places']
           // })
          //  JwtModule.forRoot({
          //    config:{
          //      tokenGetter: tokenGetter,
          //      allowedDomains: ["127.0.0.1:5000"],
          //      disallowedRoutes: [],
          //    },
          // }),
           ],
  providers: [{ provide: RouteReuseStrategy, 
                useClass: IonicRouteStrategy},
                UntappdServerService,
                StorageService,
                NavparamService,
                NativeGeocoder,
                { provide: JWT_OPTIONS, useValue: JWT_OPTIONS},
                JwtHelperService
              ],
  bootstrap: [AppComponent],
})
export class AppModule {}
