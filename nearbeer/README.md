Let's always drink the best beer

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

To run the server, first run setup.sh to export necessary envrinment variables. Run in same venv as app, in backend directory to export Auth0 variables (domain, audience, algorithms, tokens/secrets):

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

## NearBeer frontend 

The NearBeer App 

# Acknowledgements

The data stored in the NearBear Postgres database was obtained via the untappd API [untappd.com].  There is a separate REST API that I created to pull beer data from Untappd.  This other API was left out of this project because it involves a limited number of user requests to the untappd server.  Therefore, for testing purposes of the NearBeer API, I chose to query the Untappd server once and use static data in my NearBeer project.

