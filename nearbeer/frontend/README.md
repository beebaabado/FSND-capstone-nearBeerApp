# The NearBeer Frontend Ionic App
##### by Connie Compos 2021

This is the frontend for the Full Stack Nano Degree Capstone project Nearbeer project.  This is a tab based application which allows the user to login to authenticate with Auth0 credentials and access the nearbeer database with a menu system.  This is a demo application thus not all tabs are fully functional. 

### Requires nearbeer backend app to be up and running

See backend app README [here](../backend/README.md)


## FOR LOCAL INSTALLATION/TESTING
### Installing dependencies

#### Node and npm

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).


#### Virtual Enviornment

Recommend using a virtual environment for Python projects to keep your dependencies separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### NODE Dependencies

Once your virtual environment is setup and running, change directories to the `/frontend` directory and run the following command to install all required node packages:

```bash
npm install
```

This will install the following key dependencies

##### Key Dependencies

- [link title](actual link)

- []() 
  
## AUTH0 ROLE BASED Authentication/access control

### Role: Brewer  
Description: Admin for Near Beer site.  Able to view/add/delete/update beers, styles, user ratings
Permissions:

- get:beer-details	Retrieve info for one beer
- get:beers	Retrieve list of beers
- get:styles	Retrieve list of beer styles
- patch:beer-user-rating	Update user rating for one beer
- post:beers	Add a new beer	
- view:simple	Simple table view for admin use

User with role Brewer sample JWT: 
```json
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMzNTIyMDIyLCJleHAiOjE2MzM2MDg0MjIsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.ZrzhVG5hO_1MviO4H759eUBzMCQkH7CttOKzXhqa00y9lDpwTjn9lJ-gRV5wnZcQSLXdmHHdgYAFQEqPI9aYuX-yjt3zClynk8WyQ7eaVTxaiEoOwCUXQ6ikh0TJcknT0FagHXU1BNb2mNx67UMX0hML4kYz1GG4KZrezBF2L1vQDCD036UD0PCE5ee0X2-mxKHo0h8xvbjIQm2IcUz20NhtrAchxs-f5SF3oxRsAT75rBlM8soLnbe6iYAaW-ojf3BSyDwFaV85H6-J93-RhBA15hUNN-VwZHTtk3ot4kmBypiemq58Q0rkrJx5R57N-Ol8Sqmd0UDz7JIzp_X_Ow
```
JWT Payload:
```json
{
  "iss": "https://product-demos.us.auth0.com/",
  "sub": "auth0|60e885be5308090068fff542",
  "aud": [
    "beernear",
    "https://product-demos.us.auth0.com/userinfo"
  ],
  "iat": 1633522022,
  "exp": 1633608422,
  "azp": "ziR3Cuw3SWmFhkPWfThF9LDz7gkXnMH6",
  "scope": "openid profile email",
  "permissions": [
    "delete:beers",
    "get:beer-details",
    "get:beers",
    "get:styles",
    "patch:beer-user-rating",
    "post:beers",
    "view:simple"
  ]
}
```

### Role: Beer-lover  
Description: Beer enthusiast can view beers and update user ratings on beers.
Permissions: 

- get:beer-details	Retrieve info for one beer	
- get:beers	Retrieve list of beers
- patch:beer-user-rating	Update user rating for one beer

User with role Beer-lover sample JWT:
```json
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NTFjYTg1MjJhMDA2OTEyODhkYyIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMzNDcxOTY1LCJleHAiOjE2MzM1NTgzNjUsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJwYXRjaDpiZWVyLXVzZXItcmF0aW5nIl19.13vX9Mw9eVY9XAvNg7I0yiD7Bi8_ytOD1tRHIqgSndD68QVb9CHkTgvRF-XcwpwfKwe1SkgpDw6HEBQhykKiEoaLuTCt2KIMEgU2_07yBgAaRVq6kcf7ZqSKNwpe9xmXJJHUM-QVsfTqybA-oP46oXleOxDpuhHn9msnR5MAsXA3a36a2tD9-9AU8j3AZESfCH4j-Zo9GVXzd1TsGeXUmRAZCS6-IR7FyFYdkNrBegBU32O2CJsM5U8diLwpzJpHa-z3dRr9R-AvKIMvKNLzyhhD6ignpEM2YMsshRCdD7OqKVHLuHcAp6UOotw7aosPqHFfaP2O5xrvclZnTIhWXQ
```
JWT Payload:
```json
{
  "iss": "https://product-demos.us.auth0.com/",
  "sub": "auth0|60e8851ca8522a00691288dc",
  "aud": [
    "beernear",
    "https://product-demos.us.auth0.com/userinfo"
  ],
  "iat": 1633471965,
  "exp": 1633558365,
  "azp": "ziR3Cuw3SWmFhkPWfThF9LDz7gkXnMH6",
  "scope": "openid profile email",
  "permissions": [
    "get:beer-details",
    "get:beers",
    "patch:beer-user-rating"
  ]
}



#### HEROKU 

#### verify backend is up and running
To test that backend is running remotely on Heroku you can access this link from a web browser -- requires no authentication:

```
https://capstone-nearbeer-app.herokuapp.com/beers/template?city=erie
```
#### 
You can also use the following curl commands from terminal to test if backend is up and running.  You must have a valid access token.  This will return json list of all beers in the database.

``` curl
API call with bearer token

curl -X GET  'https://capstone-nearbeer-app.herokuapp.com/' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMzMDM2NTY5LCJleHAiOjE2MzMxMjI5NjksImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.H2zeuGIer51szGKdKpCmvYNcEXjmCvY607F6FBOVQfwAD5XhJkRFJz3pqcI4ds14Lkf_2YkTmAniQsC841UqxylcFO5Ng2zeuXcMytTgtBAg5wI-RDYvmH5Yj7YCkpLxYfKEINK4WHPLgL9yimVey7gU9GOW4x_Ghpd2Ft9GfEubd-x38zF_kldxIjBIvSSDmLM67FFbacnVH5DFBAF6r6c4-v2PkLi2tkGszAQwwlndT0vwApt2fY5z73fI8_s0RlgEtNRA7CmjfJS_IugzXdgAnbym0gL1yKB0CA1AjnMLfh5oG434HTuka1VHzZaCAg-mm9F9D5c3ucN7xmOQmg'
```

### Acknowledgements



