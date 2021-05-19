import { Injectable } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class NavparamService {
  
  navParamData = {};

  constructor() { }

  setNavData( paramKey, navData) {
    this.navParamData[paramKey] = navData;
    console.log("Nav params set: ", this.navParamData[paramKey]);
  }

  getNavData(paramKey="") {
    if ((this.navParamData === null) || (this.navParamData === undefined))
      return 0; 
    if (paramKey == "")  
       return this.navParamData;
    else
       return this.navParamData[paramKey];

    console.log("Nav params get: ", this.navParamData);   
  }
}
