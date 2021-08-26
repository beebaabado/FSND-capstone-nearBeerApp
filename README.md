<<<<<<< HEAD
# FSND-capstone-nearBeerApp
Let's always drink the best beer
=======
## NearBeer Backend 

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

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

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

Run in same venv as app, in backend directory to export Auth0 variables (domain, audience, algorithms, tokens/secrets):

```bash
 . ./setup.sh 
```

```bash
flask run --reload
```

To run unit test cases.  Start in parent directory (in nearbeer directory) run:

```bash
 python -m backend.tests.test_beer_server --verbose
```

# HEROKU



# test from heroku app  

API call with bearer token

curl -X GET  'https://capstone-nearbeer-app.herokuapp.com/' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjI5ODY4MTg2LCJleHAiOjE2Mjk5NTQ1ODYsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.Ya_Z4-JQzN6Qyb8qQDofonR-Lr1qknVYk7ADJZmQQPTNXAHvWHge0QyFtuTCMPQMYiBju-U6xyC74cZvtUnIeOaWwqB1C1PPNUmsC-COsHYi5jai8hRmmVftyK7wXCklkA3sdpho0Tre_FFeVNh4JtCgwu-DX6ZSzkhZQ92sqbrz6B-G1BVJnWdX697_y0QuVOXpiiGmXzFQmOnIKw_JppzhgAEgOO6OGSuc2b9XntJvNCEhfog3Fq5fmdCW-FyEsoo_-3I24PMtruQ5VmGaO1nKeltJhxMkLI08lYxIa4hUbyygbdny5LiWLhz8YDoRA-u8l-LjIBRP1vzOxvPrqg'  



# Acknowledgements

The data stored in the NearBear Postgres database was obtained via the untappd API [untappd.com].  There is a separate REST API that I created to pull beer data from Untappd.  This other API was left out of this project because it involves a limited number of user requests to the untappd server.  Therefore, for testing purposes of the NearBeer API, I chose to query the Untappd server once and use static data in my NearBeer project.

>>>>>>> 69d3d39ff5e545cb5fbc9abefd2ffcb1f49c15c0
