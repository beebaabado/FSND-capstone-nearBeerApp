#!/bin/bash

echo 'Local setup.sh environment variables'
# local environment variables for FSND Capstone project NearBear.
export AUTH0_DOMAIN='product-demos.us.auth0.com'
export ALGORITHMS='RS256'
export API_AUDIENCE='beernear'

# Environment variables for local development
    
export FLASK_APP='beer_server.py'
export FLASK_ENV='development'
#export POSTGRES_DATABASE_URL='postgresql://postgres@localhost:5432/nearbeer'  
export SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost:5432/nearbeer'
export DATABASE_URI='postgresql://postgres@localhost:5432/nearbeer'
export DATABASE_URI_TEST='postgresql://postgres@localhost:5432/nearbeer'
# For unit testing purposes
export TEST_BREWER_AUTH_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMzNDcwOTg0LCJleHAiOjE2MzM1NTczODQsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.eCiJFLYjrd_wcdiU14DHcOGak9rTTyiC5H-9hhH_na6usZ_KHCkVTZixOfXkw8eoI9PI8ttVnljaJZkcyheUFLQYcIGt3dVQWCbN7bJ0U4-y5qgCq6-DP8RhEODPA7m5AQ_VFjlamwkZaoPDOoWlbEvH3pGZ8WuvQWBKh2lDcfSV4D7faHLN4FMxR0EcNbWra1yDRqR2Kdg82I6Uko3AvN0z2cwaNuJ0Br4gULMR434JXC4a3uoAIVEU83p5ftYx4FqeLRdR5-GTiRCApqVVkizl61rxbFaEmANGEjoqjVW8Be61q7asMk5VL0A8PacpJ7mXuY9QrLgd3hCLZZURzg'
export TEST_BEER_LOVER_AUTH_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NTFjYTg1MjJhMDA2OTEyODhkYyIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMzNDcxOTY1LCJleHAiOjE2MzM1NTgzNjUsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJwYXRjaDpiZWVyLXVzZXItcmF0aW5nIl19.13vX9Mw9eVY9XAvNg7I0yiD7Bi8_ytOD1tRHIqgSndD68QVb9CHkTgvRF-XcwpwfKwe1SkgpDw6HEBQhykKiEoaLuTCt2KIMEgU2_07yBgAaRVq6kcf7ZqSKNwpe9xmXJJHUM-QVsfTqybA-oP46oXleOxDpuhHn9msnR5MAsXA3a36a2tD9-9AU8j3AZESfCH4j-Zo9GVXzd1TsGeXUmRAZCS6-IR7FyFYdkNrBegBU32O2CJsM5U8diLwpzJpHa-z3dRr9R-AvKIMvKNLzyhhD6ignpEM2YMsshRCdD7OqKVHLuHcAp6UOotw7aosPqHFfaP2O5xrvclZnTIhWXQ'
export TEST_INVALID_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjI2MzYwNTM5LCJleHAiOjE2MjYzNjc3MzksImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.qt7Xv8TyJKoqqx-izkMnylx_KVTn9XLVCsET5RmmVQyJs_4yg_wiwpqqwh5W7nxkBUd6tHzMCd3vfrBwOm3Xfdn7iGYqTsBjpSsusuCo0vWlsiCiX73EZi6X6t70lmvEvyZ2L81NVUfBpMc1Yhmo_w9i9srpgys-wZj-QY5Fo77Vsx4Nih5zGR8bTgbWIWBmI1odYmoATTJfNNP3iwlbbigpnAbViU316PI5MFHCaSBWp3Q9NL_Tb6Qd1j41ezj3kPqF0TlGuPo-Lpz1BOxcbDboFnzei8g4nhfFzU1gSNeCUZdeEJViON_2VaVkV0HLaYeRL8xeaP54PUnbzNEySP'


# echo 'NEARBEER VARS'
# echo 'AUTH0_DOMAIN: ' $AUTH0_DOMAIN
# echo 'ALGORITHMS: ' $ALGORITHMS
# echo 'API_AUDIENCE: ' $API_AUDIENCE
# echo 'TEST_BREWER_AUTH_TOKEN: ' $TEST_BREWER_AUTH_TOKEN
# echo 'TEST_BEER_LOVER_AUTH_TOKEN: ' $TEST_BEER_LOVER_AUTH_TOKEN
# echo 'TEST_INVALID_TOKEN: ' $TEST_INVALID_TOKEN
# echo 'FLASK_APP: ' $FLASK_APP
# echo 'FLASK_ENV: ' $FLASK_ENV
# echo 'POSTGRES_DATABASE_URL: ' $POSTGRES_DATABASE_URL
# echo 'SQLALCHEMY_DATABASE_URI: ' $SQLALCHEMY_DATABASE_URI
# echo 'DATABASE_URI: ' $DATABASE_URI
# echo 'DATABASE_URI_TEST: ' $DATABASE_URI_TEST