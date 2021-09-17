# This script creates/resets the near beer database and inserts test data 
# Must be run from the nearbeer/backend folder

# Drops database first
psql -U postgres -c "DROP DATABASE nearbeer"

# Create nearbear databsse 
psql -U postgres -c "CREATE DATABASE nearbeer"

# run migrations to create tables in database
export FLASK_APP='beer_server.py'
flask db upgrade

# insert test data
psql -U postgres -d nearbeer -q -f database/beerdata/sql/beer_with_user_rating_dump.sql -f database/beerdata/sql/venuetabledump.sql -f database/beerdata/sql/styletabledump.sql -f database/beerdata/sql/beervenuetabledump.sql 
