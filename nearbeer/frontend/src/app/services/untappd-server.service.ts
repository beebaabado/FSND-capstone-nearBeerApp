import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { Platform } from '@ionic/angular';
import { AuthService } from './auth.service';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})

export class UntappdServerService {
  private headers = new HttpHeaders()
  .set('Content-Type', 'application/json')
  .set('Accept', 'application/json');

private httpOptions = {
headers: this.headers
};

private allBeersData=[];
private stylesList=[];
//private getApiUrl : string = "http://10.0.2.2:5000/"; // to work with android emulator and devices
private getApiUrl : string = environment.apiServerUrl; // iOS and browsers

  constructor(
       private auth: AuthService,
       private http: HttpClient,
       public platform: Platform
       ) {
    console.log('UntappdServerService started... ');
    platform.ready().then(() => {
       if (this.platform.is('android')){
         this.getApiUrl = "http://10.0.2.2:5000";
         console.log("UntappdServerService: Running on Android device. Using Url -- ", this.getApiUrl);
       }
      else
         console.log("UntappdServerService: Running on iOS/browser device. Using default Url for host -- ", this.getApiUrl);
    });    
  }

  getHeaders() {
    const header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${this.auth.activeJWT()}`)
    };
    console.log("auth0 JWT token: ", this.auth.activeJWT());
    return header;
  }
  
  getBeerList(location:any){
      // future...use lat, long in location instead of city name
      // clear our allBeers
      this.allBeersData=[];
      let beerUrl = this.getApiUrl + "/beers"
      console.log("UntappdServerService:cityUrl: ", beerUrl);
      let city = location['city_url_name'];
      if (this.auth.activeJWT()) {
        beerUrl = beerUrl.concat('/' + city.toString() + '/') ;
      }
      else
        beerUrl = beerUrl.concat('?city=' + city)
      
      console.log("UntappdServerService:locations: ", beerUrl);
      return this.http.get(beerUrl, this.getHeaders()).pipe(
        tap(data => console.log("UntappdService: Beers/Venues data:  ", data)),                 // interecept stream to print data 
        map(data=>{this.allBeersData.push(data);  // if you return this line get length only which = 1
                   return this.allBeersData;}));  // just return data
  }
  
  getStyles(){
    this.stylesList = [];
    const stylesUrl = this.getApiUrl + "/styles/"
    return this.http.get(stylesUrl, this.getHeaders()).pipe(
      tap(data => console.log("UntappdService: Styles data:  ", data)),                 // interecept stream to print data 
      map(data=>{this.stylesList.push(data);  // if you return this line get length only which = 1
                return this.stylesList;}));  // just return data
  }

  //TODO...make a real error handler
  private handleError(error: any) {
    console.log (error);
    return error;
  }

}
