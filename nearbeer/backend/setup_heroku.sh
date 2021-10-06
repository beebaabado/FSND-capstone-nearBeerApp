#!/bin/bash
# Heroku environment variables for FSND Capstone project NearBear.
export AUTH0_DOMAIN='product-demos.us.auth0.com'
export ALGORITHMS='RS256'
export API_AUDIENCE='beernear'
export SQLALCHEMY_DATABASE_URI='postgresql://tymiuxxwxkccqf:b137e9dbb038c08b2b8da273150f2da4556a5ac2bcce1fe5375be98106b078ab@ec2-52-203-74-38.compute-1.amazonaws.com:5432/d9qq2ri9p09bh1'
export DATABASE_URI='postgresql://tymiuxxwxkccqf:b137e9dbb038c08b2b8da273150f2da4556a5ac2bcce1fe5375be98106b078ab@ec2-52-203-74-38.compute-1.amazonaws.com:5432/d9qq2ri9p09bh1'

echo 'NEARBEER HEROKU env vars from setup_heroku.sh'
echo 'AUTH0_DOMAIN: ' $AUTH0_DOMAIN
echo 'ALGORITHMS: ' $ALGORITHMS
echo 'API_AUDIENCE: ' $API_AUDIENCE
echo 'SQLALCHEMY_DATABASE_URI: ' $SQLALCHEMY_DATABASE_URI
echo 'DATABASE_URI: ' $DATABASE_URI
