import { Component, NgZone, AfterViewInit, ViewChild, ElementRef } from '@angular/core';
//import { AgmCoreModule } from '@agm/core';
import { NavparamService } from 'src/app/services/navparam.service';
import { Plugins } from '@capacitor/core';
const { Geolocation, Toast } = Plugins;  // built in to get device location
import { NativeGeocoder, NativeGeocoderResult, NativeGeocoderOptions } from '@ionic-native/native-geocoder/ngx';

@Component({
  selector: 'app-map',
  templateUrl: 'map.page.html',
  styleUrls: ['map.page.scss']
})
export class MapPage implements AfterViewInit {

  @ViewChild('mapContainer', {static: false}) gmap: ElementRef;
  location: any;
  coords: any;
  showingCurrent: boolean = true;
  address: string;
  title: string = "Veunes";   //TODO get from navparams when user selects either venues or beer view?  
  infoWindow = new google.maps.InfoWindow;
  map: google.maps.Map;
  lat = 39.984520;
  lng = -105.242960;
  coordinates =  new google.maps.LatLng(this.lat, this.lng);
  
  mapOptions: google.maps.MapOptions = {
    center: this.coordinates,
    zoom: 12,
    mapTypeControl: false,
    zoomControl: true,
    zoomControlOptions: {
      //style: google.maps.ZoomControlStyle.SMALL   I think does not exist in updated API
      position: google.maps.ControlPosition.RIGHT_TOP
    },
    streetViewControl: false,
  };
  
  //TODO:  this is temp to test multiple markers on the map
  //       need to create this list dynamically with venues or beers in area
  //       confirm with Ron.  
  markers = [
    {
      position: new google.maps.LatLng(39.9843, -105.2494),
      //map: this.map,  //error because this.map not iniitilized yet
      //icon: "TODO with custom icon"
      title: "Southern Sun"
    },
    {
      position: new google.maps.LatLng(39.9833, -105.2497),
      //map: this.map,  //error because this.map not iniitilized yet
      //icon: "todo with custom icon"
      title: "Murphy's South"
    }
  ];

  //TODO:  this is temp to test multiple markers on the map
  //       need to create this list dynamically with venues or beers in area
  //       confirm with Ron.  
  markers2 = [
    {
      position: new google.maps.LatLng(39.9843, -105.2494),
      //map: this.map,  //error because this.map not iniitilized yet
      //icon: "TODO with custom icon"
      title: "Juicy Bits"
    },
    {
      position: new google.maps.LatLng(39.9833, -105.2497),
      //map: this.map,  //error because this.map not iniitilized yet
      //icon: "todo with custom icon"
      title: "Nightmare on Brett Sour Cherry"
    }
  ];

  marker = new google.maps.Marker({
    position: this.coordinates,
    title: "Your location"
  });

  constructor(
    private navParamService: NavparamService,
    private nativeGeocoder: NativeGeocoder, 
    private ngZone: NgZone
  ) {}
  
  ngOnInit() {
    //this.setCurrentPosition();
  }

  ngAfterViewInit() {
    this.mapInitializer();
  }

  //TODO:  check that lat and long are set before mapInitializer is called in ngAfterViewInit!!!
  ionViewWillLoaad(){
    console.log("map page: ionViewWillLoad: Entering");
    //this.setLocationCoordinates();
    this.setCurrentPosition();  
  }


  mapInitializer() {
    this.map = new google.maps.Map(this.gmap.nativeElement, this.mapOptions);
    
    // add click event for the default marker on map
    this.marker.addListener("click", () => {
        this.infoWindow.setContent(this.marker.getTitle());
        this.infoWindow.open(this.marker.getMap(), this.marker);
    });
    // this is default marker
    this.marker.setMap(this.map);
    // Add the rest here
    this.loadMarkers(this.markers);
   }
 

  /*
   * Loads markers from markers[].  Assumes this.map has abeen
   * initialized
   */  
  loadMarkers(markers: any) {

     this.markers.forEach(markerInfo => {
       const marker = new google.maps.Marker({...markerInfo});
      //TODO add location address? or "custom content from navParams OR uses one infoWindow and reuse on each click???
      let markerText = "<p>" + marker.getTitle() + "<\p>" + "<p>" + "Coming...info about beers or venue." + "<\p>"
      const infoWindow = new google.maps.InfoWindow({content: markerText}); 
      
      marker.addListener("click", () => {
        this.infoWindow.setContent(markerText);
        this.infoWindow.open(marker.getMap(), marker);
      });

      // add the marker to the map
      marker.setMap(this.map);
      
      // Debug only...remove
      console.log("Marker: ", marker);
    });
  }

  async locate() {
    const cd = await Geolocation.getCurrentPosition();
    this.coords = cd.coords;
  }

  setLocationCoordinates(){
    this.location = this.navParamService.getNavData("location");
    this.lat = this.location['lat'];
    this.lng = this.location['lng'];
    console.log(`Lat, Long: ${this.lat} : ${this.lng}`);
  } 
 

  async setCurrentPosition() {
    try {
    console.log("Entering getCurrentPosition..."); 
    const coordinates = await Geolocation.getCurrentPosition();
    this.ngZone.run(() => {
      this.lat = coordinates.coords.latitude;
      this.lng = coordinates.coords.longitude;
    })
    this.showingCurrent = true;
    } catch (err) {
      //this.errorMessage = err;
      console.log("geolocation getCurrentPosition error: ", err);
    }
  }

  async setAddress(){
    if (this.address != "") {
      let options: NativeGeocoderOptions = {
        useLocale: true,
        maxResults: 5
      };
      this.nativeGeocoder.forwardGeocode(this.address, options)
        .then((result: NativeGeocoderResult[]) => {
          this.ngZone.run(() => {
            this.lat = parseFloat(result[0].latitude);
            this.lng = parseFloat(result[0].longitude);
          })
          this.showingCurrent = false;
        })
        .catch((error: any) => console.log(error));
       }
       else{
         await Toast.show( {
           text: 'Please enter address'
         });
       }
    }
}
