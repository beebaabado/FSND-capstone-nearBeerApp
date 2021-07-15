# filename: beer_server_unittest.py
# author:  modified by Connie Compos
# date: 07/12/2021
# version number: n/a
# Full Stack Web Developer Nanodegree Nearbeer API Backend unittests
# for testing capstone project API used by Udacity by custom Beer is Near app
# 
# must run from package root in folder backend

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
        
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "nearbeer_test"
        self.database_path = "postgresql://{}@{}/{}".format('postgres', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path) 

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            #self.db.create_all()
        
        # auth token from environment
        test_brewer = self.app.config['TEST_BREWER_AUTH_TOKEN']
        #print(f'BREWER TOKEN: {test_brewer}')
        test_beer_lover = self.app.config['TEST_BEER_LOVER_AUTH_TOKEN']
        #print(f'BEER LOVER TOKEN: {test_beer_lover}')

        # Create authorization token
        self.headers_beer_lover = [
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {test_beer_lover}')
            ]

        self.headers_brewer = [
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {test_brewer}')
            ]   

        # # default data
        # # get last question in question table for deletion as default
        # self.question_to_delete_id = 0
        # self.player_to_delete_id = 0
        # self.category_to_delete_id = 0
        
        # player = Player.query.order_by(Player.id.desc()).first()
        # if player:
        #     self.player_to_delete_id = player.id

        # question = Question.query.order_by(Question.id.desc()).first()  
        # if question:
        #     self.question_to_delete_id = question.id

        # category = Category.query.order_by(Category.id.desc()).first()
        # if category:
        #     self.category_to_delete_id = category.id

        # self.quiz_category = {'id': 4, 
        #                     'type':'History'}

        # self.invalid_quiz_category = {'id': 100, 
        #                     'type':'History'}


        # self.new_player = {"name": "Trivia Olivia"}
        # self.new_category = {"category_type": "Music"}

        # self.new_question = Question (
        #     question = "Who is widely considered to be the world's first computer programmer?",
        #     answer = "Ada Lovelace",
        #     difficulty = 3,
        #     category = 4,
        #     rating = 3
        # )
        # self.new_question = self.new_question.format()


        # self.invalid_new_question = Question (
        #     question = "Who is widely considered to be the world's first computer programmer?",
        #     answer = "Ada Lovelace",
        #     difficulty = 3,
        #     category = self.quiz_category,
        #     rating = 3
        # )
        # self.invalid_new_question = self.invalid_new_question.format()

        # self.previous_questions = [
        #         {
        #         "id": 5,
        #             "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
        #             "answer": "Maya Angelou",
        #             "category": 4,
        #             "difficulty": 2,
        #             "rating": 3
        #         }, 
        #         {
        #             "id": 9,
        #             "question": "What boxer's original name is Cassius Clay?",
        #             "answer": "Muhammad Ali",
        #             "category": 4,
        #             "difficulty": 1,
        #             "rating": 3
        #         },
        #         {
        #             "id": 12, 
        #             "question": "Who invented Peanut Butter?", 
        #             "answer": "George Washington Carver", 
        #             "category": 4, 
        #             "difficulty": 2,
        #             "rating": 3
        #         },
        #         {
        #             "id": 23, 
        #             "question": "Which dung beetle was worshipped by the ancient Egyptians?", 
        #             "answer": "Scarab", 
        #             "category": 4, 
        #             "difficulty": 4,
        #             "rating": 3
        #         }]

    
    def tearDown(self):
        """Executed after reach test"""
        #self.db.drop_all()
        pass

    
    """
    Test cases run in order of function name
    """
    
    def test_get_beers_public(self):
        """ Test GET beers public endpoint"""
        res = self.client().get('/beers/boulder/')
        self.assertEqual(res.status_code, 200)
        #  this is not correct function self.assertTemplateUseed('city_list.html')
        #self.assertIn("beers", res.data)
        #self.assertIn("city", res.data)

    def test_get_beers_(self):
        """ Test GET beers endpoint with authentication"""
        res = self.client().get('/beers/boulder/', headers=self.headers_brewer)
        data_temp = json.loads(res.data)
        data = data_temp[0]
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['beers'])
        self.assertTrue(len(data['beers']))
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()