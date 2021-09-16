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

# Role Based Authentication/access control defined in Auth0

Role: Brewer
Permissions:

delete:beers      allows user to delete beer from nearbeer database
get:beer-details  



# HEROKU



# test from heroku app  

API call with bearer token

curl -X GET  'https://capstone-nearbeer-app.herokuapp.com/' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMwNjE3MDU1LCJleHAiOjE2MzA3MDM0NTUsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.KXn_4TUVMseVSDPzd3hVWMuuC_xIgKxiBCE6p9oapsVa3LTK5dEIJiAVrC9ykw7nf0jMKhVebiXsUrfwQB_s2x6uOYCpGS2Exs4IEFJAaRn99lafGKFVPFTaz8UtdHdNNpO5ICTlg115-sGyqfc14BHqPgC6B0V6Hgw_jXdFXMskxg82QiNJsrimArT2V2Vh87mbwM_1frIXWT94RpYJvUusaQAW_DDwnzTqgN_kF4KHDjasCGlSz_fxdV21IRBtaugzf_JOFhSEp08j-WI6Oj9YUfbYkZiYBFE-6eOf-gbgLCF5MnSqQ4iGjn_wnvbwoG2445tPFZI0DNr9rU5V2A'


# Acknowledgements

The data stored in the NearBear Postgres database was obtained via the untappd API [untappd.com].  There is a separate REST API that I created to pull beer data from Untappd.  This other API was left out of this project because it involves a limited number of user requests to the untappd server.  Therefore, for testing purposes of the NearBeer API, I chose to query the Untappd server once and use static data in my NearBeer project.

