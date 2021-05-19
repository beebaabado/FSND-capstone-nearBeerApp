import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
//import { Platform } from '@ionic/angular';

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
//private getApiUrl : string = "http://10.0.2.2:8000/"; // to work with android emulator and devices
private getApiUrl : string = "http://127.0.0.1:8000/"; // iOS and browsers

  constructor(
       private http: HttpClient,
       //private platform: Platform
       ) {
    console.log('UntappdServerService started... ');
    // platform.ready().then(() => {
    //   if (this.platform.is('android')){
    //     console.log("Running on Android device.")
    //     this.getApiUrl = "http://10.0.2.2:8000";
    //   }
    //   else
    //     console.log("Running on iOS/browser device.")
    // });
  }
  
  

  getBeerList(location:any){
      // future...use lat, long in location instead of city name
      // clear our allBeers
      this.allBeersData=[];
      const cityUrl = this.getApiUrl + "beers/"
      let city = location['city_url_name'];
      return this.http.get(cityUrl.concat(city.toString())).pipe(
        tap(data => console.log("UntappdService: Beers/Venues data:  ", data)),                 // interecept stream to print data 
        map(data=>{this.allBeersData.push(data[0]);  // if you return this line get length only which = 1
                   return this.allBeersData;}));  // just return data
  }
  
  getStyles(){
    this.stylesList = [];
    const stylesUrl = this.getApiUrl + "styles"
    return this.http.get(stylesUrl).pipe(
      tap(data => console.log("UntappdService: Styles data:  ", data)),                 // interecept stream to print data 
      map(data=>{this.stylesList.push(data[0]);  // if you return this line get length only which = 1
                return this.stylesList;}));  // just return data
  }

  //TODO...make a real error handler
  private handleError(error: any) {
    console.log (error);
    return error;
  }

}
