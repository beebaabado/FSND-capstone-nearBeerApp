#!/bin/bash
# local environment variables for FSND Capstone project NearBear.
export NEAR_BEER_ENV='local'
export AUTH0_DOMAIN='product-demos.us.auth0.com'
export ALGORITHMS='RS256'
export API_AUDIENCE='beernear'
export FLASK_APP='beer_server.py'
export FLASK_ENV='development'
export SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost:5432/nearbeer'
export DATABASE_URI='postgresql://postgres@localhost:5432/nearbeer'
export DATABASE_URI_TEST='postgresql://postgres@localhost:5432/nearbeer'
# For unit testing purposes
export TEST_BREWER_AUTH_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMzNTIyMDIyLCJleHAiOjE2MzM2MDg0MjIsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.ZrzhVG5hO_1MviO4H759eUBzMCQkH7CttOKzXhqa00y9lDpwTjn9lJ-gRV5wnZcQSLXdmHHdgYAFQEqPI9aYuX-yjt3zClynk8WyQ7eaVTxaiEoOwCUXQ6ikh0TJcknT0FagHXU1BNb2mNx67UMX0hML4kYz1GG4KZrezBF2L1vQDCD036UD0PCE5ee0X2-mxKHo0h8xvbjIQm2IcUz20NhtrAchxs-f5SF3oxRsAT75rBlM8soLnbe6iYAaW-ojf3BSyDwFaV85H6-J93-RhBA15hUNN-VwZHTtk3ot4kmBypiemq58Q0rkrJx5R57N-Ol8Sqmd0UDz7JIzp_X_Ow'
export TEST_BEER_LOVER_AUTH_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NTFjYTg1MjJhMDA2OTEyODhkYyIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMzNTIzMjU1LCJleHAiOjE2MzM2MDk2NTUsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJwYXRjaDpiZWVyLXVzZXItcmF0aW5nIl19.kHhelGX5qDC-NHm-jLHm7-ItqapEp6GPV5oDJtbR6GJuvMqmYpVj0kXB2lMIKb6ffzCyhVGW3mHH3FPERF4fuVaSjv2Y_JrtB0V3VZWc62i6MCqENZtIVwp_YqU894FWz2IRE3GXGKcQOj2P5xEp5hJ6nFGVcRzhzjMUpciyveLMscbi0wL9oVuA1NICrLlAsAPHYBHmuyrwytGirI3A8tGLIDqm4elsZpxky6m2La62dnfynVJMKBVJB6XRivyTBBW6bWBx7hymOEVHIEdbTSdXXhDkOFvhE8rK7azE-5v64S_adtRp7mI9ZOSXGYPHixMvtKTsuAI9QqCqlksDyQ'
export TEST_INVALID_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjI2MzYwNTM5LCJleHAiOjE2MjYzNjc3MzksImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.qt7Xv8TyJKoqqx-izkMnylx_KVTn9XLVCsET5RmmVQyJs_4yg_wiwpqqwh5W7nxkBUd6tHzMCd3vfrBwOm3Xfdn7iGYqTsBjpSsusuCo0vWlsiCiX73EZi6X6t70lmvEvyZ2L81NVUfBpMc1Yhmo_w9i9srpgys-wZj-QY5Fo77Vsx4Nih5zGR8bTgbWIWBmI1odYmoATTJfNNP3iwlbbigpnAbViU316PI5MFHCaSBWp3Q9NL_Tb6Qd1j41ezj3kPqF0TlGuPo-Lpz1BOxcbDboFnzei8g4nhfFzU1gSNeCUZdeEJViON_2VaVkV0HLaYeRL8xeaP54PUnbzNEySP'

echo 'NEARBEER LOCAL env vars from setup_local.sh'
echo 'AUTH0_DOMAIN: ' $AUTH0_DOMAIN
echo 'ALGORITHMS: ' $ALGORITHMS
echo 'API_AUDIENCE: ' $API_AUDIENCE
echo 'TEST_BREWER_AUTH_TOKEN: ' $TEST_BREWER_AUTH_TOKEN
echo 'TEST_BEER_LOVER_AUTH_TOKEN: ' $TEST_BEER_LOVER_AUTH_TOKEN
echo 'TEST_INVALID_TOKEN: ' $TEST_INVALID_TOKEN
echo 'FLASK_APP: ' $FLASK_APP
echo 'FLASK_ENV: ' $FLASK_ENV
echo 'SQLALCHEMY_DATABASE_URI: ' $SQLALCHEMY_DATABASE_URI
echo 'DATABASE_URI: ' $DATABASE_URI
echo 'DATABASE_URI_TEST: ' $DATABASE_URI_TEST