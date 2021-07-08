#!/usr/bin/python3
import os
import copy
import json
from flask import Flask, render_template, jsonify, abort, request
from flask_cors import CORS
from .database.models import Beer, Venue, BeerVenue, Style, db_drop_and_create_all, setup_db

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

# database init
db_drop_and_create_all()

#read config file
#app.config.from_object('config')
filename = os.path.join(os.path.dirname(__file__), 'config_settings.json')
with open(filename) as f:
#with app.open_instance_resource('backend/database/config_settings.json') as f:
    config = json.load(f)
    #print (config)
default_city = config['default_location']
#print(f'default_city: {default_city} ')

''' returns list of beers for default city (boulder)
    public view for simple test of api
'''
@app.route("/")
def index(): 
  beers = Beer.query.all()
  #print(beers)
  beers_formatted = [beer.format() for beer in beers]
  return jsonify([{
             "status": 200,
             "beers": beers_formatted,
        }])

''' returns list of beers
'''
@app.route("/beers/")
@app.route("/beers/<city>")
def get_city_beer(city=default_city):
    beers_venue_list = BeerVenue.query.all()
    beers_by_city=[]
  
    for beerItem in beers_venue_list:
        venue=Venue.query.filter_by(id=beerItem.venue_id).all()
        if venue[0].city.lower() == city.lower():
          tempbeer={}
          beer=Beer.query.filter_by(id=beerItem.beer_id).all()
          # Beer class not modifiable so convert to dict and add venue info
          #tempbeer = row2dict(beer[0]) 
          tempbeer = row2dict_lambda(beer[0])
          tempbeer['venue'] = venue[0].format()
          beers_by_city.append(tempbeer)

    return jsonify([{
        "current_city": city,
        "beer_count": len(beers_by_city),
        "beers_by_city": beers_by_city
        }])


'''Endpoint GET /styles
   returns list of styles
'''
@app.route("/styles/")
def get_styles():
    styles = Style.query.all() 
    formatted_styles = [style.format() for style in styles]
    
    return jsonify([{
        "style_count": len(formatted_styles),
        "styles": formatted_styles
        }])

'''Endpoint POST /beers 
   insert new beer object into database
   Specified venue in new beer object must be valid and exist in Venue table
'''
@app.route("/beers/", methods=['POST'])
def create_beer():
    
    body = request.get_json()
    if body==None:
        print("NO BODY")
        abort(400)
    try: 

        # check if beer exists
        print("check if beer exists.")
        beer = Beer.query.filter_by(bid = body['bid'], venue_id=body['venue_id']).one_or_none()
        if beer!=None:
          abort(422)
              
        print("verify venue exists.")      
        venue = Venue.query.filter(Venue.venue_id == body['venue_id']).one_or_none()
        if venue==None:
            abort(400)

        print("Create new beer object")
        new_beer = Beer(
            bid = body['bid'],
            name = body['name'],
            slug = body['slug'],
            style = body['style'],
            brewery_name = body['brewery_name'],
            brewery_slug = body['brewery_slug'],
            last_seen = body['last_seen'],
            major_style = body['major_style'],
            rating = body['rating'],
            abv = body['abv'],
            url = body['url'],
            venue_id = body['venue_id'],
        )
    
        print ("Insert new beer object)")
        new_beer.insert()
        
        print ("return...")
        return jsonify({
            "status_code": 200,
            "success": True,
            "beer": new_beer.format()
        }), 200
    except:
        abort(422)  


'''
Endpoint PATCH /beers/<id>
Require the 'patch:beers' permission
<id> is the existing beer id
Can only update rating of existing beer
Returns update beer with new rating
'''
@app.route('/beers/<int:id>', methods=['PATCH'])
def update_beer(id):
    
    body = request.get_json()
    if body==None:
        print("NO BODY")
        abort(400)
    try: 
        # check if beers exists
        print(f"Verify beer exists.({id})")
        beer = Beer.query.get(id)
        print(f'Beer to be updated: {beer}')
        if beer==None:
          abort(404)
        
    
        updated_rating = body['rating']  
        print(f'New Rating: {updated_rating}') 
        if updated_rating:
            print("rating is valid.")
            beer.rating = updated_rating 
        beer.update()
            
        return jsonify({
            "status_code": 200,
            "success": True,
            "beer": [beer.format()]
        }), 200
    except:
        abort(422) 


'''
Endpoint DELETE /beers/<id>
require the 'delete:beers' permission        
<id> is the existing beer id
returns deleted beer id
'''
@app.route('/beers/<int:id>', methods=['DELETE'])
#@requires_auth('delete:beers')
def delete_beer(id):
    #print(payload)
    # check if beer exists
    beer = Beer.query.filter(Beer.id==id).one_or_none()

    if beer==None:
        abort(404)
    try:       
        beer.delete()
        return jsonify({
            "status_code": 200,
            "success": True,
            "delete": id
        }), 200
    except:
        abort(422)  

''' converts rows to dictionary from list object 
    lambda same as def...just concise version
'''
row2dict_lambda = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
def row2dict(row):
    tempdict = {}
    for column in row.__table__.columns:
        tempdict[column.name] = str(getattr(row, column.name))
    return tempdict
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
