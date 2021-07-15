import { Component, OnInit } from '@angular/core';
import { Plugins } from '@capacitor/core';
import { NavparamService } from 'src/app/services/navparam.service';
import { StorageService } from '../../services/storage.service';
import { Router } from '@angular/router';
const { Geolocation } = Plugins;
import { NativeGeocoder, NativeGeocoderResult, NativeGeocoderOptions } from '@ionic-native/native-geocoder/ngx';


@Component({
  selector: 'app-settings',
  templateUrl: './settings.page.html',
  styleUrls: ['./settings.page.scss'],
})
export class SettingsPage implements OnInit {
  city: string;
  state: string;
  latitude: number = 40.017624;  //Boulder
  longitude: number = -105.27966;
  position: any;
  positionWatchId: any;
  errorMessage: any;
  address: any;
  settings_changed: boolean = false;
  
  GeolocationOptions = {enableHighAccuracy: true, timeout: 30000 }; // maximumAge: }
  constructor( 
     private storage: StorageService, 
     private navparamService: NavparamService,
     private router: Router,
     private nativeGeocoder: NativeGeocoder
     ) { }
  
  ngOnInit() {
    }
  
  ionViewWillEnter(){
    console.log("Settings Page ionViewWillEnter: ");
    this.settings_changed = false;
    console.log("settings page settings changed to false:", this.settings_changed);
  }
    // a little help from 
  // https://medium.com/enappd/use-geolocation-geocoding-and-
  // reverse-geocoding-in-ionic-capacitor-b494264f0e85
  // and https://github.com/ionic-team/capacitor/issues/1279
  async getCurrentPosition(city:string="") {
    try {
    console.log("Entering getCurrentPosition..."); 
    const coordinates = await Geolocation.getCurrentPosition(this.GeolocationOptions);
    this.position = coordinates;
    this.latitude = coordinates.coords.latitude;
    this.longitude = coordinates.coords.longitude;
    console.log("Current latitude: ", this.latitude);
    console.log("Current longitude: ", this.longitude);
    } catch (err) {
      this.errorMessage = err;
      console.log("geolocation getCurrentPosition error: ", err);
    }
  }
  
  watchPosition() {
    console.log("Entering watchPosition..."); 
    const wait = Geolocation.watchPosition({}, (coordinates, err) => {
      this.position = coordinates;
      this.latitude = coordinates.coords.latitude;
      this.longitude = coordinates.coords.longitude;
      console.log("Current latitude: ", this.latitude);
      console.log("Current longitude: ", this.longitude);
    })
  }
  
  async setAddress(){
    let options: NativeGeocoderOptions = {
      useLocale: true,
      maxResults: 5
    };
    try {
        const result: NativeGeocoderResult[] = await this.nativeGeocoder.reverseGeocode(this.latitude, this.longitude, options);
        console.log("RESULT: NativeGeocoderResult: ", result[0]);
        this.address = result[0];
      } catch(error: any) {
        console.log(error)
      } 
      finally {
        console.log("Got address info")
      }    
  }

  goBack(){
    this.router.navigate(['/tabs/beer']);
  }

  saveSettings() {
      // Location Settings
      this.setAddress().then(() =>
      {
        const location = this.navparamService.getNavData('location');
        const current_city = location?.city;
        const current_state = location?.state;
        this.city = this.address['locality'];
        this.state = this.address['administrativeArea'];
        if ((this.city != current_city) && (this.state != current_state)) {
          this.settings_changed = true;
          this.navparamService.setNavData("location", {'city': this.city, 'state': this.state, 'latitude': this.latitude, 'longitude': this.longitude});
          this.navparamService.setNavData("settings_changed", true);
          console.log("naveparams setings changed: ", this.navparamService.getNavData("settings_changed"));
          this.storage.set("location", {'city': this.city, 'state': this.state, 'latitude': this.latitude, 'longitude': this.longitude});
        }
      });
  }
}
