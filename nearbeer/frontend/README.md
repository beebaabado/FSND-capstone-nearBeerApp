# The NearBeer Frontend Ionic App


## FOR LOCAL INSTALLATION/TESTING
### Installing dependencies

#### Node

Follow instructions to install the latest version of node for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


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

Role: Brewer
Permissions:

delete:beers      allows user to delete beer from nearbeer database
get:beer-details  

Role: Drinker
Permissions: 


### Requires nearbeer backend app to be up and running

See backend app README [here](../backend/README.md)

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

