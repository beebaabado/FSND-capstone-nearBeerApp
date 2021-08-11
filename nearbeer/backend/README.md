run in same venv as app:

 . ./setup.sh in backend directory to export  Auth0 variables (domain, audience, algorithms, tokens/secrets) 


 from parent directory (in nearbeer directory) run :
 python -m backend.tests.test_beer_server --verbose




 # Acknowledgements

 The data stored in the NearBear Postgres database was obtained via the untappd API [untappd.com].  There is a separate REST API that I created to pull beer data from Untappd.  This other API was left out of this project because it involves a limited number of user requests to the untappd server.  Therefore, for testing purposes of the NearBeer API, I chose to query the Untappd server once and use static data in my NearBeer project.

