INSERT INTO beer(name, abv, slug, stle, bid,) VALUES('Chocolate River Stout');

        "beer_abv": 13.5, 
        "beer_name": "Mulberry White", 
        "beer_slug": "superstition-meadery-mulberry-white", 
        "beer_style": "Mead - Other", 
        "bid": 4317430, 
        "brewery_name": "Superstition Meadery", 
        "brewery_slug": "superstition-meadery", 
        "last_seen": "2021-05-30T04:22:59", 
        "major_style": "Mead", 
        "rating_score": 4.7, 
        "untappd_url": "https://untappd.com/b/superstition-meaderysuperstition-meadery-mulberry-white/4317430", 
        "venue_id": "5237140"
      },  



#in psql : import data from json file (json output from original beer server)
 create temp table tmp (data json);
 insert into tmp values (:'content');
\set content `cat /Users/connie/Desktop/MyProjects/Udacity_coursework/FullStackWebDeveloper/practicecode/udacity-full-stack-web-dev/FSND-capstone-nearBeerApp/nearbeer/backend/database/beers.json`
# I think column names must match for this insert to work
insert into tempbeer select p.* from json_populate_recordset(null::tempbeer, (select data from tmp)) as p;  

#move into beer table
INSERT into beer (beer_abv, beer_name, beer_slug, beer_style, bid,  brewery_name, brewery_slug, last_seen, major_style, rating_score, untappd_url, venue_id) select (beer_abv, beer_name, beer_slug, beer_style, bid,  brewery_name, brewery_slug, last_seen, major_style, rating_score, untappd_url, venue_id) from tempbeer


# specifying fields..example...not valid statement for beer table
insert into beer(id, key, value)
select (data->>'id')::int8, data->>'key', data->>'value' from tmp;

#outside of psql:  single table dump
 pg_dump --table=beer --data-only --column-inserts nearbeer > beertabledump.sql
#restore data
 psql -U postgres -d nearbeer < beertabledump.sql 
# multiple file restore 
psql -U username -d databasename -q -f file1 -f file2
psql -U postgres -d nearbeer -q -f beer_with_user_rating_dump.sql -f venuetabledump.sql -f styletabledump.sql -f beervenuetabledump.sql

# set content variable to venues json data 
\set content `cat /Users/connie/Desktop/MyProjects/Udacity_coursework/FullStackWebDeveloper/practicecode/udacity-full-stack-web-dev/FSND-capstone-nearBeerApp/nearbeer/backend/database/venues.json`
# Extract nexted json data
# NOTE: ->  operator to extract json, ->> to get text 
# gives back all key/values for each venue
SELECT * , tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) ->> 'venue_name' AS venue
FROM tmp;

# gives back list of venue ids
SELECT json_object_keys((tmp.data ->> 'venues')::json) FROM tmp;

# gives back list of venue names 
SELECT  tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) ->> 'venue_name' AS venue_name
FROM tmp;

# combine the two in one select to get id and venue ... wordy but for now works for my purposes...use to get all value to populuate tempvenue columns
SELECT json_object_keys((tmp.data ->> 'venues')::json) , tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) ->> 'venue_name' as venue_name
FROM tmp;


INSERT into tempvenue ( venue_id, venue_name, venue_slug, lng, lat, venue_city, venue_state, venue_address, venue_country)
SELECT json_object_keys((tmp.data ->> 'venues')::json) as "venue_id",
tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) ->> 'venue_name' as venue_name,
tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) ->> 'venue_slug' as venue_slug, 
(tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) -> 'location' ->> 'lng')::numeric(10,7) as lng,
(tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) -> 'location' ->> 'lat')::numeric(10,7) as lat,
tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) -> 'location' ->> 'venue_city' as venue_city,
tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) -> 'location' ->> 'venue_state' as venue_state,
tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) -> 'location' ->> 'venue_address' as venue_address,
tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) -> 'location' ->> 'venue_country' as venue_country
tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::josn) -> 'beer_id' ->> '
FROM tmp;


# example of getting nested json 
SELECT json_object_keys((tmp.data ->> 'venues')::json) as venue_id, 
(tmp.data -> 'venues' -> json_object_keys((tmp.data ->> 'venues')::json) -> 'location' ->> 'lng')::numeric(10,7) as lng 
from tmp;

# Transfer temp venue to venue table
# Note no parens for SELECT fields...leads to syntax error where number of insert items don't match  it could be that if the columns names are exactly the same then you can use parens???
INSERT into venue ( venue_id, name, slug, lng, lat, city, state, address, country) SELECT  venue_id, venue_name, venue_slug, lng, lat, venue_city, venue_state, venue_address, venue_country from tempvenue;

# using flask migrate
To create initial migration start with empty database.  I dropped the database and recreated it to clear schema.
Then ran 
flask db migrate -m "message"
check version file under versions folder
flask db upgrade
use psql to make sure tables created
Now each time change db schema run db migrate and db upgrade process


# arrays to strings (note like in json file array to string in postgres)
create temp table tmp (data json);
\set content `cat /Users/connie/Desktop/MyProjects/Udacity_coursework/FullStackWebDeveloper/practicecode/udacity-full-stack-web-dev/FSND-capstone-nearBeerApp/nearbeer/backend/database/beerdata/styles.json`
insert into tmp values (:'content');
create table tempstyles ( major varchar(25), patterns text array);
insert into tempstyles select p.* from json_populate_recordset(null::tempstyles, (select data from tmp)) as p;
insert into style (major, sub_styles) select major, array_to_string(patterns, ',') from tempstyles;

# RUNNING ionic / angular  in emulator 
## For Android
ionic capacitor run android -l --external

# insert data into beervenue association table

# saving to heroku remote
git add .
git commit -m " comment "
# Make sure to run this from the top level of the tree:
git subtree push --prefix nearbeer/backend heroku main
git push using:  heroku main

# sending access token in url example
https://base.url?access_token=f4f4994a875f461ca4d7708b9e027df4

# using curl
curl -X GET \
  'https://baseurl/endpoint/' \
  -H 'authorization: Basic dXNlcm5hbWU6MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MA==' 

# test from heroku app, will need to update access tokens
 
# from local server

get list of beers

curl -X GET  'http://127.0.0.1:5000/' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMxNjY5OTg4LCJleHAiOjE2MzE3NTYzODgsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.fk0y9PsQZkf6Pzi6I6qcoBFz6LqRGS6MmeBfTBW0qtgt2FMMCHmZhJGifW-WZxt2fmBIv7cj_f5TthELwhKJfNW4wHmj2qQnAJ2AUUnDYzcIuV08S8yHmGvWEEOAzOmN4zrF6pnxVrWXMBsipTnb5tvl2WfyRCSY95r2x1nseSeAl7MjIElPA6UZYv3aL9ufsiwqSuDwINROPeKEldpUWLgAbZeuvMqrbGiwQeQR7ku2O3etivNDzR2zdaZs3GH5jVq1xJu8RrCUZSFrluIp8yP0JqGwNzUio91sHvfn9W2N6EidM0GHFLjwNffOjQNrlmQJOsFt2jLhPjOcT1uljw'

# Get no auth needed
curl -X GET  'https://capstone-nearbeer-app.herokuapp.com/beers?city=lyons'


# Get with auth
curl -X GET  'https://capstone-nearbeer-app.herokuapp.com/'  -H 'authorization: Bearer  eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMxODE5Mzg4LCJleHAiOjE2MzE5MDU3ODgsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.CpNAH5XGNQTpKVdJ15FOZGvMIOY57Aye6tw7_uqYekoOmifVJDbUAA_9CHvVOUerYtKp6MIHR9Ask_mbAA5n9y40uyfNL1r0dLgUi-Yq-pJ8yC5K_bkwr_p9HAlPT0VrLrz-wcfY-hjOSgpbgUGVcZZmb4LrJH1mf6eIkTaIXTQrJ5mdYpCP-LLq6IXwLitmoFoOw3KeZxvw4-tBgTMCDpsIQ7twIB_kgEs1HuQKJADQekJVKSqN07_0eOWKHoeuup04zkh7vsWA9k0Ul0CBcKHvV1RP-ppw7KUMBkZaXPp9Xz1_J-FoD0wKvWFfERBWlir9BKOct3Hy7ZAI2zxzqA'

curl -X GET  'https://capstone-nearbeer-app.herokuapp.com/beers' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMxNjY5OTg4LCJleHAiOjE2MzE3NTYzODgsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.fk0y9PsQZkf6Pzi6I6qcoBFz6LqRGS6MmeBfTBW0qtgt2FMMCHmZhJGifW-WZxt2fmBIv7cj_f5TthELwhKJfNW4wHmj2qQnAJ2AUUnDYzcIuV08S8yHmGvWEEOAzOmN4zrF6pnxVrWXMBsipTnb5tvl2WfyRCSY95r2x1nseSeAl7MjIElPA6UZYv3aL9ufsiwqSuDwINROPeKEldpUWLgAbZeuvMqrbGiwQeQR7ku2O3etivNDzR2zdaZs3GH5jVq1xJu8RrCUZSFrluIp8yP0JqGwNzUio91sHvfn9W2N6EidM0GHFLjwNffOjQNrlmQJOsFt2jLhPjOcT1uljw'

# Add a new beer POST use local db

curl -X POST  http://127.0.0.1:5000/beers/ -H "Content-type: application/json" -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMxODk1OTMyLCJleHAiOjE2MzE5ODIzMzIsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.fBzNgVAuCpv2dU94PSHGhgmx_aXsKZ9WomvRaMw5IB6rWMIZvjustfwVwgg_Ae94IsgQuA47EXjLjIrbdOTMCiB8Qeyns4tGZpD1ywRhPVz5hrxcVZZBDaIJ7LYJddzmwJHHlYNPmS9QQNqSBiO5cqJlLTwI_Gd-iKTGqGVaT-eeSae0Yp3RQB0-WcvNYHhsBAxlLmJuc2mb8l0FVOKYl23jyLNZx8busZg3zN1CkXA6sCvo6H4agNWJF0uyHuE3k6rfo3QMcaQfgIzPAGzbaI1bn03HNwbAFmfytbk9JK8fh11N2cMIMNlpa-GVzy0uaPriAfXg3IRZ9OTNJqvdyg'  -d '{"abv":"12.2", "bid":"555555X", "brewery_name":"Fremont Brewing", "brewery_slug":"fremont-brewing", "last_seen":"2021-05-29 04:11:28", "major_style":"Ale", "name":"Momo Meow Brew 5000 (2021)", "rating":"2.75", "user_rating":"3.00","slug":"fremont-brewing-brew-5000-2021", "style":"Barleywine - English", "url":"https://untappd.com/b/fremont-brewingfremont-brewing-brew-5000-2021/4246950", "venue_id":"5480785"}'

# Delete a beer by id
curl -X DELETE -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMxODk1OTMyLCJleHAiOjE2MzE5ODIzMzIsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.fBzNgVAuCpv2dU94PSHGhgmx_aXsKZ9WomvRaMw5IB6rWMIZvjustfwVwgg_Ae94IsgQuA47EXjLjIrbdOTMCiB8Qeyns4tGZpD1ywRhPVz5hrxcVZZBDaIJ7LYJddzmwJHHlYNPmS9QQNqSBiO5cqJlLTwI_Gd-iKTGqGVaT-eeSae0Yp3RQB0-WcvNYHhsBAxlLmJuc2mb8l0FVOKYl23jyLNZx8busZg3zN1CkXA6sCvo6H4agNWJF0uyHuE3k6rfo3QMcaQfgIzPAGzbaI1bn03HNwbAFmfytbk9JK8fh11N2cMIMNlpa-GVzy0uaPriAfXg3IRZ9OTNJqvdyg' http://127.0.0.1:5000/beers/1037/
# To run the server, execute:
# Run in same venv as app, in backend directory to export Auth0 variables (domain, audience, algorithms, tokens/secrets):
# run setup.sh to put token into environment variables
```bash
 . ./setup.sh 
```

```bash
flask run --reload
```



# updating frontend for heroku  use subtree for frontend app
git commit -am "update Procfile for frontend with correct startup command yet...try again"
git subtree push --prefix nearbeer/frontend heroku-frontend main
git subtree push --prefix nearbeer/backend heroku-backend main

# running heroku session in bash
heroku run bash -a <heroku app name> 

#run flask unittests from project root
