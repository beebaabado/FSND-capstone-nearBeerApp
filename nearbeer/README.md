# NEAR BEER Demo app  
This applications is a tool to help users find the highest rated beers near their current location.   

## HEROKU
Near beer front and backends are depolyed on Heroku.  You can access the app at [https://capstone-nearbeer-front.herokuapp.com/tabs/home](https://capstone-nearbeer-front.herokuapp.com/tabs/home)


### Login instructions

Select the User page to login.  There are two valid user accounts.  Use separate sessions to be logged into both users at the same time.  For example, use incognito mode in Chrome, or use two different browsers: Chrome, Safari, or Firefox.

User with Brewer Role:

```
Username:  halsaves@gmail.com
Password:  Demob33rbrewer
```
User with Drinker Role:

```
Username: highlyillogical0101@gmail.com
Password: Demob33rdrinker
```

Once you are logged in, a valid JWT token is displayed on the screen for backend unit testing purposes and also to demonstrate that the user was logged in correctly.

### Get beers for city
Now you can use the app to find beers for a specific set of ciites.  The beer data used for this demo application is static and is not current.  Navigate to the Beers page. Click the Search menu (uppper left side). Select the location icon. Select a city from the dropdown menu (upper ride side).  The page should update with list of beers for that city.  There is a bit of delay if the Heroku dynos for this app are shutdown; they will be restarted automatically.

## FRONTEND
For specifics on frontend refer to the frontend app README [here](frontend/README.md)

## BACKEND
For specifics on backend and local testing of backend with unnittest refer to the backend app README [here](backend/README.md)