import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# COMPLETED IMPLEMENT DATABASE URL and set other options for SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/nearbeer'
# Prevent warning concerning use of Flask-SQLAlchemy event system causing overhead in memory usage
SQLALCHEMY_TRACK_MODIFICATIONS = False

# For unit testing purposes 
TEST_BREWER_AUTH_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjI2MzIyODMwLCJleHAiOjE2MjYzMzAwMzAsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.m3nNM0QMJ1eAviJHNUugXAUlWuvOU3t16zGRezFzBqUqDK1i4QWL4QNNr3EHqQyDRUEWbkEoH6xRwXTSQ8tOxixj9Pt-Z2SXf3ZX9VpeSZMbvetm7Q9VCUJuiUkgpnhURwOIMPfthwPaTuEd9vf30NcyqcTcOWzMQqxI45s0TcdIxfAMXl_lJpx0Uw8QnTMc8nZKJXbIkK90ZnVxqmKWXBZgL-QW05q5A5Gz4IjM8ekPXWPi19F3kMSJGu4bufl4EtP9ALR82YAj2IZEWUr-f_s3zLO1ypKjkgKiRJZY9jOw_8wjeRu7OZjMPlRwuG0UbaSx-6oc3CyIinyMOWBECQ'
TEST_BEER_LOVER_AUTH_TOKEN = ''
