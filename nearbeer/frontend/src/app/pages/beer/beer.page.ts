import { Component, ViewChild } from '@angular/core';
import { map } from 'rxjs/operators'
import { UntappdServerService } from '../../services/untappd-server.service';
import { StorageService } from '../../services/storage.service';
import { IonicSelectableComponent } from 'ionic-selectable';
import { IonContent, IonSelect} from '@ionic/angular';
import { Router } from '@angular/router';
import { NavparamService } from 'src/app/services/navparam.service';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-beer',
  templateUrl: 'beer.page.html',
  styleUrls: ['beer.page.scss']
})
export class BeerPage {
 
  cityList =  [{ id: 0, city_name: 'Boulder',   url_name: 'boulder' },
               { id: 1, city_name: 'Longmont', url_name: 'longmont'},
               { id: 2, city_name: 'Lyons',  url_name: 'lyons'},
               { id: 3, city_name: 'Broomfield', url_name: 'broomfield'},
               { id: 4, city_name: 'Erie', url_name: 'erie'},
               { id: 5, city_name: 'Louisville', url_name: 'louisville'},
               { id: 6, city_name: 'Westminster', url_name: 'westminster'},
               { id: 7, city_name: 'Lafayette', url_name: 'lafayette'}];
  //headerList = ["Rating", "Brewery", "Beer", "Variety", "Venue", "ABV", "Last Seen"];
  headerList = [ "Venue",  "Brewery/Beer", "Variety (ABV)", "Rating/Your Rating"];
  beerList = [];
  styleList = [];     
  venueList = [];
  style = {id:0, style: 'IPA'};
  selectedStyles = [];
  currentStyleList = [];
  oldestCheckin:Date = new Date();
  newestCheckin:Date = new Date();
  private sortOrder = 0;  // 0 asc, 1 desc
  private searchList = [];  // list of values to filter beer, pulled from beerList
  private filteredSearchList = [];
  private searchIconRange = new Set([ 1, 2, 3, 4]);
  private showSearchBar:number = 0;
  showHeaders = new Set([0, 1, 3, 4]);
  searchTerm:string = "";
  prev_city = "";
  refreshBeers:boolean = true;
  city:string = "Select a City";
  state:string = "";
  current_location = {};
  city_url_name:string = "";
  user_rating:string = "0.00"
  headerWithFocus = 2;  // default is filter on variety aka style
  hideList = true;
  prevScrollTop:number = 0;   //assume we start at top of page
  hideSearchList:boolean = true;
  hideSelectCity:boolean = true;
  hideGoTopButton:boolean = true;
  hideFabMenu:boolean = true;
  hideUserRating:boolean = true;
  UserLoggedIn = false;

  @ViewChild('styleComponent', {static: false}) styleComponent: IonicSelectableComponent;
  @ViewChild('content', {static: false}) content: IonContent;  // static=false because not in ngOnInit()...I think...
  constructor(
    private untappdService: UntappdServerService, 
    private storage: StorageService, 
    private navparamService: NavparamService,
    private auth: AuthService,
    private router: Router) {
      this.getStyles();
    }   
 
  ionViewWillEnter() {
    console.log("Beerpage ionViewWillEnter");
    console.log("ionViewWillEnter:Nav param settings", this.navparamService.getNavData("location"));
    this.getStylePropertiesFromStorage();
    this.selectedStyles=this.styleList.slice();
    this.prev_city = this.city;
    if (this.navparamService.getNavData("settings_changed") === true) {
      console.log("ionViewWillEnter: navparams");
      this.current_location = this.navparamService.getNavData("location");
      this.city = this.current_location['city'];
      this.state = this.current_location['state'];
      console.log("Beers Page: ionViewWillEnter: City changed: ", this.city);
      console.log("Beers Page: ionViewWillEnter: State changed: ", this.state);
      this.refreshBeers = true;
    }
    else {
      console.log("ionViewWillEnter:getLocationPropertiesFromStorage");
      this.getLocationPropertiesFromStorage();
    }
    
    // if not logged in hide all controls and limit view
    if (this.auth.activeJWT()) {
      this.hideFabMenu = false;
      this.UserLoggedIn = true;
    }

  }

  getStylePropertiesFromStorage() {
    this.storage.get('selected_styles').then((val) => {
      this.selectedStyles = val;
    })
    .catch(()=>{
      console.log("getPropertiesFromStorage: No style filters in local storage.");
      this.selectedStyles = this.styleList;
    });
  }
  
  getLocationPropertiesFromStorage(){
    this.storage.get('current_location').then((val) => {
      if (val) 
        if (val != "Select A City") {
          console.log('getPropertiesFromStorage:  From local storage current location (city): ', val);
          this.city = val;
          this.city_url_name = this.cityList.find( ({ city_name }) => city_name === this.city )?.url_name;
        }
        //else
          //console.log("getPropertiesFromStorage:  No city found in local storage...user needs to select a city.");
     })
     .catch(()=>{
      this.selectedStyles = this.styleList;
    });

  }

  scrollingTriggered(event) { 
    // Check direction of scrolling to determine if goToTop button should be hidden
    let currentScrollTop = event.detail.scrollTop;
    if (currentScrollTop == 0)
      this.hideGoTopButton = true;    
    else 
      this.hideGoTopButton = false;   
  }

  scrollToTop() {  
    this.content.scrollToTop(0);
    this.hideGoTopButton = true;
  }
  
  toggleAllFilterComponents(show) {
    this.hideList = show;
    this.hideSearchList = show;
    this.hideSelectCity = show;
    this.content.scrollToTop(0);

  } 

  displayStyleList(hideIt) {
    this.toggleAllFilterComponents(true);
    this.hideList = hideIt;
  
    this.storage.get('selected_styles').then((val) => {
      console.log('From local storage selected styles: ', val);
      this.selectedStyles = val;
    });

  }
  
  displayUserRating(hideIt){
    this.toggleAllFilterComponents(true);
    this.hideUserRating = hideIt;
    console.log("HERE IN displayUserRating...");
  }

  filterByVenue(hideIt) {
   this.toggleAllFilterComponents(true);
   this.hideSearchList = hideIt;
   this.headerWithFocus=0;
  }
  
  filterByMultiple(hideIt){
    this.toggleAllFilterComponents(true);
    this.router.navigate(['/tabs/filter-options']);
  } 
  // TEMP function to sort by venue and then by style and rating 
  venue_style_rating_sort() {
 
    // count frequency of items   
    let counts = [], searchListByVenue = [], venues = [];
    this.headerWithFocus = 0; 
    this.buildSearchList();
    searchListByVenue = this.searchList;

    // get list of venues an frequency of appearance in beerlist
    for (var i = 0; i < searchListByVenue.length; i++) {
      let venue = searchListByVenue[i].value;
      venues[venue] =  (venues[venue]  || 0) + 1; 
  };

  // for each venue in venues count list 
  // find matching rows in beerList by venue_id
  var totalCount = 0, totalkeys = 0, listByVenues = [], oneVenueList =[], venueID="";
  for (let key in venues) {
    totalCount += venues[key];
    totalkeys +=1;
    console.log(`{"venue" : "${key}", "count" : ${venues[key]}},`);
     
     
    oneVenueList = this.beerList.filter( (listItem ) => listItem.venue_name === key );
    venueID = oneVenueList.find( (venue) => venue.venue_name === key)?.venue_id;
    console.log(`"VENUE LIST for ${key}: `);
    console.log(oneVenueList);
    console.log(`{"id" : "${venueID}, "name": ${key}, "beers": ${oneVenueList[0].beer_name}}`);
    listByVenues.push({"id": venueID, "name": key, "beers": oneVenueList});
  }
   
   console.log(listByVenues); 
   this.navparamService.setNavData("listByVenues", listByVenues);
   this.router.navigate(['/tabs/filter-options']);
   
 } 
  searchLocation(hideIt) { 
   this.toggleAllFilterComponents(true);
   this.hideSelectCity = hideIt;

   // get saved city from local storage
   this.storage.get('current_location').then((val) => {
      console.log('From local storage current location (city): ', val);
      this.prev_city = this.city;
      this.city = val;
      this.city_url_name = this.cityList.find( ({ city_name }) => city_name === this.city )?.url_name;
   });
  }

  displayMostPopularByStyleList() {
    // more of a test function to get counts
    //TODO:   write new filter function that repeats 
    // search on entire list for each search string and puts 
    // beer styles in a list.
    // then count frequency of styles
    // then convert to set to remove duplicates.
    // the build style list for the new list and
    // display filtered list
    
    this.toggleAllFilterComponents(true);

    // count frequency of items   
    let counts = [], sortedStyles = [];
    this.headerWithFocus = 2; 
    this.buildSearchList();
    sortedStyles = this.searchList;

    for (var i = 0; i < sortedStyles.length; i++) {
      let style= sortedStyles[i].value;
      counts[style] =  (counts[style]  || 0) + 1; 
    }
    
    var totalCount = 0, totalkeys = 0, uniqueStyle = "";
    let sortedCounts = counts.sort();
    for (let key in sortedCounts) {
       totalCount += sortedCounts[key];
       totalkeys +=1;   // so we have counts of non duplicates
      // uniqueStyle = sortedCounts.filter( (styleItem) => key.includes("key") )
      // oneVenueList = this.beerList.filter( (listItem ) => listItem.venue_name === key );
       console.log(`{"style" : "${key}", "count" : ${sortedCounts[key]}},`);
    };

    // further refine list by collapsing styles with same key words e.g
    // IPA, SOUR, STOUT, etc...these will become the major styles that
    // user can use to filter the big beer list
    console.log(sortedCounts); 
    console.log("TOTAL BEER COUNT: ", this.beerList.length);
    console.log("TOTAL Style list count:  ", sortedStyles.length);
    console.log("TOTAL count in counts:  ", totalCount);
    console.log("TOTAL number of styles (not duplicates): ", totalkeys);

  }
  
  setStyle(event){
    console.log(event.srcElement.value);
  }

  toggleItems() {
    this.styleComponent.toggleItems(this.styleComponent.itemsToConfirm.length ? false : true);
  }

  clear() {
    this.styleComponent.clear();
    //this.styleComponent.close();
  }

  confirm() {
    this.styleComponent.confirm();
    this.styleComponent.close();
  }
/** 
 *  Triggered when city selection changes 
 *  Also triggers when page loads and ion-select options are populated with city choices
 * 
 *  TODO:  There is a "bug/behavior" that ion-select event gets triggered when options are loaded but none are selected.  value = undefined. 
 */
  setCityEventTriggered(_event: any) { 
     console.log("setCityEventTriggered   Entering...");      
     // event triggered again reset 
     if (!this.refreshBeers){
       console.log ("Don't refresh beers.");
       this.refreshBeers = true;
       return;
     } 

     if ((this.city != "Select A City") && (this.city != this.prev_city)) {
        console.log("setCityEventTriggered: New city selected: ", this.city)
        this.city_url_name = this.cityList.find( ({ city_name }) => city_name === this.city )?.url_name;
        if (this.city_url_name != undefined) {
          this.getBeers(); 
          // save selected styles to local storage
          this.storage.set('current_location', this.city);
        }  
      }
        
  }
  // Build clean styleList and then toggle hidden flag based upon if 
  // seleted styles are present in list 
  styleChangeEventTriggered(event: {
    component: IonicSelectableComponent,
    value: any
  }) {
     var count = 0;  //TODO:  REMOVE THIS
     const userSelectedStyles = event.component.value;  // array of seclected style items       
     this.headerWithFocus = 2;  //"Variety"
     this.buildSearchList(true);  
     let listofBeerStyles = this.searchList.slice();
     userSelectedStyles.forEach((selStyle) => {
        console.log("selStyle: ", selStyle);
        listofBeerStyles.forEach((style) => {
            console.log("style: ", style);
            if (style['major_style'].toLowerCase() == selStyle['id'].toLowerCase()){
                style.hidden = 0;
                count +=1;
             }
        });
     }); // User selected styles

      // Might be duplicates  TODO...might not need this...changed how filter works above
      // look at merging this with above loop.
      var deDupedList = [...new Set(listofBeerStyles)];
      deDupedList.forEach((style) => {
        let rowID = 'row' + style.index;
         if (style.hidden) 
          // TODO:  user ViewChildren to access rows 
          document.getElementById(rowID).hidden = true; 
         else 
           document.getElementById(rowID).hidden= false;
      }); 
      
      this.storage.set('selected_styles', this.selectedStyles);
       //TODO:  REMOVE THESE
      console.log("COUNT: ", count); // to keep track if all beers show up / manually tally counts for each category.  
  }

  setUserRatingEventTriggered(event: any) {
    console.log ("USER RATING: ", this.user_rating);
  }


/**
 * Summary. 
 *
 * Description. 
 */
  private buildBeerList(beerData){
    // unpack beer and venue info
    let tempBeerList = [], venues = {}, venue_id = "";
    const data = beerData[0];
    console.log(data);
    data['beers'].forEach((beer) => {
        var beerItem={};
        beerItem = beer;
        venue_id = beerItem['venue_id'];
        beerItem['venue_name'] = beer['venue']['name'];   
        tempBeerList.push(beerItem);
    });

    console.log (tempBeerList);
    return tempBeerList;
  }            
  
  /**
 * Summary. 
 *
 * Description. 
 */
//"styles" : [
 // {"major": "IPA", "patterns": ["IPA"]},
  
  private buildStyleList(styles) {
    // add id property to stylelist
    var tempStylesList = [];
    // for (let key in styles) {
    //   var styleItem = styles[key];
    //   styleItem['patterns_formatted'] = styleItem['patterns'].join(", "); //formatted for ionic-selectable component group text
    //   styleItem['id'] = key;  // for ionic-selectable component group text
    //   tempStylesList.push(styleItem);
    // }
    styles.forEach((style) => {
      var styleItem={};
      styleItem['patterns_formatted'] = style['sub_styles'];
      styleItem['id'] = style['major'];
      tempStylesList.push(styleItem);
    });
    console.log(tempStylesList)
    return tempStylesList;
  }

  /**
  * Summary. 
  *
  * Ansynchronous call to untappd API. 
  */
  getBeers(){
    
    console.log("getBeers:  Entering...", this.city_url_name);
    this.current_location['city_url_name'] = this.city_url_name;
    this.beerList=[];
    this.untappdService.getBeerList(this.current_location).pipe(
      map(beers=>{  
        return [this.buildBeerList(beers), beers[0]['venues']];
      }))  
      .subscribe(result=>{   
        console.log("RESULT: ", result);
        this.beerList = result[0];
        //this.beerList = this.sortByHeader("Rating", 1, this.beerList).slice();
        this.venueList = result[1];
        this.getOldestCheckinDate();
    });
  }

  /**
  * Summary. 
  *
  * Ansynchronous call to untappd API. 
  */
  getStyles() {
    console.log("getStyles:  Entering...");
    this.untappdService.getStyles().pipe(
      map(styles=>{  
        return this.buildStyleList(styles[0]['styles']); 
      }))  
      .subscribe(result=>{   
        this.styleList = result;
    });

  }

  // returns value <string> of beerlist property
  // uses current this.headerWithFocus 
  private getBeerListProperty(header) {
  
    let property = "beer_style";  //default
    
    switch(header) {
      case "Rating":
        property="rating_score";
        break;
      case "Brewery/Beer":
        property="brewery_name";
        break;
      case "Beer":
        property="beer_name";
        break;
      case "Variety (ABV)":
         property="beer_style";
         break;
      case "Venue":
         property="venue_name";
         break; 
      case "ABV":
         property="beer_abv";
         break;
      case "Last Seen":
         property="last_seen"
         break;              
      default:
         property="beer_style";
    }
    
    return property;

  }

  // builds abbreviated beer list with beer row index, style (aka variety) and hidden boolean value for weather row should be hidden
  // uses this.headerWithFocus to determine which beer property to filter by.  e.g. variety or venue
  private buildSearchList(hideListItems = false) {

    //pull values from beerList column with focus
    this.searchList = [];

    for ( let beer_key in this.beerList) {
      const beer=this.beerList[beer_key];
      let property = this.getBeerListProperty(this.headerList[this.headerWithFocus])  
      this.searchList.push({ "index": beer_key, "value": beer[property], "major_style": beer["major_style"], "hidden": hideListItems});
    }
    console.log(this.searchList);
  }

  // Get oldest checkin time
  getOldestCheckinDate() {
    var list = this.beerList.slice();
     //list = this.sortByHeader("Last Seen", 0, list).slice();
     
    //remove this checking runtime of sorting
    const startTime = performance.now();

     list = list.sort((a,b)=>{
       return a['last_seen'] > b['last_seen'] ? 1 : a['last_seen'] < b['last_seen'] ? -1 : 0;    
      });
     this.oldestCheckin = list[0]['last_seen'];
     this.newestCheckin = list[list.length-1]['last_seen'];

     // remove this...checking run time
    const duration = performance.now() - startTime;
    console.log(`sortDates took ${duration}ms`);

  }
  
  // sortOrder is optional, will use this.sortOrder as default
  private sortByHeader(header, sortOrder = 1, beerList) {
    
    var copyList = beerList.slice();  //sort is mutable

    // update direction of sort
    this.sortOrder = sortOrder;
    
    //Get valid property name 
    let property = this.getBeerListProperty(header);

    //remove this checking runtime of sorting
    const startTime = performance.now();
    
    // too slow using collator
    // var collator = new Intl.Collator(undefined, {
    //   numeric: true,
    //   sensitivity: 'base'
    // });
    
    // if (this.sortOrder == 0) {
    //   copyList.sort((a, b) => collator.compare(a[property], b[property]));
    // }
    // else {
    //   copyList.sort((a,b) => collator.compare(b[property], a[property]));
    // }
    
    // 
    let isNumber = false;
    if (property === "rating_score" || property === "beer_abv")
      isNumber = true;

    if (this.sortOrder == 0) {
      copyList = copyList.sort((a,b) => {
        if (isNumber)
           return (a[property] - b[property]);
        else   
           return a[property].localeCompare(b[property]);
      })
    }
    else {
      copyList = copyList.sort((a,b) => {
        if (isNumber)
           return (b[property] - a[property]);
        else  
           return b[property].localeCompare(a[property]);
      })
    }

    this.sortOrder?  0 : 1;

    // remove this...checking run time
    const duration = performance.now() - startTime;
    console.log(`sortTable took ${duration}ms`);
    
    return copyList;

  }
    
  // 
  sortTableEventTriggered(colIndex, header, event) {
    // toggle up/down arrow
    console.log("SortTable by...", header);
   // this.toggleDirectionArrow(colIndex, event);  // using heading to toggle sort direction instead of arrow icons
    this.toggleDirection(colIndex, event);     
    //this.tableSorted = "true";
    this.beerList = this.sortByHeader(header, this.sortOrder, this.beerList).slice();
    
    // build style list because order of beer list changed
    this.buildSearchList();
  }
  
  // filter beerlist by column 
  filterbyColSearchEventTriggered() {
     // build search list to sync with beerlist
     this.buildSearchList();
    
     // filter out only beers with searchTerm in name
     // start with entire list
     this.filteredSearchList = this.searchList.slice();
  
     // split search term words into array remove space, dashes, forward slash
    let listSearchTerms = this.searchTerm.split(/[ -\/]+/);
     
     //loop for each search term refine filtered list
     listSearchTerms.forEach((term) => {
       this.filteredSearchList = this.refineFilter(this.filteredSearchList, term);   
     });
      
     //build search list because order of beer list might have changed
     this.buildSearchList();

  }
  
  // Input is single word - takes string from list of strings previously split from searchbar  in this.searchTerm.
  // Strips any chars/spaces around string and searches it against list of styles
  // Hides/shows rows that are in filtered list
  // returns furter filtered list of styles 
  private refineFilter(filteredSearchList, filterString) {
    // filter out only beers with fitlerString in name
    var filteredListRefined = [];

    // Show filtered beer list by hiding rows associated with items in this.beerList
    // strip white space and special characters around the string
    const searchString = filterString.toLowerCase().replace(/\W/, '');

    var filteredSearchString = '';
    filteredSearchList.forEach((item) => { 
      filteredSearchString = item.value.toLowerCase().replace(/[\W_]/g, '');
      let rowID = 'row' + item.index;

      //TODO:  Implement..."looks like" search  eg suthern = southern?
      if (filteredSearchString.includes(searchString)) {
         filteredListRefined.push(item);

        // TODO  use angular @childrenView to get this element 
        document.getElementById(rowID).hidden = false; 
      }
      else {
        document.getElementById(rowID).hidden=true;
      } 
    }); 

    return filteredListRefined;
  }

  
  displaySearchIcon(index){
    return this.searchIconRange.has(index);   //Note:  array.includes() does not work with numbers...using set
  } 

  toggleSearchBar(index) {
      
    let placeholder = "";

    switch (index) {
        case "0":
          placeholder="Search for beer by rating";
          break;
        case "1":
          placeholder="Search for beer by Brewery";
          break;
        case "2":
          placeholder="Search for beer by name";
          break;
        case "3":
          placeholder="Search for beer by style";
           break;
        case "4":
          placeholder="Search for beer by venue";
           break; 
        case "5":
            placeholder="Search for beer by ABV";
           break;
        case "Last 6":
          placeholder="";
           break;              
        default:
          placeholder="Search";
      } 
      
      // change to use @childView
      this.headerWithFocus = index;
      document.getElementById('search-bar-1').setAttribute("placeholder", placeholder);
      if (!this.showSearchBar) {
        document.getElementById('search-bar-1').hidden = false;
        this.showSearchBar = 1;
      }
      else {
        document.getElementById('search-bar-1').hidden = true;
        this.showSearchBar = 0;
      }
  } 

  private toggleDirection(colIndex, event) {
    this.sortOrder = (this.sortOrder ? 0 : 1);
  }

}  // end beer page