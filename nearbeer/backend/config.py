''' Configuration file for Nearbeer App
'''
import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TESTING = False

# HEROKU database DO NOT REMOVE
SQLALCHEMY_DATABASE_URI='postgresql://tymiuxxwxkccqf:b137e9dbb038c08b2b8da273150f2da4556a5ac2bcce1fe5375be98106b078ab@ec2-52-203-74-38.compute-1.amazonaws.com:5432/d9qq2ri9p09bh1'
DATABASE_URI='postgresql://tymiuxxwxkccqf:b137e9dbb038c08b2b8da273150f2da4556a5ac2bcce1fe5375be98106b078ab@ec2-52-203-74-38.compute-1.amazonaws.com:5432/d9qq2ri9p09bh1'

# Prevent warning concerning use of Flask-SQLAlchemy event system causing overhead in memory usage
SQLALCHEMY_TRACK_MODIFICATIONS = False

# For unit testing purposes moved to setup.sh file
#DATABASE_URI_TEST='postgresql://postgres@localhost:5432/nearbeer'
