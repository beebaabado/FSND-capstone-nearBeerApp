// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url  run heroku locally  with 'heroku local web'
  //apiServerUrl: 'https://capstone-nearbeer-app.herokuapp.com',
  auth0: {
    url: 'product-demos.us', // the auth0 domain prefix
    audience: 'beernear', // the audience set for the auth0 app
    clientId: 'ziR3Cuw3SWmFhkPWfThF9LDz7gkXnMH6', // the client id generated for the auth0 app
    //callbackURL: 'https://capstone-nearbeer-front.herokuapp.com', //'http://localhost:8080', // the base url of the running ionic application. 
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
}


/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.
