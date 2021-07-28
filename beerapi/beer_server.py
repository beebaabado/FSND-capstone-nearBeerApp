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
    if testconfig==True:
        app.config['TESTING']=True
    else:
        app.config['TESTING']=False
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

    # beer config file...not app config file
    filename = os.path.join(os.path.dirname(__file__), 'config_settings.json')
    with open(filename) as f:
        config = json.load(f)
    default_city = config['default_location']

    ''' returns public view of list of beers for particular city using simple jinja2 template no authorization
    '''
    @app.route("/beers/template", methods=['GET'])
    def get_city_beer_public_template_view():
        beers_venue_list = BeerVenue.query.all()
        beers_by_city=[]
        
        city = request.args.get('city')
        if city==None:
            abort(400, "City not specified.")

        for beerItem in beers_venue_list:
            venue=Venue.query.filter_by(id=beerItem.venue_id).all()
            if venue[0].city.lower() == city.lower():
                tempbeer={}
                beer=Beer.query.filter_by(id=beerItem.beer_id).all()
                # Beer class not modifiable error so convert to dict and add venue info
                tempbeer = row2dict_lambda(beer[0])
                tempbeer['venue'] = venue[0].format()
                beers_by_city.append(tempbeer)

        return render_template('city_list.html', city=city, beers=beers_by_city)  
 
    ''' returns json formatted list of beers public view for front end no authorization
    '''
    @app.route("/beers", methods=['GET'])
    def get_city_beer_public_view():
        beers_venue_list = BeerVenue.query.all()
        beers_by_city=[]
        
        city = request.args.get('city')
        if city==None:
            abort(400, "City not specified.")

        for beerItem in beers_venue_list:
            venue=Venue.query.filter_by(id=beerItem.venue_id).all()
            if venue[0].city.lower() == city.lower():
                tempbeer={}
                beer=Beer.query.filter_by(id=beerItem.beer_id).all()
                # Beer class not modifiable so convert to dict and add venue info
                tempbeer = row2dict_lambda(beer[0])
                tempbeer['venue'] = venue[0].format()
                beers_by_city.append(tempbeer)

        if beers_by_city == []:
            abort(400, f'No beers for city {city}.')

        return jsonify({
            "status_code": 200,
            "success": True,
            "current_city": city,
            "beer_count": len(beers_by_city),
            "beers": beers_by_city
            })

    ''' returns list of all beers
        admin view for simple test of api
    '''
    @app.route("/", methods=['GET'])
    @requires_auth('view:simple')
    def index(payload): 
        beers = Beer.query.all()
        beers_formatted = [beer.format() for beer in beers]
        return jsonify({
                    "status_code": 200,
                    "success": True,
                    "beers": beers_formatted,
                })

    ''' 
        returns list of beers 
        city defaults to default_location in config_setings.json
    '''
    @app.route("/beers/<city>/", methods=['GET'])
    @requires_auth('get:beers')
    def get_city_beer(payload, city=default_city):
        beers_venue_list = BeerVenue.query.all()
        beers_by_city=[]
    
        for beerItem in beers_venue_list:
            venue=Venue.query.filter_by(id=beerItem.venue_id).all()
            if venue[0].city.lower() == city.lower():
                tempbeer={}
                beer=Beer.query.filter_by(id=beerItem.beer_id).all()
                # Beer class not modifiable so convert to dict and add venue info
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
    Endpoint GET /beer-details/   Detail for one beer specifed by beer id
    '''
    @app.route('/beer-details/', methods=['GET'])
    @requires_auth('get:beer-details')
    def get_beer_detail(payload):
     
        body = request.get_json()
        if body==None:
            print("NO BODY")
            abort(400)
        try: 
            beer = Beer.query.filter(Beer.id==body['beer_id']).one_or_none()
            if beer == None:
                abort(404, "Beer not found.") 

            return jsonify({
                "status_code": 200,
                "success": True,
                "beers": beer.format() 
            }), 200
        except:
            abort(422)

    '''Endpoint GET /styles/ returns list of styles
    '''
    @app.route("/styles/")
    @requires_auth('get:styles')
    def get_styles(payload):
        styles = Style.query.all() 
        formatted_styles = [style.format() for style in styles]
        
        return jsonify({
            "status_code": 200,
            "success": True,
            "style_count": len(formatted_styles),
            "styles": formatted_styles
            })

    '''Endpoint POST /beers 
       insert new beer object into database
       Specified venue in new beer object must be valid and exist in Venue table
    '''
    @app.route("/beers/", methods=['POST'])
    @requires_auth('post:beers')
    def create_beer(payload): 
        body = request.get_json()
        if body==None:
            print("NO BODY")
            abort(400)
        try: 

            # check if beer exists
            beer = Beer.query.filter(Beer.bid == body['bid'], Beer.venue_id==body['venue_id']).one_or_none()   
            if beer!=None:
                abort(400, "Create_beer: Beer already exists.")  

            venue = Venue.query.filter(Venue.venue_id == body['venue_id']).one_or_none() 
            if venue==None:
                abort(400, "Create_beer: Venue not found.")

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
                user_rating = body['user_rating'],
                abv = body['abv'],
                url = body['url'],
                venue_id = body['venue_id'],
            )
        
            new_beer.insert()
            new_beervenue = BeerVenue(
                beer_id = new_beer.id,
                venue_id = venue.id
            )
            new_beervenue.insert()
    
            return jsonify({
                "status_code": 200,
                "success": True,
                "created": new_beer.id
            }), 200
        except:
            abort(422)  


    '''
    Endpoint PATCH /rating/
    Require the 'patch:beer-user-rating' permission
    <id> is the existing beer id
    Can only update uwer_rating of existing beer
    Returns update beer with new rating
    '''
    @app.route('/rating/', methods=['PATCH'])
    @requires_auth('patch:beer-user-rating')
    def update_beer(payload):
        
        body = request.get_json()
        if body==None:
            print("NO BODY")
            abort(400)
        try: 
            # check if beers exists
            beer = Beer.query.get(body['id'])
            if beer==None:
                abort(404, "Update beer: beer not found.")
            
            updated_rating = body['user_rating']  
            if updated_rating:
                beer.user_rating = updated_rating 
            beer.update()
                
            return jsonify({
                "status_code": 200,
                "success": True,
                "modified": beer.id
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
        # check if beer exists
        beer = Beer.query.filter(Beer.id==id).one_or_none()

        if beer==None:
            abort(404, "Delete beer: Beer not found.")

        venue = Venue.query.filter(Venue.venue_id == beer.venue_id).one_or_none()
        if venue==None:
            abort(404, "Delete beer: Venue not found.")
        
        beervenue = BeerVenue.query.filter(BeerVenue.venue_id == venue.id, BeerVenue.beer_id == beer.id).one_or_none()
        if beervenue==None:
            abort(404, "Delete beer: Beer, Venue record not found.")
        print(f"beer_server::delete_beer::beervenue: { beervenue.beer_id, beervenue.venue_id}")
        try:       
            
            beervenue.delete()
            beer.delete()
            
            return jsonify({
                "status_code": 200,
                "success": True,
                "deleted": id
            }), 200


        except:
            abort(422)  

    ''' converts rows to dictionary from list object 
        lambda same as def ...just concise version
    '''
    row2dict_lambda = lambda row: {c.name: str(getattr(row, c.name)) for c in row.__table__.columns}
    # def row2dict(row):
    #     tempdict = {}
    #     for column in row.__table__.columns:
    #         tempdict[column.name] = str(getattr(row, column.name))
    #     return tempdict

    # --------------------- ERROR handlers ---------------------------------
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found",
            "description": error.description
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable",
            "description": error.description
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request",
            "description": error.description
        }), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed",
            "description": error.description
        }), 405


    @app.errorhandler(500)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error",
            "description": error.description
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