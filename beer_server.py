#!/usr/bin/python3
import os
import pprint
from flask import Flask, render_template, jsonify, abort
from flask_cors import CORS
from .database.models import Beer, Venue, db_drop_and_create_all, setup_db

app = Flask(__name__)
setup_db(app)

# Set up CORS. Allow for all origins.
CORS(app, resources={r"./*": {"origins": "*"}})
@app.after_request
def after_request(response):
  #response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
  response.headers.add('Access-Control-Allow-Headers', 'accept, Content-Type')
  response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, PATCH, DELETE, OPTIONS')
  return (response)


db_drop_and_create_all()

''' returns list of beers for default city (boulder)
'''
@app.route("/")
def index(): 
  
  beers = Beer.query.all()
  print(beers)
  beers_formatted = [beer.format() for beer in beers]
  return jsonify([{
             "status": 200,
             "beers": beers_formatted,
        }])

# --------------------- ERROR handlers ---------------------------------
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
         "success": False,
         "error": 422,
         "message": "unprocessable"
    }), 422

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
         "success": False,
         "error": 400,
         "message": "bad request"
    }), 400

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
          "success": False,
          "error": 405,
          "message": "method not allowed"
    }), 405


@app.errorhandler(500)
def method_not_allowed(error):
    return jsonify({
          "success": False,
          "error": 500,
          "message": "Internal Server Error"
    }), 500


  
if __name__ == "__main__":
  app.run(host='127.0.0.1', port=5000, debug=True)
