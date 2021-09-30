# The NearBeer Backend App

### INSTALLING DEPENDENCIES

#### Python 3.8.x

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### Posgressql Server 13.x

Nearbeer has been tested on version 13 (note version 14 is available but the Nearbeer app has not yet been tested on this version).  Nearbeer requires postgres sql server to be installed and running ([http](https://www.postgresql.org/))

#### Virtual Enviornment

Recommend using a virtual environment for Python projects to keep your dependencies separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once your virtual environment is setup and running, change directories to the `/backend` directory and run the following command to install all required packages:

```bash
pip install -r requirements.txt
```

This will install the following key dependencies

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the Postgres database used by backend. 

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## AUTH0 ROLE BASED Authentication/access control

Role: Brewer
Permissions:

delete:beers      allows user to delete beer from nearbeer database
get:beer-details  

Role: Drinker
Permissions: 


### RUNNING THE SERVER for local testing

From within the `./backend` directory first ensure you are working using your created virtual environment.

```bash
export FLASK_APP=beer_server.py;
```

#### LOCAL - To run the server, execute:

Run in same venv as app, in backend directory to export Auth0 variables (domain, audience, algorithms, tokens/secrets):

```bash
 . ./setup.sh 
```
Setup nearbeer database (seeded with test data).  Assumes that Postgresql server is properly installed and running. Script creates a nearbeer database, then uses flask migrattion to create needed tables. Test data is then inserted into the database.

```bash
. ./create_nearbeer_db.sh
```
```bash
flask run --reload
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

The data stored in the NearBear Postgres database was obtained via the untappd API [untappd.com].  There is a separate REST API that I created to pull beer data from Untappd.  This other API was left out of this project because it involves a limited number of user requests to the untappd server.  Therefore, for testing purposes of the NearBeer API, I chose to query the Untappd server once and use static data in my NearBeer project.

