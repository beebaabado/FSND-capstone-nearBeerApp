# The NearBeer Backend App

## General Information

### Base URL
This project has been deployed on HEROKU at the following base address: [https://capstone-nearbeer-app.herokuapp.com](https://capstone-nearbeer-app.herokuapp.com) 

The backend is hosted locally at the following default address:

http://localhost:5000

http://127.0.0.1:5000

You must specify an endpoint or you will get an "Authorization header is expected" error.  API documentaiton can be found [here](README_beer_server_api.md).

## BACKEND PROJECT FILES and API documentation

Clone the nearbeer project at [https://github.com/beebaabado/FSND-capstone-nearBeerApp.git](https://github.com/beebaabado/FSND-capstone-nearBeerApp.git).  

## INSTALLING DEPENDENCIES

### Python 3.8.x  

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


### Posgressql Server 13.x

Nearbeer has been tested on version 13 (note version 14 is available but the Nearbeer app has not yet been tested on this version).  Nearbeer requires postgres sql server to be installed and running ([http](https://www.postgresql.org/))

### Virtual Enviornment

Recommend using a virtual environment for Python projects to keep your dependencies separate and organaized. Instructions for setting up a virtual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### PIP Dependencies

Once your virtual environment is setup and running, change directories to the `FSND-capstone-nearBeerApp/nearbeer/backend` directory and run the following command to install all required packages:

```bash
pip install -r requirements.txt
```

This will install the following key dependencies

#### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the Postgres database used by backend. 

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## AUTH0 ROLE BASED Authentication/access control

Role: Brewer  
Description: Admin for Near Beer site.  Able to view/add/delete/update beers, styles, user ratings
Permissions:

- get:beer-details	Retrieve info for one beer
- get:beers	Retrieve list of beers
- get:styles	Retrieve list of beer styles
- patch:beer-user-rating	Update user rating for one beer
- post:beers	Add a new beer	
- view:simple	Simple table view for admin use


Role: Beer-lover  
Description: Beer enthusiast can view beers and update user ratings on beers.
Permissions: 

- get:beer-details	Retrieve info for one beer	
- get:beers	Retrieve list of beers
- patch:beer-user-rating	Update user rating for one beer

### Getting valid JWT tokens for backend testing

Refer to frontend app README [here](../frontend/README.md) for procedure to get valid JWT tokens.  Update backend/setup_local.sh file with valid tokens. 

- TEST_BREWER_AUTH_TOKEN
- TEST_BEER_LOVER_AUTH_TOKEN

## Setup server for local testing

From within the `./backend` directory first ensure you are working using your virtual environment.

#### LOCAL - To run the server, execute:

Run in same venv as app, in backend directory to export Auth0 variables (domain, audience, algorithms, tokens/secrets), and FLASK_APP/ENV vars:

```bash
 . ./setup_local.sh 
```
Setup nearbeer database (seeded with test data).  Assumes that Postgresql server is properly installed and running. Script creates a nearbeer database, then uses flask migrattion to create needed tables. Test data is then inserted into the database.

```bash
. ./create_nearbeer_db.sh
```
Quick test to see if database is setup properly
```bash
flask run --reload
```
Note:  Use http for localhost or curl command will fail
```bash
curl -X GET  'http://localhost:5000/beers/template?city=Boulder' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMzNTIyMDIyLCJleHAiOjE2MzM2MDg0MjIsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.ZrzhVG5hO_1MviO4H759eUBzMCQkH7CttOKzXhqa00y9lDpwTjn9lJ-gRV5wnZcQSLXdmHHdgYAFQEqPI9aYuX-yjt3zClynk8WyQ7eaVTxaiEoOwCUXQ6ikh0TJcknT0FagHXU1BNb2mNx67UMX0hML4kYz1GG4KZrezBF2L1vQDCD036UD0PCE5ee0X2-mxKHo0h8xvbjIQm2IcUz20NhtrAchxs-f5SF3oxRsAT75rBlM8soLnbe6iYAaW-ojf3BSyDwFaV85H6-J93-RhBA15hUNN-VwZHTtk3ot4kmBypiemq58Q0rkrJx5R57N-Ol8Sqmd0UDz7JIzp_X_Ow'
```

### TESTING THE BACKEND app

#### Unit testing with local database
You can run test_beer_server.py to run suite of tests for each end point in beer_server.py  You will need to 
setup local database and load data using provided sql files

To run unit test cases.  Start in parent directory (in nearbeer directory) run:

```bash
 python -m backend.tests.test_beer_server --verbose
```

#### HEROKU

#### verify remote backend is up and running
To test that backend is running remotely on Heroku you can access this link from a web browser -- requires no authentication:

```
https://capstone-nearbeer-app.herokuapp.com/beers/template?city=erie
```
#### 
You can also use the following curl commands from terminal to test if backend is up and running.  You must have a valid access token.  This will return json list of all beers in the database.

``` curl
API call with bearer token  Note: Use valid JWT token

curl -X GET  'https://capstone-nearbeer-app.herokuapp.com/' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMzNTIyMDIyLCJleHAiOjE2MzM2MDg0MjIsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.ZrzhVG5hO_1MviO4H759eUBzMCQkH7CttOKzXhqa00y9lDpwTjn9lJ-gRV5wnZcQSLXdmHHdgYAFQEqPI9aYuX-yjt3zClynk8WyQ7eaVTxaiEoOwCUXQ6ikh0TJcknT0FagHXU1BNb2mNx67UMX0hML4kYz1GG4KZrezBF2L1vQDCD036UD0PCE5ee0X2-mxKHo0h8xvbjIQm2IcUz20NhtrAchxs-f5SF3oxRsAT75rBlM8soLnbe6iYAaW-ojf3BSyDwFaV85H6-J93-RhBA15hUNN-VwZHTtk3ot4kmBypiemq58Q0rkrJx5R57N-Ol8Sqmd0UDz7JIzp_X_Ow'
```

### Acknowledgements

The data stored in the NearBear Postgres database was obtained via the untappd API [untappd.com].  There is a separate REST API that I created to pull beer data from Untappd.  This other API was left out of this project because it involves a limited number of user request to the untappd API.  Therefore, for testing purposes of the NearBeer API, I chose to query the Untappd server once and use static data in my NearBeer project demo.

