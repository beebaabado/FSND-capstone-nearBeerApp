#!/usr/bin/python3
import os
import pprint
from flask import Flask, render_template, jsonify, abort
from flask_cors import CORS
import untappd

app = Flask(__name__)

# Set up CORS. Allow for all origins.
CORS(app, resources={r"./*": {"origins": "*"}})
@app.after_request
def after_request(response):
  #response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
  response.headers.add('Access-Control-Allow-Headers', 'accept, Content-Type')
  response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, PATCH, DELETE, OPTIONS')
  return (response)


untappd = untappd.Untappd(os.path.dirname(os.path.abspath(__file__)) + '/untappd.json', '/Volumes/untappd/keys.json')
valid_cities = ['boulder', 'minneapolis', 'granite_shoals', 'goleta'] #test data...delete or move to file
current_city = "boulder"

''' returns list of beers for default city (boulder)
'''
@app.route("/")
def index():
  data = untappd.top_beers_near(current_city)
  beers = data['beers']
  venues = data['venues']

  return jsonify([{
             "status": 200,
             "beers": beers,
             "venues": venues,
             "count_beers": len(beers),
             "count_venues": len(venues)
        }])

''' returns list of valid styles and subgroups of styles
'''
@app.route("/styles")
def get_styles():
  styles = untappd.get_styles()

  if len(styles) == 0:
    abort(404)

  return jsonify([{
             "status": 200,
             "styles": styles,
             "count": len(styles)
                }])

''' For testing purposes simple flask template - table view
'''
@app.route("/simple/<city>")
def simple_city_beers(city):
  if city not in valid_cities:
    return render_template("errorMsg.html", message="Oh no...no beers!")
  current_city=city
  beers_venues = untappd.top_beers_near(current_city)
  if len(beers_venues) == 0:
    abort(404)
  return render_template("city_list.html", city=city, beers=beers_venues['beers'], venues=beers_venues['venues'])


''' returns list of beers for specified city, if in valid cities list.
'''
@app.route("/beers/<city>")
def city_beers(city):
  if city not in valid_cities:
    print ("Untappd_server:  city not found.")
    return "Error ... city not supported."
  current_city=city
  data = untappd.top_beers_near(current_city)
  beers = data['beers']
  venues = data['venues']

  return jsonify([{
             "status": 200,
             "beers": beers,
             "venues": venues,
             "count_beers": len(beers),
             "count_venues": len(venues)
        }])

 # --------------------- ERROR handlers TODO add error handling to routes/functions ---------------------------------

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
  app.run(host='0.0.0.0', port=8000, debug=True)
