# NEAR BEER Demo app  
This applications is a tool to help users find the highest rated beers near their current location.  I am creating an app to run on android and iOs devices with filtering options, maps with venue locations and listings of beers. For the purposes of this capstone project,  I have simplified the front end to display lists of beers.  Other features are not implemented.

## HEROKU
Near beer front and backends are depolyed on Heroku.  You can access the app at [https://capstone-nearbeer-front.herokuapp.com/tabs/home](https://capstone-nearbeer-front.herokuapp.com/tabs/home)

The frontend end queries the backend at [https://capstone-nearbeer-app.herokuapp.com](https://capstone-nearbeer-app.herokuapp.com)

### Login instructions

From a browser window, navigate to the frontend address noted above. Select the User tab to login.  User will be redirected to Auth0 login screen. There are two valid user accounts.  Use separate sessions to be logged into both users at the same time.  For example, use incognito mode in Chrome, or use two different browsers: Chrome, Safari, or Firefox.

Role permissions are defined in [backend README](backend/README.md)

User with Brewer Role:

```
Username:  halsaves@gmail.com
Password:  Demob33rbrewer
```
User with Drinker Role (has limited permissions):

```
Username: highlyillogical0101@gmail.com
Password: Demob33rdrinker
```

Once you are logged in, a valid JWT token is displayed on the screen for backend unit testing purposes and also to demonstrate that the user was logged in correctly.

### Get beers for city
Now you can use the app to find beers for a specific set of ciites.  The beer data used for this demo application is static and is not current.  I chose to not have it update in real time for this project due to constraints on number of API calls I can make to the untappd API.  Navigate to the Beers page. Click the Search menu (uppper left side). Select the location icon. Select a city from the dropdown menu (upper right side).  The page should update with list of beers for that city.  There is a bit of delay if the Heroku dynos for this app (front and back) are shutdown due to inactivity; they will be restarted automatically.   Sometimes it can take a few seconds for the page to refresh.

## FRONTEND
For specifics on frontend refer to the frontend app README [here](frontend/README.md)

## BACKEND
For specifics on backend and local testing of backend with unnittest refer to the backend app README [here](backend/README.md)