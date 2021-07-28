# filename: beer_server_unittest.py
# author:  modified by Connie Compos
# date: 07/12/2021
# version number: n/a
# Full Stack Web Developer Nanodegree Nearbeer API Backend unittests
# for testing capstone project API used by Udacity by custom Beer is Near app
# 
# uses temporary auth0 bearer token in config.py 
# must run from package root in folder backend  using command line:
# python -m beerapi.tests.test_beer_server --verbose

import os, sys
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
# for debugging relative imports print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
from ..beer_server import create_app, setup_db
from ..database.models import Beer, Venue, BeerVenue, Style

class BeerServerTestCase(unittest.TestCase):
    """This class represents the near bear server test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        # This function is called before each testcase
        # pass in testmode = True
        self.app = create_app(True)
        
        self.client = self.app.test_client
        #self.database_name = "nearbeer_test"
        #self.database_path = "postgresql://{}@{}/{}".format('postgres', 'localhost:5432', self.database_name)
        #setup_db(self.app, self.database_path) 

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            #self.db.create_all()
        
        # auth token from environment
        #test_brewer = self.app.config['TEST_BREWER_AUTH_TOKEN']
        test_brewer = os.environ.get('TEST_BREWER_AUTH_TOKEN')
        #print(f'BREWER TOKEN: {test_brewer}')
        #test_beer_lover = self.app.config['TEST_BEER_LOVER_AUTH_TOKEN']
        test_beer_lover = os.environ.get('TEST_BEER_LOVER_AUTH_TOKEN')
        #print(f'BEER LOVER TOKEN: {test_beer_lover}')
        #test_invalid_token = self.app.config['TEST_INVALID_TOKEN']
        test_invalid_token = os.environ.get('TEST_INVALID_TOKEN')
        # Create authorization token
        self.headers_beer_lover = [
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {test_beer_lover}')
            ]

        self.headers_brewer = [
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {test_brewer}')
            ]   

        self.headers_invalid = [
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {test_invalid_token}')
            ]   
        # default data
        # get last question in question table for deletion as default
        self.beer_to_delete_id = 0

        self.new_beer = {
            "abv": "12.2", 
            "bid": "555555X", 
            "brewery_name": "Fremont Brewing", 
            "brewery_slug": "fremont-brewing", 
            "last_seen": "2021-05-29 04:11:28", 
            "major_style": "Ale", 
            "name": "Momo Meow Brew 5000 (2021)", 
            "rating": "2.75", 
            "user_rating": "3.00",
            "slug": "fremont-brewing-brew-5000-2021", 
            "style": "Barleywine - English", 
            "url": "https://untappd.com/b/fremont-brewingfremont-brewing-brew-5000-2021/4246950", 
            "venue_id": "5480785"
        }

        self.new_beer2 = {
            "abv": "12.2", 
            "bid": "XXXXXXX", 
            "brewery_name": "Fremont Brewing", 
            "brewery_slug": "fremont-brewing", 
            "last_seen": "2021-05-29 04:11:28", 
            "major_style": "Ale", 
            "name": "Momo Meow Brew 5000 (2021)", 
            "rating": "2.75", 
            "user_rating": "3.00",
            "slug": "fremont-brewing-brew-5000-2021", 
            "style": "Barleywine - English", 
            "url": "https://untappd.com/b/fremont-brewingfremont-brewing-brew-5000-2021/4246950", 
            "venue_id": "5480785"
        }

    def tearDown(self):
        """Executed after reach test"""
        #self.db.drop_all()
        pass

    """
    Test cases run in order of function name
    """

    """
    Public endpoint test cases
    """
    def test_get_beers_public_template(self):
        """ Test GET beers public template endpoint """
        res = self.client().get('/beers/template?city=boulder/')
        self.assertEqual(res.status_code, 200)
        # TODO fix test case this is not correct function self.assertTemplateUseed('city_list.html')
        #self.assertIn("beers", res.data)
        #self.assertIn("city", res.data)

    def test_get_beers_public_template_fail(self):
        """ Test GET beers public template endpoint failure"""
        res = self.client().get('/beers/template')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], "bad request")
        self.assertEqual(data['description'], "City not specified.")
    
    def test_get_beers_public(self):
        """ Test GET beers endpoint without authentication"""
        res = self.client().get('/beers?city=erie')
        data_temp = json.loads(res.data)
        data = data_temp
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['beers'])
        self.assertTrue(len(data['beers']))

    def test_get_beers_public_bad_endpoint_fail(self):
        """ Test GET beers endpoint without authentication bad url failure"""
        res = self.client().get('/beers/')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['error'], 405)
        self.assertTrue(data['message'], "resource not found")    
    
    """
    Endpoint test cases requiring authorization header
    """
    def test_get_beers_with_auth(self):
        """ Test GET beers endpoint with authentication"""
        res = self.client().get('/beers/boulder/', headers=self.headers_brewer)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['beers'])
        self.assertTrue(len(data['beers']))

    def test_get_beers_with_auth_fail(self):
        """ Test GET beers endpoint with authentication...invalid city failure"""
        res = self.client().get('/beers/nocity/', headers=self.headers_brewer)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertTrue(data['message'], "bad request")
        self.assertTrue(data['description'], "No Beers for city nocity.")

    def test_get_beers_with_auth_fail(self):
        """ Test GET beers endpoint with authentication...invalid auth token failure"""
        res = self.client().get('/beers/nocity/', headers=self.headers_invalid)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(data['message'], "bad request")

    def test_get_styles_with_auth(self):
        """ Test GET styles endpoint with authentication"""
        res = self.client().get('/styles/', headers=self.headers_brewer)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['styles'])
        self.assertEqual(len(data['styles']), data['style_count'])

    def test_get_styles_with_auth_fail(self):
        """ Test GET styles endpoint with authentication...invalid auth token failure"""
        res = self.client().get('/styles/', headers=self.headers_invalid)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertTrue(data['message'], "bad request")
    
    def test_get_beer_details_with_auth(self):
        """ Test GET beer details for given beer id"""
        res = self.client().get('/beer-details/', headers=self.headers_brewer, json={'beer_id':'888'})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['beers'])
        self.assertTrue(len(data['beers']))


    def test_get_beer_details_with_auth_fail(self):
        """ Test GET beer details for given invalid beer id failure"""
        res = self.client().get('/beer-details/', headers=self.headers_brewer, json={'beer_id':'10000'})
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], "unprocessable")  

    def test_get_beer_details_with_auth_no_data_fail(self):
        """ Test GET beer details missing beer id failure"""
        res = self.client().get('/beer-details/', headers=self.headers_brewer)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], "bad request")  

    def test_post_new_beer(self):
        """ Test POST new beer """
        res = self.client().post('/beers/', headers=self.headers_brewer, json=self.new_beer)
        data = json.loads(res.data)
        beer = Beer.query.filter(Beer.id==data['created']).one_or_none()  
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['created'], beer.id)  
        self.beer_to_delete_id = beer.id 
    
    def test_post_new_beer_already_exists_fail(self):
        """ Test POST new beer already exists failure"""
        res = self.client().post('/beers/', headers=self.headers_brewer, json=self.new_beer)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], "unprocessable")  
    
    def test_post_new_beer_no_data_fail(self):
        """ Test POST new beer no data failure"""
        res = self.client().post('/beers/', headers=self.headers_brewer)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], "bad request") 

    # NOTE:  named to force post of new beer to happen before trying to delete it
    def test_posted_new_beer_delete_beer(self):
        """ Test DELETE beer with beer id""" 
        # get last beer which was just added in create test case
        beer = Beer.query.order_by(Beer.id.desc()).first()
        if beer:
            self.beer_to_delete_id = beer.id
        delete_path="/beers/" + str(self.beer_to_delete_id) + "/"
        res = self.client().delete(delete_path, headers=self.headers_brewer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], self.beer_to_delete_id)  

    def test_posted_new_beer_delete_beer_fail(self):
        """ Test DELETE beer with invalid beer id failure""" 
        res = self.client().delete('/beers/5000/', headers=self.headers_brewer)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "resource not found")   
        self.assertEqual(data['error'], 404)
    
    def test_post_update_rating(self):
        """ Test update beer rating """
        res = self.client().patch('/rating/', headers=self.headers_brewer, json={ "id":1, "user_rating": "4.25"})
        data = json.loads(res.data)
        beer = Beer.query.filter(Beer.id==data['modified']).one_or_none() 
        self.assertEqual(res.status_code, 200) 
        self.assertEqual(data['modified'], beer.id)
        self.assertEqual(beer.user_rating, 4.25)
        self.assertEqual(data['success'], True)
    
    def test_post_update_rating_fail(self):
        """ Test update beer rating failure """
        res = self.client().patch('/rating/', headers=self.headers_brewer, json={ "id":1, "rating": "4.25"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422) 
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")

    """
    Auth0 Role Beer-lover access control test cases
    """
    def test_1_post_new_beer_role_beer_lover_no_permissions_fail(self):
        """ Test POST new beer no permissions role beer_lover failure"""
        res = self.client().post('/beers/', headers=self.headers_beer_lover, json=self.new_beer2)
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['error'], 401)
        self.assertEqual(data['message'], "Permissions not found.")      
    
    def test_2_get_beers_role_beer_lover(self):
        """ Test GET beers role beer_lover"""
        res = self.client().get('/beers/boulder/', headers=self.headers_beer_lover)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['beers'])
        self.assertTrue(len(data['beers']))

    def test_3_get_beer_details_role_beer_lover(self):
        """ Test GET beer detail role beer_lover"""
        res = self.client().get('/beer-details/', headers=self.headers_beer_lover, json={"beer_id": 2})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['beers'])
        self.assertTrue(len(data['beers']))    
         
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()