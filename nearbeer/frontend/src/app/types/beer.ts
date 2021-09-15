export class Beer {
    
    id: number = 0;
    rating: number = 0.0;
    brewery:string = "brewery unknown";
    name:string = "name unknown";
    style:string = "sytle unknown";
    venue:string = "venue unknown";
    abv:number = 0.0;
    last_seen: string = "";   
    untappd_page: string = "www.untappd.com";
    user_rating: number = 0.0;

    constructor (
        fields?: {
        id?: number,    
        rating?: number,
        brewery?: string,
        name?: string,
        style?: string,
        venue?: string,
        abv?: number,
        last_seen?: string,
        untappd_page?: string,
        user_rating?: number,
       }) {
         
       if (fields) Object.assign(this, fields);
       this.printToLog();
    }
  
    printToLog(){ 
      console.log(" Beer: ", this.id);
      console.log("rating: :", this.rating);
      console.log("brewery: ", this.brewery);
      console.log("name: ", this.name);
      console.log("styel: ", this.style);
      console.log ("venue: ", this.venue);
      console.log("abv:  ", this.abv);
      console.log("last_seen: ", this.last_seen);
      console.log("untappd_page: ", this.untappd_page);
      console.log("user_raring:", this.user_rating);
    }

    setValues(
        fields?: {
            id?: number,    
            rating?: number,
            brewery?: string,
            name?: string,
            style?: string,
            venue?: string,
            abv?: number,
            last_seen?: string,
            untappd_page?: string //Date formatted as 'mediumDate',
            user_rating?: number,
           }) {
             
           if (fields) Object.assign(this, fields);

           this.printToLog();
      }        
}
