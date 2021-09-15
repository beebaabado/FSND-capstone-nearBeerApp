export const environment = {
  production: true,
  //apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url  run heroku locally  with 'heroku local web'
  apiServerUrl: 'https://capstone-nearbeer-app.herokuapp.com',
  auth0: {
    url: 'product-demos.us', // the auth0 domain prefix
    audience: 'beernear', // the audience set for the auth0 app
    clientId: 'ziR3Cuw3SWmFhkPWfThF9LDz7gkXnMH6', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8080', // the base url of the running ionic application. 
  }
};
