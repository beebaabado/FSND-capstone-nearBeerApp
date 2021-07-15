#!/usr/bin/python3
import os
import json
from flask import Flask, render_template, jsonify, abort, request
from flask_cors import CORS
from .database.models import Beer, Venue, BeerVenue, Style, db_drop_and_create_all, setup_db
from .auth.auth import AuthError, requires_auth

def create_app(testconfig=None):

    app = Flask(__name__)

    #print(f'APP NAME: {__name__}')
    # debug relative imports issue print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
    app.config.from_pyfile('config.py')
    setup_db(app)
    
    # Set up CORS. Allow for all origins.
    CORS(app, resources={r"./*": {"origins": "*"}})
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        #response.headers.add('Access-Control-Allow-Headers', 'accept, Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, PATCH, DELETE, OPTIONS')
        return (response)

    '''
    uncomment the following line to initialize the datbase
    !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
    !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
    !! NOTE Make sure in folder backend/database and run command to fill database before accessing server:
    !! NOTE psql -U postgres -d nearbeer -q -f beer_with_user_rating_dump.sql -f venuetabledump.sql -f styletabledump.sql -f beervenuetabledump.sql
    '''
    #db_drop_and_create_all()

    #read beer config file...not app config file
    filename = os.path.join(os.path.dirname(__file__), 'config_settings.json')
    with open(filename) as f:
    #with app.open_instance_resource('backend/database/config_settings.json') as f:
        config = json.load(f)
        #print (config)
    default_city = config['default_location']
    #print(f'default_city: {default_city} ')

    ''' returns public view of list of beers for particular city using template
    '''
    @app.route("/beers/<city>/", methods=['GET'])
    def get_city_beer_public_view(city=default_city):
        beers_venue_list = BeerVenue.query.all()
        #print(beers_venue_list)
        beers_by_city=[]
    
        for beerItem in beers_venue_list:
            venue=Venue.query.filter_by(id=beerItem.venue_id).all()
            #print(f'Venue city: {venue[0].city}')
            if venue[0].city.lower() == city.lower():
                tempbeer={}
                beer=Beer.query.filter_by(id=beerItem.beer_id).all()
                # Beer class not modifiable so convert to dict and add venue info
                #tempbeer = row2dict(beer[0]) 
                tempbeer = row2dict_lambda(beer[0])
                tempbeer['venue'] = venue[0].format()
                beers_by_city.append(tempbeer)

        # return jsonify([{
        #     "status_code": 200,
        #     "success": True,
        #     "current_city": city,
        #     "beer_count": len(beers_by_city),
        #     "beers": beers_by_city,
        #     }])

        return render_template('city_list.html', city=city, beers=beers_by_city)  


    ''' returns list of all beers
        admin view for simple test of api
    '''
    @app.route("/", methods=['GET'])
    @requires_auth('view:simple')
    #def index(payload): 
    def index(): 
        beers = Beer.query.all()
        #print(beers)
        beers_formatted = [beer.format() for beer in beers]
        return jsonify({
                    "status": 200,
                    "beers": beers_formatted,
                })

    ''' returns list of beers
    '''
    @app.route("/beers/<city>/", methods=['GET'])
    @requires_auth('get:beers')
    def get_city_beer(payload, city=default_city):
        print(payload)
        beers_venue_list = BeerVenue.query.all()
        print(beers_venue_list)
        beers_by_city=[]
    
        for beerItem in beers_venue_list:
            venue=Venue.query.filter_by(id=beerItem.venue_id).all()
            print(f'Venue city: {venue[0].city}')
            if venue[0].city.lower() == city.lower():
                tempbeer={}
                beer=Beer.query.filter_by(id=beerItem.beer_id).all()
                # Beer class not modifiable so convert to dict and add venue info
                #tempbeer = row2dict(beer[0]) 
                tempbeer = row2dict_lambda(beer[0])
                tempbeer['venue'] = venue[0].format()
                beers_by_city.append(tempbeer)

        return jsonify({
            "status_code": 200,
            "success": True,
            "current_city": city,
            "beer_count": len(beers_by_city),
            "beers": beers_by_city
            })

    '''
    Endpoint GET /beer-details   Detail for one beer specifed by beer id - with 
    '''
    @app.route('/beer-details/', methods=['GET'])
    @requires_auth('get:beer-details')
    def get_beer_detail(payload):
    #print(payload)
        
        body = request.get_json()
        if body==None:
            print("NO BODY")
            abort(400)
        try: 
            print('BEERID')
            beer = Beer.query.filter(Beer.id==body['beer_id']).one_or_none()
            if beer == None:
                abort(404) 

            return jsonify({
                "status_code": 200,
                "success": True,
                "beers": beer.format()
            }), 200
        except:
            abort(422)

    '''Endpoint GET /styles
    returns list of styles
    '''
    @app.route("/styles/")
    @requires_auth('get:styles')
    def get_styles(payload):
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
    @requires_auth('get:beers')
    def create_beer(payload):
        
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
    Can only update uwer_rating of existing beer
    Returns update beer with new rating
    '''
    @app.route('/beers/<int:id>/', methods=['PATCH'])
    @requires_auth('patch:beer-user-rating')
    def update_beer(payload, id):
        
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
            
        
            updated_rating = body['user_rating']  
            print(f'New Rating: {updated_rating}') 
            if updated_rating:
                print("user rating is valid.")
                beer.user_rating = updated_rating 
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
    @app.route('/beers/<int:id>/', methods=['DELETE'])
    @requires_auth('delete:beers')
    def delete_beer(payload, id):
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
        lambda same as def ...just concise version
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


    '''
    error handler for AuthError
    '''
    @app.errorhandler(AuthError)
    def auth_error(ex):
        return jsonify({
            "success": False,
            "error": ex.status_code,
            "message": ex.error['description']
        }), ex.status_code
        
    
    #if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=5000, debug=True)

    return app